import type { Skill } from "@/types/cv"

type SkillsSectionProps = {
  skills: Skill[]
}

export function SkillsSection({ skills }: SkillsSectionProps) {
  const groupedSkills = skills.reduce<Record<string, Skill[]>>((groups, skill) => {
    const category = skill.category?.trim() || "Other"
    groups[category] = [...(groups[category] || []), skill]
    return groups
  }, {})

  const categoryOrder = [
    "Backend",
    "Frontend",
    "Database",
    "Testing",
    "Security",
    "DevOps",
    "Cloud & Deployment",
    "Observability",
    "Other",
  ]

  const categories = Object.entries(groupedSkills).sort(([left], [right]) => {
    const leftIndex = categoryOrder.indexOf(left)
    const rightIndex = categoryOrder.indexOf(right)
    return (leftIndex === -1 ? categoryOrder.length : leftIndex)
      - (rightIndex === -1 ? categoryOrder.length : rightIndex)
  })

  return (
    <section id="skills" className="max-w-6xl mx-auto px-6 py-24 md:py-32">
      <h2 className="text-3xl font-bold mb-12">Skills</h2>

      <div className="grid gap-8 md:grid-cols-2">
        {categories.map(([category, categorySkills]) => (
          <div key={category} className="rounded-3xl border border-zinc-800 bg-zinc-950 p-6">
            <h3 className="mb-4 text-sm font-semibold uppercase tracking-[0.18em] text-purple-300">
              {category}
            </h3>
            <div className="flex flex-wrap gap-3">
              {categorySkills.map((skill) => (
                <span
                  key={skill.id}
                  className="rounded-xl border border-zinc-800 bg-zinc-900 px-4 py-2 text-sm text-zinc-200"
                >
                  {skill.name}
                </span>
              ))}
            </div>
          </div>
        ))}

        {skills.length === 0 && (
          <p className="text-zinc-500">No skills yet</p>
        )}
      </div>
    </section>
  )
}
