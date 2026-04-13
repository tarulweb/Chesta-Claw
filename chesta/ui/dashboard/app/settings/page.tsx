'use client';
import React from 'react';
import { Shield, Key, Trash2 } from 'lucide-react';

export default function SettingsPage() {
  return (
    <div className="space-y-8 max-w-2xl">
      <h1 className="text-3xl font-bold">System Settings</h1>
      <section className="space-y-4">
        <h2 className="text-xl font-bold flex items-center gap-2"><Shield size={20} className="text-blue-500"/> Security</h2>
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
          <div className="flex justify-between items-center">
            <div>
              <p className="font-bold">Dangerous Command Whitelist</p>
              <p className="text-sm text-slate-400">Require approval for system-level commands.</p>
            </div>
            <button className="bg-blue-600 px-4 py-2 rounded-lg text-sm">Configure</button>
          </div>
        </div>
      </section>
      <section className="space-y-4">
        <h2 className="text-xl font-bold flex items-center gap-2"><Key size={20} className="text-blue-500"/> API Credentials</h2>
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
           <p className="text-sm text-slate-400 mb-4">Keys are encrypted with your OS keychain.</p>
           <button className="border border-slate-700 px-4 py-2 rounded-lg text-sm w-full">Manage Keys</button>
        </div>
      </section>
      <section className="pt-8 border-t border-slate-800">
        <button className="text-red-500 flex items-center gap-2 hover:bg-red-500/10 px-4 py-2 rounded-lg transition-colors">
          <Trash2 size={20}/>
          <span>Purge All System Data</span>
        </button>
      </section>
    </div>
  );
}
