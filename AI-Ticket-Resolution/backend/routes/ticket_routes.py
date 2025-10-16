from flask import Blueprint, request, jsonify

ticket_bp = Blueprint('tickets', __name__)

@ticket_bp.route('/tickets', methods=['GET'])
def get_tickets():
    # Placeholder for getting all tickets
    return jsonify({"message": "Get all tickets"})

@ticket_bp.route('/tickets', methods=['POST'])
def create_ticket():
    # Placeholder for creating a new ticket
    data = request.json
    return jsonify({"message": "Ticket created", "data": data}), 201

@ticket_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    # Placeholder for getting a specific ticket
    return jsonify({"message": f"Get ticket {ticket_id}"})