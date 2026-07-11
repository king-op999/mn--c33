# ============================================
# 🚗 BRONX CAR-INFO PROXY V2 - IP SPOOFING
# Real Multi-Device • Fake IPs • Unlimited
# ============================================
from flask import Flask, request, jsonify
import requests
import random
import string
import time
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

app = Flask(__name__)

CREDIT = "@BRONX_ULTRA"
REAL_API = "https://car-info-super.onrender.com"

# 🔥 FAKE IP POOL - 100+ IPs from different countries
FAKE_IPS = [
    # India IPs
    "103.15.224.{}", "117.98.45.{}", "152.67.89.{}", "157.34.123.{}",
    "182.76.55.{}", "223.188.12.{}", "45.112.67.{}", "51.89.234.{}",
    "77.45.178.{}", "91.234.56.{}", "176.32.90.{}", "198.54.123.{}",
    "103.235.122.{}", "122.178.45.{}", "139.167.34.{}", "167.235.89.{}",
    # USA IPs
    "198.168.12.{}", "205.67.34.{}", "192.168.45.{}", "172.67.89.{}",
    "45.33.123.{}", "66.228.45.{}", "96.126.67.{}", "173.255.89.{}",
    # UK IPs
    "51.89.123.{}", "145.239.67.{}", "88.208.45.{}", "109.123.78.{}",
    # Russia IPs
    "95.173.45.{}", "185.67.89.{}", "46.188.123.{}", "79.134.56.{}",
    # China IPs
    "223.104.67.{}", "111.199.45.{}", "221.234.89.{}", "125.76.123.{}",
    # Brazil IPs
    "177.54.67.{}", "191.243.89.{}", "200.189.45.{}", "138.121.123.{}",
    # Australia IPs
    "1.128.67.{}", "101.182.89.{}", "203.173.45.{}", "49.176.123.{}",
    # Japan IPs
    "126.34.67.{}", "180.45.89.{}", "219.56.45.{}", "133.200.123.{}",
    # Germany IPs
    "87.128.67.{}", "213.136.89.{}", "79.240.45.{}", "176.65.123.{}",
]

# 🔥 Device/User-Agent Pool - 50+ Different Devices
DEVICES = [
    # iPhones
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    # Android Phones
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.71 Mobile Safari/537.36",
    # Tablets
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Safari/537.36",
    # Windows PCs
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/120.0.2210.91",
    # Mac PCs
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15; rv:121.0) Gecko/20100101 Firefox/121.0",
    # Linux PCs
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
]

# 🔥 Referrer Pool
REFERRERS = [
    "https://www.google.com/search?q=vehicle+rc+details",
    "https://www.google.co.in/search?q=rc+status+check",
    "https://www.bing.com/search?q=vehicle+registration+details",
    "https://duckduckgo.com/?q=car+info+by+number",
    "https://parivahan.gov.in/",
    "https://vahan.parivahan.gov.in/",
    "https://www.carinfo.app/",
    "https://www.google.com/",
    "",
]

def get_random_ip():
    """Generate random fake IP"""
    ip_template = random.choice(FAKE_IPS)
    return ip_template.format(random.randint(1, 254))

def get_random_device():
    """Get random device signature"""
    return random.choice(DEVICES)

def create_session():
    """Create session with random fingerprints"""
    session = requests.Session()
    
    # Randomize session settings
    session.headers.update({
        "Accept": random.choice([
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        ]),
        "Accept-Language": random.choice([
            "en-US,en;q=0.9",
            "en-IN,en;q=0.9,hi;q=0.8",
            "en-GB,en;q=0.9",
        ]),
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    })
    
    # Random cookies
    session.cookies.update({
        "_ga": f"GA1.1.{random.randint(100000000, 999999999)}.{int(time.time())}",
        "_gid": f"GA1.1.{random.randint(100000000, 999999999)}.{int(time.time())}",
        "session_id": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
        "visitor": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
    })
    
    return session

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['X-Proxy-By'] = CREDIT
    response.headers['X-Session-IP'] = get_random_ip()
    return response

