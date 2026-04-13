'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Send, Terminal as TerminalIcon } from 'lucide-react';

export default function Terminal() {
  const [logs, setLogs] = useState<{timestamp: string, message: string, type: string}[]>([]);
  const [input, setInput] = useState('');
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Connect to WebSocket
    const ws = new WebSocket('ws://localhost:8000/ws/logs');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setLogs(prev => [...prev, {
        timestamp: new Date().toLocaleTimeString(),
        message: data.message,
        type: data.type
      }]);
    };
    return () => ws.close();
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input) return;

    setLogs(prev => [...prev, {
      timestamp: new Date().toLocaleTimeString(),
      message: `> ${input}`,
      type: 'user'
    }]);

    try {
      await fetch('http://localhost:8000/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal: input }),
      });
    } catch (err) {
      console.error(err);
    }

    setInput('');
  };

  return (
    <div className="flex flex-col h-[calc(100vh-8rem)] bg-black border border-slate-800 rounded-xl overflow-hidden font-mono text-sm">
      <div className="bg-slate-900 px-4 py-2 border-b border-slate-800 flex items-center gap-2">
        <TerminalIcon size={16} className="text-slate-400" />
        <span className="text-slate-400">CHESTA SYSTEM TERMINAL</span>
      </div>

      <div ref={scrollRef} className="flex-1 p-4 overflow-y-auto space-y-1">
        {logs.map((log, i) => (
          <div key={i} className={`flex gap-3 ${log.type === 'user' ? 'text-blue-400' : 'text-green-500'}`}>
            <span className="text-slate-600">[{log.timestamp}]</span>
            <span className="whitespace-pre-wrap">{log.message}</span>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="p-4 border-t border-slate-800 bg-slate-900 flex gap-4">
        <span className="text-blue-500">$</span>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter goal or command..."
          className="flex-1 bg-transparent border-none outline-none text-white"
          autoFocus
        />
        <button type="submit" className="text-slate-500 hover:text-white transition-colors">
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}
