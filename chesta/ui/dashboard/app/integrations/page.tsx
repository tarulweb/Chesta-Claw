'use client';
import React from 'react';
import { MessageSquare, Mail } from 'lucide-react';

export default function IntegrationsPage() {
  const channels = [
    { name: 'Telegram', status: 'Connected', icon: MessageSquare },
    { name: 'Discord', status: 'Connected', icon: MessageSquare },
    { name: 'WhatsApp', status: 'Pending', icon: MessageSquare },
    { name: 'Gmail', status: 'Offline', icon: Mail },
  ];

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Messenger Ecosystem</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {channels.map((ch) => (
          <div key={ch.name} className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <div className="flex items-center gap-4 mb-4">
              <ch.icon className="text-blue-500" />
              <h3 className="text-lg font-bold">{ch.name}</h3>
            </div>
            <div className="flex items-center justify-between">
              <span className={`text-sm ${ch.status === 'Connected' ? 'text-green-500' : 'text-slate-500'}`}>{ch.status}</span>
              <button className="text-xs border border-slate-600 px-2 py-1 rounded hover:bg-slate-700 transition-colors">Manage</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
