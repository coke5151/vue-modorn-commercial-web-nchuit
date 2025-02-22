<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="bg-white p-8 shadow-lg rounded-lg w-96">
            <h2 class="text-2xl font-bold text-center mb-6">Login</h2>
            <form @submit.prevent="handleLogin">
                <div class="mb-4">
                    <label for="email" class="block text-gray-700">Email</label>
                    <input v-model="email" type="email" id="email" required
                        class="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500" />
                </div>

                <div class="mb-4">
                    <label for="password" class="block text-gray-700">Password</label>
                    <input v-model="password" type="password" id="password" required
                        class="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500" />
                </div>

                <button type="submit"
                    class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition">
                    Login
                </button>
            </form>

            <p class="mt-4 text-center">
                Don't have an account? 
                <router-link to="/register" class="text-blue-500 hover:underline">Sign up</router-link>
            </p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watchEffect } from "vue";
import { useAuthStore } from "@/stores/authStore";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const authStore = useAuthStore();
const router = useRouter();

// 如果已登入，則自動跳轉到首頁
watchEffect(() => {
    if (authStore.isAuthenticated) {
        router.push("/");
    }
});

const handleLogin = async () => {
    const success = await authStore.login({ email: email.value, password: password.value });
    if (success) {
        router.push("/"); // 登入成功後跳轉到首頁
    } else {
        alert("Login failed, please check your credentials.");
    }
};
</script>
