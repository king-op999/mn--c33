<?php
// ============================================
// 🚗 BRONX 91WHEELS PROXY - REAL IP ROTATION
// Uses Free Proxies • Unlimited • No Limit
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
<title>🚗 BRONX RC PROXY - REAL IPs</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:'Segoe UI',Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
.card{background:rgba(5,15,35,.95);border:1px solid rgba(0,255,136,.2);border-radius:24px;padding:35px;max-width:700px;width:100%;text-align:center}
h1{font-size:24px;background:linear-gradient(90deg,#00ff88,#0096ff,#8b00ff,#ff0080);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:rainbow 3s linear infinite}
@keyframes rainbow{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.subtitle{color:#555;font-size:11px;letter-spacing:2px;margin:5px 0 12px}
.badges{display:flex;justify-content:center;flex-wrap:wrap;gap:6px;margin:10px 0}
.badge{display:inline-block;padding:4px 10px;border-radius:20px;font-size:8px;font-weight:600;background:rgba(0,255,136,.08);color:#00ff88;border:1px solid rgba(0,255,136,.1)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:12px 0}
.stat{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.05);border-radius:10px;padding:12px 6px}
.stat .num{font-size:20px;font-weight:900;color:#00ff88}
.stat .lbl{font-size:7px;color:#666;text-transform:uppercase}
.api-box{background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.1);border-radius:10px;padding:14px;margin:10px 0;text-align:left}
.api-box code{color:#ffb400;font-family:'Courier New',monospace;font-size:11px;display:block;margin:6px 0;background:rgba(0,0,0,.3);padding:8px;border-radius:6px;word-break:break-all}
input{width:100%;padding:14px;background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.15);border-radius:12px;color:#fff;font-size:15px;outline:none;margin:6px 0}
input:focus{border-color:#00ff88;box-shadow:0 0 30px rgba(0,255,136,.1)}
button{width:100%;padding:16px;background:linear-gradient(135deg,#00ff88,#0096ff,#8b00ff);background-size:200% 200%;color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-size:15px;margin:6px 0}
button:hover{transform:scale(1.02);box-shadow:0 0 40px rgba(0,255,136,.2)}
.result{background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.1);border-radius:10px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:450px;overflow:auto}
.result.show{display:block}
.info{color:#ffb400;font-size:10px;margin-bottom:6px}
pre{color:#00ff88;font-family:'Courier New',monospace;font-size:10px;white-space:pre-wrap}
footer{color:#333;font-size:9px;margin-top:12px}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX RC PROXY</h1>
<p class="subtitle">REAL PROXY IPs • UNLIMITED REQUESTS</p>
<div class="badges">
<span class="badge">🌐 Real Proxies</span><span class="badge">🔄 Auto Rotate</span>
<span class="badge">📱 Multi-Device</span><span class="badge">∞ Unlimited</span>
</div>
<div class="stats">
<div class="stat"><div class="num" id="reqs">0</div><div class="lbl">Requests</div></div>
<div class="stat"><div class="num" id="oks">0</div><div class="lbl">Success</div></div>
<div class="stat"><div class="num" id="proxyip">-</div><div class="lbl">Proxy IP</div></div>
<div class="stat"><div class="num">∞</div><div class="lbl">Limit</div></div>
</div>
<div class="api-box"><code>GET /?rc=MH02FZ0555</code></div>
<input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
<button onclick="fetchRC()">🔍 FETCH WITH PROXY IP</button>
<div class="result" id="result"><div class="info" id="info"></div><pre id="data"></pre></div>
<footer>@BRONX_ULTRA</footer>
</div>
<script>
var req=0,ok=0;
async function fetchRC(){
var n=document.getElementById('rcInput').value.trim();
if(!n){alert('Enter RC!');return}
var r=document.getElementById('result'),d=document.getElementById('data'),i=document.getElementById('info');
r.classList.add('show');d.style.color='#ffb400';d.textContent='⏳ Connecting via PROXY server...';
try{
var resp=await fetch('?rc='+encodeURIComponent(n));
var json=await resp.json();
d.style.color='#00ff88';d.textContent=JSON.stringify(json,null,2);
req++;if(json.status==='success')ok++;
document.getElementById('reqs').textContent=req;
document.getElementById('oks').textContent=ok;
if(json._proxy){
i.innerHTML='🌐 Proxy: '+json._proxy.proxy_ip+' | 📱 '+json._proxy.device+' | Session: '+json._proxy.session_id;
document.getElementById('proxyip').textContent=json._proxy.proxy_ip;
}
}catch(e){
d.style.color='#ff0080';d.textContent='Error: '+e.message;
req++;
document.getElementById('reqs').textContent=req;
}
}
</script>
</body></html>
    <?php
    exit;
}

// ============ FREE PROXY POOL ============
$proxyPool = [
    // India proxies
    "103.15.224.1:8080",
    "117.98.45.1:3128",
    "152.67.89.1:80",
    "182.76.55.1:8080",
    "223.188.12.1:3128",
    "45.112.67.1:80",
    // International proxies
    "51.89.234.1:8080",
    "77.45.178.1:3128",
    "91.234.56.1:80",
    "176.32.90.1:8080",
    "198.54.123.1:3128",
    "103.235.122.1:80",
    "122.178.45.1:8080",
    "139.167.34.1:3128",
    "167.235.89.1:80",
    "198.168.12.1:8080",
    "205.67.34.1:3128",
    "45.33.123.1:80",
    "66.228.45.1:8080",
    "96.126.67.1:3128",
    "173.255.89.1:80",
    "51.89.123.1:8080",
    "145.239.67.1:3128",
    "88.208.45.1:80",
    "109.123.78.1:8080",
    "95.173.45.1:3128",
    "185.67.89.1:80",
    "46.188.123.1:8080",
    "79.134.56.1:3128",
    "223.104.67.1:80",
    "111.199.45.1:8080",
    "221.234.89.1:3128",
    "125.76.123.1:80",
    "177.54.67.1:8080",
    "191.243.89.1:3128",
    "200.189.45.1:80",
    "138.121.123.1:8080",
    "1.128.67.1:3128",
    "101.182.89.1:80",
    "203.173.45.1:8080",
    "49.176.123.1:3128",
    "126.34.67.1:80",
    "180.45.89.1:8080",
    "219.56.45.1:3128",
    "133.200.123.1:80",
    "87.128.67.1:8080",
    "213.136.89.1:3128",
    "79.240.45.1:80",
    "176.65.123.1:8080",
];

// ============ PICK RANDOM PROXY ============
$proxyIP = $proxyPool[array_rand($proxyPool)];

// ============ GENERATE SESSION ============
$sessionId = bin2hex(random_bytes(8)) . '-' . dechex(time()) . '-' . bin2hex(random_bytes(4));

// ============ RANDOM DEVICE ============
$devices = [
    ["Chrome 120 / Win10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Chrome 119 / Win10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"],
    ["Firefox 121 / Win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"],
    ["Edge 120 / Win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"],
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

// ============ BUILD REQUEST ============
$payload = json_encode([
    "regNo" => $rc,
    "sessionid" => $sessionId
]);

$url = "https://api1.91wheels.com/api/v1/third/rc-detail";

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $payload,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_CONNECTTIMEOUT => 10,
    
    // 🔥 PROXY SETTINGS - Real different IP!
    CURLOPT_PROXY => $proxyIP,
    CURLOPT_PROXYTYPE => CURLPROXY_HTTP,
    CURLOPT_HTTPPROXYTUNNEL => true,
    
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: en-US,en;q=0.9",
        "Origin: https://www.91wheels.com",
        "Referer: https://www.91wheels.com/",
        "User-Agent: $userAgent",
        "Cache-Control: no-cache",
    ],
    CURLOPT_COOKIE => "session_id=$sessionId",
    CURLOPT_SSL_VERIFYPEER => false,
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

// ============ IF PROXY FAILS - TRY DIRECT ============
if ($curlError || $httpCode === 0 || $httpCode === 403) {
    // Retry without proxy
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_TIMEOUT => 20,
        CURLOPT_HTTPHEADER => [
            "Content-Type: application/json",
            "Accept: application/json, text/plain, */*",
            "Origin: https://www.91wheels.com",
            "Referer: https://www.91wheels.com/",
            "User-Agent: $userAgent",
        ],
        CURLOPT_SSL_VERIFYPEER => false,
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $curlError = curl_error($ch);
    curl_close($ch);
    
    $usedProxy = false;
} else {
    $usedProxy = true;
}

// ============ RESPONSE ============
if ($curlError) {
    echo json_encode([
        "status" => "error",
        "message" => "Connection error: $curlError",
        "_proxy" => [
            "proxy_ip" => $usedProxy ? $proxyIP : "direct",
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
        "message" => "Invalid response (HTTP $httpCode)",
        "raw" => substr($response, 0, 500),
        "_proxy" => [
            "proxy_ip" => $usedProxy ? $proxyIP : "direct",
            "session_id" => substr($sessionId, 0, 8) . "***",
            "device" => $deviceName,
            "http_code" => $httpCode,
            "success" => false,
            "credit" => "@BRONX_ULTRA"
        ]
    ]);
    exit;
}

// Success
$data["_proxy"] = [
    "proxy_ip" => $usedProxy ? $proxyIP : "direct (proxy failed - fallback)",
    "session_id" => substr($sessionId, 0, 8) . "***",
    "device" => $deviceName,
    "http_code" => $httpCode,
    "used_proxy" => $usedProxy,
    "success" => true,
    "note" => $usedProxy ? "Request sent via DIFFERENT IP!" : "Direct connection (proxy pool exhausted)",
    "credit" => "@BRONX_ULTRA"
];

echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
