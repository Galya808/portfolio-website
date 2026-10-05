"use client"

import { motion } from "framer-motion"
import Image from "next/image"
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
            className={`bg-zinc-900 border border-zinc-800 rounded-3xl overflow-hidden hover:border-purple-500/50 transition ${project.title === "Helpdesk Platform" ? "md:col-span-2" : ""}`}
          >
            <div className={`relative bg-zinc-800 ${project.title === "Helpdesk Platform" ? "h-64 md:h-96" : "h-56"}`}>
              {project.image_url ? (
                <Image
                  src={project.image_url}
                  alt={`${project.title} preview`}
                  fill
                  unoptimized
                  sizes={project.title === "Helpdesk Platform" ? "(min-width: 768px) 1152px, 100vw" : "(min-width: 768px) 576px, 100vw"}
                  className="object-cover object-top"
                />
              ) : (
                <div className="h-full flex items-center justify-center bg-gradient-to-br from-zinc-800 to-purple-950/50 text-zinc-400">
                  {project.title}
                </div>
              )}
            </div>

            <div className="p-8">
              <h3 className="text-2xl font-semibold mb-4">{project.title}</h3>

              {project.description && (
                <p className="text-zinc-400 leading-relaxed mb-6">{project.description}</p>
              )}

              {project.technologies && (
                <div className="flex flex-wrap gap-2 mb-7">
                  {project.technologies.split(",").map((technology) => (
                    <span
                      key={technology.trim()}
                      className="rounded-full border border-zinc-700 px-3 py-1 text-xs text-zinc-300"
                    >
                      {technology.trim()}
                    </span>
                  ))}
                </div>
              )}

              <div className="flex gap-4">
                {project.github_url && (
                  <a
                    href={project.github_url}
                    target="_blank"
                    rel="noreferrer"
                    className="bg-white text-black px-4 py-2 rounded-xl text-sm"
                  >
                    GitHub
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
