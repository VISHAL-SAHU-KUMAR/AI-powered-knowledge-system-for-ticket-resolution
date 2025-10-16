from flask import Flask, send_from_directory, jsonify, request
import os
import json
from datetime import datetime
import pickle
import sys

# Add the model directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))

# Import our database service
from database.database_service import db_service
from database.models import Ticket

# Get the absolute path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')

app = Flask(__name__)

# Load the trained model
def load_model():
    try:
        with open('intent_model.pkl', 'rb') as f:
            model = pickle.load(f)
        print("AI model loaded successfully")
        return model
    except FileNotFoundError:
        print("No trained model found. Using fallback classification.")
        return None

# Load the model when the app starts
ai_model = load_model()

# Simple classification function using the loaded model
def classify_text(text, model):
    """Classify text using the loaded model"""
    if model is None:
        # Fallback classification
        text_lower = text.lower()
        if any(keyword in text_lower for keyword in ['password', 'account', 'login']):
            return 'account_access'
        elif any(keyword in text_lower for keyword in ['billing', 'payment', 'charge']):
            return 'billing'
        elif any(keyword in text_lower for keyword in ['bug', 'crash', 'error']):
            return 'bug_report'
        elif any(keyword in text_lower for keyword in ['feature', 'request']):
            return 'feature_request'
        else:
            return 'general_inquiry'
    
    # Use the trained model
    text_lower = text.lower()
    scores = {}
    for category, keywords in model.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        scores[category] = score
    
    # Return category with highest score, or 'general' if no matches
    if max(scores.values()) > 0:
        return max(scores.items(), key=lambda x: x[1])[0]
    else:
        return 'general_inquiry'

# Serve frontend files
@app.route('/')
def home():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Check if the requested file exists in the frontend directory
    file_path = os.path.join(FRONTEND_DIR, path)
    if os.path.exists(file_path):
        return send_from_directory(FRONTEND_DIR, path)
    else:
        # Return 404 for non-existent static files
        return jsonify({"error": "File not found"}), 404

# API routes for tickets
@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    try:
        tickets = db_service.get_all_tickets()
        # Convert Ticket objects to dictionaries for JSON serialization
        tickets_data = []
        for ticket in tickets:
            tickets_data.append({
                "id": ticket.id,
                "subject": ticket.subject,
                "description": ticket.description,
                "priority": ticket.priority,
                "status": ticket.status,
                "category": ticket.category,
                "created_at": ticket.created_at,
                "updated_at": ticket.updated_at,
                "user_id": ticket.user_id
            })
        return jsonify({"tickets": tickets_data})
    except Exception as e:
        print(f"Error getting tickets: {e}")
        return jsonify({"tickets": []})

@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    try:
        data = request.get_json()
        
        # Create a new ticket object
        ticket = Ticket(
            subject=data.get("subject", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            status="open",
            category=classify_text(data.get("description", ""), ai_model),
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        # Save to database
        created_ticket = db_service.create_ticket(ticket)
        
        if created_ticket:
            # Convert to dictionary for JSON response
            ticket_data = {
                "id": created_ticket.id,
                "subject": created_ticket.subject,
                "description": created_ticket.description,
                "priority": created_ticket.priority,
                "status": created_ticket.status,
                "category": created_ticket.category,
                "created_at": created_ticket.created_at,
                "updated_at": created_ticket.updated_at,
                "user_id": created_ticket.user_id
            }
            return jsonify({"message": "Ticket created", "ticket": ticket_data}), 201
        else:
            return jsonify({"error": "Failed to create ticket"}), 500
    except Exception as e:
        print(f"Error creating ticket: {e}")
        return jsonify({"error": "Failed to create ticket"}), 500

@app.route('/api/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    try:
        ticket = db_service.get_ticket_by_id(ticket_id)
        if ticket:
            # Convert to dictionary for JSON response
            ticket_data = {
                "id": ticket.id,
                "subject": ticket.subject,
                "description": ticket.description,
                "priority": ticket.priority,
                "status": ticket.status,
                "category": ticket.category,
                "created_at": ticket.created_at,
                "updated_at": ticket.updated_at,
                "user_id": ticket.user_id
            }
            return jsonify({"ticket": ticket_data})
        else:
            return jsonify({"error": "Ticket not found"}), 404
    except Exception as e:
        print(f"Error getting ticket {ticket_id}: {e}")
        return jsonify({"error": "Failed to get ticket"}), 500

# API routes for AI responses
@app.route('/api/ai/respond', methods=['POST'])
def get_ai_response():
    data = request.get_json()
    query = data.get("query", "")
    
    # Use the trained model to classify the query
    classification = classify_text(query, ai_model)
    
    # Generate a response based on classification
    responses = {
        'account_access': f"I understand you're having an account access issue: '{query}'. To reset your password, please go to the login page and click 'Forgot Password'. If you're locked out, please contact our support team.",
        'billing': f"This appears to be a billing-related query: '{query}'. For billing issues, you can update your payment method in Account Settings or contact our billing department at billing@example.com.",
        'bug_report': f"Thanks for reporting this bug: '{query}'. Our development team will investigate this issue. Please provide any additional details that might help us reproduce the problem.",
        'feature_request': f"Thank you for your feature request: '{query}'. We appreciate your feedback and will consider it for future development.",
        'data': f"I see you're asking about data: '{query}'. You can export your data from Account Settings > Privacy > Data Export. For data deletion requests, please contact privacy@example.com.",
        'general_inquiry': f"Thank you for your inquiry: '{query}'. This is an AI-generated response. A human agent will review your ticket and respond shortly."
    }
    
    response = responses.get(classification, f"Thank you for your query: '{query}'. This is an AI-generated response. A human agent will review your ticket and respond shortly.")
    
    return jsonify({"response": response, "classification": classification})

@app.route('/api/ai/classify', methods=['POST'])
def classify_ticket():
    data = request.get_json()
    ticket_text = data.get("text", "")
    
    # Use the trained model to classify the ticket
    classification = classify_text(ticket_text, ai_model)
    
    return jsonify({"classification": classification})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)