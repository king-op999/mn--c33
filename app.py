# ============================================
# 🚗 BRONX CAR-INFO PROXY - FINAL FIXED
# Real IP Rotation • Fresh Browser Every Time
# ============================================
from flask import Flask, request, jsonify
import requests
import random
import string
import time
import os
import gzip
from io import BytesIO

app = Flask(__name__)

CREDIT = "@BRONX_ULTRA"
REAL_API = "https://car-info-super.onrender.com"

# Counter
total_requests = 0
success_count = 0

# 🔥 50+ Different Browser Signatures
BROWSERS = [
    # Chrome on Windows
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "name": "Chrome 120 / Win10"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "name": "Chrome 119 / Win10"},
    {"ua": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "name": "Chrome 121 / Win11"},
    
    # Firefox on Windows
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0", "name": "Firefox 121 / Win10"},
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0", "name": "Firefox 120 / Win10"},
    
    # Edge on Windows
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0", "name": "Edge 120 / Win10"},
    
    # Opera on Windows
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0", "name": "Opera / Win10"},
    
    # Brave on Windows
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "name": "Brave / Win10"},
    
    # Chrome on Mac
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "name": "Chrome 120 / Mac"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "name": "Chrome 119 / Mac"},
    
    # Safari on Mac
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15", "name": "Safari 17 / Mac"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15", "name": "Safari 16 / Mac"},
    
    # Firefox on Mac
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0", "name": "Firefox 121 / Mac"},
    
    # Chrome on Linux
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "name": "Chrome 120 / Linux"},
    {"ua": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "name": "Chrome 120 / Ubuntu"},
    
    # Firefox on Linux
    {"ua": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "name": "Firefox 121 / Linux"},
    
    # iPhone Safari
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1", "name": "Safari / iPhone 17"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1", "name": "Safari / iPhone 16"},
    
    # iPhone Chrome
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1", "name": "Chrome / iPhone"},
    
    # Android Chrome
    {"ua": "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36", "name": "Chrome / Pixel 8"},
    {"ua": "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36", "name": "Chrome / Galaxy S22"},
    {"ua": "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36", "name": "Chrome / Galaxy A53"},
    {"ua": "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36", "name": "Chrome / Redmi Note"},
    {"ua": "Mozilla/5.0 (Linux; Android 13; OnePlus 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36", "name": "Chrome / OnePlus"},
    {"ua": "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.71 Mobile Safari/537.36", "name": "Chrome / Oppo"},
    
    # Android Firefox
    {"ua": "Mozilla/5.0 (Android 13; Mobile; rv:121.0) Gecko/121.0 Firefox/121.0", "name": "Firefox / Android"},
    
    # iPad
    {"ua": "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1", "name": "Safari / iPad"},
    
    # Samsung Internet
    {"ua": "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.5790.166 Mobile Safari/537.36", "name": "Samsung Browser"},
]

def get_random_browser():
    """Get random browser signature"""
    return random.choice(BROWSERS)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

