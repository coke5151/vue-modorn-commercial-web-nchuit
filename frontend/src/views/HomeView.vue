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
        <li v-for="news in newsStore.newsList" :key="news.id" class="border-b pb-2 text-gray-700">
          <router-link :to="`/news/${news.id}`" class="text-blue-500 hover:underline">
            {{ news.title }}
          </router-link>
          <p class="text-gray-500 text-sm">{{ news.subtitle }}</p>
        </li>
      </ul>
    </section>

    <!-- 🔥 熱門產品 -->
    <section class="mb-10">
      <h2 class="text-2xl font-bold text-gray-800">🔥 熱門產品</h2>
      <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="product in popularProducts" :key="product.id" class="bg-white shadow-md rounded-lg p-4">
          <img :src="product.image_url" alt="product" class="w-full h-40 object-cover rounded">
          <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
          <p class="text-gray-500 line-through">{{ product.price }} NT</p>
          <p class="text-red-500 font-bold">{{ product.discounted_price }} NT</p>
          <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View Details</router-link>
        </div>
      </div>
    </section>

    <!-- 🎯 今日特惠 -->
    <section>
      <h2 class="text-2xl font-bold text-gray-800">🎯 今日特惠</h2>
      <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="product in todayDeals" :key="product.id" class="bg-yellow-100 shadow-md rounded-lg p-4">
          <img :src="product.image_url" alt="product" class="w-full h-40 object-cover rounded">
          <h2 class="text-lg font-semibold mt-2">{{ product.name }}</h2>
          <p class="text-gray-500 line-through">{{ product.price }} NT</p>
          <p class="text-red-500 font-bold">{{ product.discounted_price }} NT</p>
          <router-link :to="'/product/' + product.id" class="text-blue-500 mt-2 inline-block">View Details</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useProductStore } from "@/stores/productStore";
import { storeToRefs } from "pinia";
import { useNewsStore } from "@/stores/newsStore";

const newsStore = useNewsStore();
const { newsList } = storeToRefs(newsStore);
if (newsList.value.length === 0 || newsList.value === null || newsList.value === undefined)
  newsStore.fetchNews();
const ProductStore = useProductStore()
const { products } = storeToRefs(ProductStore)
// 🖼️ 橫幅圖片
const bannerImage = ref(new URL('@/assets/banner.png', import.meta.url).href);

// 📰 最新消息
const latestNews = ref([
  { id: 1, title: "⚡ 新品上市！AI 智慧滑鼠震撼登場！", link: "/news/1" },
  { id: 2, title: "🎉 限時折扣：指定商品 85 折！", link: "/news/2" },
  { id: 3, title: "🚀 AI 商城全面升級，體驗新 UI！", link: "/news/3" }
]);
// 🔥 熱門產品
const popularProducts = computed(() => products.value);
// 🎯 今日特惠
const todayDeals = computed(() => products.value);
</script>
