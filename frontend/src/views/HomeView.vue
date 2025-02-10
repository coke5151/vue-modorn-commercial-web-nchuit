<template>
  <div class="container mx-auto px-6 py-10">
    <h1 class="text-3xl font-bold text-gray-800">Welcome to AI-Commerce</h1>
    <p class="mt-2 text-gray-600">Discover AI-powered product recommendations</p>

    <div class="mt-6 grid grid-cols-2 md:grid-cols-4 gap-6">
      <div v-for="product in products" :key="product.id" class="bg-white shadow-md rounded-lg p-4">
        <img :src="product.image" alt="product" class="w-full h-40 object-cover rounded">
        <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
        <p class="text-gray-500">{{ product.price }} USD</p>
        <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const products = ref([
    { id: 1, name: "Gaming Mouse 1", price: 999, stock: 188, brand: "Logitech", connectionType: "Wireless", gamingCertified: true, 
      comboSet: false, productType: "Standard", BSMI: "R41126", NCC: "CCAI23LP0120T2", shippingLocation: "Kaohsiung, Taiwan",
      image: new URL('@/assets/00001.jpg', import.meta.url).href },
      
    { id: 2, name: "Gaming Mouse 2", price: 799, stock: 374, brand: "Logitech", connectionType: "Wired", gamingCertified: true, 
      comboSet: false, productType: "Special Edition", BSMI: "R41127", NCC: "CCAI23LP0120T3", shippingLocation: "Taipei, Taiwan",
      image: new URL('@/assets/00002.jpg', import.meta.url).href }
]);

</script>
