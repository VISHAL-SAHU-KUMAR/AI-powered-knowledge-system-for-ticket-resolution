"""
Test script for Supabase database integration
"""
import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from database.database_service import db_service
from database.models import Ticket, User, KnowledgeBaseEntry

def test_database_operations():
    """
    Test all database operations
    """
    print("Testing Supabase database integration...")
    
    # Test creating a ticket
    print("\n1. Testing ticket creation...")
    ticket = Ticket(
        subject="Test Ticket",
        description="This is a test ticket for database integration",
        priority="medium",
        status="open",
        category="test"
    )
    
    created_ticket = db_service.create_ticket(ticket)
    if created_ticket:
        print(f"✓ Ticket created successfully with ID: {created_ticket.id}")
    else:
        print("✗ Failed to create ticket")
    
    # Test getting all tickets
    print("\n2. Testing fetching all tickets...")
    tickets = db_service.get_all_tickets()
    print(f"✓ Found {len(tickets)} tickets in database")
    
    # Test creating a user
    print("\n3. Testing user creation...")
    user = User(
        email="test@example.com",
        name="Test User"
    )
    
    created_user = db_service.create_user(user)
    if created_user:
        print(f"✓ User created successfully with ID: {created_user.id}")
    else:
        print("✗ Failed to create user")
    
    # Test getting knowledge base entries
    print("\n4. Testing knowledge base retrieval...")
    entries = db_service.get_knowledge_base_entries()
    print(f"✓ Found {len(entries)} knowledge base entries")
    
    # Test searching knowledge base
    print("\n5. Testing knowledge base search...")
    search_results = db_service.search_knowledge_base("password")
    print(f"✓ Found {len(search_results)} entries matching 'password'")
    
    print("\n✓ All database tests completed!")

if __name__ == "__main__":
    test_database_operations()