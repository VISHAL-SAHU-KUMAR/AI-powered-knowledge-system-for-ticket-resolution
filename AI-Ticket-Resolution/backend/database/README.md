# Database Integration with Supabase

This directory contains all the database integration code for the AI Ticket Resolution system using Supabase.

## Overview

The AI Ticket Resolution system uses Supabase as its backend database. Supabase provides:
- PostgreSQL database
- Real-time subscriptions
- Authentication
- Storage
- Edge functions

## Database Schema

The system uses three main tables:

1. **tickets** - Stores all support tickets
2. **users** - Stores user information
3. **knowledge_base** - Stores FAQ and support articles

See [schema.sql](schema.sql) for the complete database schema.

## Configuration

The Supabase client is configured with the following credentials:

- **Project URL**: `https://vhdmrdirbqgyuykqtjkf.supabase.co`
- **API Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZoZG1yZGlyYnFneXV5a3F0amtmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA1MDc5MjcsImV4cCI6MjA3NjA4MzkyN30.ADX5WguNqo0TOUn4gaYo9kYRHxgb0QNiv_RkJvk-VGw`

## Files

- [supabase_client.py](supabase_client.py) - Supabase client initialization
- [models.py](models.py) - Data models for tickets, users, and knowledge base entries
- [database_service.py](database_service.py) - Database service layer with CRUD operations
- [schema.sql](schema.sql) - Database schema definition

## Usage

The database service is automatically initialized when the application starts. You can use it in your routes like this:

```python
from database.database_service import db_service

# Get all tickets
tickets = db_service.get_all_tickets()

# Create a new ticket
new_ticket = Ticket(subject="Test", description="Test ticket")
created_ticket = db_service.create_ticket(new_ticket)
```

## Security

This implementation uses Row Level Security (RLS) to ensure that users can only access their own data. The policies are defined in the schema.sql file.