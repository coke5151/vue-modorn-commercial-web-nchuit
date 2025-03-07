<!-- SearchResults.vue -->
<template>
    <div class="container mx-auto px-6 py-10 flex">
        <!-- 🏷️ 類別篩選欄 -->
        <aside class="w-1/4 pr-6 border-r">
            <h2 class="text-xl font-bold mb-4">Filter by Category</h2>
            <div v-for="category in uniqueCategories" :key="category" class="mb-2">
                <label class="inline-flex items-center">
                    <input type="checkbox" :value="category" v-model="selectedCategories"
                        class="form-checkbox text-blue-500">
                    <span class="ml-2">{{ category }}</span>
                </label>
            </div>
        </aside>

        <!-- 📄 搜尋結果 -->
        <div class="w-3/4 pl-6">
            <h2 class="text-2xl font-bold mb-4">Search Results of "{{ searchQuery }}"</h2>
            <div v-if="filteredProducts.length">
                <div v-for="product in filteredProducts" :key="product.id"
                    class="border rounded-lg p-4 mb-4 flex items-center">
                    <img :src="product.image_url" alt="product image" class="w-20 h-20 object-cover rounded-lg mr-4" />
                    <div>
                        <h3 class="text-lg font-bold">{{ product.name }}</h3>
                        <p class="text-gray-500">{{ product.brand }}</p>
                        <p class="text-blue-500 font-bold">${{ product.price }}</p>
                        <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">
                            View Details
                        </router-link>
                    </div>
                </div>
            </div>
            <p v-else class="text-gray-500">No products found.</p>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useProductStore } from '@/stores/productStore';
import { storeToRefs } from 'pinia';
const productStore = useProductStore();
const { filteredProducts, uniqueCategories, selectedCategories, searchQuery }= storeToRefs(productStore);
</script>
