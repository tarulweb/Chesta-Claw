import React from 'react';
import { Activity, ShieldCheck, Server, Terminal } from 'lucide-react';

export default function Dashboard() {
  const stats = [
    { label: 'Active Agents', value: '1', icon: Activity, color: 'text-green-500' },
    { label: 'API Health', value: '100%', icon: ShieldCheck, color: 'text-blue-500' },
    { label: 'Resource Usage', value: '250MB', icon: Server, color: 'text-purple-500' },
    { label: 'Tasks Completed', value: '12', icon: Terminal, color: 'text-yellow-500' },
  ];

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Dashboard</h1>

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
          <h2 className="text-xl font-bold mb-4">Agent Activity</h2>
          <div className="space-y-4">
            <div className="bg-slate-900 p-4 rounded-lg border border-slate-800">
              <div className="flex justify-between text-sm mb-1">
                <span className="text-blue-400 font-mono">CEO_BRAIN</span>
                <span className="text-slate-500">Just now</span>
              </div>
              <p className="text-slate-300">Monitoring API health for all providers...</p>
            </div>
          </div>
        </div>

        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 min-h-[400px]">
          <h2 className="text-xl font-bold mb-4">Resource Monitor</h2>
          <div className="h-64 flex items-end gap-2 px-4">
            {[40, 60, 45, 70, 50, 85, 30].map((h, i) => (
              <div
                key={i}
                className="flex-1 bg-blue-500/20 border-t-2 border-blue-500 rounded-t"
                style={{ height: `${h}%` }}
              ></div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
