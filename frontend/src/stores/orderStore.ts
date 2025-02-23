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
