import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";

export const useOrderStore = defineStore("order", () => {
    const orders = ref([]);
    const selectedOrder = ref(null); // ✅ 改為 `null`
    const loading = ref(true);
    const authStore = useAuthStore();

    const fetchOrders = async () => {
        if (!authStore.isAuthenticated) return;
        try {
            loading.value = true;
            const response = await axios.get("/api/orders", {
                headers: { Authorization: `Bearer ${authStore.token}` }
            });
            const images = import.meta.glob('@/assets/items/*.jpg', { eager: true });
            // 建立映射表 { 檔名: 圖片路徑 }
            const imageMap = Object.fromEntries(
            Object.entries(images).map(([path, module]) => {
                const filename = path.split('/').pop(); // 取得檔名
                return [filename, (module as { default: string }).default]; // 儲存 { "item1.jpg": "打包後的圖片URL" }
            })
            );
            // 指定對應的圖片
            // 🔄 監聽 `products` 變化並更新 `image_url`
            response.data.forEach((order : any) => {
                order.items.forEach((item : any) => {
                    const filename = item.image.split("/").pop(); // 取得圖片檔名
                    item.image = imageMap[filename] || "/assets/default.jpg"; // 設定對應圖片，找不到則使用預設圖片
                })
            });
            orders.value = response.data;
        } catch (error : any) {
            console.error("獲取訂單失敗:", error.response?.data || error.message);
        } finally {
            loading.value = false;
        }
    };

    const setSelectedOrder = (order : any) => {
        selectedOrder.value = order; // ✅ 這樣 `selectedOrder` 會被 Pinia 永久保存
    };

    return { orders, loading, fetchOrders, selectedOrder, setSelectedOrder };
});
