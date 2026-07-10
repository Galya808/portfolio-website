"use client"

import { AboutSection } from "@/components/AboutSection"
import { ContactSection } from "@/components/ContactSection"
import { EducationSection } from "@/components/EducationSection"
import { ExperienceSection } from "@/components/ExperienceSection"
import { HeroSection } from "@/components/HeroSection"
import { Navbar } from "@/components/Navbar"
import { ProjectsSection } from "@/components/ProjectsSection"
import { SkillsSection } from "@/components/SkillsSection"
import { useCvData } from "@/hooks/useCvData"

export default function Home() {
  const { projects, skills, experiences, education } = useCvData()

  return (
    <main className="bg-black text-white min-h-screen overflow-x-hidden">
      <Navbar />
      <HeroSection />
      <AboutSection />
      <SkillsSection skills={skills} />
      <ExperienceSection experiences={experiences} />
      <EducationSection education={education} />
      <ProjectsSection projects={projects} />
      <ContactSection />
    </main>
  )
}
