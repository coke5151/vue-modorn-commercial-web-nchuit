<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-semibold text-center mb-6">Register</h2>
            <form @submit.prevent="handleRegister">
                <div class="mb-4">
                    <label class="block text-gray-700">Name</label>
                    <input v-model="form.name" type="text" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Email</label>
                    <input v-model="form.email" type="email" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Password</label>
                    <input v-model="form.password" type="password" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Address</label>
                    <input v-model="form.address" type="text" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Birth Date</label>
                    <input v-model="form.birth_date" type="date" required class="border p-2 w-full rounded-lg" />
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
    name: "",
    email: "",
    password: "",
    address: "",
    birth_date: "",
});

const handleRegister = async () => {
    try {
        await axios.post("/api/auth/register", form.value);
        alert("Registration successful! ✅");
        router.push("/login");
    } catch (error) {
        console.error(error.response?.data?.error || "Registration failed!");
        alert(error.response?.data?.error || "Registration failed! ❌");
    }
};
</script>
