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
                <input v-model="user.email" type="email" class="border p-2 w-full rounded-lg" disabled />
            </div>
            <button @click="saveProfile"
                class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
                Save Changes
            </button>
        </div>

        <!-- 訂單歷史記錄 -->
        <div class="bg-white shadow-lg rounded-lg p-6">
            <h2 class="text-xl font-semibold mb-4">Order History</h2>
            <div v-if="orders.length">
                <div v-for="order in orders" :key="order.id" class="border-b p-4">
                    <p><strong>Order ID:</strong> {{ order.id }}</p>
                    <p><strong>Date:</strong> {{ order.date }}</p>
                    <p><strong>Total:</strong> ${{ order.total }}</p>
                </div>
            </div>
            <p v-else class="text-gray-500">No orders found.</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

// 模擬使用者資料
const user = ref({
    name: "John Doe",
    email: "john.doe@example.com",
});

// 模擬訂單數據
const orders = ref([]);

// 假裝從 API 載入訂單
onMounted(() => {
    orders.value = [
        { id: "12345", date: "2025-02-08", total: 49.99 },
        { id: "67890", date: "2025-02-05", total: 79.99 },
    ];
});

// 模擬儲存用戶資料
const saveProfile = () => {
    alert("Profile updated successfully! 🎉");
};
</script>