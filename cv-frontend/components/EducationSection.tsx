import type { Education } from "@/types/cv"

type EducationSectionProps = {
  education: Education[]
}

export function EducationSection({ education }: EducationSectionProps) {
  return (
    <section id="education" className="max-w-6xl mx-auto px-6 py-24 md:py-32">
      <h2 className="text-3xl font-bold mb-12">Education</h2>

      <div className="space-y-8">
        {education.map((item) => (
          <div key={item.id} className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="flex flex-col md:flex-row md:justify-between md:items-center mb-4">
              <h3 className="text-2xl font-semibold">{item.institution}</h3>

              <p className="text-zinc-500">
                {item.start_year} - {item.end_year ?? "Present"}
              </p>
            </div>

            {item.degree && <p className="text-zinc-300 mb-2">{item.degree}</p>}

            {item.field_of_study && (
              <p className="text-zinc-400">{item.field_of_study}</p>
            )}
          </div>
        ))}

        {education.length === 0 && (
          <p className="text-zinc-500">No education data yet</p>
        )}
      </div>
    </section>
  )
}
