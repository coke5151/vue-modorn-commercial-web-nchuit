<template>
  <div class="container mx-auto px-6 py-10">
    <!-- 🎉 橫幅廣告 -->
    <div class="relative w-full h-64 mb-8">
      <img :src="bannerImage" alt="banner" class="w-full h-full object-cover rounded-lg shadow-md">
    </div>

    <!-- 📰 最新消息 -->
    <section class="mb-10">
      <h2 class="text-2xl font-bold text-gray-800">📰 最新消息</h2>
      <ul class="mt-4 space-y-2">
        <li v-for="news in latestNews" :key="news.id" class="border-b pb-2 text-gray-700">
          <router-link :to="news.link" class="text-blue-500 hover:underline">
            {{ news.title }}
          </router-link>
        </li>
      </ul>
    </section>

    <!-- 🔥 熱門產品 -->
    <section class="mb-10">
      <h2 class="text-2xl font-bold text-gray-800">🔥 熱門產品</h2>
      <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="product in popularProducts" :key="product.id" class="bg-white shadow-md rounded-lg p-4">
          <img :src="product.image" alt="product" class="w-full h-40 object-cover rounded">
          <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
          <p class="text-gray-500">{{ product.price }} USD</p>
          <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View Details</router-link>
        </div>
      </div>
    </section>

    <!-- 🎯 今日特惠 -->
    <section>
      <h2 class="text-2xl font-bold text-gray-800">🎯 今日特惠</h2>
      <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="product in todayDeals" :key="product.id" class="bg-yellow-100 shadow-md rounded-lg p-4">
          <img :src="product.image" alt="product" class="w-full h-40 object-cover rounded">
          <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
          <p class="text-gray-500 line-through">{{ product.originalPrice }} USD</p>
          <p class="text-red-500 font-bold">{{ product.discountPrice }} USD</p>
          <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View Details</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";

// 🖼️ 橫幅圖片
const bannerImage = ref(new URL('@/assets/banner.jpg', import.meta.url).href);

// 📰 最新消息
const latestNews = ref([
  { id: 1, title: "⚡ 新品上市！AI 智慧滑鼠震撼登場！", link: "/news/1" },
  { id: 2, title: "🎉 限時折扣：指定商品 85 折！", link: "/news/2" },
  { id: 3, title: "🚀 AI 商城全面升級，體驗新 UI！", link: "/news/3" }
]);

// 🔥 熱門產品
const popularProducts = ref([
{ id: 1, name: "Gaming Mouse 1", price: 999, stock: 188, brand: "Logitech", connectionType: "Wireless", gamingCertified: true, 
      comboSet: false, productType: "Standard", BSMI: "R41126", NCC: "CCAI23LP0120T2", shippingLocation: "Kaohsiung, Taiwan",
      image: new URL('@/assets/00001.jpg', import.meta.url).href },
      
    { id: 2, name: "Gaming Mouse 2", price: 799, stock: 374, brand: "Logitech", connectionType: "Wired", gamingCertified: true, 
      comboSet: false, productType: "Special Edition", BSMI: "R41127", NCC: "CCAI23LP0120T3", shippingLocation: "Taipei, Taiwan",
      image: new URL('@/assets/00002.jpg', import.meta.url).href }
]);

// 🎯 今日特惠
const todayDeals = ref([
{ id: 1, name: "Gaming Mouse 1", originalPrice: 999, discountPrice: 799, stock: 188, brand: "Logitech", connectionType: "Wireless", gamingCertified: true, 
      comboSet: false, productType: "Standard", BSMI: "R41126", NCC: "CCAI23LP0120T2", shippingLocation: "Kaohsiung, Taiwan",
      image: new URL('@/assets/00001.jpg', import.meta.url).href },
      
    { id: 2, name: "Gaming Mouse 2", originalPrice: 799, discountPrice: 599, stock: 374, brand: "Logitech", connectionType: "Wired", gamingCertified: true, 
      comboSet: false, productType: "Special Edition", BSMI: "R41127", NCC: "CCAI23LP0120T3", shippingLocation: "Taipei, Taiwan",
      image: new URL('@/assets/00002.jpg', import.meta.url).href }
]);
</script>
