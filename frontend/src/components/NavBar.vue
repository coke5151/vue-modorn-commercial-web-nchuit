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
                    <input type="text" placeholder="Search products..."
                        class="w-full p-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500" />
                    <button class="bg-blue-500 text-white px-6 py-3 hover:bg-blue-600 transition">
                        🔍
                    </button>
                </div>
            </div>


            <!-- 📌 導覽連結（桌機版） -->
            <div class="hidden md:flex items-center gap-x-10">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/shop" class="nav-link">Shop</router-link>

                <!-- 🛒 購物車 -->
                <!-- 🛒 購物車 -->
                <router-link to="/cart" class="relative nav-link flex items-center">
                    🛒 Cart
                    <span v-if="cart.length > 0"
                        class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold px-2 py-0.5 rounded-full">
                        {{ cart.length }}
                    </span>
                </router-link>

                
                <!-- 👤 個人頁面 -->
                <router-link to="/profile" class="nav-link">Profile</router-link>
            </div>

            <!-- 📱 漢堡選單（手機版） -->
            <button @click="toggleMenu" class="md:hidden text-gray-700 focus:outline-none">
                ☰
            </button>
        </div>

        <!-- 🔍 響應式搜尋框（手機版） -->
        <div class="md:hidden px-4 py-2">
            <input type="text" placeholder="Search..."
                class="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>

        <!-- 📱 響應式選單 -->
        <div v-if="menuOpen" class="md:hidden bg-white shadow-md py-4 space-y-4">
            <router-link to="/" class="block text-center nav-link">Home</router-link>
            <router-link to="/shop" class="block text-center nav-link">Shop</router-link>
            <router-link to="/cart" class="block text-center nav-link">Cart</router-link>
            <router-link to="/profile" class="block text-center nav-link">Profile</router-link>
        </div>
    </nav>
</template>

<script setup>
import { ref, computed } from "vue";
import { useCartStore } from "@/stores/cartStore";

const cartStore = useCartStore();
const cart = computed(() => cartStore.cart);
const totalPrice = computed(() => cartStore.totalPrice);

// 📱 漢堡選單開關
const menuOpen = ref(false);
const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
};
</script>

<style scoped>
@import "tailwindcss";

/* 🖌️ 通用導覽連結樣式 */
.nav-link {
    @apply text-gray-600 font-medium hover:text-blue-500 transition cursor-pointer;
}

</style>