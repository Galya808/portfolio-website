// здесь можно добавить любые функции, которые будут использоваться для работы с API, 
// например, функции для получения данных о проектах, навыках, опыте и образовании.

import { api } from "./api"
import type { Education, Experience, Project, Skill } from "@/types/cv"

export function getProjects() {
  return api.get<Project[]>("/projects/")
}

export function getSkills() {
  return api.get<Skill[]>("/skills/")
}

export function getExperience() {
  return api.get<Experience[]>("/experience/")
}

export function getEducation() {
  return api.get<Education[]>("/education/")
}
