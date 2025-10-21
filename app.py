# app.py (Updated Version)

from flask import Flask, request, jsonify
import json

# Import your custom modules
from prompt_builder import create_meal_suggestion_prompt
from services import get_nutrition_data
from llm_service import get_llm_completion  # <--- ADD THIS IMPORT

app = Flask(__name__)

@app.route('/meal-suggestion', methods=['POST'])
def get_meal_suggestion():
    # 1. Request Initiation
    request_data = request.get_json()
    if not request_data or 'user_profile' not in request_data:
        return jsonify({"error": "A 'user_profile' object is required in the request body."}), 400
    
    user_profile = request_data.get('user_profile')
    available_ingredients = request_data.get('available_ingredients')

    # 2. LLM Interaction
    prompt = create_meal_suggestion_prompt(user_profile, available_ingredients)
    
    # --- THIS IS THE KEY CHANGE ---
    # Replace the hardcoded string with a call to your new function
    llm_response_str = get_llm_completion(prompt)
    # ----------------------------
    
    try:
        llm_data = json.loads(llm_response_str)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse response from LLM.", "raw_response": llm_response_str}), 500

    # Check if the LLM returned an error inside its JSON
    if 'error' in llm_data:
         return jsonify({"error": "An error occurred with the LLM service.", "details": llm_data.get('details')}), 500

    meal_option_a = llm_data.get('meal_option_a')
    meal_option_b = llm_data.get('meal_option_b')

    # 3. Data Enrichment
    if meal_option_a:
        nutrition_a = get_nutrition_data(meal_option_a['ingredients'])
        meal_option_a['nutritional_breakdown'] = nutrition_a

    if meal_option_b:
        nutrition_b = get_nutrition_data(meal_option_b['ingredients'])
        meal_option_b['nutritional_breakdown'] = nutrition_b

    # 4. Response Assembly
    final_response = {
        "meal_option_a": meal_option_a,
        "meal_option_b": meal_option_b
    }

    return jsonify(final_response), 200

if __name__ == '__main__':
    app.run(debug=True)