"use client"

import { useState } from "react"

export function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <nav className="fixed top-0 w-full border-b border-zinc-800 bg-black/80 backdrop-blur z-50">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between">
        <h1 className="font-bold text-lg">GA</h1>

        <button
          className="md:hidden text-sm"
          onClick={() => setMenuOpen((isOpen) => !isOpen)}
        >
          Menu
        </button>

        <div className="hidden md:flex gap-6 text-sm text-zinc-400">
          <a href="#about" className="hover:text-white transition">About</a>
          <a href="#skills" className="hover:text-white transition">Skills</a>
          <a href="#experiences" className="hover:text-white transition">Experiences</a>
          <a href="#education" className="hover:text-white transition">Education</a>
          <a href="#projects" className="hover:text-white transition">Projects</a>
          <a href="#contact" className="hover:text-white transition">Contact</a>
        </div>
      </div>

      {menuOpen && (
        <div className="md:hidden flex flex-col px-6 pb-4 gap-4 text-zinc-400 bg-black">
          <a href="#skills">Skills</a>
          <a href="#education">Education</a>
          <a href="#projects">Projects</a>
          <a href="#contact">Contact</a>
        </div>
      )}
    </nav>
  )
}
