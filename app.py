# ============================================
# 🚗 BRONX RC PROXY V4 - REAL PROXY ROTATION
# Uses Free Proxies • Different Real IPs
# ============================================
from flask import Flask, request, jsonify
import requests
import random
import time
import os
import threading

app = Flask(__name__)

CREDIT = "@BRONX_ULTRA"
REAL_API = "https://car-info-super.onrender.com"

# 🔥 FREE PROXY POOL - Auto-updated
PROXY_LIST = []
working_proxies = []
total_requests = 0
success_count = 0

def fetch_free_proxies():
    """Fetch free proxies from multiple sources"""
    global PROXY_LIST
    
    proxies = set()
    
    # Source 1: proxyscrape
    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all", timeout=10)
        for line in r.text.strip().split('\n'):
            line = line.strip()
            if line:
                proxies.add(line)
    except: pass
    
    # Source 2: proxy-list.download
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=http", timeout=10)
        for line in r.text.strip().split('\n'):
            line = line.strip()
            if line:
                proxies.add(line)
    except: pass
    
    # Source 3: openproxy.space
    try:
        r = requests.get("https://openproxy.space/list/http", timeout=10)
        for line in r.text.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                proxies.add(line)
    except: pass
    
    PROXY_LIST = list(proxies)
    print(f"✅ Fetched {len(PROXY_LIST)} proxies!")

def check_proxy(proxy):
    """Test if proxy works with our API"""
    try:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        r = requests.get(REAL_API, proxies=proxies, timeout=5)
        if r.status_code == 200:
            return True
    except:
        pass
    return False

def find_working_proxies():
    """Find working proxies in background"""
    global working_proxies
    while True:
        print(f"🔄 Testing {len(PROXY_LIST)} proxies...")
        working = []
        for proxy in PROXY_LIST[:50]:  # Test 50 at a time
            if check_proxy(proxy):
                working.append(proxy)
                print(f"✅ Working: {proxy}")
        working_proxies = working
        print(f"🔥 {len(working_proxies)} working proxies!")
        
        # Refresh proxy list if low
        if len(working_proxies) < 5:
            fetch_free_proxies()
        
        time.sleep(300)  # Refresh every 5 minutes

def get_random_proxy():
    """Get random working proxy"""
    global working_proxies
    if working_proxies:
        return random.choice(working_proxies)
    return None

