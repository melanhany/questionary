import axios from "axios"

export default axios.create({
    baseURL: 'https://api.rawg.io/api',
    params: {
        key: '3da3f6d0d4e64596bc4c3468749c5e30'
    }
})