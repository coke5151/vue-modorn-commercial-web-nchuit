<template>
    <div v-if="news" class="container mx-auto p-6">
        <!-- 標題與副標題 -->
        <div class="text-center mb-6">
            <h1 class="text-4xl font-bold">{{ news.title }}</h1>
            <p class="text-gray-500 mt-2">{{ news.subtitle }}</p>
        </div>

        <!-- 橫幅圖片 -->
        <div class="mb-6">
            <img :src="url + news.image_url" alt="News banner" class="w-full rounded-lg shadow-md">
        </div>

        <!-- 文章內容 -->
        <VueMarkdownRender :source="markdownText" />


        <!-- 社群分享 -->
        <div class="mt-6 flex justify-center gap-4">
            <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Facebook</button>
            <button class="bg-blue-400 text-white px-4 py-2 rounded hover:bg-blue-500">Twitter</button>
            <button class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Share</button>
        </div>
    </div>
</template>

<script setup>
import { computed,ref } from "vue";
import { useRoute } from "vue-router";
import { useNewsStore } from "@/stores/newsStore";
import { storeToRefs } from "pinia";
import VueMarkdownRender from "vue-markdown-render";
const route = useRoute();
const newsStore = useNewsStore();
const { newsList } = storeToRefs(newsStore);
if (newsList.value.length === 0 || newsList.value === null || newsList.value === undefined)
    newsStore.fetchNews();
const news = computed(() => newsList.value.find((news) => news.id === Number(route.params.id)));
const url = new URL('@/', import.meta.url).href;
const markdownText = computed(() => news.value.content);
</script>