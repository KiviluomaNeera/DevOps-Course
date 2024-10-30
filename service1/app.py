from flask import Flask, jsonify
import socket
import subprocess
import json
import time
import requests
import signal
import sys

app = Flask(__name__)

# Function to get container info
def get_container_info():
    # Get IP address
    ip_address_1 = socket.gethostbyname(socket.gethostname())
    
    # Get running processes
    processes_1 = subprocess.check_output(["ps", "-ax"]).decode("utf-8")
    
    # Get disk space
    disk_space_1 = subprocess.check_output(["df", "-h", "/"]).decode("utf-8")
    
    # Get uptime
    uptime_1 = subprocess.check_output(["uptime", "-p"]).decode("utf-8")

    # Get info for Service 2
    service2_info = get_service2_info()
    
    return json.dumps({
        "Service1": {
            "ip_address": ip_address_1,
            "processes": processes_1,
            "disk_space": disk_space_1,
            "uptime": uptime_1
        },
        "Service2": service2_info
    })

def get_service2_info():
    try:
        # Make a request to Service 2
        response = requests.get("http://service2:3000/info")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.RequestException as e:
        return {"error": str(e)}  # Handle request exceptions

# HTTP route
@app.route('/request')
def index():
    result = jsonify(get_container_info())

    time.sleep(2)

    return result

def graceful_exit(signal, frame):
    print("Shutting down gracefully")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_exit)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)