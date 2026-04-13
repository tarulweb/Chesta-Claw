'use client';

import React from 'react';
import { Zap, Download, Plus } from 'lucide-react';

const prebuiltSkills = [
  { name: 'Full-Stack Gen', category: 'Dev', description: 'Generate Next.js + FastAPI apps.' },
  { name: 'Web Research', category: 'Research', description: 'Deep multi-source search.' },
  { name: 'Doc Gen', category: 'Productivity', description: 'PDF/Word templates.' },
  { name: 'Terminal', category: 'System', description: 'Sandboxed shell access.' },
];

export default function SkillsPage() {
  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Skills Marketplace</h1>
        <button className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg flex items-center gap-2 transition-colors">
          <Plus size={18} />
          <span>Create Custom Skill</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {prebuiltSkills.map((skill) => (
          <div key={skill.name} className="bg-slate-800 p-6 rounded-xl border border-slate-700 hover:border-blue-500/50 transition-colors group">
            <div className="flex items-start justify-between mb-4">
              <div className="bg-blue-500/10 p-3 rounded-lg text-blue-500">
                <Zap size={24} />
              </div>
              <span className="text-xs font-mono text-slate-500 uppercase tracking-wider">{skill.category}</span>
            </div>
            <h3 className="text-xl font-bold mb-2">{skill.name}</h3>
            <p className="text-slate-400 text-sm mb-6">{skill.description}</p>
            <button className="w-full bg-slate-700 hover:bg-slate-600 py-2 rounded-lg flex items-center justify-center gap-2 transition-colors">
              <Download size={16} />
              <span>Install Skill</span>
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
