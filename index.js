// ============================================
// 🚗 BRONX RC API V2.0 – ULTIMATE ANTI-KILLER
// 2000+ Sessions • 50+ Browsers • Never Blocked
// ============================================
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;
const CREDIT = "@BRONX_ULTRA";

// ============ REAL API ============
const REAL_API = "https://car-info-super.onrender.com/?rc=";

// ============ 50+ USER AGENTS (Chrome, Firefox, Safari, Opera, Brave, Edge) ============
const USER_AGENTS = [
    // Chrome Android
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nothing Phone 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2211) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S24) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; moto g60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    // Chrome Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    // Firefox
    "Mozilla/5.0 (Android 13; Mobile; rv:121.0) Gecko/121.0 Firefox/121.0",
    "Mozilla/5.0 (Android 14; Mobile; rv:122.0) Gecko/122.0 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.3; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux i686; rv:120.0) Gecko/20100101 Firefox/120.0",
    // Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    // Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 EdgA/120.0.0.0",
    // Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 OPR/80.0.0.0",
    // Brave
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Brave/1.60.0",
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Brave/1.60.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Brave/1.61.0",
    // Samsung Browser
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/120.0.0.0 Mobile Safari/537.36",
    // UC Browser
    "Mozilla/5.0 (Linux; U; Android 13; en-US; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UCBrowser/16.0 Mobile Safari/537.36",
    // DuckDuckGo
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.0.0 Mobile Safari/537.36 DuckDuckGo/5.0",
    // Xiaomi
    "Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.0",
    // Huawei
    "Mozilla/5.0 (Linux; Android 12; HarmonyOS; ALN-AL80) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/15.0 Mobile Safari/537.36",
    // Vivaldi
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Vivaldi/6.5.0",
    // iOS Chrome
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.0.0 Mobile/15E148 Safari/604.1",
    // iOS Firefox
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15",
    // Tablets
    "Mozilla/5.0 (Linux; Android 13; SM-X906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    // More variety
    "Mozilla/5.0 (Linux; Android 12; moto g62 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; LGE LM-G900N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SHARP AQUOS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
];

// ============ REFERERS ============
const REFERERS = [
    "https://www.google.com/",
    "https://www.google.co.in/",
    "https://www.google.com/search?q=vehicle+rc+details",
    "https://www.google.co.in/search?q=rc+status+check",
    "https://www.bing.com/",
    "https://search.yahoo.com/",
    "https://duckduckgo.com/",
    "https://m.facebook.com/",
    "https://www.instagram.com/",
    "https://t.me/",
    "https://www.reddit.com/",
    "https://in.pinterest.com/",
    "",
];

// ============ LANGUAGES ============
const LANGUAGES = [
    "en-US,en;q=0.9",
    "en-IN,en;q=0.9,hi;q=0.8",
    "en-GB,en;q=0.9",
    "hi-IN,hi;q=0.9,en;q=0.8",
    "en-US,en;q=0.9,es;q=0.8",
    "en-US,en;q=0.9,fr;q=0.7",
    "",
];

// ============ SEC-CH-UA (Browser identity) ============
const SEC_CH_UA = [
    '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    '"Google Chrome";v="120", "Chromium";v="120", "Not?A_Brand";v="24"',
    '"Not_A Brand";v="99", "Google Chrome";v="122", "Chromium";v="122"',
    '"Microsoft Edge";v="120", "Chromium";v="120", "Not?A_Brand";v="24"',
    '"Brave";v="120", "Chromium";v="120", "Not?A_Brand";v="24"',
    '"Opera";v="106", "Chromium";v="120", "Not?A_Brand";v="24"',
];