# Browser signatures
BROWSERS = [
    {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36", "name": "Chrome/Win"},
    {"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Version/17.1 Mobile/15E148 Safari/604.1", "name": "Safari/iPhone"},
    {"ua": "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 Chrome/120.0.6099.144 Mobile Safari/537.36", "name": "Chrome/Android"},
    {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36", "name": "Chrome/Mac"},
    {"ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36", "name": "Chrome/Linux"},
]

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 BRONX RC PROXY V4</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
.card{background:#0a1a2a;border:1px solid #ff0080;border-radius:20px;padding:30px;max-width:700px;width:100%;text-align:center}
h1{color:#ff0080;font-size:22px}
.badge{display:inline-block;padding:4px 10px;border-radius:20px;font-size:9px;margin:3px;background:rgba(255,0,128,.1);color:#ff0080;border:1px solid rgba(255,0,128,.3)}
.badge.g{color:#00ff88;border-color:rgba(0,255,136,.3)}
.badge.y{color:#ffb400;border-color:rgba(255,180,0,.3)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:10px 0}
.st{background:#000;padding:10px;border-radius:8px;text-align:center}
.st .v{font-size:18px;font-weight:700;color:#ff0080}
.st .l{font-size:7px;color:#666}
code{color:#00ff88;background:#000;padding:8px;display:block;margin:8px 0;border-radius:8px;font-size:11px}
input{width:100%;padding:12px;background:#000;border:1px solid #ff0080;border-radius:8px;color:#fff;font-size:14px;margin:6px 0}
button{width:100%;padding:14px;background:#ff0080;color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;font-size:14px;margin:4px 0}
button:hover{background:#ff1493}
.result{background:#000;border:1px solid #00ff88;border-radius:8px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:400px;overflow:auto}
.result.show{display:block}
pre{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX RC PROXY V4</h1>
<p style="color:#666;font-size:11px">REAL Proxy Rotation • Different IPs</p>
<div style="margin:8px 0">
<span class="badge y">🌐 Real Proxies</span>
<span class="badge g">🔄 Auto Rotate</span>
<span class="badge">📱 Multi-Browser</span>
<span class="badge g">∞ Unlimited</span>
</div>
<div class="stats">
<div class="st"><div class="v" id="proxies">0</div><div class="l">PROXIES</div></div>
<div class="st"><div class="v" id="total">0</div><div class="l">REQUESTS</div></div>
<div class="st"><div class="v" id="success">0</div><div class="l">SUCCESS</div></div>
<div class="st"><div class="v" id="ip">-</div><div class="l">LAST IP</div></div>
</div>
<code>GET /rc?term=MH02FZ0555</code>
<input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
<button onclick="lookup()">🔍 FETCH WITH NEW IP</button>
<div class="result" id="result"><pre id="resultData"></pre></div>
<p style="color:#444;font-size:9px;margin-top:10px">@BRONX_ULTRA</p>
</div>
<script>
var t=0,s=0;
async function lookup(){
var n=document.getElementById('rcInput').value.trim();
if(!n)return;
var d=document.getElementById('result'),p=document.getElementById('resultData');
d.classList.add('show');p.style.color='#ffb400';p.textContent='Connecting through NEW proxy IP...';
try{
var r=await fetch('/rc?term='+encodeURIComponent(n));
var j=await r.json();
p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2);
t++;
if(j._proxy&&j._proxy.success) s++;
document.getElementById('total').textContent=t;
document.getElementById('success').textContent=s;
if(j._proxy){
document.getElementById('ip').textContent=j._proxy.ip||'-';
document.getElementById('proxies').textContent=j._proxy.pool_size||0;
}
}catch(e){
p.style.color='#ff0080';p.textContent='Error: '+e.message;
t++;
document.getElementById('total').textContent=t;
}
}
</script>
</body></html>'''

@app.route('/rc')
def rc_proxy():
    global total_requests, success_count
    total_requests += 1
    
    term = request.args.get('term', '').strip().upper().replace(' ', '').replace('-', '')
    
    if not term:
        return jsonify({"error": "Missing RC number"}), 400
    
    browser = random.choice(BROWSERS)
    proxy = get_random_proxy()
    
    headers = {
        "User-Agent": browser["ua"],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }
    
    try:
        # METHOD 1: With proxy
        if proxy:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            resp = requests.get(
                f"{REAL_API}/?rc={term}",
                headers=headers,
                proxies=proxies,
                timeout=15
            )
            
            if resp.status_code == 200:
                try:
                    data = resp.json()
                    success_count += 1
                    data["_proxy"] = {
                        "ip": proxy.split(":")[0],
                        "browser": browser["name"],
                        "pool_size": len(working_proxies),
                        "success": True,
                        "credit": CREDIT
                    }
                    return jsonify(data)
                except:
                    pass
        
        # METHOD 2: Direct (fallback)
        resp = requests.get(f"{REAL_API}/?rc={term}", headers=headers, timeout=15)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                success_count += 1
                data["_proxy"] = {
                    "ip": "direct",
                    "browser": browser["name"],
                    "success": True,
                    "credit": CREDIT
                }
                return jsonify(data)
            except:
                return jsonify({
                    "status": "success",
                    "data": resp.text[:5000],
                    "_proxy": {"ip": "direct", "success": True, "credit": CREDIT}
                })
        
        return jsonify({
            "success": resp.status_code == 200,
            "message": resp.text[:500] if resp.text else f"Status: {resp.status_code}",
            "_proxy": {
                "ip": proxy.split(":")[0] if proxy else "direct",
                "browser": browser["name"],
                "pool_size": len(working_proxies),
                "success": False,
                "credit": CREDIT
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)[:200],
            "_proxy": {"success": False, "credit": CREDIT}
        }), 500

@app.route('/proxies')
def list_proxies():
    return jsonify({
        "total": len(PROXY_LIST),
        "working": len(working_proxies),
        "proxies": working_proxies[:20]
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "api": "/rc?term=MH02FZ0555"}), 404

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Initial fetch
    fetch_free_proxies()
    
    # Start proxy checker in background
    checker = threading.Thread(target=find_working_proxies, daemon=True)
    checker.start()
    
    port = int(os.environ.get('PORT', 3000))
    print(f"🚗 BRONX RC PROXY V4 - REAL IP ROTATION")
    print(f"🌐 {len(PROXY_LIST)} Proxies Fetched")
    print(f"🚀 http://localhost:{port}")
    app.run(host='0.0.0.0', port=port)
