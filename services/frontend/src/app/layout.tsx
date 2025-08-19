import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'CLOAK IAM',
  description: 'Enterprise Continuous Least-Privilege IAM Platform',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}