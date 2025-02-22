<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-semibold text-center mb-6">Register</h2>
            <form @submit.prevent="handleRegister">
                <div class="mb-4">
                    <label class="block text-gray-700">Email</label>
                    <input type="email" v-model="form.email" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Password</label>
                    <input type="password" v-model="form.password" required class="border p-2 w-full rounded-lg" />
                </div>
                <button type="submit" class="w-full bg-green-500 text-white py-2 rounded-lg hover:bg-green-600 transition mt-4">
                    Register
                </button>
                <p class="text-center text-gray-600 mt-4">
                    Already have an account?
                    <router-link to="/login" class="text-blue-500">Login</router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const form = ref({
    email: "",
    password: "",
});

const handleRegister = async () => {
    try {
        const response = await axios.post("/api/auth/register", form.value);
        alert("Registration successful!");
        router.push("/login");
    } catch (error) {
        console.error(error);
        alert("Registration failed! ❌");
    }
};
</script>