function getRandomHeaders() {
    const ua = USER_AGENTS[Math.floor(Math.random() * USER_AGENTS.length)];
    const isMobile = ua.includes('Mobile') || ua.includes('Android') || ua.includes('iPhone');
    
    return {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": LANGUAGES[Math.floor(Math.random() * LANGUAGES.length)],
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": REFERERS[Math.floor(Math.random() * REFERERS.length)],
        "Cache-Control": Math.random() > 0.5 ? "no-cache" : "max-age=0",
        "Pragma": Math.random() > 0.5 ? "no-cache" : "",
        "Sec-Ch-Ua": SEC_CH_UA[Math.floor(Math.random() * SEC_CH_UA.length)],
        "Sec-Ch-Ua-Mobile": isMobile ? "?1" : "?0",
        "Sec-Ch-Ua-Platform": isMobile ? '"Android"' : '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": Math.random() > 0.5 ? "none" : "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Connection": "keep-alive",
        "X-Forwarded-For": `${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}`,
        "X-Real-IP": `${Math.floor(Math.random()*223)+1}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}`,
    };
}

// ============ CORS ============
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    if (req.method === 'OPTIONS') return res.sendStatus(200);
    next();
});

app.use(express.json());

// ============ HOME ============
app.get('/', (req, res) => {
    const H = `${req.protocol}://${req.get('host')}`;
    res.send(`<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 BRONX RC API V2</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:'Rajdhani',sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(0,150,255,.06),transparent 60%),radial-gradient(ellipse at 80% 100%,rgba(139,0,255,.04),transparent 60%);pointer-events:none;z-index:0}
.card{background:rgba(5,15,35,.9);border:1px solid rgba(0,150,255,.1);border-radius:20px;padding:35px;max-width:650px;width:100%;text-align:center;position:relative;z-index:1;backdrop-filter:blur(20px)}
h1{font-family:'Orbitron',sans-serif;font-size:26px;background:linear-gradient(90deg,#0096ff,#00d4ff,#8b00ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:8px}
.badge{display:inline-block;background:rgba(0,255,136,.06);color:#00ff88;padding:4px 14px;border-radius:20px;font-size:10px;border:1px solid rgba(0,255,136,.12);margin:4px}
.section{background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.08);border-radius:12px;padding:16px;margin:14px 0;text-align:left}
code{color:#00ff88;font-family:monospace;font-size:10px;word-break:break-all;display:block;margin:6px 0;background:rgba(0,0,0,.3);padding:8px;border-radius:6px}
input{width:100%;padding:12px;background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.08);border-radius:10px;color:#fff;font-size:14px;outline:none;margin:8px 0;font-family:'Rajdhani',sans-serif}
input:focus{border-color:#0096ff}
button{width:100%;padding:14px;background:linear-gradient(135deg,#0096ff,#0066cc);color:#fff;border:none;border-radius:10px;font-weight:700;cursor:pointer;font-family:'Orbitron',sans-serif;font-size:14px;margin:6px 0;transition:.3s}
button:hover{transform:scale(1.02);box-shadow:0 0 25px rgba(0,150,255,.2)}
.result{background:rgba(0,0,0,.5);border:1px solid rgba(0,255,136,.08);border-radius:10px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:500px;overflow:auto}
.result.show{display:block}
pre{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap}
</style></head><body>
<div class="card">
<h1>🚗 BRONX RC API V2</h1>
<p style="color:#667;font-size:12px">ULTIMATE ANTI-KILLER • ${USER_AGENTS.length}+ Browsers • Never Blocked</p>
<div style="margin:10px 0"><span class="badge">🔄 Auto Rotate</span><span class="badge">📱 ${USER_AGENTS.length} UAs</span><span class="badge">🎭 Fake IPs</span><span class="badge">⚡ Unlimited</span></div>
<div class="section"><p style="color:#0096ff;font-weight:700">🔗 API</p><code>GET /rc?term=MH02FZ0555</code></div>
<input type="text" id="rcInput" placeholder="RC Number (e.g., MH02FZ0555)">
<button onclick="lookup()">🔍 LOOKUP</button>
<div class="result" id="result"><pre id="resultData"></pre></div>
<p style="color:#667;font-size:10px;margin-top:14px">@BRONX_ULTRA</p>
</div>
<script>
async function lookup(){
var n=document.getElementById('rcInput').value.trim();if(!n)return alert('Enter RC!');
var d=document.getElementById('result'),p=document.getElementById('resultData');
d.classList.add('show');p.style.color='#ffb400';p.textContent='🔍 Searching...';
try{var r=await fetch('/rc?term='+encodeURIComponent(n));var j=await r.json();p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2)}catch(e){p.style.color='#ff3366';p.textContent='❌ '+e.message}}
</script>
</body></html>`);
});

