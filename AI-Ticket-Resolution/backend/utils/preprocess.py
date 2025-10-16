import re
import string

def clean_text(text):
    """
    Clean and preprocess text data
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_text(text):
    """
    Tokenize text into words
    """
    # Simple tokenization by splitting on whitespace
    tokens = text.split()
    return tokens

def preprocess_pipeline(text):
    """
    Complete preprocessing pipeline
    """
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    return tokens