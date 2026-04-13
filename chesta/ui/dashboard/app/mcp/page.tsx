'use client';
import React from 'react';
import { Box, Check } from 'lucide-react';

export default function MCPPage() {
  const servers = [
    { name: 'Filesystem', status: 'Running', type: 'Core' },
    { name: 'Google Search', status: 'Installed', type: 'Custom' },
    { name: 'Blender', status: 'Available', type: 'Marketplace' },
  ];

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">MCP Registry</h1>
      <div className="grid grid-cols-1 gap-4">
        {servers.map((s) => (
          <div key={s.name} className="bg-slate-800 p-4 rounded-xl border border-slate-700 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Box className="text-blue-500" />
              <div>
                <h3 className="font-bold">{s.name}</h3>
                <p className="text-xs text-slate-500">{s.type}</p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-xs text-green-500 flex items-center gap-1"><Check size={12}/> {s.status}</span>
              <button className="bg-slate-700 px-3 py-1 rounded text-xs">Configure</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
