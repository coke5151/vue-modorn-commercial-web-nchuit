<template>
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-3xl font-bold mb-6">User Profile</h1>

        <!-- 使用者資訊 -->
        <div class="bg-white shadow-lg rounded-lg p-6 mb-6">
            <h2 class="text-xl font-semibold mb-4">Profile Information</h2>
            <div class="mb-4">
                <label class="block text-gray-700">Name</label>
                <input v-model="user.name" type="text" class="border p-2 w-full rounded-lg" />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700">Email</label>
                <input v-model="user.email" type="email" class="border p-2 w-full rounded-lg bg-gray-200" disabled />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700">Address</label>
                <input v-model="user.address" type="text" class="border p-2 w-full rounded-lg" />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700">Birth Date</label>
                <input v-model="user.birth_date" type="date" class="border p-2 w-full rounded-lg" />
            </div>
            <button @click="saveProfile"
                class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
                Save Changes
            </button>
        </div>

        <!-- 訂單歷史記錄 -->
        <OrderHistory></OrderHistory>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import OrderHistory from "./OrderHistory.vue";

const user = ref({
    name: "",
    email: "",
    address: "",
    birth_date: "",
});

const token = localStorage.getItem("token");  // 取得儲存的 JWT Token

const fetchUserProfile = async () => {
    try {
        const response = await axios.get("/api/profile", {
            headers: { Authorization: `Bearer ${token}` }  // 附加 JWT Token
        });
        user.value = response.data;
    } catch (error) {
        console.error("Failed to fetch user profile:", error);
    }
};

const saveProfile = async () => {
    try {
        await axios.put("/api/profile", user.value, {
            headers: { Authorization: `Bearer ${token}` }
        });
        alert("Profile updated successfully! 🎉");
    } catch (error) {
        console.error("Failed to update profile:", error);
        alert("Update failed! ❌");
    }
};


// 進入頁面時載入資料
onMounted(fetchUserProfile);
</script>
