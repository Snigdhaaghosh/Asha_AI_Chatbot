from flask import Blueprint, request, jsonify, render_template
from app.chatbot import generate_response

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@routes.route("/ask", methods=["POST"])
def ask_bot():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    response = generate_response(user_input)
    return jsonify({"response": response})