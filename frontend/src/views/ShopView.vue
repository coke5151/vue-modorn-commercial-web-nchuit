<template>
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-3xl font-bold text-gray-800">Shop</h1>

        <!-- 🔍 搜尋框 -->
        <input v-model="searchQuery" type="text" placeholder="Search for products..."
            class="w-full p-2 mt-4 border border-gray-300 rounded-lg" />

        <!-- 🔖 篩選選單 -->
        <div class="flex space-x-4 mt-4">
            <select v-model="selectedCategory" class="p-2 border rounded-lg">
                <option value="">All Categories</option>
                <option v-for="category in categories" :key="category" :value="category">
                    {{ category }}
                </option>
            </select>

            <select v-model="selectedPriceRange" class="p-2 border rounded-lg">
                <option value="">All Prices</option>
                <option value="0-100">$0 - $100</option>
                <option value="100-500">$100 - $500</option>
                <option value="500-1000">$500 - $1000</option>
                <option value="1000-1500">$1000 - $1500</option>
                <option value="1500-2000">$1500 - $2000</option>
                <option value="2000-99999999">$2000+</option>
            </select>
        </div>

        <!-- 🛒 商品列表 -->
        <div class="mt-6 grid grid-cols-2 md:grid-cols-4 gap-6">
            <div v-for="product in filteredProducts" :key="product.id" class="bg-white shadow-md rounded-lg p-4">
                <img :src="url + product.image_url" alt="product" class="w-full h-40 object-cover rounded">
                <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
                <p class="text-gray-500">${{ product.price }}</p>
                <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View
                    Details</router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useProductStore } from "@/stores/productStore";
import { storeToRefs } from "pinia";
import { ref, computed } from "vue";

const ProcductStore = useProductStore();
const { products } = storeToRefs(ProcductStore);
const url = new URL("@/", import.meta.url).href;

const searchQuery = ref("");
const selectedCategory = ref("");
const selectedPriceRange = ref("");

// 定義可選的商品類別
const categories = computed(() => {
    return [...new Set(products.value.map((p) => p.category))];
});

// **篩選商品的 computed 計算屬性**
const filteredProducts = computed(() => {
    return products.value.filter((product) => {
        // 🔍 根據搜尋關鍵字篩選
        const matchesSearch = product.name.toLowerCase().includes(searchQuery.value.toLowerCase());

        // 🔖 根據類別篩選
        const matchesCategory = selectedCategory.value ? product.category === selectedCategory.value : true;

        // 💰 根據價格範圍篩選
        let matchesPrice = true;
        if (selectedPriceRange.value) {
            const [min, max] = selectedPriceRange.value.split("-").map(Number);
            matchesPrice = product.price >= min && product.price <= max;
        }

        return matchesSearch && matchesCategory && matchesPrice;
    });
});
</script>