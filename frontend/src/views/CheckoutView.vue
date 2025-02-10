<template>
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-3xl font-bold mb-6">Checkout</h1>

        <!-- 顯示購物車內的商品 -->
        <div v-if="cart.length" class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Order Summary</h2>
            <div v-for="item in cart" :key="item.id" class="flex justify-between p-4 border-b">
                <span>{{ item.name }} (x{{ item.quantity }})</span>
                <span>${{ item.price * item.quantity }}</span>
            </div>
            <h2 class="text-xl font-bold mt-4 text-right">Total: ${{ totalPrice }}</h2>
        </div>

        <!-- 📌 配送資訊 -->
        <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Shipping Details</h2>
            <form @submit.prevent="placeOrder">
                <div class="mb-4">
                    <label class="block text-gray-700">Full Name</label>
                    <input type="text" v-model="form.name" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Address</label>
                    <input type="text" v-model="form.address" required class="border p-2 w-full rounded-lg" />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Phone Number</label>
                    <input type="tel" v-model="form.phone" required class="border p-2 w-full rounded-lg" />
                </div>

                <!-- 📌 付款方式 -->
                <h2 class="text-xl font-semibold mb-2">Payment Method</h2>
                <div class="flex gap-4 mb-6">
                    <label class="flex items-center">
                        <input type="radio" v-model="form.payment" value="credit_card" required />
                        <span class="ml-2">Credit Card</span>
                    </label>
                    <label class="flex items-center">
                        <input type="radio" v-model="form.payment" value="bank_transfer" />
                        <span class="ml-2">Bank Transfer</span>
                    </label>
                    <label class="flex items-center">
                        <input type="radio" v-model="form.payment" value="digital_wallet" />
                        <span class="ml-2">Digital Wallet</span>
                    </label>
                </div>

                <!-- 📌 提交按鈕 -->
                <button type="submit"
                    class="bg-green-500 text-white px-4 py-2 rounded-lg w-full hover:bg-green-600 transition">
                    Place Order
                </button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useCartStore } from "@/stores/cartStore";
import { useRouter } from "vue-router";

const cartStore = useCartStore();
const cart = cartStore.cart;
const totalPrice = cartStore.totalPrice;
const router = useRouter();

const form = ref({
    name: "",
    address: "",
    phone: "",
    payment: "",
});

// 📌 模擬提交訂單
const placeOrder = () => {
    if (!form.value.payment) {
        alert("Please select a payment method.");
        return;
    }

    alert("Order placed successfully! 🎉");
    cartStore.cart = []; // 清空購物車
    router.push("/"); // 導回首頁
};
</script>