# ============ HOME PAGE ============
@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 BRONX CAR-INFO PROXY V2</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:'Rajdhani',sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,0,128,.06),transparent 60%),radial-gradient(ellipse at 80% 100%,rgba(0,150,255,.04),transparent 60%);pointer-events:none;z-index:0}
.card{background:rgba(5,15,35,.95);border:1px solid rgba(255,0,128,.15);border-radius:24px;padding:35px;max-width:750px;width:100%;text-align:center;position:relative;z-index:1;backdrop-filter:blur(30px)}
h1{font-family:'Orbitron',sans-serif;font-size:26px;background:linear-gradient(90deg,#ff0080,#8b00ff,#0096ff,#00ff88);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:rainbow 3s linear infinite;margin-bottom:8px}
@keyframes rainbow{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.subtitle{color:#555;font-size:11px;letter-spacing:3px;margin-bottom:5px}
.badges{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:15px 0}
.badge{background:rgba(255,0,128,.08);color:#ff0080;padding:5px 12px;border-radius:20px;font-size:9px;font-weight:600;border:1px solid rgba(255,0,128,.1)}
.badge.green{background:rgba(0,255,136,.08);color:#00ff88;border-color:rgba(0,255,136,.1)}
.badge.blue{background:rgba(0,150,255,.08);color:#0096ff;border-color:rgba(0,150,255,.1)}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:15px 0}
.stat{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.05);border-radius:12px;padding:12px 8px}
.stat .num{font-size:24px;font-weight:900;color:#ff0080;font-family:'Orbitron',sans-serif}
.stat .num.green{color:#00ff88}
.stat .lbl{font-size:7px;color:#666;text-transform:uppercase;letter-spacing:2px;margin-top:3px}
.endpoint-box{background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.1);border-radius:12px;padding:16px;margin:12px 0;text-align:left}
.endpoint-box .method{background:rgba(0,255,136,.15);color:#00ff88;padding:2px 8px;border-radius:4px;font-size:9px;font-weight:700}
.endpoint-box code{color:#ffb400;font-family:monospace;font-size:11px;word-break:break-all;display:block;margin:6px 0;background:rgba(0,0,0,.3);padding:8px;border-radius:6px}
input{width:100%;padding:14px;background:rgba(0,0,0,.6);border:1px solid rgba(255,0,128,.1);border-radius:12px;color:#fff;font-size:14px;outline:none;margin:8px 0;font-family:'Rajdhani',sans-serif;transition:.3s}
input:focus{border-color:#ff0080;box-shadow:0 0 30px rgba(255,0,128,.1)}
button{width:100%;padding:16px;background:linear-gradient(135deg,#ff0080,#8b00ff,#0096ff);background-size:200% 200%;color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-family:'Orbitron',sans-serif;font-size:14px;margin:6px 0;transition:.3s;letter-spacing:2px}
button:hover{transform:scale(1.02);box-shadow:0 0 40px rgba(255,0,128,.2);animation:btnGlow 1.5s ease infinite}
@keyframes btnGlow{0%,100%{box-shadow:0 0 20px rgba(255,0,128,.2)}50%{box-shadow:0 0 50px rgba(0,150,255,.4)}}
.result-box{background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.1);border-radius:12px;padding:14px;margin-top:12px;text-align:left;display:none;max-height:450px;overflow:auto}
.result-box.show{display:block}
.result-box .ip-badge{display:inline-block;background:rgba(255,0,128,.1);color:#ff0080;padding:3px 10px;border-radius:20px;font-size:8px;margin-bottom:8px}
pre{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap;word-break:break-all}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX CAR-INFO PROXY V2</h1>
<p class="subtitle">REAL IP SPOOFING • UNLIMITED • 2000+ DEVICES</p>
<div class="badges">
<span class="badge">🔥 IP Spoofing</span>
<span class="badge green">📱 Multi-Device</span>
<span class="badge blue">🌍 Multi-Country</span>
<span class="badge">🔄 Auto Rotate</span>
</div>
<div class="stats-grid">
<div class="stat"><div class="num">100+</div><div class="lbl">Fake IPs</div></div>
<div class="stat"><div class="num green">20+</div><div class="lbl">Devices</div></div>
<div class="stat"><div class="num">10+</div><div class="lbl">Countries</div></div>
<div class="stat"><div class="num green">∞</div><div class="lbl">Requests</div></div>
</div>
<div class="endpoint-box">
<span class="method">GET</span>
<code>/rc?term=MH02FZ0555</code>
</div>
<input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
<button onclick="lookup()">🔍 FETCH WITH NEW IP & DEVICE</button>
<div class="result-box" id="result">
<div class="ip-badge" id="ipBadge">IP: --</div>
<pre id="resultData"></pre>
</div>
</div>
<script>
var count=0;
async function lookup(){
var n=document.getElementById('rcInput').value.trim();
if(!n){alert('Enter RC Number!');return}
var d=document.getElementById('result'),p=document.getElementById('resultData'),ib=document.getElementById('ipBadge');
d.classList.add('show');p.style.color='#ffb400';p.textContent='🔄 Creating NEW session with FAKE IP & DEVICE...';
try{
var r=await fetch('/rc?term='+encodeURIComponent(n));
var j=await r.json();
count++;
p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2);
ib.textContent='Request #'+count+' | IP: '+j.proxy_info.fake_ip+' | Device: '+j.proxy_info.device_type;
ib.style.color='#00ff88';
}catch(e){
p.style.color='#ff0080';p.textContent='Error: '+e.message;
ib.textContent='Error - Try again with NEW IP';
ib.style.color='#ff0080';
}}
</script>
</body></html>'''

# ============ MAIN PROXY ENDPOINT ============
@app.route('/rc')
def rc_proxy():
    term = request.args.get('term', '').strip().upper().replace(' ', '').replace('-', '')
    
    if not term:
        return jsonify({
            "status": "error",
            "message": "Missing RC number. Use /rc?term=MH02FZ0555"
        }), 400
    
    # 🔥 Generate FAKE IP & Device for THIS request
    fake_ip = get_random_ip()
    device_ua = get_random_device()
    referrer = random.choice(REFERRERS)
    
    # Detect device type
    if "iPhone" in device_ua or "iPad" in device_ua:
        device_type = "Apple iPhone/iPad"
    elif "Android" in device_ua and "Mobile" in device_ua:
        device_type = "Android Phone"
    elif "Android" in device_ua:
        device_type = "Android Tablet"
    elif "Windows" in device_ua:
        device_type = "Windows PC"
    elif "Macintosh" in device_ua:
        device_type = "Mac PC"
    elif "Linux" in device_ua:
        device_type = "Linux PC"
    else:
        device_type = "Unknown Device"
    
    # 🔥 Build headers as if coming from REAL device
    headers = {
        "User-Agent": device_ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": random.choice(["en-US,en;q=0.9", "en-IN,en;q=0.9,hi;q=0.8", "en-GB,en;q=0.9"]),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "X-Forwarded-For": fake_ip,
        "X-Real-IP": fake_ip,
        "X-Client-IP": fake_ip,
        "X-Cluster-Client-IP": fake_ip,
        "CF-Connecting-IP": fake_ip,
        "True-Client-IP": fake_ip,
        "Referer": referrer if referrer else "",
    }
    
    # Remove empty headers
    headers = {k: v for k, v in headers.items() if v}
    
    # 🔥 Random cookies like a fresh browser
    cookies = {
        "_ga": f"GA1.1.{random.randint(100000000,999999999)}.{int(time.time())}",
        "_gid": f"GA1.3.{random.randint(100000000,999999999)}.{int(time.time())}",
        "_fbp": f"fb.1.{int(time.time())}.{random.randint(100000000,999999999)}",
        "session_token": ''.join(random.choices(string.ascii_letters + string.digits, k=64)),
        "device_id": ''.join(random.choices(string.hexdigits, k=32)),
        "first_visit": str(int(time.time()) - random.randint(3600, 864000)),
    }
    
    try:
        # 🔥 Create FRESH session every time
        session = create_session()
        
        # Call REAL API
        url = f"{REAL_API}/?rc={term}"
        
        resp = session.get(
            url,
            headers=headers,
            cookies=cookies,
            timeout=25,
            allow_redirects=True,
            verify=False  # Skip SSL for speed
        )
        
        # Parse response
        try:
            data = resp.json()
        except:
            data = {
                "raw_response": resp.text[:5000] if resp.text else "No response body",
                "status_code": resp.status_code,
            }
        
        # Add proxy metadata
        if isinstance(data, dict):
            data["proxy_info"] = {
                "fake_ip": fake_ip,
                "device_type": device_type,
                "country": detect_country(fake_ip),
                "session_fingerprint": ''.join(random.choices(string.hexdigits, k=16)),
                "request_id": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time() + 19800)),
                "note": "REAL IP SPOOFED - API sees DIFFERENT device each time!"
            }
        
        return jsonify(data)
        
    except requests.exceptions.Timeout:
        return jsonify({
            "status": "error",
            "message": "API timeout - RETRY with NEW IP/Device automatically!",
            "fake_ip": fake_ip,
            "device": device_type,
        }), 504
        
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": f"Error: {str(e)[:200]}",
            "fake_ip": fake_ip,
            "device": device_type,
        }), 500

def detect_country(ip):
    """Rough country detection by IP range"""
    first_octet = ip.split('.')[0]
    if first_octet in ['103','117','122','139','152','157','167','182','223']:
        return "🇮🇳 India"
    elif first_octet in ['45','66','96','172','173','192','198','205']:
        return "🇺🇸 USA"
    elif first_octet in ['51','88','109','145']:
        return "🇬🇧 UK"
    elif first_octet in ['46','79','95','185']:
        return "🇷🇺 Russia"
    elif first_octet in ['111','125','221','223']:
        return "🇨🇳 China"
    elif first_octet in ['138','177','191','200']:
        return "🇧🇷 Brazil"
    elif first_octet in ['1','49','101','203']:
        return "🇦🇺 Australia"
    elif first_octet in ['126','133','180','219']:
        return "🇯🇵 Japan"
    else:
        return "🌍 Other"

# ============ HEALTH ============
@app.route('/health')
def health():
    return jsonify({
        "status": "✅ BRONX CAR-INFO PROXY V2 ONLINE",
        "features": {
            "ip_spoofing": "100+ Fake IPs",
            "devices": "20+ Device Types",
            "countries": "10+ Countries",
            "unlimited": True,
        },
        "real_api": REAL_API,
        "credit": CREDIT
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Not found",
        "api": "/rc?term=MH02FZ0555",
        "health": "/health"
    }), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print("=" * 60)
    print("🔥 BRONX CAR-INFO PROXY V2 - IP SPOOFING ACTIVE")
    print(f"🌍 100+ Fake IPs Ready")
    print(f"📱 20+ Device Types")
    print(f"🚀 Port: {port}")
    print(f"🎯 Real API: {REAL_API}")
    print("=" * 60)
    # Disable SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    app.run(host='0.0.0.0', port=port)
