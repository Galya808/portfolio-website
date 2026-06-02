"use client"

import { useEffect, useState } from "react"
import { api } from "@/lib/api"
import { motion } from "framer-motion"

type Project = {
  id: number
  title: string
  description: string
  github_url?: string
  live_url?: string
  technologies?: string
  image_url?: string
}

type Skill = {
  id: number
  name: string
  category: string
  proficiency_level: number
}

type Experience = {
  id: number
  company_name: string
  position: string
  description: string
  start_date: string
  end_date: string
  is_current: boolean
}

type Education = {
  id: number
  institution: string
  degree: string
  field_of_study: string
  start_year: string
  end_year: string
}

export default function Home() {
  const [projects, setProjects] = useState<Project[]>([])
  const [skills, setSkills] = useState<Skill[]>([])
  const [experiences, setExperiences] = useState<Experience[]>([])
  const [education, setEducation] = useState<Education[]>([])

  useEffect(() => {
    api.get("/projects/")
      .then(res => setProjects(res.data))
      .catch(err => console.log(err))

    api.get("/skills/")
      .then(res => setSkills(res.data))
      .catch(err => console.log(err))

    api.get("/experience/")
      .then(res => setExperiences(res.data))
      .catch(err => console.log(err))

    api.get("/education/")
      .then(res => setEducation(res.data))
      .catch(err => console.log(err))
  }, [])

  return (
    <main className="bg-black text-white min-h-screen overflow-x-hidden">
      
      {/* NAVBAR */}
      <nav className="fixed top-0 w-full border-b border-zinc-800 bg-black/80 backdrop-blur z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between">
          <h1 className="font-bold text-lg">GA</h1>

          <button className="md:hidden text-sm">
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
      </nav>

      {/* HERO */}
      <section className="min-h-screen flex items-center">
        <div className="absolute top-40 left-1/2 -translate-x-1/2 w-[300px] md:w-[500px] h-[500px] bg-purple-500/20 blur-[120px] rounded-full overflow-hidden"></div>
        <motion.div 
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="max-w-6xl mx-auto px-6"
        >

          <p className="text-zinc-500 mb-4">
            FullStack Developer
          </p>

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

      {/* ABOUT */}
      <section
        id="about"
        className="max-w-6xl mx-auto px-6 py-24 md:py-32"
      >
        <h2 className="text-3xl font-bold mb-8">
          About Me
        </h2>

        <p className="text-zinc-400 max-w-3xl leading-relaxed text-lg">
          Computer Science student interested in backend engineering,
          cloud technologies and modern web development.
          Currently building fullstack applications using FastAPI,
          PostgreSQL, Docker and Next.js.
        </p>
      </section>

      {/* SKILLS */}
      <section 
        id="skills" 
        className="max-w-6xl mx-auto px-6 py-24 md:py-32"
      >
        <h2 className="text-3xl font-bold mb-12">
          Skills
        </h2>

        <div className="flex flex wrap gap-4">
          {skills.map(skill => (
            <div 
              key={skill.id} 
              className="bg-zinc-900 border border-zinc-800 px-5 py-3 rounded-2xl hover:border-zinc-700 transition"
            >
              <p className="font-medium">
                {skill.name}
              </p>

              <p className="text-sm text-zinc-500">
                {skill.category}
              </p>
            </div>
          ))}

          {skills.length === 0 && (
            <p className="text-zinc-500">
              No skills yet
            </p>
          )}
        </div>

      </section>

      {/* EXPERIENCE */}
      <section
        id="experiences"
        className="max-w-6xl mx-auto px-6 py-24 md:py-32"
      >
        <h2 className="text-3xl font-bold mb-12">
          Experience
        </h2>

        <div className="space-y-8">
          {experiences.map(exp => (
            <div 
              key={exp.id}
              className="border-l border-zinc-700 pl-6"
            >
              <div className="flex flex-col md:flex-row md:justify-between md:items-center mb-2">
                <h3 className="text-xl font-semibold"> 
                  {exp.position}
                </h3>
                
                <p className="text-zinc-500 text-sm">
                  {new Date(exp.start_date).getFullYear()} - {
                    exp.is_current
                      ? "Present"
                      : new Date(exp.end_date).getFullYear()
                  }
                </p>
              </div>

              <p className="text-zinc-300 mb-3">
                {exp.company_name}
              </p>

              <p className="text-zinc-400 leading-relaxed">
                {exp.description}
              </p>
            </div>
          ))}

          {experiences.length === 0 && (
            <p className="text-zinc-500">
              No experience yet
            </p>
          )}
        </div>
      </section>

      {/* EDUCATION */}
      <section 
        id="education"
        className="max-w-6xl mx-auto px-6 py-24 md:py-32"
      >
        <h2 className="text-3xl font-bold mb-12">
          Education
        </h2>

        <div className="space-y-8">
          {education.map(edu => (
            <div 
              key={edu.id}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8"
            >
              <div className="flex flex-col md:flex-row md:justify-between md:items-center md-4">

                <h3 className="text-2xl font-semibold">
                  {edu.institution}
                </h3>

                <p className="text-zinc-500">
                  {edu.start_year} - {edu.end_year}
                </p>
              </div>

              <p className="text-zinc-300 mb-2">
                {edu.degree}
              </p>

              <p className="text-zinc-400">
                {edu.field_of_study}
              </p>
            </div>
          ))}

          {education.length === 0 && (
            <p className="text-zinc-500">
              No education data yet
            </p>
          )}
        </div>
      </section>

      {/* PROJECTS */}
      <section
        id="projects"
        className="max-w-6xl mx-auto px-6 py-24 md:py-32 scroll-mt-6"
      >
        <h2 className="text-3xl font-bold mb-12">
          Projects
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">

          {projects.map(project => (
            <motion.div
              initial={{ opacity: 0, y: 30}}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              viewport={{ once: true }}
              key={project.id}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl overflow-hidden hover:border-zinc-700 transition"
            >
              <div className="h-48 bg-zinc-800 flex items-center justify-center text-zinc-500">
                Project Image
              </div>

              <div className="p-8">
                <h3 className="text-2xl font-semibold mb-4">
                  {project.title}
                </h3>

                <p className="text-zinc-400 leading-relaxed mb-6">
                  {project.description}
                </p>

                {project.technologies && (
                  <p className="text-sm text-zinc-500 mb-6">
                    {project.technologies}
                  </p>
                )}

                <div className="flex gap-4">
                  {project.github_url && (
                    <a
                      href={project.github_url}
                      target="_blank"
                      className="bg-white text-black px-4 py-2 rounded-xl text-sm"
                    >
                      Github
                    </a>
                  )}

                  {project.live_url && (
                    <a 
                      href={project.live_url}
                      target="_blank"
                      className="border border-zinc-700 px-4 py-2 rounded-xl text-sm"
                    >
                      Live demo
                    </a>
                  )}
                </div>
              </div>
            </motion.div>
          ))}

          {projects.length === 0 && (
            <p className="text-zinc-500">
              No projects yet.
            </p>
          )}

        </div>
      </section>

      {/* CONTACT */}
      <section
        id="contact"
        className="max-w-6xl mx-auto px-6 py-24 md:py-32"
      >
        <h2 className="text-3xl font-bold mb-8">
          Contact
        </h2>

        <div className="flex flex-col gap-4 text-zinc-400 break-words">
          <p>Email: your@email.com</p>
          <p>GitHub: github.com/yourname</p>
          <p>LinkedIn: linkedin.com/in/yourname</p>
        </div>
      </section>

    </main>
  )
}