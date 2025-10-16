from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class Ticket:
    """
    Data model for a support ticket
    """
    id: Optional[int] = None
    subject: str = ""
    description: str = ""
    priority: str = "medium"  # low, medium, high, urgent
    status: str = "open"      # open, in_progress, resolved, closed
    category: str = "general"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    user_id: Optional[str] = None

@dataclass
class User:
    """
    Data model for a user
    """
    id: Optional[str] = None
    email: str = ""
    name: str = ""
    created_at: Optional[str] = None

@dataclass
class KnowledgeBaseEntry:
    """
    Data model for a knowledge base entry
    """
    id: Optional[int] = None
    question: str = ""
    answer: str = ""
    category: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

def ticket_to_dict(ticket: Ticket) -> Dict[str, Any]:
    """
    Convert a Ticket object to a dictionary for database storage
    """
    return {
        "subject": ticket.subject,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": ticket.status,
        "category": ticket.category,
        "created_at": ticket.created_at or datetime.now().isoformat(),
        "updated_at": ticket.updated_at or datetime.now().isoformat(),
        "user_id": ticket.user_id
    }

def dict_to_ticket(data: Dict[str, Any]) -> Ticket:
    """
    Convert a dictionary from database to a Ticket object
    """
    return Ticket(
        id=data.get("id"),
        subject=data.get("subject", ""),
        description=data.get("description", ""),
        priority=data.get("priority", "medium"),
        status=data.get("status", "open"),
        category=data.get("category", "general"),
        created_at=data.get("created_at"),
        updated_at=data.get("updated_at"),
        user_id=data.get("user_id")
    )