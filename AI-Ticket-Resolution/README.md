# 🧠 AI-Powered Knowledge Engine for Smart Support and Ticket Resolution

This project leverages **Artificial Intelligence (AI)** and **Retrieval-Augmented Generation (RAG)** to automate customer support and streamline ticket resolution processes. The system uses **Natural Language Processing (NLP)** to understand user queries, retrieve the most relevant information from a dynamic knowledge base, and generate accurate, context-aware responses. By combining retrieval and generation, the engine ensures both factual accuracy and conversational fluency. It continuously learns from past interactions to improve precision, reduce response time, and minimize human intervention.

---

## 🚀 Key Features

- 🔍 **RAG-based Query Understanding** – Retrieves and integrates relevant knowledge before response generation  
- 🤖 **Automated Ticket Classification & Resolution** – Categorizes incoming tickets and provides instant AI-driven replies  
- 📚 **Dynamic Knowledge Base Search & Update** – Keeps information fresh with real-time data updates  
- 💬 **AI-Generated Context-Aware Responses** – Natural conversational replies with factual accuracy  
- 📈 **Continuous Learning & Performance Tracking** – Learns from resolved tickets to enhance future accuracy  
- 🗄️ **Supabase Database Integration** – Secure, scalable database with real-time capabilities

---

## 🧩 Tech Stack

| Component | Technologies Used |
|------------|------------------|
| **Frontend** | HTML, CSS, JavaScript (for UI) |
| **Backend** | Python (Flask) |
| **AI/NLP** | Custom rule-based classifier (extensible to TensorFlow/scikit-learn) |
| **Database** | Supabase (PostgreSQL with real-time capabilities) |
| **Knowledge Engine** | RAG + Embeddings + Vector Search |
| **Version Control** | Git & GitHub |

---

## 🧠 System Workflow

1. **User submits a support query or ticket** via web UI or API  
2. **AI model processes the query** using NLP & classification algorithms  
3. **System stores ticket in Supabase database** with proper categorization  
4. **Knowledge base search** finds relevant solutions from internal data  
5. **Response generator** formulates a fluent, context-aware answer  
6. **AI engine logs ticket status** and updates its knowledge base  

---

## 📂 Project Structure

```
AI-Ticket-Resolution/
│
├── backend/
│   ├── app.py                 # Flask backend main file
│   ├── requirements.txt       # Python dependencies
│   ├── config.py              # Configuration variables
│   ├── model/
│   │   ├── intent_model.pkl   # Trained classification model
│   │   └── train_model.py     # Script for training
│   ├── routes/
│   │   ├── ticket_routes.py   # API for ticket creation and fetching
│   │   └── ai_routes.py       # API for AI responses
│   ├── utils/
│   │   ├── preprocess.py      # Text cleaning & tokenization
│   │   └── knowledge_search.py# Finds best answer from knowledge base
│   ├── database/
│   │   ├── supabase_client.py # Supabase client initialization
│   │   ├── database_service.py# Database operations
│   │   ├── models.py          # Data models
│   │   ├── schema.sql         # Database schema
│   │   └── README.md          # Database documentation
│   └── docs/
│       └── agile_documentation.md  # Agile planning file
│
├── frontend/
│   ├── index.html             # Ticket submission UI
│   ├── style.css              # Basic styling
│   ├── script.js              # API calls & dynamic updates
│
├── data/
│   ├── knowledge_base.csv     # FAQs, problems & solutions
│   └── sample_tickets.csv     # Training or testing data
│
├── INSTALL.md                 # Installation guide
├── setup.py                   # Installation script
├── LICENSE                    # MIT License
├── README.md                  # Full project description
└── .gitignore                 # To ignore unnecessary files
```

---

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)
- **Web browser** (Chrome, Firefox, Safari, etc.)

### Backend Dependencies

The backend requires the following Python libraries:

| Library | Version | Purpose |
|---------|---------|---------|
| **Flask** | 2.0.1 | Web framework for the backend API |
| **scikit-learn** | 1.0.2 | Machine learning library for AI classification |
| **pandas** | 1.3.3 | Data manipulation and analysis |
| **numpy** | 1.21.2 | Numerical computing |
| **supabase** | 0.7.1 | Supabase client for database integration |

### Frontend Dependencies

The frontend uses only native web technologies:
- **HTML5** - Structure and content
- **CSS3** - Styling and layout
- **JavaScript (ES6+)** - Interactivity and API communication

No additional frontend libraries or frameworks are required.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI-Ticket-Resolution
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Train the model (optional, already pre-trained):**
   ```bash
   cd model
   python train_model.py
   cd ..
   ```

5. **Start the backend server:**
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000`

6. **Access the frontend:**
   Open your browser and navigate to `http://localhost:5000`
   
   Alternatively, you can directly open `frontend/index.html` in your browser, but this will not have backend functionality.

---

## ▶️ Running the Application

### Running the Backend

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

---

## 🗄️ Supabase Database Integration

This project uses Supabase as its backend database with the following configuration:

- **Project URL**: `https://vhdmrdirbqgyuykqtjkf.supabase.co`
- **API Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZoZG1yZGlyYnFneXV5a3F0amtmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA1MDc5MjcsImV4cCI6MjA3NjA4MzkyN30.ADX5WguNqo0TOUn4gaYo9kYRHxgb0QNiv_RkJvk-VGw`

The database integration provides:
- Secure data storage with Row Level Security (RLS)
- Real-time data synchronization
- Scalable PostgreSQL backend
- RESTful API for data operations

See [backend/database/README.md](backend/database/README.md) for more details.

---

## 📋 Agile Development Plan

### Sprint 1: Planning
- **Goal:** Build AI model and Flask backend
- **Tasks:** Data preprocessing, training model, database integration

### Sprint 2: Integration
- **Goal:** Connect frontend & backend with Supabase
- **Tasks:** Build API, test endpoints, implement real-time features

### Sprint 3: Evaluation
- **Goal:** Final testing and documentation
- **Tasks:** Report generation, bug fixes, performance optimization

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For any queries or suggestions, please open an issue or contact the project maintainers.