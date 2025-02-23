<template>
    <div class="container mx-auto p-6">
        <h1 class="text-2xl font-bold mb-4">訂單詳情 #{{ orderId }}</h1>

        <div v-if="loading" class="text-center py-10">
            <p class="text-lg text-gray-600">載入中...</p>
        </div>

        <div v-else-if="product">
            <p class="text-gray-600">總金額: ${{ product.total }}</p>
            <p class="text-gray-500">下單時間: {{ product.created_at }}</p>

            <h2 class="font-semibold mt-4">商品列表：</h2>
            <ul>
                <li v-for="item in product.items" :key="item.product_id" class="flex items-center gap-4 py-2">
                    <img :src="url + item.image" alt="商品圖片" class="w-16 h-16 rounded-md object-cover">
                    <div>
                        <router-link :to="'/product/' + item.product_id" class="text-blue-500 hover:underline">
                            {{ item.name }}
                        </router-link>
                        <p class="text-gray-600">數量: {{ item.quantity }}</p>
                        <p class="text-gray-600">單價: ${{ item.price }}</p>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import { useOrderStore } from "@/stores/orderStore";
import { storeToRefs } from "pinia";

const OrderStore = useOrderStore();
const { selectedOrder } = storeToRefs(OrderStore);
const loading = ref(false);
console.log(selectedOrder.value);
const route = useRoute();
const orderId = ref(route.params.id);
const product = selectedOrder.value;
const url = new URL('@/', import.meta.url).href;
</script>
