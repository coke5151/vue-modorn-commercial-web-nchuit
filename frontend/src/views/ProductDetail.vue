<template>
    <div class="container mx-auto px-6 py-10">
        <div v-if="product" class="flex flex-col md:flex-row gap-6">
            <!-- 商品圖片 -->
            <img :src="product.image_url" alt="product image" class="w-full md:w-1/3 object-cover rounded-lg" />

            <!-- 商品資訊 -->
            <div class="flex-1">
                <!-- Breadcrumb 導覽 -->
                <nav class="text-sm text-gray-500 mb-4">
                    <router-link to="/" class="hover:text-blue-500">Shopee</router-link>
                    <span class="mx-2">›</span>
                    <router-link to="/electronics" class="hover:text-blue-500">Electronics & Laptops</router-link>
                    <span class="mx-2">›</span>
                    <router-link to="/keyboards-mice" class="hover:text-blue-500">Keyboards & Mice</router-link>
                    <span class="mx-2">›</span>
                    <span class="text-gray-700 font-semibold">{{ product.name }}</span>
                </nav>

                <!-- 商品標題與價格 -->
                <h1 class="text-3xl font-bold">{{ product.name }}</h1>
                <p class="text-gray-500 text-lg mt-2">${{ product.discounted_price != 0 ? product.discounted_price : product.price }} NT</p>

                <!-- 商品規格 -->
                <div class="mt-6 border-t pt-4">
                    <h3 class="text-lg font-semibold">Product Specifications</h3>
                    <ul class="text-gray-600 mt-2 space-y-2">
                        <li><strong>Limited Offer Stock:</strong> {{ product.stock }}</li>
                        <li><strong>Brand:</strong> {{ product.brand }}</li>
                        <li><strong>Connection Type:</strong> {{ product.connectionType }}</li>
                        <li><strong>Gaming Certified:</strong> {{ product.gamingCertified ? 'Yes' : 'No' }}</li>
                        <li><strong>Combo Set:</strong> {{ product.comboSet ? 'Yes' : 'No' }}</li>
                        <li><strong>Product Type:</strong> {{ product.productType }}</li>
                        <li><strong>BSMI Certification:</strong> {{ product.BSMI }}</li>
                        <li><strong>NCC Certification:</strong> {{ product.NCC }}</li>
                        <li><strong>Shipping From:</strong> {{ product.shippingLocation }}</li>
                    </ul>
                </div>

                <!-- 數量選擇 & 加入購物車按鈕 -->
                <div class="mt-6 flex items-center">
                    <label class="block mr-3 font-semibold">Quantity:</label>
                    <input type="number" v-model="quantity" min="1" class="border p-2 w-20 rounded-lg" />

                    <button @click="addToCart"
                        class="bg-blue-500 text-white px-4 py-2 rounded-lg ml-4 hover:bg-blue-600 transition">
                        🛒 Add to Cart
                    </button>
                </div>
            </div>
        </div>
        <p v-else class="text-center text-gray-500">Loading product...</p>
    </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRoute } from "vue-router";
import { useCartStore } from "@/stores/cartStore";
import { useProductStore } from "@/stores/productStore";
import { storeToRefs } from "pinia";

const route = useRoute();
const cartStore = useCartStore();

const ProductStore = useProductStore()
const { loading,products } = storeToRefs(ProductStore)

const quantity = ref(1);
const product = computed(() => products.value.find((p) => p.id == route.params.id));

// 🔹 加入購物車
const addToCart = () => {
    if (product.value) {
        cartStore.addToCart({ ...product.value, quantity: quantity.value });
        alert("Added to cart!");
    }
};
</script>
