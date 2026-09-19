import React, { useState, useEffect } from 'react'

const API = '/api'

function useFetch(url, options = {}) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    setLoading(true)
    fetch(`${API}${url}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
        ...(localStorage.getItem('token') ? { Authorization: `Bearer ${localStorage.getItem('token')}` } : {}),
      },
    })
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false))
  }, [url])

  return { data, loading, error }
}

async function apiPost(url, body) {
  const res = await fetch(`${API}${url}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(localStorage.getItem('token') ? { Authorization: `Bearer ${localStorage.getItem('token')}` } : {}),
    },
    body: JSON.stringify(body),
  })
  return res.json()
}

const styles = {
  app: { minHeight: '100vh', background: '#0f172a' },
  header: { background: '#1e293b', borderBottom: '1px solid #334155', padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' },
  logo: { fontSize: '20px', fontWeight: 'bold', color: '#38bdf8' },
  nav: { display: 'flex', gap: '8px' },
  navBtn: (active) => ({ padding: '8px 16px', borderRadius: '6px', border: 'none', cursor: 'pointer', background: active ? '#3b82f6' : 'transparent', color: active ? 'white' : '#94a3b8', fontWeight: active ? 'bold' : 'normal', fontSize: '14px' }),
  main: { padding: '24px', maxWidth: '1200px', margin: '0 auto' },
  card: { background: '#1e293b', borderRadius: '12px', padding: '20px', marginBottom: '16px', border: '1px solid #334155' },
  cardTitle: { fontSize: '16px', fontWeight: 'bold', color: '#38bdf8', marginBottom: '12px' },
  stat: { textAlign: 'center', padding: '16px' },
  statValue: { fontSize: '32px', fontWeight: 'bold', color: '#38bdf8' },
  statLabel: { fontSize: '13px', color: '#94a3b8', marginTop: '4px' },
  grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px' },
  table: { width: '100%', borderCollapse: 'collapse', fontSize: '13px' },
  th: { textAlign: 'left', padding: '10px 12px', borderBottom: '2px solid #334155', color: '#94a3b8', fontWeight: '600' },
  td: { padding: '10px 12px', borderBottom: '1px solid #1e293b' },
  badge: (color) => ({ display: 'inline-block', padding: '2px 8px', borderRadius: '12px', fontSize: '11px', fontWeight: 'bold', background: color === 'green' ? '#065f46' : color === 'red' ? '#7f1d1d' : color === 'yellow' ? '#78350f' : '#1e3a5f', color: color === 'green' ? '#34d399' : color === 'red' ? '#f87171' : color === 'yellow' ? '#fbbf24' : '#60a5fa' }),
  btn: { padding: '10px 20px', borderRadius: '8px', border: 'none', cursor: 'pointer', background: '#3b82f6', color: 'white', fontWeight: 'bold', fontSize: '14px' },
  btnSuccess: { padding: '10px 20px', borderRadius: '8px', border: 'none', cursor: 'pointer', background: '#10b981', color: 'white', fontWeight: 'bold', fontSize: '14px' },
  btnDanger: { padding: '10px 20px', borderRadius: '8px', border: 'none', cursor: 'pointer', background: '#ef4444', color: 'white', fontWeight: 'bold', fontSize: '14px' },
  input: { padding: '8px 12px', borderRadius: '6px', border: '1px solid #334155', background: '#0f172a', color: '#e2e8f0', fontSize: '14px', width: '100%' },
  select: { padding: '8px 12px', borderRadius: '6px', border: '1px solid #334155', background: '#0f172a', color: '#e2e8f0', fontSize: '14px' },
  row: { display: 'flex', gap: '12px', marginBottom: '12px', alignItems: 'center', flexWrap: 'wrap' },
}

function Login({ onLogin }) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const handleLogin = async () => {
    const res = await apiPost('/auth/login', { username, password })
    if (res.token) {
      localStorage.setItem('token', res.token)
      localStorage.setItem('user', JSON.stringify(res))
      onLogin(res)
    } else {
      setError('Invalid credentials')
    }
  }

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div style={{ ...styles.card, width: '360px' }}>
        <h2 style={{ textAlign: 'center', marginBottom: '20px', color: '#38bdf8' }}>Privacy CDP Login</h2>
        {error && <p style={{ color: '#f87171', marginBottom: '12px', textAlign: 'center' }}>{error}</p>}
        <input style={{ ...styles.input, marginBottom: '12px' }} placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
        <input style={{ ...styles.input, marginBottom: '16px' }} type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        <button style={{ ...styles.btn, width: '100%' }} onClick={handleLogin}>Login</button>
        <p style={{ fontSize: '12px', color: '#64748b', marginTop: '12px', textAlign: 'center' }}>
          Demo: admin/admin123, marketing_user/marketing123, support_user/support123
        </p>
      </div>
    </div>
  )
}

