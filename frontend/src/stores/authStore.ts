// 📂 src/stores/authStore.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";
import axios from "axios";

// 登入回應類型
interface LoginResponse {
    access_token: string;
    user_id: string;
}

export const useAuthStore = defineStore("auth", () => {
    const token = ref<string | null>(localStorage.getItem("token"));
    const user = ref<string | null>(null);
    
    // 是否已登入
    const isAuthenticated = computed(() => !!token.value);

    // 設定 Token & 使用者資訊
    const setAuth = (authData: LoginResponse) => {

        token.value = authData.access_token;
        user.value = authData.user_id;
        localStorage.setItem("token", authData.access_token);
    };

    // 登入
    const login = async (credentials: { email: string; password: string }) => {
        try {
            const response = await axios.post<LoginResponse>("/api/auth/login", credentials);
            console.log("登入成功:", response.data);
            setAuth(response.data);
            return true;
        } catch (error: any) {
            console.error("登入失敗:", error.response?.data || error.message);
            return false;
        }
    };

    // 註冊
    const register = async (userData: { username: string; email: string; password: string }) => {
        try {
            await axios.post("/api/auth/register", userData);
            return true;
        } catch (error: any) {
            console.error("註冊失敗:", error.response?.data || error.message);
            return false;
        }
    };

    // 登出
    const logout = () => {
        token.value = null;
        user.value = null;
        localStorage.removeItem("token");
    };

    return { token, user, isAuthenticated, login, register, logout };
});
