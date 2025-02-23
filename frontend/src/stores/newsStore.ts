import { defineStore } from "pinia";
import { ref, computed } from "vue";
import axios from "axios";

interface NewsItem {
    id: number;
    // Add other properties of a news item here
}

export const useNewsStore = defineStore("news", () => {
    const newsList = ref<NewsItem[]>([]);
    const isLoading = ref(false);

    // 取得所有新聞（首頁）
    const fetchNews = async () => {
        if (newsList.value.length > 0) return; // 避免重複請求
        try {
            isLoading.value = true;
            const response = await axios.get("/api/news");
            newsList.value = response.data;
        } catch (error) {
            console.error("獲取新聞失敗:", error);
        } finally {
            isLoading.value = false;
        }
    };

    // 根據 ID 取得特定新聞（詳細頁面）
    const getNewsById = (id: string) => {
        return newsList.value.find((news) => news.id === parseInt(id));
    };

    return { newsList, isLoading, fetchNews, getNewsById };
});
