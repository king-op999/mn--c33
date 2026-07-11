<?php
// ============================================
// 🚗 BRONX 91WHEELS RC PROXY API
// Unlimited Sessions • Auto Rotation
// ============================================

header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, OPTIONS");
header("Access-Control-Allow-Headers: *");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$rc = trim($_GET['rc'] ?? $_GET['term'] ?? '');

// ============ HOME PAGE ============
if ($rc === '') {
    header("Content-Type: text/html");
    ?>
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🚗 BRONX 91WHEELS PROXY</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:'Segoe UI',Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,0,128,.08),transparent 60%),radial-gradient(ellipse at 80% 100%,rgba(0,150,255,.06),transparent 60%);pointer-events:none;z-index:0}
.card{background:rgba(5,15,35,.95);border:1px solid rgba(255,0,128,.15);border-radius:24px;padding:35px;max-width:700px;width:100%;text-align:center;position:relative;z-index:1;backdrop-filter:blur(30px)}
h1{font-size:24px;background:linear-gradient(90deg,#ff0080,#8b00ff,#0096ff,#00ff88);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:rainbow 3s linear infinite;margin-bottom:5px}
@keyframes rainbow{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.subtitle{color:#555;font-size:11px;letter-spacing:2px;margin-bottom:12px}
.badges{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:12px 0}
.badge{display:inline-block;padding:5px 14px;border-radius:20px;font-size:9px;font-weight:600;background:rgba(255,0,128,.08);color:#ff0080;border:1px solid rgba(255,0,128,.1)}
.badge.green{background:rgba(0,255,136,.08);color:#00ff88;border-color:rgba(0,255,136,.1)}
.badge.blue{background:rgba(0,150,255,.08);color:#0096ff;border-color:rgba(0,150,255,.1)}
.badge.yellow{background:rgba(255,180,0,.08);color:#ffb400;border-color:rgba(255,180,0,.1)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:15px 0}
.stat{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.05);border-radius:12px;padding:14px 8px}
.stat .num{font-size:24px;font-weight:900;color:#ff0080}
.stat .num.green{color:#00ff88}
.stat .lbl{font-size:7px;color:#666;text-transform:uppercase;letter-spacing:2px;margin-top:3px}
.api-box{background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.1);border-radius:12px;padding:16px;margin:12px 0;text-align:left}
.api-box .method{background:rgba(0,255,136,.15);color:#00ff88;padding:3px 10px;border-radius:5px;font-size:10px;font-weight:700}
.api-box code{color:#ffb400;font-family:'Courier New',monospace;font-size:11px;display:block;margin:8px 0;background:rgba(0,0,0,.3);padding:10px;border-radius:8px;word-break:break-all}
input{width:100%;padding:14px;background:rgba(0,0,0,.6);border:1px solid rgba(255,0,128,.15);border-radius:12px;color:#fff;font-size:15px;outline:none;margin:8px 0;transition:.3s}
input:focus{border-color:#ff0080;box-shadow:0 0 30px rgba(255,0,128,.1)}
button{width:100%;padding:16px;background:linear-gradient(135deg,#ff0080,#8b00ff,#0096ff);background-size:200% 200%;color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-size:15px;margin:8px 0;transition:.3s;letter-spacing:1px}
button:hover{transform:scale(1.02);box-shadow:0 0 40px rgba(255,0,128,.2)}
.result{background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.1);border-radius:12px;padding:14px;margin-top:12px;text-align:left;display:none;max-height:450px;overflow:auto}
.result.show{display:block}
.result .info{color:#ffb400;font-size:10px;margin-bottom:8px}
pre{color:#00ff88;font-family:'Courier New',monospace;font-size:10px;white-space:pre-wrap;word-break:break-all}
footer{color:#333;font-size:9px;margin-top:15px;letter-spacing:1px}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX 91WHEELS PROXY</h1>
<p class="subtitle">REAL RC DATA • UNLIMITED SESSIONS</p>
<div class="badges">
<span class="badge">🔄 New Session</span>
<span class="badge green">📱 10+ Devices</span>
<span class="badge blue">🌐 91Wheels API</span>
<span class="badge yellow">∞ Unlimited</span>
</div>
<div class="stats">
<div class="stat"><div class="num" id="reqs">0</div><div class="lbl">Requests</div></div>
<div class="stat"><div class="num green" id="oks">0</div><div class="lbl">Success</div></div>
<div class="stat"><div class="num" id="sess">-</div><div class="lbl">Session</div></div>
<div class="stat"><div class="num green">∞</div><div class="lbl">Limit</div></div>
</div>
<div class="api-box">
<span class="method">GET</span>
<code>?rc=MH02FZ0555</code>
</div>
<input type="text" id="rcInput" placeholder="Enter Vehicle RC Number..." autocomplete="off">
<button onclick="fetchRC()">🔍 FETCH RC DETAILS</button>
<div class="result" id="result">
<div class="info" id="info"></div>
<pre id="data"></pre>
</div>
<footer>@BRONX_ULTRA • 91Wheels Proxy API</footer>
</div>
<script>
var req=0,ok=0;
async function fetchRC(){
var n=document.getElementById('rcInput').value.trim();
if(!n){alert('Please enter RC Number!');return}
var r=document.getElementById('result'),d=document.getElementById('data'),i=document.getElementById('info');
r.classList.add('show');d.style.color='#ffb400';d.textContent='⏳ Creating new session & fetching data...';
i.textContent='';
try{
var resp=await fetch('?rc='+encodeURIComponent(n));
var json=await resp.json();
d.style.color='#00ff88';d.textContent=JSON.stringify(json,null,2);
req++;
if(json.status==='success')ok++;
document.getElementById('reqs').textContent=req;
document.getElementById('oks').textContent=ok;
if(json._proxy){
i.innerHTML='🔑 Session: '+json._proxy.session_id+' | 📱 '+json._proxy.device+' | ✅ Status: '+(json._proxy.success?'200 OK':'Error');
document.getElementById('sess').textContent=json._proxy.session_id;
}
}catch(e){
d.style.color='#ff0080';d.textContent='❌ Error: '+e.message;
req++;
document.getElementById('reqs').textContent=req;
i.textContent='❌ Failed';
}
}
</script>
</body></html>
    <?php
    exit;
}

// ============ GENERATE UNIQUE SESSION ============
$sessionId = bin2hex(random_bytes(8)) . '-' . dechex(time()) . '-' . bin2hex(random_bytes(4));

// ============ RANDOM DEVICE ============
$devices = [
    ["Chrome 120 / Windows 10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Chrome 119 / Windows 10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"],
    ["Firefox 121 / Windows", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"],
    ["Edge 120 / Windows", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"],
    ["Chrome 120 / Mac", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Safari 17 / Mac", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"],
    ["Safari / iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"],
    ["Chrome / Android", "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36"],
    ["Chrome / Galaxy", "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36"],
    ["Chrome / Linux", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
];

$device = $devices[array_rand($devices)];
$deviceName = $device[0];
$userAgent = $device[1];

// ============ BUILD PAYLOAD ============
$payload = json_encode([
    "regNo" => $rc,
    "sessionid" => $sessionId
]);

// ============ CURL REQUEST ============
$url = "https://api1.91wheels.com/api/v1/third/rc-detail";

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $payload,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: en-US,en;q=0.9",
        "Origin: https://www.91wheels.com",
        "Referer: https://www.91wheels.com/",
        "User-Agent: $userAgent",
        "Cache-Control: no-cache",
        "Pragma: no-cache",
    ],
    CURLOPT_COOKIE => "session_id=$sessionId; _ga=GA1.1." . rand(100000,999999) . "." . time(),
    CURLOPT_SSL_VERIFYPEER => false,
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

// ============ HANDLE RESPONSE ============
if ($error) {
    echo json_encode([
        "status" => "error",
        "message" => $error,
        "_proxy" => [
            "session_id" => substr($sessionId, 0, 8) . "***",
            "device" => $deviceName,
            "success" => false,
            "credit" => "@BRONX_ULTRA"
        ]
    ]);
    exit;
}

$data = json_decode($response, true);

if (!$data) {
    echo json_encode([
        "status" => "error",
        "message" => "Invalid response from API",
        "http_code" => $httpCode,
        "_proxy" => [
            "session_id" => substr($sessionId, 0, 8) . "***",
            "device" => $deviceName,
            "success" => false,
            "credit" => "@BRONX_ULTRA"
        ]
    ]);
    exit;
}

// Success - add proxy info
$data["_proxy"] = [
    "session_id" => substr($sessionId, 0, 8) . "***",
    "device" => $deviceName,
    "http_code" => $httpCode,
    "success" => true,
    "note" => "NEW session generated for this request!",
    "credit" => "@BRONX_ULTRA"
];

echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