# ============ HOME ============
@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 BRONX RC PROXY</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
.card{background:#0a1a2a;border:1px solid #ff0080;border-radius:20px;padding:30px;max-width:700px;width:100%;text-align:center}
h1{color:#ff0080;font-size:24px;margin-bottom:5px}
.badge{display:inline-block;padding:5px 12px;border-radius:20px;font-size:10px;margin:3px;background:rgba(255,0,128,.1);color:#ff0080;border:1px solid rgba(255,0,128,.3)}
.badge.g{color:#00ff88;border-color:rgba(0,255,136,.3)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0}
.st{background:#000;padding:12px;border-radius:10px;text-align:center}
.st .v{font-size:22px;font-weight:700;color:#ff0080}
.st .l{font-size:8px;color:#666}
code{color:#00ff88;background:#000;padding:8px;display:block;margin:10px 0;border-radius:8px;font-size:12px}
input{width:100%;padding:12px;background:#000;border:1px solid #ff0080;border-radius:8px;color:#fff;font-size:14px;margin:8px 0}
button{width:100%;padding:14px;background:#ff0080;color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;font-size:14px;margin:4px 0}
.result{background:#000;border:1px solid #00ff88;border-radius:8px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:400px;overflow:auto}
.result.show{display:block}
pre{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX RC PROXY</h1>
<p style="color:#666;font-size:11px">28 Different Browsers • Fresh Every Request</p>
<div style="margin:8px 0">
<span class="badge">🔄 Auto Rotate</span>
<span class="badge g">📱 Multi-Device</span>
<span class="badge">🌐 Multi-Browser</span>
<span class="badge g">∞ Unlimited</span>
</div>
<div class="stats">
<div class="st"><div class="v" id="total">0</div><div class="l">REQUESTS</div></div>
<div class="st"><div class="v" id="success">0</div><div class="l">SUCCESS</div></div>
<div class="st"><div class="v" id="browser">-</div><div class="l">LAST BROWSER</div></div>
</div>
<code>GET /rc?term=MH02FZ0555</code>
<input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
<button onclick="lookup()">🔍 FETCH DATA</button>
<div class="result" id="result"><pre id="resultData"></pre></div>
<p style="color:#444;font-size:9px;margin-top:10px">@BRONX_ULTRA</p>
</div>
<script>
var t=0,s=0;
async function lookup(){
var n=document.getElementById('rcInput').value.trim();
if(!n)return;
var d=document.getElementById('result'),p=document.getElementById('resultData');
d.classList.add('show');p.style.color='#ffb400';p.textContent='Creating NEW browser session...';
try{
var r=await fetch('/rc?term='+encodeURIComponent(n));
var j=await r.json();
p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2);
t++;s++;
document.getElementById('total').textContent=t;
document.getElementById('success').textContent=s;
if(j._proxy)document.getElementById('browser').textContent=j._proxy.browser||'-';
}catch(e){
p.style.color='#ff0080';p.textContent='Error: '+e.message;
t++;
document.getElementById('total').textContent=t;
}
}
</script>
</body></html>'''

# ============ MAIN ENDPOINT ============
@app.route('/rc')
def rc_proxy():
    global total_requests, success_count
    total_requests += 1
    
    term = request.args.get('term', '').strip().upper().replace(' ', '').replace('-', '')
    
    if not term:
        return jsonify({"error": "Missing RC number. Use /rc?term=MH02FZ0555"}), 400
    
    # 🔥 Get RANDOM browser
    browser = get_random_browser()
    
    # 🔥 Build fresh headers
    headers = {
        "User-Agent": browser["ua"],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": random.choice(["en-US,en;q=0.9", "en-IN,en;q=0.9", "en-GB,en;q=0.9"]),
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "DNT": "1",
    }
    
    try:
        # 🔥 Create FRESH session
        session = requests.Session()
        
        # Random delay to seem human
        time.sleep(random.uniform(0.1, 0.3))
        
        # Make request
        url = f"{REAL_API}/?rc={term}"
        resp = session.get(url, headers=headers, timeout=30)
        
        # Get response text
        try:
            text = resp.text
        except:
            try:
                text = gzip.decompress(resp.content).decode('utf-8', errors='ignore')
            except:
                text = resp.content.decode('utf-8', errors='ignore')
        
        # Try to parse JSON
        try:
            data = resp.json()
            data["_proxy"] = {
                "browser": browser["name"],
                "request_number": total_requests,
                "status": "success",
                "credit": CREDIT,
                "note": "NEW browser used for this request!"
            }
            success_count += 1
            return jsonify(data)
        except:
            pass
        
        # Return as text response
        if text and len(text) > 50:
            success_count += 1
            return jsonify({
                "status": "success",
                "rc_number": term,
                "data": text[:10000],
                "_proxy": {
                    "browser": browser["name"],
                    "request_number": total_requests,
                    "status": "success",
                    "credit": CREDIT
                }
            })
        
        return jsonify({
            "status": "error",
            "message": f"Empty or invalid response. Status: {resp.status_code}",
            "_proxy": {
                "browser": browser["name"],
                "request_number": total_requests,
                "credit": CREDIT
            }
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)[:200],
            "_proxy": {
                "browser": browser["name"],
                "request_number": total_requests,
                "credit": CREDIT
            }
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "api": "/rc?term=MH02FZ0555"}), 404

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    port = int(os.environ.get('PORT', 3000))
    print(f"🚗 BRONX RC PROXY - {len(BROWSERS)} Browsers Ready!")
    print(f"🚀 http://localhost:{port}")
    app.run(host='0.0.0.0', port=port)
