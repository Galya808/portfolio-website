import type { Experience } from "@/types/cv"

type ExperienceSectionProps = {
  experiences: Experience[]
}

function getExperienceEndYear(experience: Experience) {
  if (experience.is_current) {
    return "Present"
  }

  if (!experience.end_date) {
    return ""
  }

  return new Date(experience.end_date).getFullYear()
}

export function ExperienceSection({ experiences }: ExperienceSectionProps) {
  return (
    <section id="experiences" className="max-w-6xl mx-auto px-6 py-24 md:py-32">
      <h2 className="text-3xl font-bold mb-12">Experience</h2>

      <div className="space-y-8">
        {experiences.map((experience) => (
          <div key={experience.id} className="border-l border-zinc-700 pl-6">
            <div className="flex flex-col md:flex-row md:justify-between md:items-center mb-2">
              {experience.position && (
                <h3 className="text-xl font-semibold">{experience.position}</h3>
              )}

              <p className="text-zinc-500 text-sm">
                {new Date(experience.start_date).getFullYear()} - {getExperienceEndYear(experience)}
              </p>
            </div>

            {experience.company_name && (
              <p className="text-zinc-300 mb-3">{experience.company_name}</p>
            )}

            {experience.description && (
              <p className="text-zinc-400 leading-relaxed">{experience.description}</p>
            )}
          </div>
        ))}

        {experiences.length === 0 && (
          <p className="text-zinc-500">No experience yet</p>
        )}
      </div>
    </section>
  )
}
