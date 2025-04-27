from app.utils.bias_detector import bias_detector
from app.utils.rag_engine import query_knowledge_base

def generate_response(user_input):
    # Check for bias
    bias_results = bias_detector.detect_bias(user_input)
    if any([bias_results["gender_bias"], bias_results["role_bias"], bias_results["workplace_bias"]]):
        bias_explanation = bias_detector.get_bias_explanation(bias_results)
        return f"{bias_explanation}\n\nLet's try to rephrase your question in a more inclusive way. What would you like to know?"

    return query_knowledge_base(user_input)