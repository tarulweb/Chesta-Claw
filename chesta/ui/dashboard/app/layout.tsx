import React from 'react';
import {
  LayoutDashboard,
  Users,
  Zap,
  Cpu,
  Settings,
  Terminal as TerminalIcon,
  Puzzle,
  MessageSquare,
  GitBranch
} from 'lucide-react';
import Link from 'next/link';
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const menuItems = [
    { icon: LayoutDashboard, label: 'Dashboard', href: '/' },
    { icon: Users, label: 'Agents', href: '/agents' },
    { icon: Zap, label: 'Skills', href: '/skills' },
    { icon: GitBranch, label: 'Workflows', href: '/workflows' },
    { icon: Cpu, label: 'Models', href: '/models' },
    { icon: Puzzle, label: 'MCP', href: '/mcp' },
    { icon: MessageSquare, label: 'Integrations', href: '/integrations' },
    { icon: TerminalIcon, label: 'Terminal', href: '/terminal' },
    { icon: Settings, label: 'Settings', href: '/settings' },
  ];

  return (
    <html lang="en">
      <body className="bg-slate-900 text-white min-h-screen flex">
        <aside className="w-64 border-r border-slate-800 p-4 flex flex-col gap-4">
          <div className="text-2xl font-bold text-blue-500 mb-8 px-4">CHESTA CLAW</div>
          <nav className="flex-1">
            <ul className="space-y-2">
              {menuItems.map((item) => (
                <li key={item.label}>
                  <Link href={item.href} className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-slate-800 transition-colors">
                    <item.icon size={20} />
                    <span>{item.label}</span>
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
        </aside>
        <main className="flex-1 p-8 overflow-auto">
          {children}
        </main>
      </body>
    </html>
  );
}
