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
            const images = import.meta.glob('@/assets/news/*.jpg', { eager: true });
            // 建立映射表 { 檔名: 圖片路徑 }
            const imageMap = Object.fromEntries(
            Object.entries(images).map(([path, module]) => {
                const filename = path.split('/').pop(); // 取得檔名
                return [filename, (module as { default: string }).default]; // 儲存 { "item1.jpg": "打包後的圖片URL" }
            })
            );
            // 指定對應的圖片
            // 🔄 監聽 `products` 變化並更新 `image_url`
            response.data.forEach((product : any) => {
                const filename = product.image_url.split("/").pop(); // 取得圖片檔名
                product.image_url = imageMap[filename] || "/assets/default.jpg"; // 設定對應圖片，找不到則使用預設圖片
            });
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
