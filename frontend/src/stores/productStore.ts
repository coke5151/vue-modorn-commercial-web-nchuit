// src/stores/productStore.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import axios from 'axios';

export const useProductStore = defineStore('product', () => {
    const products = ref<
        {
            id: number;
            name: string;
            category: string;
            price: number;
            discounted_price: number;
            image_url: string;
            quantity: number;
            stock: number;
            brand: string;
            connectionType: string;
            gamingCertified: boolean;
            comboSet: boolean;
            productType: string;
            BSMI: string;
            NCC: string;
            shippingLocation: string;
        }[]
    >([]);
    const searchQuery = ref('');
    const selectedCategories = ref<string[]>([]);
    const loading = ref(true); // 追蹤加載狀態

    const filteredProducts = computed(() => {
        let result = products.value;

        if (searchQuery.value) {
            result = result.filter(product =>
                product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
            );
        }

        if (selectedCategories.value.length > 0) {
            result = result.filter(product => selectedCategories.value.includes(product.category));
        }
        return result;
    });

    const uniqueCategories = computed(() =>
        Array.from(new Set(products.value.map(product => product.category)))
    );

    // 註冊
    const fetchData = async () => {
        try {
            loading.value = false; // 開始載入
            const response = await axios.get("/api/products");
            console.log("獲取資料成功:", response.data);
            products.value = response.data;
            return true;
        } catch (error: any) {
            console.error("獲取資料失敗:", error.response?.data || error.message);
            return false;
        } finally {
            loading.value = true; //
        }
    };

    return {    
        products,
        searchQuery,
        selectedCategories,
        filteredProducts,
        uniqueCategories,
        fetchData,
    };
});
