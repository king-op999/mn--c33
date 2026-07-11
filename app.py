# ============================================
# 🚗 CAR-INFO SUPER PROXY API
# Multi-Session • Auto IP Rotation • Unlimited
# ============================================
from flask import Flask, request, jsonify
import requests
import random
import string
import time

app = Flask(__name__)

CREDIT = "@BRONX_ULTRA"

# Real API base
REAL_API = "https://car-info-super.onrender.com"

# 🔥 Session Pool - 2000+ unique sessions
SESSION_POOL = []
CURRENT_SESSION = 0

def generate_session_id():
    """Generate random session ID"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(32))

def init_session_pool():
    """Create 2000+ sessions at startup"""
    global SESSION_POOL
    SESSION_POOL = [generate_session_id() for _ in range(2000)]
    print(f"✅ Created {len(SESSION_POOL)} sessions!")

def get_next_session():
    """Get next session (round-robin)"""
    global CURRENT_SESSION
    session = SESSION_POOL[CURRENT_SESSION]
    CURRENT_SESSION = (CURRENT_SESSION + 1) % len(SESSION_POOL)
    return session

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# ============ HOME ============
@app.route('/')
def home():
    base = request.host_url.rstrip('/')
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 CAR-INFO SUPER PROXY</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#000a14;color:#d0d8f0;font-family:'Rajdhani',sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}}
body::before{{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(0,255,136,.06),transparent 60%),radial-gradient(ellipse at 80% 100%,rgba(139,0,255,.04),transparent 60%);pointer-events:none;z-index:0}}
.card{{background:rgba(5,15,35,.9);border:1px solid rgba(0,255,136,.1);border-radius:20px;padding:30px;max-width:700px;width:100%;text-align:center;position:relative;z-index:1;backdrop-filter:blur(20px)}}
h1{{font-family:'Orbitron',sans-serif;font-size:24px;background:linear-gradient(90deg,#00ff88,#0096ff,#8b00ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:6px}}
.badge{{display:inline-block;background:rgba(0,255,136,.06);color:#00ff88;padding:4px 14px;border-radius:20px;font-size:10px;border:1px solid rgba(0,255,136,.12);margin:4px}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0}}
.stat{{background:rgba(0,0,0,.5);border:1px solid rgba(0,255,136,.08);border-radius:10px;padding:12px 8px;text-align:center}}
.stat .val{{font-size:22px;font-weight:900;color:#00ff88;font-family:'Orbitron',sans-serif}}
.stat .lbl{{font-size:8px;color:#666;text-transform:uppercase;letter-spacing:2px;margin-top:2px}}
input{{width:100%;padding:14px;background:rgba(0,0,0,.5);border:1px solid rgba(0,255,136,.08);border-radius:10px;color:#fff;font-size:14px;outline:none;margin:8px 0;font-family:'Rajdhani',sans-serif}}
input:focus{{border-color:#00ff88}}
button{{width:100%;padding:14px;background:linear-gradient(135deg,#00ff88,#0096ff);color:#fff;border:none;border-radius:10px;font-weight:700;cursor:pointer;font-family:'Orbitron',sans-serif;font-size:14px;margin:6px 0;transition:.3s}}
button:hover{{transform:scale(1.02);box-shadow:0 0 25px rgba(0,255,136,.2)}}
.result{{background:rgba(0,0,0,.5);border:1px solid rgba(0,255,136,.08);border-radius:10px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:500px;overflow:auto}}
.result.show{{display:block}}
pre{{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap;word-break:break-all}}
code{{color:#ffb400;font-family:monospace;font-size:10px;word-break:break-all;display:block;margin:6px 0;background:rgba(0,0,0,.3);padding:8px;border-radius:6px}}
</style></head>
<body>
<div class="card">
<h1>🚗 CAR-INFO SUPER PROXY</h1>
<p style="color:#667;font-size:12px">2000+ Sessions • Auto Rotation • Unlimited</p>
<div style="margin:10px 0">
<span class="badge">🔄 Auto Session</span><span class="badge">🚫 No Limit</span><span class="badge">⚡ Fast</span>
</div>
<div class="stats">
<div class="stat"><div class="val" id="sessionCount">2000</div><div class="lbl">Sessions</div></div>
<div class="stat"><div class="val" id="usedCount">0</div><div class="lbl">Used</div></div>
<div class="stat"><div class="val">∞</div><div class="lbl">Requests</div></div>
</div>
<p style="color:#0096ff;font-weight:700">🔗 API Endpoint</p>
<code>GET /rc?term=MH02FZ0555</code>
<input type="text" id="rcInput" placeholder="RC Number (e.g., MH02FZ0555)">
<button onclick="lookup()">🔍 LOOKUP</button>
<div class="result" id="result"><pre id="resultData"></pre></div>
<p style="color:#667;font-size:10px;margin-top:14px">Proxy powered by @BRONX_ULTRA</p>
</div>
<script>
var usedCount=0;
async function lookup(){{
var n=document.getElementById('rcInput').value.trim();if(!n)return alert('Enter RC!');
var d=document.getElementById('result'),p=document.getElementById('resultData');
d.classList.add('show');p.style.color='#ffb400';p.textContent='🔄 Fetching with new session...';
try{{
var r=await fetch('/rc?term='+encodeURIComponent(n));
var j=await r.json();
p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2);
usedCount++;
document.getElementById('usedCount').textContent=usedCount;
}}catch(e){{p.style.color='#ff3366';p.textContent='❌ '+e.message}}}}
</script>
</body></html>'''

# ============ PROXY RC ENDPOINT ============
@app.route('/rc')
def rc_proxy():
    term = request.args.get('term', '').strip().upper().replace(' ', '').replace('-', '')
    
    if not term:
        return jsonify({"status": "error", "message": "Missing RC number. Use /rc?term=MH02FZ0555", "credit": CREDIT}), 400
    
    # Get fresh session
    session_id = get_next_session()
    
    # Multiple User-Agents for rotation
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    ]
    
    ua = user_agents[current_session % len(user_agents)]
    
    headers = {
        "User-Agent": ua,
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    
    # Add random cookies/session
    cookies = {
        "session_id": session_id,
        "visitor_id": generate_session_id()[:16],
        "request_count": str(random.randint(1, 100)),
    }
    
    try:
        # Call real API with rotating session
        url = f"{REAL_API}/?rc={term}"
        
        resp = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            timeout=20,
            allow_redirects=True
        )
        
        # Try to parse as JSON
        try:
            data = resp.json()
        except:
            # If not JSON, return as text
            data = {
                "status": "success",
                "raw_response": resp.text[:5000],  # Limit text size
                "content_type": resp.headers.get("content-type", "text/plain"),
            }
        
        # Add proxy info
        if isinstance(data, dict):
            data["proxy_info"] = {
                "session_used": session_id[:8] + "***",
                "session_pool": len(SESSION_POOL),
                "requests_made": CURRENT_SESSION,
                "user_agent_type": "Chrome/Firefox/Safari (rotating)",
                "proxy_by": CREDIT,
                "note": "Each request uses NEW session - NO LIMIT! 🚀"
            }
        
        return jsonify(data)
        
    except requests.exceptions.Timeout:
        return jsonify({
            "status": "error",
            "message": "Real API timeout. Try again (new session will be used).",
            "credit": CREDIT
        }), 504
        
    except requests.exceptions.ConnectionError:
        return jsonify({
            "status": "error",
            "message": "Cannot connect to real API. Check if car-info-super is online.",
            "credit": CREDIT
        }), 502
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Proxy error: {str(e)[:200]}",
            "credit": CREDIT
        }), 500

# ============ HEALTH CHECK ============
@app.route('/health')
def health():
    return jsonify({
        "status": "✅ ONLINE",
        "sessions": len(SESSION_POOL),
        "used": CURRENT_SESSION,
        "real_api": REAL_API,
        "credit": CREDIT
    })

# ============ RESET SESSIONS ============
@app.route('/reset')
def reset_sessions():
    init_session_pool()
    return jsonify({
        "status": "✅ Sessions Reset!",
        "sessions": len(SESSION_POOL),
        "message": "All 2000 fresh sessions created!"
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "home": "/", "api": "/rc?term=RC_NUMBER", "health": "/health"}), 404

if __name__ == '__main__':
    # Initialize 2000 sessions
    init_session_pool()
    
    port = int(os.environ.get('PORT', 3000))
    print("=" * 50)
    print("🚗 CAR-INFO SUPER PROXY API")
    print(f"📦 {len(SESSION_POOL)} Sessions Ready!")
    print(f"🔄 Auto Session Rotation ACTIVE")
    print(f"🎯 Real API: {REAL_API}")
    print(f"🚀 http://localhost:{port}")
    print(f"🔗 API: http://localhost:{port}/rc?term=MH02FZ0555")
    print("=" * 50)
    app.run(host='0.0.0.0', port=port)
