export function ContactSection() {
  return (
    <section id="contact" className="max-w-6xl mx-auto px-6 py-24 md:py-32">
      <h2 className="text-3xl font-bold mb-8">Contact</h2>

      <p className="max-w-2xl text-lg leading-relaxed text-zinc-400 mb-8">
        I am open to backend and full-stack internship opportunities. If you
        would like to discuss a role or a project, feel free to get in touch.
      </p>

      <div className="flex flex-wrap gap-3">
        <a className="rounded-xl bg-white px-5 py-3 font-medium text-black" href="mailto:gaayapbergen@gmail.com">
          Email me
        </a>
        <a className="rounded-xl border border-zinc-700 px-5 py-3 hover:border-zinc-500" href="https://github.com/Galya808" target="_blank" rel="noreferrer">
          GitHub
        </a>
        <a className="rounded-xl border border-zinc-700 px-5 py-3 hover:border-zinc-500" href="/Galymzhan_Ayapbergen_CV_2026.pdf" download>
          Résumé
        </a>
      </div>
    </section>
  )
}
