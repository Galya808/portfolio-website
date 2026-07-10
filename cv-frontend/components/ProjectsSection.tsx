"use client"

import { motion } from "framer-motion"
import type { Project } from "@/types/cv"

type ProjectsSectionProps = {
  projects: Project[]
}

export function ProjectsSection({ projects }: ProjectsSectionProps) {
  return (
    <section id="projects" className="max-w-6xl mx-auto px-6 py-24 md:py-32 scroll-mt-24">
      <h2 className="text-3xl font-bold mb-12">Projects</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {projects.map((project) => (
          <motion.div
            initial={{ opacity: 0, y: 30 }}
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
              <h3 className="text-2xl font-semibold mb-4">{project.title}</h3>

              {project.description && (
                <p className="text-zinc-400 leading-relaxed mb-6">{project.description}</p>
              )}

              {project.technologies && (
                <p className="text-sm text-zinc-500 mb-6">{project.technologies}</p>
              )}

              <div className="flex gap-4">
                {project.github_url && (
                  <a
                    href={project.github_url}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-white text-black px-4 py-2 rounded-xl text-sm"
                  >
                    Github
                  </a>
                )}

                {project.live_url && (
                  <a
                    href={project.live_url}
                    target="_blank"
                    rel="noreferrer"
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
          <p className="text-zinc-500">No projects yet.</p>
        )}
      </div>
    </section>
  )
}
