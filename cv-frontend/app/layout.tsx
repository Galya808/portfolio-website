import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://galymzhan.xyz"),
  title: "Galymzhan Ayapbergen | Backend-Focused Software Engineer",
  description:
    "Portfolio of Galymzhan Ayapbergen, a backend-focused software engineer building production-oriented applications with FastAPI, PostgreSQL, and Next.js.",
  authors: [{ name: "Galymzhan Ayapbergen" }],
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    url: "/",
    siteName: "Galymzhan Ayapbergen",
    title: "Galymzhan Ayapbergen | Software Engineer",
    description:
      "Backend-focused software engineer building reliable full-stack applications.",
    images: [{ url: "/projects/portfolio-home.png", width: 1280, height: 720 }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Galymzhan Ayapbergen | Software Engineer",
    description:
      "Backend-focused software engineer building reliable full-stack applications.",
    images: ["/projects/portfolio-home.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
