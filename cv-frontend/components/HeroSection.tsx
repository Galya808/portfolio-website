"use client"

import { motion } from "framer-motion"

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center overflow-hidden">
      <div className="absolute top-40 left-1/2 -translate-x-1/2 w-[300px] md:w-[500px] h-[500px] bg-purple-500/20 blur-[120px] rounded-full overflow-hidden pointer-events-none" />

      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="max-w-6xl mx-auto px-6"
      >
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-purple-300 mb-5">
          Backend-focused software engineer
        </p>

        <h1 className="text-4xl sm:text-5xl md:text-7xl font-bold leading-tight mb-6">
          Galymzhan <br /> Ayapbergen
        </h1>

        <p className="text-zinc-400 max-w-xl text-base md:text-lg leading-relaxed mb-8">
          Building reliable full-stack applications with FastAPI,
          PostgreSQL, and Next.js.
        </p>

        <div className="flex flex-wrap gap-3">
          <a
            href="#projects"
            className="bg-white text-black px-6 py-3 rounded-xl font-medium hover:scale-105 transition duration-300"
          >
            View projects
          </a>
          <a
            href="/Galymzhan_Ayapbergen_CV_2026.pdf"
            download
            className="border border-zinc-700 px-6 py-3 rounded-xl font-medium hover:border-zinc-500 hover:bg-zinc-900 transition"
          >
            Download résumé
          </a>
          <a
            href="https://github.com/Galya808"
            target="_blank"
            rel="noreferrer"
            className="border border-zinc-700 px-6 py-3 rounded-xl font-medium hover:border-zinc-500 hover:bg-zinc-900 transition"
          >
            GitHub
          </a>
        </div>
      </motion.div>
    </section>
  )
}
