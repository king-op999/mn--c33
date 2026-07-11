from flask import Flask, request, Response
import requests
import random
import time
import os

app = Flask(__name__)

BASE_URL = "https://car-info-super.onrender.com"

def get_random_ua():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    ]
    return random.choice(agents)

@app.route('/rc', methods=['GET'])
def rc_details():
    rc = request.args.get('term', '').strip().upper()
    
    if not rc:
        return Response(
            '{"error": "RC number required", "usage": "/rc?term=MH02FZ0555"}',
            mimetype='application/json'
        ), 400
    
    try:
        # Naya session har request pe
        session = requests.Session()
        
        headers = {
            'User-Agent': get_random_ua(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://car-info-super.onrender.com/',
            'Origin': 'https://car-info-super.onrender.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
        }
        
        url = f"{BASE_URL}/?rc={rc}"
        
        # Call real API
        resp = session.get(url, headers=headers, timeout=30)
        
        # Return EXACT same response
        return Response(
            resp.content,
            status=resp.status_code,
            mimetype=resp.headers.get('Content-Type', 'application/json'),
            headers={
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
            }
        )
        
    except requests.exceptions.Timeout:
        return Response(
            '{"error": "Timeout"}',
            mimetype='application/json'
        ), 504
    except Exception as e:
        return Response(
            f'{{"error": "{str(e)}"}}',
            mimetype='application/json'
        ), 500


@app.route('/health', methods=['GET'])
def health():
    return Response(
        '{"status": "running"}',
        mimetype='application/json'
    )


@app.route('/', methods=['GET'])
def home():
    return Response(
        '{"service": "RC Proxy", "usage": "/rc?term=MH02FZ0555"}',
        mimetype='application/json'
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🔥 RC Proxy | Port: {port} | /rc?term=MH02FZ0555")
    app.run(host='0.0.0.0', port=port, debug=False)
