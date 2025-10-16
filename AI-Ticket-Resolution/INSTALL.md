# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Steps

### 1. Clone or download the repository
```bash
git clone <repository-url>
cd AI-Ticket-Resolution
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install required dependencies
```bash
cd backend
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- **Flask 2.0.1** - Web framework for the backend
- **scikit-learn 1.0.2** - Machine learning library for AI classification
- **pandas 1.3.3** - Data manipulation and analysis
- **numpy 1.21.2** - Numerical computing
- **supabase 0.7.1** - Supabase client for database integration

### 4. Train the AI model (optional, already pre-trained)
```bash
cd model
python train_model.py
cd ..
```

### 5. Start the application
```bash
python app.py
```

### 6. Access the application
Open your browser and navigate to `http://localhost:5000`

## ▶️ Running the Application

### Running the Backend

The backend is a Flask application that serves both the API and frontend files.

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

3. The backend will be available at:
   - `http://localhost:5000` - Main application
   - `http://localhost:5000/api/tickets` - Tickets API
   - `http://localhost:5000/api/ai/respond` - AI response API

### Running the Frontend

The frontend is served by the Flask backend. Simply navigate to `http://localhost:5000` in your browser.

For development purposes, you can also open `frontend/index.html` directly in your browser, but this will not have access to the backend APIs.

## 📦 Backend Dependencies Explained

| Package | Version | Purpose |
|---------|---------|---------|
| **Flask** | 2.0.1 | Web framework for creating the REST API and serving frontend files |
| **scikit-learn** | 1.0.2 | Used for the AI classification model (in future enhancements) |
| **pandas** | 1.3.3 | Data processing for training data (in future enhancements) |
| **numpy** | 1.21.2 | Numerical computing support for machine learning |
| **supabase** | 0.7.1 | Client library for connecting to Supabase database |

## 🖥️ Frontend Technologies

The frontend uses only native web technologies:
- **HTML5** - Structure and content
- **CSS3** - Styling and layout
- **JavaScript (ES6+)** - Interactivity and API communication

No additional frontend libraries or frameworks are required.

## 🧪 Testing the Installation

After installation, you can verify everything is working:

1. Check that the Flask server starts without errors:
   ```bash
   python app.py
   ```

2. Verify dependencies are installed:
   ```bash
   pip list
   ```

3. Test the API endpoints:
   ```bash
   curl http://localhost:5000/api/tickets
   ```

## 🛠️ Development Workflow

1. **Backend Development**: Modify files in the `backend/` directory
2. **Frontend Development**: Modify files in the `frontend/` directory
3. **AI Model Development**: Work in the `backend/model/` directory
4. **Database Schema**: Update `backend/database/schema.sql`

The Flask development server will automatically reload when you make changes to Python files.

## ⚠️ Common Issues and Solutions

### ImportError issues in IDE
The import errors you might see in your IDE are just linter warnings. As long as you've installed the dependencies with `pip install -r requirements.txt`, the application will run correctly.

### Port already in use
If you get an error that port 5000 is already in use, you can change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or another port
```

### Model not found
If you get a "model not found" error, make sure you've run the training script:
```
cd backend/model
python train_model.py
```

### Database Connection Issues
If you experience database connection issues:
1. Verify the Supabase credentials in `backend/database/supabase_client.py`
2. Ensure you have internet connectivity
3. Check that the Supabase project is properly configured

## 🔄 Updating Dependencies

To update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

To generate a new requirements file:
```bash
pip freeze > requirements.txt
```

## 🗄️ Project Structure

```
AI-Ticket-Resolution/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── config.py              # Configuration variables
│   ├── model/
│   │   ├── intent_model.pkl   # Trained AI model (generated)
│   │   ├── train_model.py     # Model training script
│   ├── routes/
│   │   ├── ticket_routes.py   # Ticket API endpoints
│   │   └── ai_routes.py       # AI API endpoints
│   ├── utils/
│   │   ├── preprocess.py      # Text preprocessing utilities
│   │   └── knowledge_search.py# Knowledge base search
│   ├── database/
│   └── docs/
├── frontend/
│   ├── index.html             # Main HTML file
│   ├── style.css              # Styling
│   └── script.js              # Client-side JavaScript
├── data/
│   ├── knowledge_base.csv     # Knowledge base
│   └── sample_tickets.csv     # Sample data
├── setup.py                  # Installation script
├── INSTALL.md                # This file
├── README.md                 # Project documentation
├── LICENSE                   # License information
└── .gitignore                # Git ignore file
```