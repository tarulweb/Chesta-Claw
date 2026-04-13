'use client';
import React from 'react';
import { Activity, ShieldCheck, Server, Terminal, Zap, GitBranch, MessageSquare } from 'lucide-react';

export default function Dashboard() {
  const stats = [
    { label: 'Active Agents', value: '3', icon: Activity, color: 'text-green-500' },
    { label: 'API Health', value: '100%', icon: ShieldCheck, color: 'text-blue-500' },
    { label: 'Resource Usage', value: '250MB', icon: Server, color: 'text-purple-500' },
    { label: 'Tasks Completed', value: '1,248', icon: Zap, color: 'text-yellow-500' },
  ];

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">System Overview</h1>
        <div className="flex gap-2">
          <span className="bg-green-500/10 text-green-500 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-2">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            CEO_BRAIN ONLINE
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat) => (
          <div key={stat.label} className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <div className="flex items-center justify-between mb-4">
              <stat.icon className={stat.color} size={24} />
            </div>
            <div className="text-2xl font-bold">{stat.value}</div>
            <div className="text-slate-400 text-sm">{stat.label}</div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 min-h-[400px]">
          <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
            <MessageSquare size={20} className="text-blue-500"/> Recent Activity
          </h2>
          <div className="space-y-4">
            {[
              { agent: 'CEO_BRAIN', msg: 'Decomposed goal: Create crypto tracker', time: '2m ago' },
              { agent: 'CODER', msg: 'Generated FastAPI backend structure', time: '5m ago' },
              { agent: 'RESEARCHER', msg: 'Fetched top 10 coin APIs from CoinGecko', time: '8m ago' },
            ].map((act, i) => (
              <div key={i} className="bg-slate-900/50 p-4 rounded-lg border border-slate-800 flex justify-between">
                <div>
                  <span className="text-blue-400 font-mono text-xs">{act.agent}</span>
                  <p className="text-slate-300 text-sm">{act.msg}</p>
                </div>
                <span className="text-slate-500 text-xs">{act.time}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
            <GitBranch size={20} className="text-purple-500"/> Workflow Performance
          </h2>
          <div className="space-y-6">
            {['App Gen', 'Data Analysis', 'Web Search'].map((w) => (
              <div key={w} className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-slate-300">{w}</span>
                  <span className="text-blue-500">85% efficiency</span>
                </div>
                <div className="w-full bg-slate-900 rounded-full h-2">
                  <div className="bg-blue-500 h-2 rounded-full" style={{ width: '85%' }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
