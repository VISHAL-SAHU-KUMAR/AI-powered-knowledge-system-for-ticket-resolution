import os

# Supabase configuration
SUPABASE_URL = "https://vhdmrdirbqgyuykqtjkf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZoZG1yZGlyYnFneXV5a3F0amtmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA1MDc5MjcsImV4cCI6MjA3NjA4MzkyN30.ADX5WguNqo0TOUn4gaYo9kYRHxgb0QNiv_RkJvk-VGw"

class MockSupabaseClient:
    """
    Mock Supabase client for development without actual dependencies
    """
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.table_name = None
    
    def from_(self, table_name):
        self.table_name = table_name
        return self
    
    def select(self, columns="*"):
        # Mock select operation
        print(f"SELECT {columns} FROM {self.table_name}")
        return self
    
    def insert(self, data):
        # Mock insert operation
        print(f"INSERT INTO {self.table_name}: {data}")
        return {"data": data, "status": 201}
    
    def update(self, data):
        # Mock update operation
        print(f"UPDATE {self.table_name}: {data}")
        return {"data": data, "status": 200}
    
    def delete(self):
        # Mock delete operation
        print(f"DELETE FROM {self.table_name}")
        return {"status": 200}
    
    def eq(self, column, value):
        # Mock equality filter
        print(f"WHERE {column} = {value}")
        return self
    
    def execute(self):
        # Mock execute operation
        print("Executing query")
        return {"data": [], "status": 200}

def get_supabase_client():
    """
    Create and return a Supabase client instance (mock version)
    In production, this would use the actual Supabase client
    """
    try:
        # Try to import the real Supabase client
        from supabase import create_client, Client
        return create_client(SUPABASE_URL, SUPABASE_KEY)
    except ImportError:
        # Fall back to mock client if dependencies aren't installed
        print("Using mock Supabase client. Install supabase package for full functionality.")
        return MockSupabaseClient(SUPABASE_URL, SUPABASE_KEY)

# Initialize the client
supabase = get_supabase_client()