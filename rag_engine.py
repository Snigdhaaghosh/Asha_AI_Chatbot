import os
import re
from groq import Groq
from .data_loader import DataLoader
from .bias_detector import bias_detector
import pandas as pd
from API_KEY import GROQ_API_KEY
from datetime import datetime

# Initialize Groq client and DataLoader
api_key = GROQ_API_KEY
client = Groq(api_key=api_key)
data_loader = DataLoader()

class ContextManager:
    def __init__(self):
        self.conversation_history = []
        self.current_context = {}
    
    def update_context(self, user_input, bot_response):
        self.conversation_history.append({
            "user": user_input,
            "bot": bot_response,
            "timestamp": datetime.now().isoformat()
        })
        # Keep only last 5 interactions for context
        if len(self.conversation_history) > 5:
            self.conversation_history = self.conversation_history[-5:]
    
    def get_context_prompt(self):
        if not self.conversation_history:
            return ""
        
        context = "Previous conversation:\n"
        for interaction in self.conversation_history:
            context += f"User: {interaction['user']}\n"
            context += f"Asha: {interaction['bot']}\n"
        return context

def format_response(text):
    # Remove markdown-style headers (##) and replace with styled HTML headers
    text = re.sub(r'##\s*([^#\n]+)', r'<h3 style="color: #2c5282; margin: 16px 0 8px 0; font-size: 1.2em;">\1</h3>', text)
    
    # Format bold text with asterisks
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong style="color: #2c5282;">\1</strong>', text)
    
    # Convert bullet points to styled list items
    text = re.sub(r'•\s*([^\n]+)', r'<li style="margin: 8px 0; position: relative; padding-left: 24px;"><span style="position: absolute; left: 0; color: #4299e1;">•</span>\1</li>', text)
    
    # Wrap bullet point lists in ul tags
    if '<li' in text:
        text = f'<ul style="list-style: none; padding: 0; margin: 12px 0;">{text}</ul>'
    
    # Style links
    text = re.sub(r'\*\*([^*]+)\*\*:', r'<span style="color: #4a5568; font-weight: 600;">\1:</span>', text)
    
    # Add emphasis to key terms
    text = re.sub(r'\*([^*]+)\*', r'<em style="color: #4a5568; font-style: normal; font-weight: 500;">\1</em>', text)
    
    # Style platform/community names
    text = re.sub(r'\*\*([^*]+)\*\*', r'<span style="color: #2b6cb0; font-weight: 600;">\1</span>', text)
    
    # Add paragraph spacing
    text = re.sub(r'\n\n', '</p><p style="margin: 12px 0;">', text)
    
    # Wrap the entire response in a styled container
    text = f'''
    <div style="
        font-family: 'Inter', system-ui, sans-serif;
        line-height: 1.6;
        color: #2d3748;
        background: white;
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    ">
        <p style="margin: 12px 0;">{text}</p>
    </div>
    '''
    
    return text

def get_relevant_data(query):
    # Check for job-related queries
    if any(word in query.lower() for word in ['job', 'career', 'position', 'role', 'work']):
        return data_loader.get_job_listings()
    
    # Check for mentorship queries
    if any(word in query.lower() for word in ['mentor', 'guidance', 'advice', 'support']):
        return data_loader.get_mentorship_programs()
    
    # Check for session queries
    if any(word in query.lower() for word in ['session', 'event', 'workshop', 'training']):
        return data_loader.get_session_details()
    
    return None

def get_groq_response(prompt, context_manager):
    try:
        # Get relevant data based on query
        relevant_data = get_relevant_data(prompt)
        data_context = ""
        if relevant_data:
            data_context = f"\nRelevant information: {str(relevant_data)}"
        
        # Get conversation context
        conversation_context = context_manager.get_context_prompt()
        
        # Check for bias and add appropriate context
        bias_results = bias_detector.detect_bias(prompt)
        bias_explanation = bias_detector.get_bias_explanation(bias_results)
        if bias_explanation:
            prompt += f"\nNote: {bias_explanation}"
        
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": """You are Asha, a helpful and friendly AI assistant focused on helping women in their careers. 
                Keep responses concise, friendly, and empathetic. Always promote gender equality and women empowerment.
                Format responses with bullet points, clear headings, and short paragraphs."""},
                {"role": "user", "content": f"{conversation_context}\n{data_context}\nUser Query: {prompt}"}
            ],
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        # Collect the streaming response
        full_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
        
        return format_response(full_response)
    except Exception as e:
        error_message = str(e)
        print(f"Error generating response: {error_message}")
        return f"Error: {error_message}. Please try again later."

def query_knowledge_base(query):
    # Initialize context
    context_manager = ContextManager()
    
    # Create a context-aware prompt
    prompt = f"""Please respond to the following query in a helpful and natural way: {query}
    Format your response with:
    - Use bullet points (•) for lists
    - Add clear headings with colons
    - Keep paragraphs short and readable
    - Use a friendly and empathetic tone
    - Focus on women empowerment and career growth
    - Address any potential gender bias
    - Provide actionable advice and resources
    Keep your response concise and friendly for women."""
    
    response = get_groq_response(prompt, context_manager)
    context_manager.update_context(query, response)
    return response