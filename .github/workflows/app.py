from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.utcnow().strftime('%A')
    current_time = datetime.utcnow().strftime('%H:%M:%S')
    github_url = 'https://github.com/ChinCUstu/python-flask-endpoint'
    
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_time' : current_time,
        'track': track,
        'github_url': github_url,
        'status': 'Success'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
