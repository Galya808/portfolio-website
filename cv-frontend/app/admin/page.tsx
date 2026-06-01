"use client"

import { useEffect, useState } from "react"
import { api } from "@/lib/api"

type Project = {
    id: number
    title: string
    description: string
}

export default function AdminPage() {
    const [projects, setProjects] = useState<Project[]>([])
    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")

    const token = typeof window !== "undefined"
        ? localStorage.getItem("token")
        : null

    const fetchProjects = async () => {
        const res = await api.get("/projects")
        setProjects(res.data)
    }

    useEffect(() => {
        fetchProjects()
    }, [])

    const handleCreate = async () => {
        await api.post(
            "/projects",
            { title, description },
            { headers: { Authorization: `Bearer ${token}` } }
        )

        alert("Project created")
        setTitle("")
        setDescription("")
    }

    const handleDelete = async (id: number) => {
        await api.delete(`/projects/${id}`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        fetchProjects()
    }

    return (
    <main className="min-h-screen bg-black text-white p-10">
      <div className="max-w-3xl mx-auto">

        <h1 className="text-2xl font-bold mb-8">Admin Panel</h1>

        {/* Create */}
        <div className="bg-zinc-900 p-6 rounded-2xl mb-10">
          <h2 className="font-semibold mb-4">Add Project</h2>

          <input
            placeholder="Title"
            className="w-full mb-3 p-2 bg-zinc-800 rounded"
            value={title}
            onChange={e => setTitle(e.target.value)}
          />

          <textarea
            placeholder="Description"
            className="w-full mb-4 p-2 bg-zinc-800 rounded"
            value={description}
            onChange={e => setDescription(e.target.value)}
          />

          <button
            onClick={handleCreate}
            className="bg-white text-black px-4 py-2 rounded"
          >
            Create
          </button>
        </div>

        {/* List */}
        <div className="bg-zinc-900 p-6 rounded-2xl">
          <h2 className="font-semibold mb-4">Your Projects</h2>

          {projects.map(p => (
            <div
              key={p.id}
              className="border border-zinc-800 rounded p-4 mb-3 flex justify-between items-center"
            >
              <div>
                <h3 className="font-semibold">{p.title}</h3>
                <p className="text-sm text-zinc-400">{p.description}</p>
              </div>

              <button
                onClick={() => handleDelete(p.id)}
                className="text-red-400"
              >
                Delete
              </button>
            </div>
          ))}

          {projects.length === 0 && (
            <p className="text-zinc-400">No projects yet</p>
          )}
        </div>

      </div>
    </main>
  )
}