function Dashboard() {
  const { data: stats } = useFetch('/audit/stats')
  const { data: batches } = useFetch('/batch')
  const { data: customers } = useFetch('/customers')
  const [seeding, setSeeding] = useState(false)
  const [discovering, setDiscovering] = useState(false)
  const [discovery, setDiscovery] = useState(null)
  const [batchRunning, setBatchRunning] = useState(false)
  const [batchResult, setBatchResult] = useState(null)

  const seedData = async () => {
    setSeeding(true)
    await apiPost('/seed', {})
    setSeeding(false)
    window.location.reload()
  }

  const discoverPII = async () => {
    setDiscovering(true)
    const res = await apiPost('/discover', {})
    setDiscovery(res)
    setDiscovering(false)
  }

  const runBatch = async () => {
    setBatchRunning(true)
    const res = await apiPost('/batch/run', {})
    setBatchResult(res)
    setBatchRunning(false)
  }

  return (
    <div>
      <div style={styles.grid}>
        <div style={styles.card}>
          <div style={styles.stat}>
            <div style={styles.statValue}>{stats?.total_audit_logs || 0}</div>
            <div style={styles.statLabel}>Audit Events</div>
          </div>
        </div>
        <div style={styles.card}>
          <div style={styles.stat}>
            <div style={styles.statValue}>{customers?.length || 0}</div>
            <div style={styles.statLabel}>Protected Records</div>
          </div>
        </div>
        <div style={styles.card}>
          <div style={styles.stat}>
            <div style={styles.statValue}>{stats?.completed_batches || 0}</div>
            <div style={styles.statLabel}>Batches Run</div>
          </div>
        </div>
        <div style={styles.card}>
          <div style={styles.stat}>
            <div style={styles.statValue}>{stats?.reveals_granted || 0}</div>
            <div style={styles.statLabel}>Reveals Granted</div>
          </div>
        </div>
      </div>

      <div style={styles.card}>
        <div style={styles.cardTitle}>Quick Actions</div>
        <div style={styles.row}>
          <button style={styles.btnSuccess} onClick={seedData} disabled={seeding}>{seeding ? 'Seeding...' : 'Seed Sample Data'}</button>
          <button style={styles.btn} onClick={discoverPII} disabled={discovering}>{discovering ? 'Discovering...' : 'Discover PII Fields'}</button>
          <button style={{ ...styles.btn, background: '#8b5cf6' }} onClick={runBatch} disabled={batchRunning}>{batchRunning ? 'Running...' : 'Run Batch Protection'}</button>
        </div>
      </div>

      {discovery && (
        <div style={styles.card}>
          <div style={styles.cardTitle}>PII Discovery Results</div>
          <table style={styles.table}>
            <thead>
              <tr><th style={styles.th}>Field</th><th style={styles.th}>Type</th><th style={styles.th}>Confidence</th><th style={styles.th}>Protection</th></tr>
            </thead>
            <tbody>
              {discovery.detections?.map((d, i) => (
                <tr key={i}>
                  <td style={styles.td}>{d.field_name}</td>
                  <td style={styles.td}>{d.entity_type}</td>
                  <td style={styles.td}>{(d.confidence * 100).toFixed(0)}%</td>
                  <td style={styles.td}><span style={styles.badge('blue')}>{d.recommended_protection}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {batchResult && (
        <div style={styles.card}>
          <div style={styles.cardTitle}>Batch Result</div>
          <pre style={{ color: '#34d399', fontSize: '13px' }}>{JSON.stringify(batchResult, null, 2)}</pre>
        </div>
      )}

      <div style={styles.card}>
        <div style={styles.cardTitle}>Recent Batch Runs</div>
        <table style={styles.table}>
          <thead>
            <tr><th style={styles.th}>Batch ID</th><th style={styles.th}>Status</th><th style={styles.th}>Rows</th><th style={styles.th}>Success</th><th style={styles.th}>Errors</th></tr>
          </thead>
          <tbody>
            {batches?.map((b, i) => (
              <tr key={i}>
                <td style={styles.td}>{b.batch_id}</td>
                <td style={styles.td}><span style={styles.badge(b.status === 'completed' ? 'green' : b.status === 'failed' ? 'red' : 'yellow')}>{b.status}</span></td>
                <td style={styles.td}>{b.total_rows}</td>
                <td style={styles.td}>{b.success_count}</td>
                <td style={styles.td}>{b.error_count}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

function Customers() {
  const { data: customers, loading } = useFetch('/customers')

  return (
    <div>
      <div style={styles.card}>
        <div style={styles.cardTitle}>Protected Customer Database</div>
        <p style={{ fontSize: '13px', color: '#94a3b8', marginBottom: '16px' }}>
          All sensitive fields are protected. Names and emails use tokenization, phone numbers use FPE.
        </p>
        {loading ? <p>Loading...</p> : (
          <table style={styles.table}>
            <thead>
              <tr><th style={styles.th}>Customer ID</th><th style={styles.th}>Name Token</th><th style={styles.th}>Email Token</th><th style={styles.th}>Mobile FPE</th><th style={styles.th}>City</th><th style={styles.th}>Segment</th></tr>
            </thead>
            <tbody>
              {customers?.map((c, i) => (
                <tr key={i}>
                  <td style={styles.td}>{c.customer_id}</td>
                  <td style={styles.td}>{c.name_token}</td>
                  <td style={styles.td}>{c.email_token}</td>
                  <td style={styles.td}>{c.mobile_fpe}</td>
                  <td style={styles.td}>{c.city}</td>
                  <td style={styles.td}><span style={styles.badge(c.segment === 'Premium' ? 'green' : 'blue')}>{c.segment}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}

function Reveal() {
  const [customerId, setCustomerId] = useState('C001')
  const [field, setField] = useState('EMAIL')
  const [purpose, setPurpose] = useState('CUSTOMER_SUPPORT')
  const [reference, setReference] = useState('TICKET-1001')
  const [result, setResult] = useState(null)

  const doReveal = async () => {
    const res = await apiPost('/reveal', { subject_id: customerId, field, purpose, reference })
    setResult(res)
  }

  return (
    <div>
      <div style={styles.card}>
        <div style={styles.cardTitle}>Controlled Reveal</div>
        <p style={{ fontSize: '13px', color: '#94a3b8', marginBottom: '16px' }}>
          Reveal plaintext sensitive values with proper authorization. All operations are audited.
        </p>
        <div style={styles.row}>
          <select style={styles.select} value={customerId} onChange={e => setCustomerId(e.target.value)}>
            <option value="C001">C001</option><option value="C002">C002</option><option value="C003">C003</option>
            <option value="C004">C004</option><option value="C005">C005</option><option value="C006">C006</option>
          </select>
          <select style={styles.select} value={field} onChange={e => setField(e.target.value)}>
            <option value="EMAIL">EMAIL</option><option value="NAME">NAME</option><option value="PHONE">PHONE</option>
          </select>
          <select style={styles.select} value={purpose} onChange={e => setPurpose(e.target.value)}>
            <option value="CUSTOMER_SUPPORT">CUSTOMER_SUPPORT</option>
            <option value="FRAUD_INVESTIGATION">FRAUD_INVESTIGATION</option>
            <option value="MARKETING">MARKETING</option>
          </select>
          <input style={{ ...styles.input, width: '200px' }} placeholder="Reference" value={reference} onChange={e => setReference(e.target.value)} />
          <button style={styles.btn} onClick={doReveal}>Reveal</button>
        </div>
      </div>

      {result && (
        <div style={styles.card}>
          <div style={styles.cardTitle}>Reveal Result</div>
          <pre style={{ color: result.outcome === 'GRANTED' ? '#34d399' : '#f87171', fontSize: '13px' }}>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  )
}

function Audit() {
  const { data: logs, loading } = useFetch('/audit?limit=50')

  return (
    <div>
      <div style={styles.card}>
        <div style={styles.cardTitle}>Audit Trail</div>
        <p style={{ fontSize: '13px', color: '#94a3b8', marginBottom: '16px' }}>
          Complete audit log of all sensitive operations. Every reveal, email, and batch is recorded.
        </p>
        {loading ? <p>Loading...</p> : (
          <table style={styles.table}>
            <thead>
              <tr><th style={styles.th}>Timestamp</th><th style={styles.th}>Actor</th><th style={styles.th}>Action</th><th style={styles.th}>Field</th><th style={styles.th}>Purpose</th><th style={styles.th}>Outcome</th></tr>
            </thead>
            <tbody>
              {logs?.map((log, i) => (
                <tr key={i}>
                  <td style={styles.td}>{log.timestamp?.replace('T', ' ').slice(0, 19)}</td>
                  <td style={styles.td}>{log.actor}</td>
                  <td style={styles.td}>{log.action}</td>
                  <td style={styles.td}>{log.field}</td>
                  <td style={styles.td}>{log.purpose}</td>
                  <td style={styles.td}><span style={styles.badge(log.outcome === 'GRANTED' ? 'green' : log.outcome === 'DENIED' ? 'red' : 'blue')}>{log.outcome}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}

function Marketing() {
  const [recipient, setRecipient] = useState('')
  const [campaignId, setCampaignId] = useState('CMP1001')
  const [templateId, setTemplateId] = useState('WELCOME')
  const [sendResult, setSendResult] = useState(null)
  const [bounceEmail, setBounceEmail] = useState('')
  const [bounceReason, setBounceReason] = useState('MAILBOX_NOT_FOUND')
  const [bounceResult, setBounceResult] = useState(null)
  const { data: emailEvents } = useFetch('/email-events')

  const sendEmail = async () => {
    const res = await apiPost('/actions/send-email', { recipient, campaign_id: campaignId, template_id: templateId })
    setSendResult(res)
  }

  const simulateBounce = async () => {
    const res = await apiPost('/webhooks/email', { email: bounceEmail, event: 'BOUNCE', reason: bounceReason })
    setBounceResult(res)
  }

  return (
    <div>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
        <div style={styles.card}>
          <div style={styles.cardTitle}>Send Marketing Email</div>
          <div style={styles.row}>
            <input style={styles.input} placeholder="Recipient Token (e.g. EMAIL_P91QZ)" value={recipient} onChange={e => setRecipient(e.target.value)} />
          </div>
          <div style={styles.row}>
            <input style={{ ...styles.input, width: '150px' }} placeholder="Campaign ID" value={campaignId} onChange={e => setCampaignId(e.target.value)} />
            <input style={{ ...styles.input, width: '150px' }} placeholder="Template ID" value={templateId} onChange={e => setTemplateId(e.target.value)} />
          </div>
          <button style={styles.btnSuccess} onClick={sendEmail}>Send Email</button>
          {sendResult && <pre style={{ marginTop: '12px', color: '#34d399', fontSize: '12px' }}>{JSON.stringify(sendResult, null, 2)}</pre>}
        </div>

        <div style={styles.card}>
          <div style={styles.cardTitle}>Simulate Bounce Webhook</div>
          <div style={styles.row}>
            <input style={styles.input} placeholder="Real Email (from webhook)" value={bounceEmail} onChange={e => setBounceEmail(e.target.value)} />
          </div>
          <div style={styles.row}>
            <input style={{ ...styles.input, width: '200px' }} placeholder="Reason" value={bounceReason} onChange={e => setBounceReason(e.target.value)} />
          </div>
          <button style={styles.btnDanger} onClick={simulateBounce}>Simulate Bounce</button>
          {bounceResult && <pre style={{ marginTop: '12px', color: '#fbbf24', fontSize: '12px' }}>{JSON.stringify(bounceResult, null, 2)}</pre>}
        </div>
      </div>

      <div style={styles.card}>
        <div style={styles.cardTitle}>Email Events</div>
        <table style={styles.table}>
          <thead>
            <tr><th style={styles.th}>Timestamp</th><th style={styles.th}>Recipient</th><th style={styles.th}>Event</th><th style={styles.th}>Campaign</th><th style={styles.th}>Reason</th></tr>
          </thead>
          <tbody>
            {emailEvents?.map((e, i) => (
              <tr key={i}>
                <td style={styles.td}>{e.timestamp?.replace('T', ' ').slice(0, 19)}</td>
                <td style={styles.td}>{e.recipient_token}</td>
                <td style={styles.td}><span style={styles.badge(e.event_type === 'SENT' ? 'green' : e.event_type === 'BOUNCE' ? 'red' : 'blue')}>{e.event_type}</span></td>
                <td style={styles.td}>{e.campaign_id}</td>
                <td style={styles.td}>{e.reason}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

function App() {
  const [page, setPage] = useState('dashboard')
  const [user, setUser] = useState(null)

  useEffect(() => {
    const saved = localStorage.getItem('user')
    if (saved) setUser(JSON.parse(saved))
  }, [])

  const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    setUser(null)
  }

  if (!user) return <Login onLogin={setUser} />

  const pages = {
    dashboard: { label: 'Dashboard', component: <Dashboard /> },
    customers: { label: 'Protected DB', component: <Customers /> },
    reveal: { label: 'Reveal', component: <Reveal /> },
    marketing: { label: 'Marketing', component: <Marketing /> },
    audit: { label: 'Audit', component: <Audit /> },
  }

  return (
    <div style={styles.app}>
      <div style={styles.header}>
        <div style={styles.logo}>Privacy-Preserving CDP</div>
        <div style={styles.nav}>
          {Object.entries(pages).map(([key, { label }]) => (
            <button key={key} style={styles.navBtn(page === key)} onClick={() => setPage(key)}>{label}</button>
          ))}
        </div>
        <div>
          <span style={{ marginRight: '12px', color: '#94a3b8', fontSize: '13px' }}>{user.username}</span>
          <button style={{ ...styles.btnDanger, padding: '6px 12px', fontSize: '12px' }} onClick={logout}>Logout</button>
        </div>
      </div>
      <div style={styles.main}>{pages[page].component}</div>
    </div>
  )
}

export default App
