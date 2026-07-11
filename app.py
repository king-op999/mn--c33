<?php
// ============================================
// 🚗 BRONX 91WHEELS PROXY API - UNLIMITED
// Multi-Session • Auto Rotation • No Limit
// ============================================

header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, OPTIONS");
header("Access-Control-Allow-Headers: *");

// Handle CORS preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Get parameters
$action = $_GET['action'] ?? 'api';
$rc = trim($_GET['rc'] ?? $_GET['term'] ?? '');

// ============ HOME PAGE ============
if ($action === 'home' || ($rc === '' && $action === 'api')) {
    ?>
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>🚗 BRONX 91WHEELS PROXY</title>
    <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#000a14;color:#d0d8f0;font-family:Arial,sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}
    .card{background:#0a1a2a;border:1px solid #ff0080;border-radius:20px;padding:30px;max-width:700px;width:100%;text-align:center}
    h1{color:#ff0080;font-size:24px;margin-bottom:5px}
    .badge{display:inline-block;padding:5px 12px;border-radius:20px;font-size:9px;margin:3px;background:rgba(255,0,128,.1);color:#ff0080;border:1px solid rgba(255,0,128,.3)}
    .badge.g{color:#00ff88;border-color:rgba(0,255,136,.3)}
    .badge.y{color:#ffb400;border-color:rgba(255,180,0,.3)}
    .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:10px 0}
    .st{background:#000;padding:10px;border-radius:8px;text-align:center}
    .st .v{font-size:18px;font-weight:700;color:#ff0080}
    .st .l{font-size:7px;color:#666}
    code{color:#00ff88;background:#000;padding:8px;display:block;margin:8px 0;border-radius:8px;font-size:12px;word-break:break-all}
    input{width:100%;padding:12px;background:#000;border:1px solid #ff0080;border-radius:8px;color:#fff;font-size:14px;margin:6px 0}
    button{width:100%;padding:14px;background:#ff0080;color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;font-size:14px;margin:4px 0}
    button:hover{background:#ff1493}
    .result{background:#000;border:1px solid #00ff88;border-radius:8px;padding:14px;margin-top:10px;text-align:left;display:none;max-height:400px;overflow:auto}
    .result.show{display:block}
    pre{color:#00ff88;font-family:monospace;font-size:10px;white-space:pre-wrap}
    </style></head>
    <body>
    <div class="card">
    <h1>🚗 BRONX 91WHEELS PROXY</h1>
    <p style="color:#666;font-size:11px">Unlimited Sessions • Auto Rotation • PHP</p>
    <div style="margin:8px 0">
    <span class="badge y">🔄 New Session</span>
    <span class="badge g">📱 Multi-Device</span>
    <span class="badge">🌐 91Wheels API</span>
    <span class="badge g">∞ Unlimited</span>
    </div>
    <div class="stats">
    <div class="st"><div class="v" id="count">0</div><div class="l">REQUESTS</div></div>
    <div class="st"><div class="v" id="success">0</div><div class="l">SUCCESS</div></div>
    <div class="st"><div class="v" id="session">-</div><div class="l">SESSION ID</div></div>
    <div class="st"><div class="v">∞</div><div class="l">LIMIT</div></div>
    </div>
    <code>GET /api.php?rc=MH02FZ0555</code>
    <input type="text" id="rcInput" placeholder="Enter RC Number..." autocomplete="off">
    <button onclick="lookup()">🔍 FETCH WITH NEW SESSION</button>
    <div class="result" id="result"><pre id="resultData"></pre></div>
    <p style="color:#444;font-size:9px;margin-top:10px">@BRONX_ULTRA</p>
    </div>
    <script>
    var c=0,s=0;
    async function lookup(){
    var n=document.getElementById('rcInput').value.trim();
    if(!n)return;
    var d=document.getElementById('result'),p=document.getElementById('resultData');
    d.classList.add('show');p.style.color='#ffb400';p.textContent='Creating NEW session...';
    try{
    var r=await fetch('?rc='+encodeURIComponent(n));
    var j=await r.json();
    p.style.color='#00ff88';p.textContent=JSON.stringify(j,null,2);
    c++;
    if(j.status==='success')s++;
    document.getElementById('count').textContent=c;
    document.getElementById('success').textContent=s;
    if(j._proxy)document.getElementById('session').textContent=j._proxy.session_id||'-';
    }catch(e){
    p.style.color='#ff0080';p.textContent='Error: '+e.message;
    c++;
    document.getElementById('count').textContent=c;
    }
    }
    </script>
    </body></html>
    <?php
    exit;
}

// ============ API ENDPOINT ============
if ($rc === '') {
    echo json_encode([
        "status" => "error",
        "message" => "Missing RC number. Use ?rc=MH02FZ0555",
        "credit" => "@BRONX_ULTRA"
    ]);
    exit;
}

// ============ GENERATE UNIQUE SESSION ============
// Har request pe NAYA session ID
$sessionId = generateSessionID();

// ============ MULTIPLE USER AGENTS ============
$userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
];

$randomUA = $userAgents[array_rand($userAgents)];

// ============ RANDOM DEVICE FINGERPRINT ============
$screenResolutions = ["1920x1080", "1366x768", "1440x900", "1536x864", "2560x1440", "390x844", "412x915", "360x800"];
$randomScreen = $screenResolutions[array_rand($screenResolutions)];
$randomColorDepth = [24, 30, 32][array_rand([24, 30, 32])];
$randomTimeZone = ["Asia/Kolkata", "America/New_York", "Europe/London", "Asia/Dubai", "Asia/Singapore"][array_rand([0,1,2,3,4])];
$randomLanguage = ["en-US,en;q=0.9", "en-IN,en;q=0.9,hi;q=0.8", "en-GB,en;q=0.9"][array_rand([0,1,2])];

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
    CURLOPT_TIMEOUT => 25,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: $randomLanguage",
        "Accept-Encoding: gzip, deflate, br",
        "Origin: https://www.91wheels.com",
        "Referer: https://www.91wheels.com/",
        "User-Agent: $randomUA",
        "Sec-Ch-Ua: \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Sec-Ch-Ua-Mobile: ?0",
        "Sec-Ch-Ua-Platform: \"Windows\"",
        "Sec-Fetch-Dest: empty",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Site: same-site",
        "Cache-Control: no-cache",
        "Pragma: no-cache",
        "DNT: 1",
    ],
    CURLOPT_COOKIE => "session_id=$sessionId; visitor=" . uniqid() . "; _ga=GA1.1." . rand(100000000, 999999999) . "." . time(),
    CURLOPT_SSL_VERIFYPEER => false,
    CURLOPT_SSL_VERIFYHOST => false,
    CURLOPT_ENCODING => "gzip, deflate, br",
]);

$res = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

// ============ HANDLE ERRORS ============
if ($curlError) {
    echo json_encode([
        "status" => "error",
        "message" => "Connection error: " . $curlError,
        "_proxy" => [
            "session_id" => substr($sessionId, 0, 8) . "***",
            "success" => false,
            "credit" => "@BRONX_ULTRA"
        ]
    ]);
    exit;
}

// ============ DECODE RESPONSE ============
$data = json_decode($res, true);

if (!$data) {
    // If not JSON, return raw
    echo json_encode([
        "status" => "error",
        "message" => "Invalid response",
        "raw_response" => substr($res, 0, 500),
        "http_code" => $httpCode,
        "_proxy" => [
            "session_id" => substr($sessionId, 0, 8) . "***",
            "success" => false,
            "credit" => "@BRONX_ULTRA"
        ]
    ]);
    exit;
}

// ============ SUCCESS - ADD PROXY INFO ============
$data["_proxy"] = [
    "session_id" => substr($sessionId, 0, 8) . "***",
    "session_full" => $sessionId,
    "user_agent" => substr($randomUA, 0, 50) . "...",
    "http_code" => $httpCode,
    "success" => ($httpCode === 200),
    "note" => "NEW session created for this request!",
    "credit" => "@BRONX_ULTRA"
];

echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);

// ============ HELPER FUNCTIONS ============
function generateSessionID() {
    // Generate unique session ID (like browser fingerprint)
    $parts = [];
    
    // Random hex strings
    $parts[] = bin2hex(random_bytes(16));
    $parts[] = dechex(time());
    $parts[] = dechex(rand(100000, 999999));
    $parts[] = uniqid('', true);
    
    // Combine and hash
    return str_replace('.', '', implode('-', $parts));
}
?>
