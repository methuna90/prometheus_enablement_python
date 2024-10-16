from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, jsonify
import requests

app1 = Flask(__name__)

# Prometheus metrics setup
metrics = PrometheusMetrics(app1)

# Track default metrics like request count, latency, and status codes.
metrics.info('app_info', 'Application info', version='1.0.0')

# URL for the check endpoint of App2
APP2_URL = 'https://google.com'

@app1.route('/home')
def home():
    try:
        # Make a request to App2's check-db endpoint to get the health status
        response = requests.get(APP2_URL)
        if response.status_code == 200:
            return jsonify({
                "message": "Network connection is OK"
            }), 200
        else:
            return jsonify({
                "message": "Network connection is Not OK"
            }), 500
    except requests.exceptions.RequestException as e:
        return jsonify({
            "message": "Network connection is Not OK",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)  # Runs on port 5000

