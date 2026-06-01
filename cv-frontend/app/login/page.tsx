"use client"

import { useState } from "react"
import { api } from "@/lib/api"
import { useRouter } from "next/navigation"

export default function LoginPage() {
    const router = useRouter()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const handleLogin = async() => {
        const params = new URLSearchParams()
        params.append("username", username)
        params.append("password", password)

        const res = await api.post("/auth/login", params)

        localStorage.setItem("token", res.data.access_token)
        router.push("/admin")
    }

    return (
    <main className="min-h-screen flex items-center justify-center bg-black text-white">
      <div className="bg-zinc-900 p-8 rounded-2xl w-80">
        <h1 className="text-xl font-semibold mb-6">Admin Login</h1>

        <input
          placeholder="Username"
          className="w-full mb-3 p-2 bg-zinc-800 rounded"
          onChange={e => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full mb-6 p-2 bg-zinc-800 rounded"
          onChange={e => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-white text-black py-2 rounded"
        >
          Login
        </button>
      </div>
    </main>
  )
}