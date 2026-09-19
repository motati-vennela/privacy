#!/usr/bin/env python3
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "static", "dashboard.html")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0f172a;color:#e2e8f0;min-height:100vh}
.header{background:#1e293b;border-bottom:1px solid #334155;padding:14px 24px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100}
.logo{font-size:18px;font-weight:700;color:#38bdf8}
.nav{display:flex;gap:6px}
.nav button{padding:8px 14px;border-radius:6px;border:none;cursor:pointer;background:transparent;color:#94a3b8;font-size:13px;font-weight:500;transition:all .2s}
.nav button.active{background:#3b82f6;color:#fff;font-weight:700}
.nav button:hover:not(.active){background:#334155;color:#fff}
.main{padding:20px;max-width:1200px;margin:0 auto}
.card{background:#1e293b;border-radius:10px;padding:18px;margin-bottom:14px;border:1px solid #334155}
.card h3{color:#38bdf8;font-size:15px;margin-bottom:10px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:14px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:14px}
@media(max-width:800px){.grid4,.grid2{grid-template-columns:1fr}}
.stat{background:#1e293b;border-radius:10px;padding:18px;text-align:center;border:1px solid #334155}
.stat .val{font-size:30px;font-weight:700;color:#38bdf8}
.stat .lbl{font-size:12px;color:#94a3b8;margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:10px;border-bottom:2px solid #334155;color:#94a3b8;font-weight:600}
td{padding:10px;border-bottom:1px solid #1e3a5f}
.badge{display:inline-block;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700}
.bg{background:#065f46;color:#34d399}
.br{background:#7f1d1d;color:#f87171}
.bb{background:#1e3a5f;color:#60a5fa}
.by{background:#78350f;color:#fbbf24}
.btn{padding:10px 18px;border-radius:8px;border:none;cursor:pointer;font-weight:700;font-size:13px;color:#fff;transition:all .2s}
.btn:hover:not(:disabled){filter:brightness(1.15);transform:translateY(-1px)}
.btn:active:not(:disabled){transform:translateY(0)}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-blue{background:#3b82f6}.btn-green{background:#10b981}.btn-purple{background:#8b5cf6}.btn-red{background:#ef4444}.btn-yellow{background:#d97706}.btn-cyan{background:#06b6d4}
.input{padding:10px 12px;border-radius:6px;border:1px solid #334155;background:#0f172a;color:#e2e8f0;font-size:13px;width:100%}
select.input{cursor:pointer}
.input:focus{outline:none;border-color:#3b82f6;box-shadow:0 0 0 2px rgba(59,130,246,.3)}
.row{display:flex;gap:10px;margin-bottom:10px;align-items:center;flex-wrap:wrap}
.row label{font-size:12px;color:#94a3b8;min-width:70px}
pre{background:#0f172a;padding:12px;border-radius:6px;font-size:12px;overflow-x:auto;white-space:pre-wrap;max-height:300px;overflow-y:auto}
.hidden{display:none!important}
.user-info{display:flex;align-items:center;gap:12px}
.user-info span{color:#94a3b8;font-size:13px}
#login-page{display:flex;justify-content:center;align-items:center;min-height:100vh}
#login-box{background:#1e293b;border-radius:12px;padding:30px;width:380px;border:1px solid #334155;box-shadow:0 20px 60px rgba(0,0,0,.5)}
#login-box h2{text-align:center;color:#38bdf8;margin-bottom:6px;font-size:22px}
#login-box .sub{text-align:center;color:#64748b;margin-bottom:24px;font-size:13px}
#login-box .input{margin-bottom:12px}
#login-box .btn{width:100%;padding:12px;font-size:15px}
#login-box .hint{font-size:11px;color:#64748b;margin-top:14px;text-align:center;line-height:1.6}
.toast{position:fixed;top:20px;right:20px;padding:12px 20px;border-radius:8px;color:#fff;font-size:13px;font-weight:600;z-index:9999;animation:slideIn .3s ease}
.toast-ok{background:#065f46;border:1px solid #34d399}
.toast-err{background:#7f1d1d;border:1px solid #f87171}
@keyframes slideIn{from{transform:translateX(100px);opacity:0}to{transform:translateX(0);opacity:1}}
.spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite;vertical-align:middle;margin-right:6px}
@keyframes spin{to{transform:rotate(360deg)}}
.flow-step{display:flex;align-items:center;gap:12px;padding:12px 14px;background:#0f172a;border-radius:8px;margin-bottom:8px;border-left:3px solid #334155}
.flow-step .num{width:28px;height:28px;background:#334155;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;color:#94a3b8}
.flow-step.done{border-left-color:#10b981}.flow-step.done .num{background:#10b981;color:#fff}
.flow-step.active{border-left-color:#fbbf24}.flow-step.active .num{background:#fbbf24;color:#000}
.flow-step .info .title{font-size:13px;font-weight:600}.flow-step .info .desc{font-size:11px;color:#94a3b8}
.mono{font-family:'Cascadia Code','Fira Code',Consolas,monospace;font-size:12px}"""

HTML_BODY = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy-Preserving CDP Dashboard</title>
</head>
<body>
<div id="login-page">
<div id="login-box">
<h2>Privacy-Preserving CDP</h2>
<p class="sub">Customer Data Protection Platform</p>
<input class="input" id="login-user" placeholder="Username" value="admin">
<input class="input" id="login-pass" type="password" placeholder="Password" value="admin123">
<button class="btn btn-blue" id="login-btn">Sign In</button>
<p class="hint">admin / admin123<br>marketing_user / marketing123<br>support_user / support123</p>
</div>
</div>
<div id="app-page" class="hidden">
<div class="header">
<div class="logo">Privacy-Preserving CDP</div>
<div class="nav" id="nav"></div>
<div class="user-info">
<span id="user-label"></span>
<button class="btn btn-red" id="logout-btn" style="padding:5px 12px;font-size:11px">Logout</button>
</div>
</div>
<div class="main" id="content"></div>
</div>
</body>
</html>"""

JS = r"""
(function(){
var API="/api",TOKEN="",PAGE="dashboard",USER=null;

function el(id){return document.getElementById(id)}
function show(id){el(id).classList.remove("hidden")}
function hide(id){el(id).classList.add("hidden")}

function toast(msg,ok){
  var d=document.createElement("div");
  d.className="toast "+(ok?"toast-ok":"toast-err");
  d.textContent=msg;
  document.body.appendChild(d);
  setTimeout(function(){d.remove()},3500);
}

function api(method,path,body){
  var opts={method:method,headers:{"Content-Type":"application/json"}};
  if(TOKEN)opts.headers["Authorization"]="Bearer "+TOKEN;
  if(body)opts.body=JSON.stringify(body);
  return fetch(API+path,opts).then(function(r){
    if(!r.ok)return r.json().then(function(e){throw new Error(e.detail||r.statusText)});
    return r.json();
  });
}

function bTag(t){
  if(t==="completed"||t==="GRANTED"||t==="SENT"||t==="DELIVERED"||t==="SUCCESS"||t==="RECORDED")return"badge bg";
  if(t==="failed"||t==="DENIED"||t==="BOUNCE"||t==="FAILED")return"badge br";
  if(t==="running")return"badge by";
  return"badge bb";
}

function esc(s){return s?s.replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"):''}

function buildNav(){
  var pages=["dashboard","customers","reveal","marketing","audit"];
  var labels={dashboard:"Dashboard",customers:"Protected DB",reveal:"Reveal",marketing:"Marketing",audit:"Audit"};
  var html="";
  for(var i=0;i<pages.length;i++){
    var p=pages[i];
    html+='<button data-page="'+p+'"'+(p===PAGE?' class="active"':'')+'>'+labels[p]+'</button>';
  }
  el("nav").innerHTML=html;
}

function navigate(p){
  PAGE=p;
  buildNav();
  var c=el("content");
  if(p==="dashboard")renderDash(c);
  else if(p==="customers")renderCust(c);
  else if(p==="reveal")renderRev(c);
  else if(p==="marketing")renderMkt(c);
  else if(p==="audit")renderAud(c);
}

/* LOGIN */
function doLogin(){
  var u=el("login-user").value;
  var p=el("login-pass").value;
  api("POST","/auth/login",{username:u,password:p}).then(function(d){
    TOKEN=d.token;USER=d;
    el("user-label").textContent=d.username+" ("+d.roles.join(", ")+")";
    hide("login-page");show("app-page");
    buildNav();navigate("dashboard");
  }).catch(function(e){
    toast("Login failed: "+e.message,false);
  });
}

function logout(){TOKEN="";USER=null;show("login-page");hide("app-page")}

/* ACTIONS */
function actSeed(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Seeding...';
  api("POST","/seed",{}).then(function(d){
    toast("Seeded "+d.count+" customers");navigate("dashboard");
  }).catch(function(e){toast(e.message,false);
  }).finally(function(){btn.disabled=false;btn.innerHTML="Seed Sample Data"});
}

function actDiscover(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Discovering...';
  api("POST","/discover",{}).then(function(d){
    var html='<div class="card"><h3>PII Discovery Results ('+d.pii_fields_detected+' fields)</h3>';
    html+='<table><thead><tr><th>Field</th><th>Entity Type</th><th>Confidence</th><th>Protection</th></tr></thead><tbody>';
    for(var i=0;i<d.detections.length;i++){
      var x=d.detections[i];
      html+='<tr><td>'+esc(x.field_name)+'</td><td>'+esc(x.entity_type)+'</td><td>'+(x.confidence*100).toFixed(0)+'%</td><td><span class="badge bb">'+esc(x.recommended_protection)+'</span></td></tr>';
    }
    html+='</tbody></table></div>';
    el("act-out").innerHTML=html;
    toast("Discovered "+d.pii_fields_detected+" PII fields");
  }).catch(function(e){toast(e.message,false);
  }).finally(function(){btn.disabled=false;btn.innerHTML="Discover PII"});
}

function actBatch(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Running batch...';
  api("POST","/batch/run",{}).then(function(d){
    var html='<div class="card"><h3>Batch Result</h3>';
    html+='<div class="row"><span class="badge bg">'+esc(d.batch_id)+'</span> <span class="badge bg">'+esc(d.status)+'</span></div>';
    html+='<p style="margin-top:10px;font-size:13px">Total: <b>'+d.total_rows+'</b> | Success: <b style="color:#34d399">'+d.success_count+'</b> | Errors: <b style="color:#f87171">'+d.error_count+'</b></p>';
    html+='</div>';
    el("act-out").innerHTML=html;
    toast("Batch completed: "+d.success_count+"/"+d.total_rows+" rows");
  }).catch(function(e){toast(e.message,false);
  }).finally(function(){btn.disabled=false;btn.innerHTML="Run Batch Protection"});
}

/* DASHBOARD */
function renderDash(c){
  c.innerHTML='<p style="color:#64748b">Loading dashboard...</p>';
  Promise.all([
    api("GET","/audit/stats").catch(function(){return{}}),
    api("GET","/batch").catch(function(){return[]}),
    api("GET","/customers").catch(function(){return[]})
  ]).then(function(res){
    var stats=res[0],batches=res[1],custs=res[2];
    var h='';
    h+='<div class="grid4">';
    h+='<div class="stat"><div class="val">'+(stats.total_audit_logs||0)+'</div><div class="lbl">Audit Events</div></div>';
    h+='<div class="stat"><div class="val">'+(custs.length||0)+'</div><div class="lbl">Protected Records</div></div>';
    h+='<div class="stat"><div class="val">'+(stats.completed_batches||0)+'</div><div class="lbl">Batches Run</div></div>';
    h+='<div class="stat"><div class="val">'+(stats.reveals_granted||0)+'</div><div class="lbl">Reveals Granted</div></div>';
    h+='</div>';
    h+='<div class="card"><h3>Quick Actions</h3>';
    h+='<div class="row">';
    h+='<button class="btn btn-green" id="btn-seed">Seed Sample Data</button>';
    h+='<button class="btn btn-blue" id="btn-discover">Discover PII</button>';
    h+='<button class="btn btn-purple" id="btn-batch">Run Batch Protection</button>';
    h+='</div><div id="act-out"></div></div>';
    h+='<div class="card"><h3>End-to-End Flow</h3>';
    var steps=[
      ["1","Seed Source Data","Load 10 sample customers with PII"],
      ["2","Discover PII Fields","Scan source for sensitive data"],
      ["3","Run Batch Protection","FPE for phones, tokenization for email/name"],
      ["4","Verify Protected DB","No plaintext PII in protected database"],
      ["5","Marketing Email Send","Send email via token, real address never exposed"],
      ["6","Bounce Handling","Webhook reverse-resolves to protected token"],
      ["7","Controlled Reveal","Authorized user reveals plaintext, audited"]
    ];
    for(var i=0;i<steps.length;i++){
      var s=steps[i];
      h+='<div class="flow-step"><div class="num">'+s[0]+'</div><div class="info"><div class="title">'+s[1]+'</div><div class="desc">'+s[2]+'</div></div></div>';
    }
    h+='</div>';
    h+='<div class="card"><h3>Recent Batch Runs</h3>';
    h+='<table><thead><tr><th>Batch ID</th><th>Status</th><th>Rows</th><th>Success</th><th>Errors</th></tr></thead><tbody>';
    if(batches.length){
      for(var j=0;j<batches.length;j++){
        var b=batches[j];
        h+='<tr><td class="mono">'+esc(b.batch_id)+'</td><td><span class="'+bTag(b.status)+'">'+esc(b.status)+'</span></td><td>'+b.total_rows+'</td><td style="color:#34d399">'+b.success_count+'</td><td style="color:'+(b.error_count?'#f87171':'#94a3b8')+'">'+b.error_count+'</td></tr>';
      }
    }else{
      h+='<tr><td colspan="5" style="color:#64748b">No batches yet. Use Quick Actions above.</td></tr>';
    }
    h+='</tbody></table></div>';
    c.innerHTML=h;
    el("btn-seed").onclick=function(){actSeed(this)};
    el("btn-discover").onclick=function(){actDiscover(this)};
    el("btn-batch").onclick=function(){actBatch(this)};
  }).catch(function(e){c.innerHTML='<p style="color:#f87171">Error: '+esc(e.message)+'</p>'});
}

/* CUSTOMERS */
function renderCust(c){
  c.innerHTML='<p style="color:#64748b">Loading protected database...</p>';
  api("GET","/customers").then(function(custs){
    var h='<div class="card"><h3>Protected Customer Database ('+custs.length+' records)</h3>';
    h+='<p style="font-size:12px;color:#94a3b8;margin-bottom:12px">All sensitive fields protected. Names/emails use tokenization, phones use FPE.</p>';
    h+='<table><thead><tr><th>Customer ID</th><th>Name Token</th><th>Email Token</th><th>Mobile FPE</th><th>City</th><th>Segment</th></tr></thead><tbody>';
    for(var i=0;i<custs.length;i++){
      var x=custs[i];
      h+='<tr><td class="mono">'+esc(x.customer_id)+'</td><td class="mono">'+esc(x.name_token)+'</td><td class="mono">'+esc(x.email_token)+'</td><td class="mono">'+esc(x.mobile_fpe)+'</td><td>'+esc(x.city)+'</td><td><span class="'+(x.segment==='Premium'?'badge bg':'badge bb')+'">'+esc(x.segment)+'</span></td></tr>';
    }
    h+='</tbody></table></div>';
    c.innerHTML=h;
  }).catch(function(e){c.innerHTML='<p style="color:#f87171">'+esc(e.message)+'</p>'});
}

/* REVEAL */
function renderRev(c){
  var opts="";
  for(var i=1;i<=10;i++){
    var cid="C00"+i;
    opts+='<option value="'+cid+'">'+cid+'</option>';
  }
  var h='<div class="card"><h3>Controlled Reveal</h3>';
  h+='<p style="font-size:12px;color:#94a3b8;margin-bottom:14px">Reveal plaintext sensitive values with proper authorization. All operations are audited.</p>';
  h+='<div class="row"><label>Customer</label><select class="input" style="width:120px" id="rev-cid">'+opts+'</select>';
  h+='<label>Field</label><select class="input" style="width:120px" id="rev-field"><option>EMAIL</option><option>NAME</option><option>PHONE</option></select>';
  h+='<label>Purpose</label><select class="input" style="width:180px" id="rev-purpose"><option>CUSTOMER_SUPPORT</option><option>FRAUD_INVESTIGATION</option><option>MARKETING</option><option>COMPLIANCE</option></select></div>';
  h+='<div class="row"><label>Reference</label><input class="input" style="width:200px" id="rev-ref" value="TICKET-1091">';
  h+='<button class="btn btn-blue" id="btn-reveal">Reveal</button></div>';
  h+='<div id="rev-result"></div></div>';
  h+='<div class="card"><h3>Access Rules</h3>';
  h+='<table><thead><tr><th>Purpose</th><th>Required Role</th><th>Description</th></tr></thead><tbody>';
  h+='<tr><td>CUSTOMER_SUPPORT</td><td><span class="badge bb">support</span></td><td>Support agents can reveal customer contact info</td></tr>';
  h+='<tr><td>FRAUD_INVESTIGATION</td><td><span class="badge bb">fraud</span></td><td>Fraud team can reveal for investigation</td></tr>';
  h+='<tr><td>MARKETING</td><td><span class="badge bb">marketing</span></td><td>Marketing can reveal for campaign verification</td></tr>';
  h+='<tr><td>COMPLIANCE</td><td><span class="badge bg">admin</span></td><td>Only admins can reveal for compliance</td></tr>';
  h+='</tbody></table>';
  h+='<p style="font-size:11px;color:#64748b;margin-top:10px">Try logging in as <b>viewer</b> (no roles) to see ACCESS_DENIED on reveal.</p></div>';
  c.innerHTML=h;
  el("btn-reveal").onclick=function(){doReveal(this)};
}

function doReveal(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Revealing...';
  api("POST","/reveal",{
    subject_id:el("rev-cid").value,
    field:el("rev-field").value,
    purpose:el("rev-purpose").value,
    reference:el("rev-ref").value
  }).then(function(d){
    el("rev-result").innerHTML='<div style="margin-top:12px;padding:14px;background:#065f46;border:1px solid #34d399;border-radius:8px"><p style="font-size:13px;color:#34d399;font-weight:700;margin-bottom:6px">GRANTED</p><p style="font-size:12px">Customer: <b>'+esc(d.subject_id||el("rev-cid").value)+'</b> | Field: <b>'+esc(d.field||el("rev-field").value)+'</b></p><p style="font-size:20px;font-weight:700;color:#fff;margin-top:8px" class="mono">'+esc(d.plaintext)+'</p><p style="font-size:11px;color:#94a3b8;margin-top:6px">This access has been logged in the audit trail.</p></div>';
    toast("Reveal GRANTED - access logged");
  }).catch(function(e){
    el("rev-result").innerHTML='<div style="margin-top:12px;padding:14px;background:#7f1d1d;border:1px solid #f87171;border-radius:8px"><p style="font-size:13px;color:#f87171;font-weight:700">ACCESS DENIED</p><p style="font-size:12px;color:#fca5a5;margin-top:4px">'+esc(e.message)+'</p><p style="font-size:11px;color:#94a3b8;margin-top:6px">This denial has been logged in the audit trail.</p></div>';
    toast("Reveal DENIED",false);
  }).finally(function(){btn.disabled=false;btn.innerHTML="Reveal"});
}

/* MARKETING */
function renderMkt(c){
  c.innerHTML='<p style="color:#64748b">Loading...</p>';
  api("GET","/customers").then(function(custs){
    var opts="";
    for(var i=0;i<custs.length;i++){
      opts+='<option value="'+esc(custs[i].email_token)+'">'+esc(custs[i].customer_id)+' - '+esc(custs[i].email_token)+'</option>';
    }
    var h='<div class="grid2">';
    h+='<div class="card"><h3>Send Marketing Email</h3>';
    h+='<p style="font-size:12px;color:#94a3b8;margin-bottom:12px">Marketing app sends email using protected token. Real address never exposed.</p>';
    h+='<div class="row"><label>Recipient</label><select class="input" id="mkt-rcpt">'+opts+'</select></div>';
    h+='<div class="row"><label>Campaign</label><input class="input" style="width:140px" id="mkt-camp" value="CMP1001"></div>';
    h+='<div class="row"><label>Template</label><input class="input" style="width:140px" id="mkt-tmpl" value="WELCOME"></div>';
    h+='<button class="btn btn-green" id="btn-send">Send Email</button>';
    h+='<div id="mkt-send-result"></div></div>';
    h+='<div class="card"><h3>Simulate Bounce Webhook</h3>';
    h+='<p style="font-size:12px;color:#94a3b8;margin-bottom:12px">Email provider sends bounce with real email. Gateway reverse-resolves to protected token.</p>';
    h+='<div class="row"><label>Email</label><input class="input" id="bnc-email" value="john@example.com"></div>';
    h+='<div class="row"><label>Reason</label><input class="input" id="bnc-reason" value="MAILBOX_NOT_FOUND"></div>';
    h+='<button class="btn btn-red" id="btn-bounce">Simulate Bounce</button>';
    h+='<div id="bnc-result"></div></div></div>';
    h+='<div class="card"><h3>Email Events</h3><div id="mkt-events"><p style="color:#64748b">Loading events...</p></div></div>';
    c.innerHTML=h;
    el("btn-send").onclick=function(){doSendEmail(this)};
    el("btn-bounce").onclick=function(){doBounce(this)};
    loadEmailEvents();
  }).catch(function(e){c.innerHTML='<p style="color:#f87171">'+esc(e.message)+'</p>'});
}

function loadEmailEvents(){
  api("GET","/email-events").then(function(evts){
    var h="";
    if(evts.length){
      h+='<table><thead><tr><th>Time</th><th>Recipient</th><th>Event</th><th>Campaign</th><th>Reason</th></tr></thead><tbody>';
      for(var i=0;i<evts.length;i++){
        var e=evts[i];
        h+='<tr><td>'+(e.timestamp||"").replace("T"," ").slice(0,19)+'</td><td class="mono">'+esc(e.recipient_token)+'</td><td><span class="'+bTag(e.event_type)+'">'+esc(e.event_type)+'</span></td><td>'+esc(e.campaign_id||"-")+'</td><td>'+esc(e.reason||"-")+'</td></tr>';
      }
      h+='</tbody></table>';
    }else{
      h='<p style="color:#64748b">No email events yet. Send an email or simulate a bounce above.</p>';
    }
    el("mkt-events").innerHTML=h;
  }).catch(function(e){el("mkt-events").innerHTML='<p style="color:#f87171">'+esc(e.message)+'</p>'});
}

function doSendEmail(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Sending...';
  api("POST","/actions/send-email",{recipient:el("mkt-rcpt").value,campaign_id:el("mkt-camp").value,template_id:el("mkt-tmpl").value}).then(function(d){
    el("mkt-send-result").innerHTML='<div style="margin-top:12px;padding:14px;background:#065f46;border:1px solid #34d399;border-radius:8px"><p style="color:#34d399;font-weight:700">Email Sent Successfully</p><p style="font-size:12px;margin-top:6px">Recipient token: <b class="mono">'+esc(d.recipient)+'</b></p><p style="font-size:12px;color:#94a3b8;margin-top:4px">Marketing app never sees the real email address.</p></div>';
    toast("Email sent to "+d.recipient);loadEmailEvents();
  }).catch(function(e){toast(e.message,false);el("mkt-send-result").innerHTML='<div style="margin-top:12px;padding:14px;background:#7f1d1d;border:1px solid #f87171;border-radius:8px"><p style="color:#f87171">'+esc(e.message)+'</p></div>';
  }).finally(function(){btn.disabled=false;btn.innerHTML="Send Email"});
}

function doBounce(btn){
  btn.disabled=true;btn.innerHTML='<span class="spinner"></span>Processing...';
  api("POST","/webhooks/email",{email:el("bnc-email").value,event:"BOUNCE",reason:el("bnc-reason").value}).then(function(d){
    el("bnc-result").innerHTML='<div style="margin-top:12px;padding:14px;background:#78350f;border:1px solid #fbbf24;border-radius:8px"><p style="color:#fbbf24;font-weight:700">Bounce Processed</p><p style="font-size:12px;margin-top:6px">Real email <b>'+esc(el("bnc-email").value)+'</b> resolved to token:</p><p style="font-size:16px;font-weight:700;color:#fff;margin-top:4px" class="mono">'+esc(d.recipient)+'</p><p style="font-size:12px;color:#94a3b8;margin-top:4px">Stored as protected ID - no plaintext in downstream systems.</p></div>';
    toast("Bounce mapped to "+d.recipient);loadEmailEvents();
  }).catch(function(e){toast(e.message,false);
  }).finally(function(){btn.disabled=false;btn.innerHTML="Simulate Bounce"});
}

/* AUDIT */
function renderAud(c){
  c.innerHTML='<p style="color:#64748b">Loading audit trail...</p>';
  Promise.all([
    api("GET","/audit?limit=50"),
    api("GET","/audit/stats").catch(function(){return{}})
  ]).then(function(res){
    var logs=res[0],stats=res[1];
    var h='<div class="grid4">';
    h+='<div class="stat"><div class="val">'+(stats.total_audit_logs||0)+'</div><div class="lbl">Total Events</div></div>';
    h+='<div class="stat"><div class="val" style="color:#34d399">'+(stats.reveals_granted||0)+'</div><div class="lbl">Reveals Granted</div></div>';
    h+='<div class="stat"><div class="val" style="color:#f87171">'+(stats.reveals_denied||0)+'</div><div class="lbl">Reveals Denied</div></div>';
    h+='<div class="stat"><div class="val">'+(stats.total_emails||0)+'</div><div class="lbl">Emails Sent</div></div></div>';
    h+='<div class="card"><h3>Audit Trail (Last 50 Events)</h3>';
    h+='<table><thead><tr><th>Time</th><th>Actor</th><th>Action</th><th>Field</th><th>Purpose</th><th>Outcome</th></tr></thead><tbody>';
    if(logs.length){
      for(var i=0;i<logs.length;i++){
        var l=logs[i];
        h+='<tr><td>'+(l.timestamp||"").replace("T"," ").slice(0,19)+'</td><td>'+esc(l.actor)+'</td><td>'+esc(l.action)+'</td><td>'+esc(l.field||"-")+'</td><td>'+esc(l.purpose||"-")+'</td><td><span class="'+bTag(l.outcome)+'">'+esc(l.outcome)+'</span></td></tr>';
      }
    }else{
      h+='<tr><td colspan="6" style="color:#64748b">No audit events yet.</td></tr>';
    }
    h+='</tbody></table></div>';
    c.innerHTML=h;
  }).catch(function(e){c.innerHTML='<p style="color:#f87171">'+esc(e.message)+'</p>'});
}

/* INIT */
document.getElementById("login-btn").onclick=doLogin;
document.getElementById("logout-btn").onclick=logout;
document.getElementById("nav").onclick=function(e){
  if(e.target.tagName==="BUTTON"&&e.target.dataset.page){
    navigate(e.target.dataset.page);
  }
};
})();
"""

html = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
html += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
html += '<title>Privacy-Preserving CDP Dashboard</title>\n'
html += '<style>\n' + CSS + '\n</style>\n'
html += '</head>\n'
html += HTML_BODY.replace('</head>', '').replace('</body>', '').replace('</html>', '')
html += '<script>\n' + JS + '\n</script>\n'
html += '</body>\n</html>'

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("Dashboard written:", os.path.getsize(OUT), "bytes")
