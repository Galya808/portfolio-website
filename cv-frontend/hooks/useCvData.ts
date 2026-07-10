// этот файл отвечает за получение данных с бэкенда и 
// их хранение в состоянии, чтобы потом передавать их в компоненты

"use client"

import { useEffect, useState } from "react"
import { getEducation, getExperience, getProjects, getSkills } from "@/lib/cvApi"
import type { Education, Experience, Project, Skill } from "@/types/cv"

export function useCvData() {
  const [projects, setProjects] = useState<Project[]>([])
  const [skills, setSkills] = useState<Skill[]>([])
  const [experiences, setExperiences] = useState<Experience[]>([])
  const [education, setEducation] = useState<Education[]>([])

  useEffect(() => {
    getProjects()
      .then((res) => setProjects(res.data))
      .catch((err) => console.log(err))

    getSkills()
      .then((res) => setSkills(res.data))
      .catch((err) => console.log(err))

    getExperience()
      .then((res) => setExperiences(res.data))
      .catch((err) => console.log(err))

    getEducation()
      .then((res) => setEducation(res.data))
      .catch((err) => console.log(err))
  }, [])

  return {
    projects,
    skills,
    experiences,
    education,
  }
}
