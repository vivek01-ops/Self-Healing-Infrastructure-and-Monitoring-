from flask import Flask, request
import subprocess
import logging
import os

# Ensure the logs directory exists
log_dir = '../logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
logging.basicConfig(filename=os.path.join(log_dir, 'webhook.log'), level=logging.INFO)

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    logging.info("Alert received: %s", request.json)
    # Run the Ansible playbook
    subprocess.call(['ansible-playbook', '../ansible/restart_nginx.yml'])
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
