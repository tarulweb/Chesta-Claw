'use client';

import React from 'react';
import { Cpu, CheckCircle2, AlertCircle } from 'lucide-react';

const providers = [
  { name: 'OpenRouter', status: 'Healthy', latency: '120ms', active: true },
  { name: 'Ollama', status: 'Offline', latency: '-', active: false },
  { name: 'LM Studio', status: 'Healthy', latency: '45ms', active: true },
  { name: 'OpenAI', status: 'Healthy', latency: '180ms', active: true },
];

export default function ModelsPage() {
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Model Providers</h1>

      <div className="grid grid-cols-1 gap-4">
        {providers.map((p) => (
          <div key={p.name} className="bg-slate-800 p-6 rounded-xl border border-slate-700 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className={`p-3 rounded-lg ${p.active ? 'bg-green-500/10 text-green-500' : 'bg-slate-700 text-slate-500'}`}>
                <Cpu size={24} />
              </div>
              <div>
                <h3 className="text-lg font-bold">{p.name}</h3>
                <div className="flex items-center gap-2 text-sm">
                  {p.active ? <CheckCircle2 size={14} className="text-green-500" /> : <AlertCircle size={14} className="text-red-500" />}
                  <span className={p.active ? 'text-green-500' : 'text-red-500'}>{p.status}</span>
                  <span className="text-slate-500">•</span>
                  <span className="text-slate-500">Latency: {p.latency}</span>
                </div>
              </div>
            </div>
            <button className="px-4 py-2 border border-slate-700 rounded-lg hover:bg-slate-700 transition-colors">
              Configure
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