// ============ RC API ENDPOINT ============
app.get('/rc', async (req, res) => {
    let rc = req.query.term || req.query.num || req.query.rc || '';
    rc = rc.trim().toUpperCase().replace(/ /g, '').replace(/-/g, '');
    
    if (!rc) {
        return res.status(400).json({
            status: "error",
            message: "Missing RC number. Use: /rc?term=MH02FZ0555",
            credit: CREDIT
        });
    }
    
    // ✅ FRESH HEADERS FOR EVERY REQUEST
    const headers = getRandomHeaders();
    
    console.log(`[${new Date().toISOString()}] Looking up: ${rc}`);
    console.log(`  UA: ${headers['User-Agent'].substring(0, 60)}...`);
    console.log(`  IP: ${headers['X-Forwarded-For']}`);
    
    try {
        const response = await axios.get(`${REAL_API}${encodeURIComponent(rc)}`, {
            headers: headers,
            timeout: 30000,
            maxRedirects: 5
        });
        
        if (response.status !== 200) {
            return res.status(500).json({
                status: "error",
                message: `API returned HTTP ${response.status}`,
                credit: CREDIT
            });
        }
        
        let data;
        try {
            data = response.data;
            // If string, try to parse
            if (typeof data === 'string') {
                try { data = JSON.parse(data); } catch(e) {}
            }
        } catch(e) {
            data = { raw: response.data };
        }
        
        // Add credit info
        if (typeof data === 'object' && !Array.isArray(data)) {
            data.credit = CREDIT;
            data.developer = CREDIT;
            data.powered_by = "BRONX ULTRA API";
            data._anti_killer = {
                user_agents: USER_AGENTS.length,
                browsers: "50+ (Chrome, Firefox, Safari, Edge, Opera, Brave, Samsung, UC, DuckDuckGo)",
                sessions: "Unlimited - New identity per request",
                fake_ips: true,
                random_headers: true,
                note: "Each request uses random User-Agent, Referer, Language, Sec-Ch-Ua, and Fake IP"
            };
        }
        
        console.log(`[✅] Success: ${rc}`);
        return res.json(data);
        
    } catch (error) {
        console.log(`[❌] Error: ${error.message}`);
        return res.status(500).json({
            status: "error",
            message: `API Error: ${error.message}`,
            credit: CREDIT
        });
    }
});

// ============ TEST ============
app.get('/test', (req, res) => {
    res.json({
        status: "✅ BRONX RC API V2 ONLINE",
        endpoint: "/rc?term=MH02FZ0555",
        features: {
            user_agents: USER_AGENTS.length,
            browsers: "Chrome, Firefox, Safari, Edge, Opera, Brave, Samsung, UC, DuckDuckGo, Vivaldi",
            anti_detection: ["Random UA", "Random Referer", "Random Language", "Random Sec-Ch-Ua", "Fake IPs", "Random Headers"],
            sessions: "Unlimited - New identity every request"
        },
        credit: CREDIT
    });
});

// ============ 404 ============
app.use((req, res) => {
    res.status(404).json({ error: "Not found", home: "/", test: "/test", api: "/rc?term=RC_NUMBER" });
});

// ============ START ============
app.listen(PORT, '0.0.0.0', () => {
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    console.log('🚗 BRONX RC API V2.0');
    console.log('🔥 ULTIMATE ANTI-KILLER');
    console.log(`📱 ${USER_AGENTS.length} Browsers`);
    console.log(`🔄 Auto Rotate • Fake IPs`);
    console.log(`🚀 http://localhost:${PORT}`);
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
});
