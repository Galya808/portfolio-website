"use client"

import { motion } from "framer-motion"

export function HeroSection() {
  return (
    <section className="min-h-screen flex items-center">
      <div className="absolute top-40 left-1/2 -translate-x-1/2 w-[300px] md:w-[500px] h-[500px] bg-purple-500/20 blur-[120px] rounded-full overflow-hidden pointer-events-none" />

      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="max-w-6xl mx-auto px-6"
      >
        <p className="text-zinc-500 mb-4">FullStack Developer</p>

        <h1 className="text-4xl sm:text-5xl md:text-7xl font-bold leading-tight mb-6">
          Galymzhan <br /> Ayapbergen
        </h1>

        <p className="text-zinc-400 max-w-xl text-base md:text-lg leading-relaxed mb-8">
          Building fullstack applications with FastAPI, PostgreSQL,
          Next.js and Docker.
        </p>

        <a
          href="#projects"
          className="bg-white text-black px-6 py-3 rounded-xl font-medium hover:scale-105 transition duration-300"
        >
          View Projects
        </a>
      </motion.div>
    </section>
  )
}
