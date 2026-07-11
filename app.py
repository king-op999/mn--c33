from flask import Flask, request, jsonify
import requests
import random
import string
import uuid
import time
import os

app = Flask(__name__)

BASE_URL = "https://car-info-super.onrender.com"

def generate_session():
    """Har request ke liye naya session ID"""
    return f"{uuid.uuid4().hex[:8]}-{uuid.uuid4().hex[:8]}-{random.randint(1000,9999)}"

def generate_device_id():
    """Har request ke liye naya device ID"""
    return ''.join(random.choice(string.hexdigits.lower()) for _ in range(32))

def generate_ip():
    """Random IP generate karo"""
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def get_random_user_agent():
    """Different browsers ke User-Agents"""
    agents = [
        # Chrome Windows
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        # Chrome Android
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
        # Safari
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
        # Firefox
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
        # Edge
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        # Brave
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Brave/1.63.0",
    ]
    return random.choice(agents)

def get_random_accept_language():
    """Different language headers"""
    languages = [
        "en-US,en;q=0.9",
        "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
        "en-GB,en;q=0.9,en-US;q=0.8",
        "en-US,en;q=0.9,hi;q=0.8",
        "en-IN,en;q=0.9",
    ]
    return random.choice(languages)

def create_fresh_session():
    """Bilkul naya session create karo"""
    session = requests.Session()
    
    # Random cookies
    session.cookies.set('session_id', f"sess_{uuid.uuid4().hex[:16]}")
    session.cookies.set('visitor_id', f"vis_{random.randint(1000000,9999999)}")
    session.cookies.set('_ga', f"GA1.1.{random.randint(100000000,999999999)}.{int(time.time())}")
    session.cookies.set('device_fingerprint', generate_device_id())
    
    return session

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
        # HAR REQUEST PE NAYA SESSION + NAYE HEADERS
        session = create_fresh_session()
        
        headers = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': get_random_accept_language(),
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Ch-Ua': f'"Chromium";v="{random.randint(118,122)}", "Not(A:Brand";v="24", "Google Chrome";v="{random.randint(118,122)}"',
            'Sec-Ch-Ua-Mobile': random.choice(['?0', '?1']),
            'Sec-Ch-Ua-Platform': random.choice(['"Windows"', '"Android"', '"macOS"', '"Linux"']),
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Origin': BASE_URL,
            'Referer': f'{BASE_URL}/',
            'X-Forwarded-For': generate_ip(),
            'X-Real-IP': generate_ip(),
            'X-Client-IP': generate_ip(),
            'X-Request-ID': str(uuid.uuid4()),
            'X-Session-ID': generate_session(),
            'X-Device-ID': generate_device_id(),
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        
        url = f"{BASE_URL}/?rc={rc}"
        
        print(f"\n🔄 New Request:")
        print(f"📱 RC: {rc}")
        print(f"🌐 IP: {headers['X-Forwarded-For']}")
        print(f"🔧 Browser: {headers['User-Agent'][:50]}...")
        print(f"🆔 Session: {headers['X-Session-ID']}")
        
        response = session.get(url, headers=headers, timeout=30)
        
        response_time = round(time.time() - start_time, 2)
        
        try:
            data = response.json()
            
            # Add metadata
            result = {
                "success": True,
                "data": data,
                "meta": {
                    "response_time_seconds": response_time,
                    "session_id": headers['X-Session-ID'],
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
            }
            
            return jsonify(result)
            
        except:
            return jsonify({
                "success": True,
                "raw": response.text[:2000],
                "meta": {
                    "response_time_seconds": response_time,
                    "session_id": headers['X-Session-ID']
                }
            })
            
    except requests.exceptions.Timeout:
        return jsonify({
            "error": True,
            "message": "Request timeout"
        }), 504
    except Exception as e:
        return jsonify({
            "error": True,
            "message": str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "running",
        "service": "Car Info Proxy API - Unlimited Sessions",
        "features": [
            "Har request naya IP",
            "Har request naya Browser",
            "Har request naya Session",
            "Unlimited requests"
        ]
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Car Info Unlimited API",
        "usage": "/rc?term=MH02FZ0555",
        "info": "Har request naya session - koi limit nahi"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"""
    🔥 CAR INFO UNLIMITED API
    📍 Port: {port}
    💡 Usage: /rc?term=MH02FZ0555
    🔄 Feature: Har request = Naya IP + Naya Browser
    """)
    app.run(host='0.0.0.0', port=port, debug=False)
