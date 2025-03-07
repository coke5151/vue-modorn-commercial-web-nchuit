<template>
    <div class="container mx-auto p-6">
        <h1 class="text-2xl font-bold mb-4">我的訂單</h1>

        <!-- 🔄 載入中提示 -->
        <div v-if="loading" class="text-center py-10">
            <p class="text-lg text-gray-600">載入中...</p>
        </div>

        <!-- ❌ 無訂單 -->
        <div v-else-if="orders.length === 0" class="text-center py-10">
            <p class="text-lg text-gray-600">目前沒有訂單。</p>
        </div>

        <!-- ✅ 訂單列表 -->
        <div v-else>
            <div v-for="order in orders" :key="order.order_id" class="border p-4 rounded-md shadow-md mb-4">
                <h2 class="text-xl font-semibold mb-2">訂單 #{{ order.order_id }}</h2>
                <p class="text-gray-600">總金額: ${{ order.total }}</p>
                <p class="text-gray-500">下單時間: {{ order.created_at }}</p>

                <div class="mt-4">
                    <h3 class="font-semibold">商品列表：</h3>
                    <ul>
                        <li v-for="item in order.items" :key="item.product_id" class="flex items-center gap-4 py-2">
                            <img :src="item.image" alt="商品圖片" class="w-16 h-16 rounded-md object-cover">
                            <div>
                                <router-link :to="{
                                    path: '/product/' + item.product_id
                                }" class="text-blue-500 hover:underline">
                                    {{ item.name }}
                                </router-link>
                                <p class="text-gray-600">數量: {{ item.quantity }}</p>
                                <p class="text-gray-600">單價: ${{ item.price }}</p>
                            </div>
                        </li>
                    </ul>
                </div>

                <button @click="goToOrderDetail(order)"
                    class="mt-3 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
                    查看詳細訂單
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, watch, watchEffect } from "vue";
import { useOrderStore } from "@/stores/orderStore";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from "pinia";

const router = useRouter();
const OrderStore = useOrderStore();
const { orders, loading } = storeToRefs(OrderStore);
const { fetchOrders, setSelectedOrder } = useOrderStore();
const goToOrderDetail = (order) => {
    setSelectedOrder(order); // ✅ 設定選擇的訂單
    router.push({
        path: `/order/${order.order_id}`,
    });
};
fetchOrders(); // 🚀 取得訂單列表
</script>
