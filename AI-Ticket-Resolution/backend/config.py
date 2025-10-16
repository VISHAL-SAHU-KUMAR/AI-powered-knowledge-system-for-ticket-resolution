import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///tickets.db'
    MODEL_PATH = 'model/intent_model.pkl'
    VECTORIZER_PATH = 'model/vectorizer.pkl'