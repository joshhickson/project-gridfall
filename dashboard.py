from flask import Flask, jsonify, render_template
import json

print("--- [DEBUG] Script starting ---")

app = Flask(__name__)
print("--- [DEBUG] Flask app object created ---")


@app.route('/')
def index():
    """Serves the main dashboard page."""
    print("--- [DEBUG] Request received for / route ---")
    return render_template('index.html')

@app.route('/api/history')
def get_history():
    """Provides the simulation history as a JSON API endpoint."""
    print("--- [DEBUG] Request received for /api/history route ---")
    try:
        with open('simulation_history.json', 'r') as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []
    return jsonify(history)

if __name__ == '__main__':
    print("--- [DEBUG] Entering main execution block ---")
    # Using host='0.0.0.0' to ensure it's accessible from outside the container.
    app.run(host='0.0.0.0', port=5001, debug=True)
    print("--- [DEBUG] Server execution finished ---")
