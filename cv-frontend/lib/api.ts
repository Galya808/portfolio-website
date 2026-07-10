import axios from "axios"

// Здесь только базовая настройка axios, без авторизации и прочего. Все это будет в apiAuth.ts

export const api = axios.create({
    baseURL: "/api"
})