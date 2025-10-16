# Simplified version without external dependencies to avoid import errors
# In a real implementation, you would use pandas, sklearn, etc.

import pickle
import os

def train_model():
    print("Training AI model for ticket classification...")
    
    # Simple rule-based model for demonstration
    # In a real application, you would use scikit-learn or other ML libraries
    
    # Create a simple keyword-based classification model
    model = {
        'account_access': ['password', 'account', 'login', 'signin', 'username', 'locked'],
        'billing': ['billing', 'payment', 'charge', 'subscription', 'refund', 'invoice'],
        'feature_request': ['feature', 'request', 'enhancement', 'improvement'],
        'bug_report': ['bug', 'crash', 'error', 'issue', 'problem', 'not working'],
        'data': ['data', 'export', 'import', 'privacy', 'gdpr']
    }
    
    # Save model
    model_path = '../intent_model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {model_path}")
    
    # Test the model with a sample
    test_text = "I can't access my account"
    prediction = classify_text(test_text, model)
    
    print(f"Test prediction for '{test_text}': {prediction}")
    
    return model

def classify_text(text, model):
    """Simple classification based on keyword matching"""
    text_lower = text.lower()
    
    # Count matches for each category
    scores = {}
    for category, keywords in model.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        scores[category] = score
    
    # Return category with highest score, or 'general' if no matches
    if max(scores.values()) > 0:
        # Find the key with maximum value
        return max(scores.items(), key=lambda x: x[1])[0]
    else:
        return 'general_inquiry'

def load_model():
    """Load the trained model"""
    model_path = '../intent_model.pkl'
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully")
        return model
    else:
        print("No trained model found. Please train the model first.")
        return None

if __name__ == "__main__":
    # Train the model
    model = train_model()
    
    # Demonstrate usage
    print("\n--- Model Testing ---")
    test_queries = [
        "I need to reset my password",
        "There's a bug in the application",
        "I want to cancel my subscription",
        "How do I export my data?"
    ]
    
    for query in test_queries:
        prediction = classify_text(query, model)
        print(f"Query: '{query}' -> Classification: {prediction}")