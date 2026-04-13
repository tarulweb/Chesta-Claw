'use client';
import React from 'react';
import { GitBranch, Play, History } from 'lucide-react';

export default function WorkflowsPage() {
  const workflows = [
    { name: 'App Generator', status: 'Draft', steps: 5 },
    { name: 'Research Pipeline', status: 'Active', steps: 3 },
  ];

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Workflow Builder</h1>
        <button className="bg-blue-600 px-4 py-2 rounded-lg text-sm flex items-center gap-2">
          <GitBranch size={18}/> New Workflow
        </button>
      </div>
      <div className="grid grid-cols-1 gap-4">
        {workflows.map(w => (
          <div key={w.name} className="bg-slate-800 p-6 rounded-xl border border-slate-700 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="bg-purple-500/10 p-3 rounded-lg text-purple-500">
                <GitBranch size={24} />
              </div>
              <div>
                <h3 className="text-lg font-bold">{w.name}</h3>
                <p className="text-sm text-slate-500">{w.steps} steps configured</p>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <span className="text-xs bg-slate-700 px-2 py-1 rounded text-slate-400">{w.status}</span>
              <button className="p-2 hover:bg-slate-700 rounded transition-colors text-green-500"><Play size={20}/></button>
              <button className="p-2 hover:bg-slate-700 rounded transition-colors text-slate-400"><History size={20}/></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
