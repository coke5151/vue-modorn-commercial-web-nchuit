<template>
    <nav class="bg-white shadow-md">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <!-- LOGO -->
            <router-link to="/" class="text-2xl font-extrabold text-gray-800 flex items-center space-x-2">
                <img src="@/assets/logo.svg" alt="Logo" class="h-8 w-auto" />
                <span>AI-Commerce</span>
            </router-link>

            <!-- 🔍 搜尋欄 -->
            <div class="hidden md:flex flex-grow px-6 md:px-12">
                <div class="w-full max-w-2xl flex bg-white border border-gray-300 rounded-md overflow-hidden shadow-sm">
                    <input v-model="searchQuery" type="text" placeholder="Search products..."
                        class="w-full p-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500" />
                    <button @click="search" class="bg-blue-500 text-white px-6 py-3 hover:bg-blue-600 transition">
                        🔍
                    </button>
                </div>
            </div>

            <!-- 📌 導覽連結（桌機版） -->
            <div class="hidden md:flex items-center gap-x-6">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/shop" class="nav-link">Shop</router-link>

                <!-- 🛒 購物車 -->
                <router-link to="/cart" class="relative nav-link flex items-center">
                    🛒 Cart
                    <span v-if="cart.length > 0"
                        class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold px-2 py-0.5 rounded-full">
                        {{ cart.length }}
                    </span>
                </router-link>

                <!-- 👤 用戶操作（登入/登出/個人頁面） -->
                <template v-if="isAuthenticated">
                    <router-link to="/profile" class="nav-link">Profile</router-link>
                    <button @click="logout"
                        class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">
                        Logout
                    </button>
                </template>
                <template v-else>
                    <router-link to="/login"
                        class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
                        Login
                    </router-link>
                    <router-link to="/register"
                        class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">
                        Register
                    </router-link>
                </template>
            </div>

            <!-- 📱 漢堡選單（手機版） -->
            <button @click="toggleMenu" class="md:hidden text-gray-700 focus:outline-none">
                ☰
            </button>
        </div>

        <!-- 🔍 響應式搜尋框（手機版） -->
        <div class="md:hidden px-4 py-2">
            <input v-model="searchQuery" type="text" placeholder="Search..."
                class="w-50 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
            <button @click="search" class="bg-blue-500 rounded-md text-white px-6 py-3 hover:bg-blue-600 transition">
                🔍
            </button>
        </div>

        <!-- 📱 響應式選單 -->
        <div v-if="menuOpen" class="md:hidden bg-white shadow-md py-4 space-y-4">
            <router-link to="/" class="block text-center nav-link">Home</router-link>
            <router-link to="/shop" class="block text-center nav-link">Shop</router-link>
            <router-link to="/cart" class="block text-center nav-link">Cart</router-link>
            <template v-if="isAuthenticated">
                <router-link to="/profile" class="block text-center nav-link">Profile</router-link>
                <button @click="logout" class="block w-full text-center text-red-500 font-medium py-2">Logout</button>
            </template>
            <template v-else>
                <router-link to="/login" class="block text-center bg-blue-500 text-white py-2 rounded-lg mx-6">Login</router-link>
                <router-link to="/register" class="block text-center bg-green-500 text-white py-2 rounded-lg mx-6">Register</router-link>
            </template>
        </div>
    </nav>
</template>

<script setup>
import { ref, computed } from "vue";
import { useCartStore } from "@/stores/cartStore";
import { useRouter } from "vue-router";
import { useProductStore } from "@/stores/productStore";
import { useAuthStore } from "@/stores/authStore"; // 使用 Auth Store 管理登入狀態

const cartStore = useCartStore();
const cart = computed(() => cartStore.cart);

const menuOpen = ref(false);
const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
};

const productStore = useProductStore();
const searchQuery = ref('');
const router = useRouter();
const search = () => {
    if(searchQuery.value.trim() === '') return;
    productStore.searchQuery = searchQuery.value.trim();
    router.push({ path: '/search' });
};

// 認證相關
const authStore = useAuthStore();
const isAuthenticated = computed(() => authStore.isAuthenticated);

const logout = () => {
    authStore.logout();
    router.push("/login");
};
</script>

<style scoped>
@import "tailwindcss";

/* 🖌️ 通用導覽連結樣式 */
.nav-link {
    @apply text-gray-600 font-medium hover:text-blue-500 transition cursor-pointer;
}
</style>
