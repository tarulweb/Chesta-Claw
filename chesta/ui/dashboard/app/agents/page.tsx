'use client';
import React from 'react';
import { Users, Shield, Zap } from 'lucide-react';

export default function AgentsPage() {
  const agents = [
    { name: 'CEO_BRAIN', status: 'Active', role: 'Orchestrator', health: '100%' },
    { name: 'RESEARCHER', status: 'Idle', role: 'Web Search', health: '98%' },
    { name: 'CODER', status: 'Active', role: 'DevOps', health: '100%' },
  ];

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Agent Fleet</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {agents.map((agent) => (
          <div key={agent.name} className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <div className="flex justify-between items-center mb-4">
              <div className="bg-blue-500/10 p-3 rounded-lg text-blue-500">
                <Users size={24} />
              </div>
              <span className="bg-green-500/10 text-green-500 text-xs px-2 py-1 rounded-full uppercase font-bold tracking-tighter">
                {agent.status}
              </span>
            </div>
            <h3 className="text-xl font-bold mb-1">{agent.name}</h3>
            <p className="text-slate-400 text-sm mb-4">{agent.role}</p>
            <div className="flex items-center gap-4 text-xs font-mono text-slate-500">
              <div className="flex items-center gap-1"><Shield size={12} /> {agent.health}</div>
              <div className="flex items-center gap-1"><Zap size={12} /> High Performance</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
