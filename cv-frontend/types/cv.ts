// Здесь определены типы данных, используемые в проекте CV-Frontend.

export type Project = {
  id: number
  title: string
  description: string | null
  github_url?: string | null
  live_url?: string | null
  technologies?: string | null
  image_url?: string | null
}

export type Skill = {
  id: number
  name: string
  category: string | null
  proficiency_level: number | null
}

export type Experience = {
  id: number
  company_name: string | null
  position: string | null
  description: string | null
  start_date: string
  end_date: string | null
  is_current: boolean | null
}

export type Education = {
  id: number
  institution: string
  degree: string | null
  field_of_study: string | null
  start_year: number
  end_year: number | null
}
