from flask import Flask, request, jsonify
import requests
import random
import string
import uuid
import time
import os
import gzip
import json

app = Flask(__name__)

BASE_URL = "https://car-info-super.onrender.com"

def generate_session():
    return f"{uuid.uuid4().hex[:8]}-{uuid.uuid4().hex[:8]}-{random.randint(1000,9999)}"

def generate_device_id():
    return ''.join(random.choice(string.hexdigits.lower()) for _ in range(32))

def generate_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def get_random_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    ]
    return random.choice(agents)

@app.route('/rc', methods=['GET'])
def rc_details():
    rc = request.args.get('term', '').strip().upper()
    
    if not rc:
        return jsonify({
            "error": True,
            "message": "RC number required",
            "usage": "/rc?term=MH02FZ0555"
        }), 400
    
    start_time = time.time()
    
    try:
        headers = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Ch-Ua': f'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        
        url = f"{BASE_URL}/?rc={rc}"
        
        print(f"\n🔄 Fetching: {url}")
        print(f"🔧 UA: {headers['User-Agent'][:60]}...")
        
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        
        response_time = round(time.time() - start_time, 2)
        
        print(f"📡 Status: {response.status_code}")
        print(f"📦 Content-Type: {response.headers.get('Content-Type', 'unknown')}")
        print(f"📏 Length: {len(response.text)} chars")
        
        # Try to get JSON from response
        content_type = response.headers.get('Content-Type', '')
        
        if 'application/json' in content_type:
            try:
                data = response.json()
                return jsonify(data)
            except:
                pass
        
        # Try to parse text as JSON
        try:
            data = json.loads(response.text)
            return jsonify(data)
        except:
            pass
        
        # If HTML, try to extract data
        if response.text.strip().startswith('<!DOCTYPE') or response.text.strip().startswith('<html'):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to find JSON in script tags or pre tags
            pre_tags = soup.find_all('pre')
            for pre in pre_tags:
                try:
                    data = json.loads(pre.text)
                    return jsonify(data)
                except:
                    pass
            
            # Return HTML as text
            text = soup.get_text(separator='\n', strip=True)
            return jsonify({
                "success": True,
                "rc": rc,
                "text": text[:3000],
                "response_time": response_time
            })
        
        # Return raw response
        return jsonify({
            "success": True,
            "rc": rc,
            "response": response.text[:3000],
            "response_time": response_time
        })
            
    except requests.exceptions.Timeout:
        return jsonify({"error": True, "message": "Request timeout"}), 504
    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "running",
        "service": "Car Info Proxy API",
        "usage": "/rc?term=MH02FZ0555"
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Car Info Unlimited API",
        "usage": "/rc?term=MH02FZ0555",
        "info": "Real response from car-info-super"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"""
    🔥 CAR INFO PROXY API
    📍 Port: {port}
    💡 Usage: /rc?term=MH02FZ0555
    """)
    app.run(host='0.0.0.0', port=port, debug=False)
