class BiasDetector:
    def __init__(self):
        # Gender bias patterns
        self.gender_biased_phrases = [
            "women can't", "women should", "only men", "female jobs",
            "male jobs", "women's work", "men's work", "because you're a woman",
            "not for women", "women are", "men are", "typical woman", "typical man",
            "like a girl", "like a boy", "man up", "act like a lady"
        ]
        
        # Stereotypical role patterns
        self.role_biased_phrases = [
            "housewife", "stay at home mom", "breadwinner", "primary caregiver",
            "nurturing role", "provider role", "emotional labor", "pink collar"
        ]
        
        # Workplace bias patterns
        self.workplace_biased_phrases = [
            "maternity leave", "work-life balance", "glass ceiling",
            "bossy", "too emotional", "not assertive enough"
        ]
    
    def detect_bias(self, text):
        """
        Detect various types of bias in the given text.
        Returns a dictionary with bias types and their occurrences.
        """
        text_lower = text.lower()
        bias_results = {
            "gender_bias": False,
            "role_bias": False,
            "workplace_bias": False,
            "biased_phrases": []
        }
        
        # Check for gender bias
        for phrase in self.gender_biased_phrases:
            if phrase in text_lower:
                bias_results["gender_bias"] = True
                bias_results["biased_phrases"].append(phrase)
        
        # Check for role bias
        for phrase in self.role_biased_phrases:
            if phrase in text_lower:
                bias_results["role_bias"] = True
                bias_results["biased_phrases"].append(phrase)
        
        # Check for workplace bias
        for phrase in self.workplace_biased_phrases:
            if phrase in text_lower:
                bias_results["workplace_bias"] = True
                bias_results["biased_phrases"].append(phrase)
        
        return bias_results
    
    def get_bias_explanation(self, bias_results):
        """
        Generate an explanation of the detected biases.
        """
        if not any([bias_results["gender_bias"], bias_results["role_bias"], bias_results["workplace_bias"]]):
            return None
        
        explanation = "I noticed some potentially biased language in your message:\n"
        
        if bias_results["gender_bias"]:
            explanation += "• There are some gender-stereotypical phrases that might reinforce traditional gender roles.\n"
        
        if bias_results["role_bias"]:
            explanation += "• Some phrases suggest stereotypical gender roles in family or society.\n"
        
        if bias_results["workplace_bias"]:
            explanation += "• There are workplace-related phrases that might reflect gender bias.\n"
        
        explanation += "\nLet's try to rephrase this in a more inclusive way that focuses on individual capabilities rather than gender."
        return explanation

# Create a singleton instance for easy import
bias_detector = BiasDetector()