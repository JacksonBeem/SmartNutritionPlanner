# prompt_builder.py

def create_meal_suggestion_prompt(user_profile, available_ingredients=None):
    """Constructs a detailed prompt for the LLM based on user data."""
    
    # User profile data from the request 
    diet = user_profile.get('dietary_preferences', 'any')
    allergies = user_profile.get('allergies', [])
    goal = user_profile.get('goal', 'general_health')

    prompt = f"You are a helpful nutrition planning assistant. Generate two distinct and varied meal suggestions for a user with the following profile:\n"
    prompt += f"- Dietary Preference: {diet}\n"
    prompt += f"- Health Goal: {goal}\n"
    
    if allergies:
        # Allergies must be strictly avoided 
        prompt += f"- Must Avoid (Allergies): {', '.join(allergies)}\n"
    
    if available_ingredients:
        # Optional list of ingredients on hand 
        prompt += f"- Try to use some of these available ingredients: {', '.join(available_ingredients)}\n"

    prompt += "\nFor each meal, provide a unique title, a list of ingredients with quantities, and step-by-step instructions."
    prompt += " Also, provide a brief 'goal_justification' explaining how the meal supports the user's goal."
    prompt += " Please format the response as a JSON object with two keys: 'meal_option_a' and 'meal_option_b'."
    
    return prompt