import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def classify_number(number):
    try:
        num = int(number)  # Validate input as integer
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    properties = []

    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Armstrong Number Check (Example)
    num_str = str(num)
    n = len(num_str)
    sum_of_powers = sum(int(digit)**n for digit in num_str)
    if sum_of_powers == num:
        properties.insert(0, "armstrong") # Armstrong numbers go first
        

    # Fetch fun fact from numbers API
    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{num}/math?json")
        fun_fact_data = fun_fact_response.json()
        fun_fact = fun_fact_data.get("text", "Fun fact not available.")  # Handle missing data
    except requests.exceptions.RequestException:
        fun_fact = "Error fetching fun fact."

    return jsonify({
        "number": num,
        "is_prime": False,  # Add prime check if needed (more complex)
        "is_perfect": False, # Add perfect number check if needed (more complex)
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": fun_fact
    }), 200

@app.route('/api/classify-number', methods=['GET'])
def api_classify():
    number = request.args.get('number')  # Extract number from request arguments

    if number is None:  # Check if number is missing
        return jsonify({"error": "Number parameter is required"}), 400

    try:
        num = int(number)  # Convert to integer (handle potential ValueError)
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    try:
        response, status_code = classify_number(num)  # Call with the number
        return response, status_code  # Return the response from classify_number()
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error (important!)
        return jsonify({"error": "An internal server error occurred."}), 500  # Return a 500 error
@app.after_request
def add_cors_headers(response):  # CORS handling
    response.headers.add('Access-Control-Allow-Origin', '*') # Or restrict to specific origins
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=5000)  # host='0.0.0.0' for external access