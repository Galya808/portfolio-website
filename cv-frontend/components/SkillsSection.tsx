import type { Skill } from "@/types/cv"

type SkillsSectionProps = {
  skills: Skill[]
}

export function SkillsSection({ skills }: SkillsSectionProps) {
  return (
    <section id="skills" className="max-w-6xl mx-auto px-6 py-24 md:py-32">
      <h2 className="text-3xl font-bold mb-12">Skills</h2>

      <div className="flex flex-wrap gap-4">
        {skills.map((skill) => (
          <div
            key={skill.id}
            className="bg-zinc-900 border border-zinc-800 px-5 py-3 rounded-2xl hover:border-zinc-700 transition"
          >
            <p className="font-medium">{skill.name}</p>

            {skill.category && (
              <p className="text-sm text-zinc-500">{skill.category}</p>
            )}
          </div>
        ))}

        {skills.length === 0 && (
          <p className="text-zinc-500">No skills yet</p>
        )}
      </div>
    </section>
  )
}
