"use client";

import axios from 'axios';
import { useState } from 'react';

export default function HomePage() {
  const [username, setUsername] = useState('admin@local');
  const [password, setPassword] = useState('changeit!');
  const [token, setToken] = useState<string | null>(null);
  const [me, setMe] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || process.env.BACKEND_URL || 'http://localhost:8000';

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      const params = new URLSearchParams();
      params.append('username', username);
      params.append('password', password);
      const res = await axios.post(`${backendUrl}/api/auth/token`, params, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      setToken(res.data.access_token);
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Login failed');
    }
  }

  async function handleMe() {
    if (!token) return;
    const res = await axios.get(`${backendUrl}/api/me`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    setMe(res.data);
  }

  return (
    <main style={{ maxWidth: 420, margin: '40px auto', fontFamily: 'Inter, system-ui, sans-serif' }}>
      <h1>CLOAK IAM</h1>
      <form onSubmit={handleLogin} style={{ display: 'grid', gap: 12 }}>
        <label>
          Username
          <input value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <label>
          Password
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <button type="submit">Login</button>
      </form>
      {error && <p style={{ color: 'crimson' }}>{error}</p>}
      {token && (
        <div style={{ marginTop: 16 }}>
          <button onClick={handleMe}>Call /api/me</button>
          {me && (
            <pre style={{ background: '#f5f5f5', padding: 12, borderRadius: 8 }}>
              {JSON.stringify(me, null, 2)}
            </pre>
          )}
        </div>
      )}
    </main>
  );
}