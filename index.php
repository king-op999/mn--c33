<?php
// ============================================
// 🚗 BRONX 91WHEELS PROXY V3 - MULTI-SOURCE
// 6+ Proxy Sources • Better Testing • Fast
// ============================================

set_time_limit(60); // 60 seconds for proxy testing

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
<title>🚗 BRONX RC PROXY V3</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000a14;color:#d0d8f0;font-family:'Segoe UI',Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
.card{background:rgba(5,15,35,.95);border:1px solid rgba(0,255,136,.2);border-radius:24px;padding:35px;max-width:700px;width:100%;text-align:center}
h1{font-size:24px;background:linear-gradient(90deg,#00ff88,#0096ff,#8b00ff,#ff0080);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:rainbow 3s linear infinite}
@keyframes rainbow{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.subtitle{color:#555;font-size:11px;letter-spacing:2px}
.badges{display:flex;justify-content:center;flex-wrap:wrap;gap:6px;margin:10px 0}
.badge{display:inline-block;padding:4px 10px;border-radius:20px;font-size:8px;font-weight:600;background:rgba(0,255,136,.08);color:#00ff88;border:1px solid rgba(0,255,136,.1)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:12px 0}
.stat{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.05);border-radius:10px;padding:12px 6px}
.stat .num{font-size:20px;font-weight:900;color:#00ff88}
.stat .lbl{font-size:7px;color:#666;text-transform:uppercase}
.api-box{background:rgba(0,0,0,.5);border:1px solid rgba(0,150,255,.1);border-radius:10px;padding:14px;margin:10px 0;text-align:left}
.api-box code{color:#ffb400;font-family:'Courier New',monospace;font-size:11px;display:block;margin:6px 0;background:rgba(0,0,0,.3);padding:8px;border-radius:6px}
input{width:100%;padding:14px;background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.15);border-radius:12px;color:#fff;font-size:15px;outline:none;margin:6px 0}
input:focus{border-color:#00ff88}
button{width:100%;padding:16px;background:linear-gradient(135deg,#00ff88,#0096ff,#8b00ff);color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-size:15px;margin:6px 0}
.result{background:rgba(0,0,0,.6);border:1px solid rgba(0,255,136,.1);border-radius:10px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:450px;overflow:auto}
.result.show{display:block}
.info{color:#ffb400;font-size:10px;margin-bottom:6px}
pre{color:#00ff88;font-family:'Courier New',monospace;font-size:10px;white-space:pre-wrap}
footer{color:#333;font-size:9px;margin-top:12px}
</style></head>
<body>
<div class="card">
<h1>🚗 BRONX RC PROXY V3</h1>
<p class="subtitle">MULTI-SOURCE PROXIES • BETTER TESTING</p>
<div class="badges">
<span class="badge">🌐 6+ Sources</span><span class="badge">✅ Tested</span>
<span class="badge">🔄 Auto Refresh</span><span class="badge">∞ Unlimited</span>
</div>
<div class="stats">
<div class="stat"><div class="num" id="reqs">0</div><div class="lbl">Requests</div></div>
<div class="stat"><div class="num" id="oks">0</div><div class="lbl">Success</div></div>
<div class="stat"><div class="num" id="prx">0</div><div class="lbl">Working</div></div>
<div class="stat"><div class="num">∞</div><div class="lbl">Limit</div></div>
</div>
<div class="api-box"><code>GET /?rc=MH02FZ0555</code></div>
<input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
<button onclick="fetchRC()">🔍 FETCH WITH PROXY</button>
<div class="result" id="result"><div class="info" id="info"></div><pre id="data"></pre></div>
<footer>@BRONX_ULTRA</footer>
</div>
<script>
var req=0,ok=0;
async function fetchRC(){
var n=document.getElementById('rcInput').value.trim();
if(!n)return;
var r=document.getElementById('result'),d=document.getElementById('data'),i=document.getElementById('info');
r.classList.add('show');d.style.color='#ffb400';d.textContent='⏳ Testing proxies & fetching data...';
try{
var resp=await fetch('?rc='+encodeURIComponent(n));
var json=await resp.json();
d.style.color='#00ff88';d.textContent=JSON.stringify(json,null,2);
req++;if(json.success)ok++;
document.getElementById('reqs').textContent=req;
document.getElementById('oks').textContent=ok;
if(json._proxy){
i.innerHTML='🌐 '+json._proxy.proxy_used+' | 📱 '+json._proxy.device+' | ✅ Pool: '+json._proxy.pool_size;
document.getElementById('prx').textContent=json._proxy.pool_size;
}
}catch(e){
d.style.color='#ff0080';d.textContent='Error: '+e.message;
req++;
}
}
</script>
</body></html>
    <?php
    exit;
}

// ============================================
// 🔥 FUNCTION: Fetch from URL with timeout
// ============================================
function fetchURL($url, $timeout = 5) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => $timeout,
        CURLOPT_CONNECTTIMEOUT => 3,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    ]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}

// ============================================
// 🔥 FETCH PROXIES FROM 6+ SOURCES
// ============================================
function fetchAllProxies() {
    $allProxies = [];
    
    // Source 1: ProxyScrape (HTTP)
    $data = fetchURL("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=all", 5);
    if ($data) {
        foreach (explode("\n", trim($data)) as $line) {
            $line = trim($line);
            if ($line && strpos($line, ':') !== false) $allProxies[] = $line;
        }
    }
    
    // Source 2: ProxyScrape (HTTPS)
    $data = fetchURL("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=2000&country=all&ssl=all&anonymity=all", 5);
    if ($data) {
        foreach (explode("\n", trim($data)) as $line) {
            $line = trim($line);
            if ($line && strpos($line, ':') !== false) $allProxies[] = $line;
        }
    }
    
    // Source 3: ProxyList.download (HTTP)
    $data = fetchURL("https://www.proxy-list.download/api/v1/get?type=http", 5);
    if ($data) {
        foreach (explode("\n", trim($data)) as $line) {
            $line = trim($line);
            if ($line && strpos($line, ':') !== false) $allProxies[] = $line;
        }
    }
    
    // Source 4: ProxyList.download (HTTPS)
    $data = fetchURL("https://www.proxy-list.download/api/v1/get?type=https", 5);
    if ($data) {
        foreach (explode("\n", trim($data)) as $line) {
            $line = trim($line);
            if ($line && strpos($line, ':') !== false) $allProxies[] = $line;
        }
    }
    
    // Source 5: OpenProxy.space
    $data = fetchURL("https://openproxy.space/list/http", 5);
    if ($data) {
        foreach (explode("\n", trim($data)) as $line) {
            $line = trim($line);
            if ($line && strpos($line, ':') !== false) $allProxies[] = $line;
        }
    }
    
    // Source 6: Proxylist.geonode.com
    $data = fetchURL("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https", 5);
    if ($data) {
        $json = json_decode($data, true);
        if (isset($json['data'])) {
            foreach ($json['data'] as $proxy) {
                $allProxies[] = $proxy['ip'] . ':' . $proxy['port'];
            }
        }
    }
    
    // Remove duplicates & shuffle
    $allProxies = array_unique($allProxies);
    shuffle($allProxies);
    
    return array_values($allProxies);
}

// ============================================
// 🔥 QUICK TEST PROXY (Lightweight)
// ============================================
function quickTestProxy($proxy) {
    $ch = curl_init("https://httpbin.org/ip");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 3,
        CURLOPT_CONNECTTIMEOUT => 2,
        CURLOPT_PROXY => $proxy,
        CURLOPT_PROXYTYPE => CURLPROXY_HTTP,
        CURLOPT_SSL_VERIFYPEER => false,
    ]);
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    return ($httpCode === 200 && $result && strpos($result, 'origin') !== false);
}

// ============================================
// 🔥 TEST PROXY WITH 91Wheels API
// ============================================
function testWith91Wheels($proxy) {
    $ch = curl_init("https://api1.91wheels.com/api/v1/third/rc-detail");
    
    $payload = json_encode([
        "regNo" => "MH02FZ0555",
        "sessionid" => "test-" . uniqid()
    ]);
    
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_TIMEOUT => 8,
        CURLOPT_CONNECTTIMEOUT => 4,
        CURLOPT_PROXY => $proxy,
        CURLOPT_PROXYTYPE => CURLPROXY_HTTP,
        CURLOPT_HTTPHEADER => [
            "Content-Type: application/json",
            "Accept: application/json",
            "Origin: https://www.91wheels.com",
            "User-Agent: Mozilla/5.0",
        ],
        CURLOPT_SSL_VERIFYPEER => false,
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($httpCode === 200 && $response) {
        $data = json_decode($response, true);
        // Check if contains real data (not limit message)
        if ($data && isset($data['data']['owner_name'])) {
            return true;
        }
        if ($data && !isset($data['message']) && strlen($response) > 200) {
            return true;
        }
    }
    
    return false;
}

// ============================================
// 🔥 MAIN LOGIC
// ============================================

// 1. Fetch all proxies
$allProxies = fetchAllProxies();

// 2. First pass: Quick test with httpbin (fast)
$quickPassed = [];
$testLimit = min(30, count($allProxies));

for ($i = 0; $i < $testLimit; $i++) {
    if (quickTestProxy($allProxies[$i])) {
        $quickPassed[] = $allProxies[$i];
        if (count($quickPassed) >= 10) break;
    }
}

// 3. Second pass: Test with 91Wheels
$workingProxies = [];
$testLimit2 = min(8, count($quickPassed));

for ($i = 0; $i < $testLimit2; $i++) {
    if (testWith91Wheels($quickPassed[$i])) {
        $workingProxies[] = $quickPassed[$i];
        if (count($workingProxies) >= 3) break;
    }
}

// 4. If no proxies passed quick test, try a few directly with 91Wheels
if (count($workingProxies) === 0 && count($allProxies) > 0) {
    $testLimit3 = min(10, count($allProxies));
    for ($i = 0; $i < $testLimit3; $i++) {
        if (testWith91Wheels($allProxies[$i])) {
            $workingProxies[] = $allProxies[$i];
            if (count($workingProxies) >= 2) break;
        }
    }
}

// 5. Select proxy
$selectedProxy = null;
$usedProxy = false;

if (count($workingProxies) > 0) {
    $selectedProxy = $workingProxies[array_rand($workingProxies)];
    $usedProxy = true;
}

// ============ DEVICE & SESSION ============
$devices = [
    ["Chrome 120 / Win10", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
    ["Chrome / Android", "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36"],
    ["Safari / iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"],
    ["Firefox / Win", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"],
    ["Chrome / Mac", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"],
];

$device = $devices[array_rand($devices)];
$sessionId = bin2hex(random_bytes(4)) . '-' . dechex(time());

// ============ MAKE REQUEST ============
$payload = json_encode(["regNo" => $rc, "sessionid" => $sessionId]);
$url = "https://api1.91wheels.com/api/v1/third/rc-detail";

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $payload,
    CURLOPT_TIMEOUT => 15,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Accept: application/json",
        "Origin: https://www.91wheels.com",
        "Referer: https://www.91wheels.com/",
        "User-Agent: " . $device[1],
    ],
    CURLOPT_SSL_VERIFYPEER => false,
]);

// Add proxy if available
if ($selectedProxy) {
    curl_setopt($ch, CURLOPT_PROXY, $selectedProxy);
    curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_HTTP);
}

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

// Fallback: If proxy failed, try direct
if (($error || $httpCode !== 200) && $selectedProxy) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_TIMEOUT => 15,
        CURLOPT_HTTPHEADER => [
            "Content-Type: application/json",
            "Accept: application/json",
            "Origin: https://www.91wheels.com",
            "Referer: https://www.91wheels.com/",
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
    "quick_tested" => count($quickPassed),
    "tested" => min(8, count($quickPassed)),
    "session_id" => substr($sessionId, 0, 8) . "***",
    "success" => !$error && $httpCode === 200,
    "credit" => "@BRONX_ULTRA"
];

echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
