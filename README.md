# Asha AI Assistant 👩‍💼

A sophisticated AI chatbot built with Flask and Groq, designed to empower women in their careers through personalized guidance, job recommendations, and bias-free interactions.

## ✨ Key Features

- **Smart Conversation**: Context-aware responses using Groq's LLM
- **Bias Detection**: Advanced gender bias detection across multiple categories:
  - Gender stereotypes
  - Role-based biases
  - Workplace biases
- **Career Resources**: Real-time access to:
  - Job listings
  - Mentorship programs
  - Training sessions
- **Modern UI**: Responsive and user-friendly interface with:
  - Clean design
  - Real-time responses
  - Beautiful formatting
  - Mobile-friendly layout

## 🛠️ Technical Stack

- **Backend**: Flask (Python)
- **AI Model**: Groq (meta-llama/llama-4-scout-17b-16e-instruct)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: CSV & JSON for job listings and program data

## 🚀 Setup Instructions

1. **Clone the Repository**
```bash
git clone <repository-url>
cd asha_ai_chatbot_final
```

2. **Set up Virtual Environment (Recommended)**
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Unix/MacOS
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Key**
Create `API_KEY.py` in the root directory:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```

5. **Prepare Data Files**
Ensure these files are present in the root directory:
- `job_listing_data.csv`
- `session_details.json`
- `mentorship_programs.json`

6. **Run the Application**
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 💡 Usage Guide

### Interacting with Asha

- **Career Guidance**: Ask about career paths, job opportunities, or skill development
- **Mentorship**: Inquire about mentorship programs and networking opportunities
- **Training**: Get information about workshops and training sessions
- **Bias-Free Communication**: Asha helps maintain inclusive language

### Example Queries

✅ Effective queries:
- "What career opportunities are available in tech?"
- "How can I develop leadership skills?"
- "Tell me about mentorship programs"
- "What training sessions are available?"

❌ Queries that will trigger bias detection:
- "What jobs are suitable for women?"
- "Why aren't women good at leadership?"
- "Is this role too demanding for a woman?"

## 🎨 UI Features

- Clean and modern interface
- Real-time message updates
- Beautifully formatted responses
- Mobile-responsive design
- Smooth animations
- Accessible color scheme

## 🔒 Privacy & Security

- No personal data storage
- Secure API key handling
- CORS protection enabled
- Input validation and sanitization

## 🤝 Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Groq for providing the LLM API
- Flask community for the excellent web framework
- Contributors and testers

## 📞 Support

For issues, questions, or contributions, please:
1. Open an issue in the repository
2. Contact the maintainers
3. Check existing documentation

---
Made with ❤️ for empowering women in tech