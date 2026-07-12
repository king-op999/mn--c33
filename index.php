<?php
// ============================================
// 🦾 BRONX ULTRA KILLER 2.0 - 91WHEELS PROXY
// 11 Sources • Super Fast • Unlimited • No Limit
// ============================================

set_time_limit(25);

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
<title>🦾 BRONX ULTRA KILLER 2.0</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000510;color:#d0d8f0;font-family:'Segoe UI',Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 30% 0%,rgba(255,0,0,.08),transparent 50%),radial-gradient(ellipse at 70% 100%,rgba(0,100,255,.06),transparent 50%);pointer-events:none}
.card{background:rgba(5,15,35,.95);border:2px solid rgba(255,50,50,.3);border-radius:24px;padding:35px;max-width:750px;width:100%;text-align:center;position:relative;z-index:1}
.card::before{content:'ULTRA KILLER 2.0';position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#ff0030;color:#fff;padding:4px 20px;border-radius:20px;font-size:9px;font-weight:900;letter-spacing:3px}
h1{font-size:28px;background:linear-gradient(90deg,#ff0030,#ff6600,#ffcc00,#ff0030);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:fire 2s linear infinite;margin:10px 0 5px}
@keyframes fire{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.subtitle{color:#666;font-size:10px;letter-spacing:3px;margin-bottom:12px}
.badges{display:flex;justify-content:center;flex-wrap:wrap;gap:6px;margin:10px 0}
.badge{display:inline-block;padding:5px 12px;border-radius:20px;font-size:8px;font-weight:700;text-transform:uppercase}
.badge.red{background:rgba(255,0,48,.1);color:#ff0030;border:1px solid rgba(255,0,48,.3)}
.badge.green{background:rgba(0,255,136,.1);color:#00ff88;border:1px solid rgba(0,255,136,.3)}
.badge.blue{background:rgba(0,150,255,.1);color:#0096ff;border:1px solid rgba(0,150,255,.3)}
.badge.yellow{background:rgba(255,180,0,.1);color:#ffb400;border:1px solid rgba(255,180,0,.3)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:15px 0}
.stat{background:rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.03);border-radius:12px;padding:14px 8px}
.stat .num{font-size:22px;font-weight:900;color:#ff0030}
.stat .num.g{color:#00ff88}
.stat .num.b{color:#0096ff}
.stat .lbl{font-size:7px;color:#555;text-transform:uppercase;letter-spacing:2px;margin-top:3px}
.api-box{background:rgba(0,0,0,.5);border:1px solid rgba(255,0,48,.1);border-radius:12px;padding:14px;margin:12px 0;text-align:left}
.api-box .get{background:rgba(0,255,136,.15);color:#00ff88;padding:3px 8px;border-radius:4px;font-size:9px;font-weight:700}
.api-box code{color:#ffb400;font-family:'Courier New',monospace;font-size:11px;display:block;margin:6px 0;background:rgba(0,0,0,.4);padding:10px;border-radius:8px;word-break:break-all}
input{width:100%;padding:14px;background:rgba(0,0,0,.7);border:2px solid rgba(255,0,48,.2);border-radius:12px;color:#fff;font-size:15px;outline:none;margin:6px 0;transition:.3s}
input:focus{border-color:#ff0030;box-shadow:0 0 30px rgba(255,0,48,.15)}
.btn-killer{width:100%;padding:16px;background:linear-gradient(135deg,#ff0030,#ff6600,#ff0030);background-size:300% 300%;color:#fff;border:none;border-radius:12px;font-weight:900;cursor:pointer;font-size:15px;margin:8px 0;letter-spacing:2px;animation:btnFire 2s ease infinite}
.btn-killer:hover{transform:scale(1.03);box-shadow:0 0 50px rgba(255,0,48,.3)}
@keyframes btnFire{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.result{background:rgba(0,0,0,.7);border:2px solid rgba(0,255,136,.1);border-radius:12px;padding:14px;margin-top:12px;text-align:left;display:none;max-height:500px;overflow:auto}
.result.show{display:block}
.info{color:#ffb400;font-size:10px;margin-bottom:8px;padding:6px 10px;background:rgba(255,180,0,.05);border-radius:6px}
pre{color:#00ff88;font-family:'Courier New',monospace;font-size:10px;white-space:pre-wrap;line-height:1.4}
footer{color:#333;font-size:9px;margin-top:15px;letter-spacing:2px}
.pulse{animation:pulse 1.5s infinite}@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
</style></head>
<body>
<div class="card">
<h1>🦾 BRONX ULTRA KILLER 2.0</h1>
<p class="subtitle">⚡ 11 SOURCES • SUPER FAST • UNLIMITED ⚡</p>
<div class="badges">
<span class="badge red">🔥 Ultra Fast</span>
<span class="badge green">🌐 11 Sources</span>
<span class="badge blue">✅ Auto Test</span>
<span class="badge yellow">∞ No Limit</span>
</div>
<div class="stats">
<div class="stat"><div class="num" id="reqs">0</div><div class="lbl">Requests</div></div>
<div class="stat"><div class="num g" id="oks">0</div><div class="lbl">Success</div></div>
<div class="stat"><div class="num b" id="prx">0</div><div class="lbl">Proxies</div></div>
<div class="stat"><div class="num g">∞</div><div class="lbl">Limit</div></div>
</div>
<div class="api-box">
<span class="get">GET</span>
<code>/?rc=MH02FZ0555</code>
</div>
<input type="text" id="rcInput" placeholder="Enter Vehicle RC Number..." autocomplete="off">
<button class="btn-killer" onclick="fetchRC()">🦾 ULTRA KILLER FETCH</button>
<div class="result" id="result">
<div class="info" id="info"></div>
<pre id="data"></pre>
</div>
<footer>BRONX ULTRA KILLER 2.0 • @BRONX_ULTRA</footer>
</div>
<script>
var req=0,ok=0;
async function fetchRC(){
var n=document.getElementById('rcInput').value.trim();
if(!n){alert('⚠️ Enter RC Number!');return}
var r=document.getElementById('result'),d=document.getElementById('data'),i=document.getElementById('info');
r.classList.add('show');d.style.color='#ff6600';d.textContent='🦾 ULTRA KILLER: Fetching proxies & data...';
d.classList.add('pulse');
try{
var start=Date.now();
var resp=await fetch('?rc='+encodeURIComponent(n));
var time=((Date.now()-start)/1000).toFixed(1);
var json=await resp.json();
d.style.color='#00ff88';d.textContent=JSON.stringify(json,null,2);
d.classList.remove('pulse');
req++;if(json.success||json.status==='success')ok++;
document.getElementById('reqs').textContent=req;
document.getElementById('oks').textContent=ok;
if(json._proxy){
i.innerHTML='⚡ Speed: '+time+'s | 🌐 Proxy: '+json._proxy.proxy_used+' | 📱 '+json._proxy.device+' | 📦 Pool: '+json._proxy.pool_size;
document.getElementById('prx').textContent=json._proxy.pool_size;
}
}catch(e){
d.style.color='#ff0030';d.textContent='❌ Error: '+e.message;
d.classList.remove('pulse');
req++;
}
}
</script>
</body></html>
    <?php
    exit;
}

// ============================================
// ⚡ ULTRA FAST PROXY FETCH (11 Sources)
// ============================================
function fetchAllProxies() {
    $proxies = [];
    
    $sources = [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=500&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout=500",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxyscan.io/download?type=http",
    ];
    
    // Multi-curl for speed
    $mh = curl_multi_init();
    $handles = [];
    
    foreach ($sources as $i => $url) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT => 3,
            CURLOPT_CONNECTTIMEOUT => 1,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_USERAGENT => 'Mozilla/5.0',
        ]);
        curl_multi_add_handle($mh, $ch);
        $handles[$i] = $ch;
    }
    
    // Execute all at once
    do {
        curl_multi_exec($mh, $running);
    } while ($running > 0);
    
    // Collect results
    foreach ($handles as $ch) {
        $result = curl_multi_getcontent($ch);
        curl_multi_remove_handle($mh, $ch);
        curl_close($ch);
        
        if ($result) {
            $lines = explode("\n", trim($result));
            foreach ($lines as $line) {
                $line = trim($line);
                if (preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}$/', $line)) {
                    $proxies[] = $line;
                }
            }
        }
    }
    
    curl_multi_close($mh);
    
    $proxies = array_unique($proxies);
    shuffle($proxies);
    
    return array_values($proxies);
}

// ============================================
// ⚡ QUICK PROXY TEST
// ============================================
function testProxyFast($proxy) {
    $ch = curl_init("https://api1.91wheels.com/api/v1/third/rc-detail");
    
    $payload = json_encode([
        "regNo" => "MH02FZ0555",
        "sessionid" => "test-" . uniqid()
    ]);
    
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_TIMEOUT => 3,
        CURLOPT_CONNECTTIMEOUT => 2,
        CURLOPT_PROXY => $proxy,
        CURLOPT_PROXYTYPE => CURLPROXY_HTTP,
        CURLOPT_HTTPHEADER => [
            "Content-Type: application/json",
            "Accept: application/json",
            "Origin: https://www.91wheels.com",
            "User-Agent: Mozilla/5.0",
        ],
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_NOBODY => false,
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($httpCode === 200 && $response && strlen($response) > 200) {
        $data = json_decode($response, true);
        if ($data && !isset($data['message']) && isset($data['data'])) {
            return true;
        }
        if ($data && isset($data['status']) && $data['status'] === 'success') {
            return true;
        }
    }
    
    return false;
}

// ============================================
// 🦾 ULTRA KILLER MAIN LOGIC
// ============================================

// 1. Fetch all proxies (parallel)
$allProxies = fetchAllProxies();

// 2. Test first 10 proxies quickly
$workingProxies = [];
$testLimit = min(12, count($allProxies));

for ($i = 0; $i < $testLimit; $i++) {
    if (testProxyFast($allProxies[$i])) {
        $workingProxies[] = $allProxies[$i];
        if (count($workingProxies) >= 3) break; // 3 working = enough
    }
}

// 3. Select proxy
$selectedProxy = null;
$usedProxy = false;

if (count($workingProxies) > 0) {
    $selectedProxy = $workingProxies[array_rand($workingProxies)];
    $usedProxy = true;
}

// ============ DEVICE ============
$devices = [
    ["Chrome 120 / Win10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Chrome / Android", "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36"],
    ["Safari / iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"],
    ["Firefox / Win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"],
    ["Chrome / Mac", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Edge / Win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"],
    ["Safari / iPad", "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"],
];

$device = $devices[array_rand($devices)];
$sessionId = bin2hex(random_bytes(4)) . '-' . dechex(time());

// ============ MAIN REQUEST ============
$payload = json_encode(["regNo" => $rc, "sessionid" => $sessionId]);
$url = "https://api1.91wheels.com/api/v1/third/rc-detail";

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $payload,
    CURLOPT_TIMEOUT => 10,
    CURLOPT_CONNECTTIMEOUT => 5,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: en-US,en;q=0.9",
        "Origin: https://www.91wheels.com",
        "Referer: https://www.91wheels.com/",
        "User-Agent: " . $device[1],
        "Cache-Control: no-cache",
    ],
    CURLOPT_COOKIE => "session_id=$sessionId",
    CURLOPT_SSL_VERIFYPEER => false,
]);

if ($selectedProxy) {
    curl_setopt($ch, CURLOPT_PROXY, $selectedProxy);
    curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_HTTP);
}

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

// Fallback: direct if proxy failed
if (($error || $httpCode !== 200) && $selectedProxy) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_TIMEOUT => 10,
        CURLOPT_HTTPHEADER => [
            "Content-Type: application/json",
            "Accept: application/json",
            "Origin: https://www.91wheels.com",
            "User-Agent: " . $device[1],
        ],
        CURLOPT_SSL_VERIFYPEER => false,
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $error = curl_error($ch);
    curl_close($ch);
    
    $usedProxy = false;
    $selectedProxy = null;
}

// ============ RESPONSE ============
$data = json_decode($response, true);

if (!$data) {
    $data = [
        "success" => false,
        "message" => $error ?: "Failed (HTTP $httpCode)",
    ];
}

$data["_proxy"] = [
    "proxy_used" => $usedProxy ? $selectedProxy : "direct",
    "device" => $device[0],
    "pool_size" => count($workingProxies),
    "total_fetched" => count($allProxies),
    "tested" => $testLimit,
    "session_id" => substr($sessionId, 0, 8) . "***",
    "success" => !$error && $httpCode === 200,
    "speed" => "ULTRA FAST",
    "credit" => "@BRONX_ULTRA"
];

echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
