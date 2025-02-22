// src/stores/productStore.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useProductStore = defineStore('product', () => {
    const products = ref([
        {
            id: 1, name: "Gaming Mouse 1", category: 'Pet Food', price: 999, stock: 188, brand: "Logitech", connectionType: "Wireless", gamingCertified: true,
            comboSet: false, productType: "Standard", BSMI: "R41126", NCC: "CCAI23LP0120T2", shippingLocation: "Kaohsiung, Taiwan",
            image: new URL('@/assets/00001.jpg', import.meta.url).href
        },

        {
            id: 2, name: "Gaming Mouse 2", category: 'Pet Food', price: 799, stock: 374, brand: "Logitech", connectionType: "Wired", gamingCertified: true,
            comboSet: false, productType: "Special Edition", BSMI: "R41127", NCC: "CCAI23LP0120T3", shippingLocation: "Taipei, Taiwan",
            image: new URL('@/assets/00002.jpg', import.meta.url).href
        }
    ]);
    const searchQuery = ref('');
    const selectedCategories = ref<string[]>([]);

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
        alert(result);
        return result;
    });

    const uniqueCategories = computed(() =>
        Array.from(new Set(products.value.map(product => product.category)))
    );

    return {
        products,
        searchQuery,
        selectedCategories,
        filteredProducts,
        uniqueCategories,
    };
});
