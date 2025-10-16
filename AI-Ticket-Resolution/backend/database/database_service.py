from typing import List, Optional, Dict, Any
from datetime import datetime
from .supabase_client import supabase
from .models import Ticket, User, KnowledgeBaseEntry, ticket_to_dict, dict_to_ticket

class DatabaseService:
    """
    Service class to handle all database operations with Supabase
    """
    
    def __init__(self):
        self.client = supabase
    
    def _handle_response(self, response):
        """Helper method to handle both real and mock responses"""
        if isinstance(response, dict):
            return response.get('data', []), response.get('status', 200)
        else:
            # Real Supabase client response
            return getattr(response, 'data', []), getattr(response, 'status', 200)
    
    # Ticket operations
    def get_all_tickets(self) -> List[Ticket]:
        """
        Retrieve all tickets from the database
        """
        try:
            if hasattr(self.client, 'from_'):
                # Try real Supabase client
                try:
                    response = self.client.from_("tickets").select("*").execute()
                    data, _ = self._handle_response(response)
                    tickets = [dict_to_ticket(ticket_data) for ticket_data in data]
                    return tickets
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    # Fall back to mock behavior
                    print("Mock: Getting all tickets")
                    return []
            else:
                # Mock implementation
                print("Mock: Getting all tickets")
                return []
        except Exception as e:
            print(f"Error fetching tickets: {e}")
            return []
    
    def get_ticket_by_id(self, ticket_id: int) -> Optional[Ticket]:
        """
        Retrieve a specific ticket by ID
        """
        try:
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("tickets").select("*").eq("id", ticket_id).execute()
                    data, _ = self._handle_response(response)
                    if data:
                        return dict_to_ticket(data[0])
                    return None
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Getting ticket by ID {ticket_id}")
                    return None
            else:
                # Mock implementation
                print(f"Mock: Getting ticket by ID {ticket_id}")
                return None
        except Exception as e:
            print(f"Error fetching ticket {ticket_id}: {e}")
            return None
    
    def create_ticket(self, ticket: Ticket) -> Optional[Ticket]:
        """
        Create a new ticket in the database
        """
        try:
            ticket_data = ticket_to_dict(ticket)
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("tickets").insert(ticket_data).execute()
                    data, _ = self._handle_response(response)
                    if data:
                        created_ticket = dict_to_ticket(data[0])
                        return created_ticket
                    return None
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Creating ticket: {ticket_data}")
                    return ticket
            else:
                # Mock implementation
                print(f"Mock: Creating ticket: {ticket_data}")
                return ticket
        except Exception as e:
            print(f"Error creating ticket: {e}")
            return None
    
    def update_ticket(self, ticket_id: int, ticket_data: Dict[str, Any]) -> Optional[Ticket]:
        """
        Update an existing ticket
        """
        try:
            ticket_data["updated_at"] = datetime.now().isoformat()
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("tickets").update(ticket_data).eq("id", ticket_id).execute()
                    data, _ = self._handle_response(response)
                    if data:
                        return dict_to_ticket(data[0])
                    return None
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Updating ticket {ticket_id} with data: {ticket_data}")
                    return None
            else:
                # Mock implementation
                print(f"Mock: Updating ticket {ticket_id} with data: {ticket_data}")
                return None
        except Exception as e:
            print(f"Error updating ticket {ticket_id}: {e}")
            return None
    
    def delete_ticket(self, ticket_id: int) -> bool:
        """
        Delete a ticket from the database
        """
        try:
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("tickets").delete().eq("id", ticket_id).execute()
                    _, status = self._handle_response(response)
                    return status == 200
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Deleting ticket {ticket_id}")
                    return True
            else:
                # Mock implementation
                print(f"Mock: Deleting ticket {ticket_id}")
                return True
        except Exception as e:
            print(f"Error deleting ticket {ticket_id}: {e}")
            return False
    
    # User operations
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by ID
        """
        try:
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("users").select("*").eq("id", user_id).execute()
                    data, _ = self._handle_response(response)
                    if data:
                        user_data = data[0]
                        return User(
                            id=user_data.get("id"),
                            email=user_data.get("email", ""),
                            name=user_data.get("name", ""),
                            created_at=user_data.get("created_at")
                        )
                    return None
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Getting user by ID {user_id}")
                    return None
            else:
                # Mock implementation
                print(f"Mock: Getting user by ID {user_id}")
                return None
        except Exception as e:
            print(f"Error fetching user {user_id}: {e}")
            return None
    
    def create_user(self, user: User) -> Optional[User]:
        """
        Create a new user in the database
        """
        try:
            user_data = {
                "email": user.email,
                "name": user.name,
                "created_at": user.created_at or datetime.now().isoformat()
            }
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("users").insert(user_data).execute()
                    data, _ = self._handle_response(response)
                    if data:
                        created_user = data[0]
                        return User(
                            id=created_user.get("id"),
                            email=created_user.get("email", ""),
                            name=created_user.get("name", ""),
                            created_at=created_user.get("created_at")
                        )
                    return None
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Creating user: {user_data}")
                    return user
            else:
                # Mock implementation
                print(f"Mock: Creating user: {user_data}")
                return user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
    
    # Knowledge base operations
    def get_knowledge_base_entries(self) -> List[KnowledgeBaseEntry]:
        """
        Retrieve all knowledge base entries
        """
        try:
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("knowledge_base").select("*").execute()
                    data, _ = self._handle_response(response)
                    entries = []
                    for entry_data in data:
                        entry = KnowledgeBaseEntry(
                            id=entry_data.get("id"),
                            question=entry_data.get("question", ""),
                            answer=entry_data.get("answer", ""),
                            category=entry_data.get("category", ""),
                            created_at=entry_data.get("created_at"),
                            updated_at=entry_data.get("updated_at")
                        )
                        entries.append(entry)
                    return entries
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print("Mock: Getting knowledge base entries")
                    return []
            else:
                # Mock implementation
                print("Mock: Getting knowledge base entries")
                return []
        except Exception as e:
            print(f"Error fetching knowledge base entries: {e}")
            return []
    
    def search_knowledge_base(self, query: str) -> List[KnowledgeBaseEntry]:
        """
        Search knowledge base entries by query
        """
        try:
            # This is a simple implementation - in production, you might want to use
            # full-text search or vector search
            if hasattr(self.client, 'from_'):
                try:
                    response = self.client.from_("knowledge_base").select("*").execute()
                    data, _ = self._handle_response(response)
                    matching_entries = []
                    query_lower = query.lower()
                    
                    for entry_data in data:
                        if (query_lower in entry_data.get("question", "").lower() or 
                            query_lower in entry_data.get("answer", "").lower()):
                            entry = KnowledgeBaseEntry(
                                id=entry_data.get("id"),
                                question=entry_data.get("question", ""),
                                answer=entry_data.get("answer", ""),
                                category=entry_data.get("category", ""),
                                created_at=entry_data.get("created_at"),
                                updated_at=entry_data.get("updated_at")
                            )
                            matching_entries.append(entry)
                    
                    return matching_entries
                except Exception as e:
                    print(f"Real client error: {e}, using mock")
                    print(f"Mock: Searching knowledge base for: {query}")
                    return []
            else:
                # Mock implementation
                print(f"Mock: Searching knowledge base for: {query}")
                return []
        except Exception as e:
            print(f"Error searching knowledge base: {e}")
            return []

# Global instance of the database service
db_service = DatabaseService()