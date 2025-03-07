<template>
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-3xl font-bold mb-6">Checkout</h1>

        <!-- 顯示購物車內的商品 -->
        <div v-if="cart.length" class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Order Summary</h2>
            <div v-for="item in cart" :key="item.id" class="flex justify-between p-4 border-b">
                <img :src="item.image_url" alt="cart item" class="w-20 h-20 object-cover rounded-lg mr-4" />
                <span>{{ item.name }} (x{{ item.quantity }})</span>
                <span>${{ item.price * item.quantity }} NT</span>
            </div>
            <h2 class="text-xl font-bold mt-4 text-right">Total: ${{ totalPrice }} NT</h2>
        </div>

        <!-- 配送資訊 -->
        <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Shipping Details</h2>
            <form @submit.prevent="placeOrder">
                <div class="mb-4">
                    <label class="block text-gray-700">Full Name (必填，至少2個中文字)</label>
                    <input type="text" v-model="form.name" @input="validateName" required class="border p-2 w-full rounded-lg" />
                    <p v-if="errors.name" class="text-red-500">{{ errors.name }}</p>
                </div>

                <!-- 地址選擇 -->
                <div class="mb-4">
                    <label class="block text-gray-700">縣市 (必填)</label>
                    <select v-model="form.city" class="border p-2 w-full rounded-lg" required>
                        <option value="">請選擇縣市</option>
                        <option v-for="city in cities" :key="city" :value="city">{{ city }}</option>
                    </select>
                </div>
                
                <div class="mb-4">
                    <label class="block text-gray-700">鄉鎮市區 (必填)</label>
                    <select v-model="form.district" class="border p-2 w-full rounded-lg" required>
                        <option value="">請選擇鄉鎮市區</option>
                        <option v-for="district in districts[form.city]" :key="district" :value="district">{{ district }}</option>
                    </select>
                </div>
                
                <div class="mb-4">
                    <label class="block text-gray-700">詳細地址 (必填)</label>
                    <input type="text" v-model="form.address" required class="border p-2 w-full rounded-lg" placeholder="如：中山路100號5樓" />
                </div>

                <div class="mb-4">
                    <label class="block text-gray-700">Phone Number (必填，台灣手機格式)</label>
                    <input type="tel" v-model="form.phone" @input="validatePhone" required class="border p-2 w-full rounded-lg" />
                    <p v-if="errors.phone" class="text-red-500">{{ errors.phone }}</p>
                </div>

                <!-- 付款方式 -->
                <h2 class="text-xl font-semibold mb-2">Payment Method (必選)</h2>
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

                <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-lg w-full hover:bg-green-600 transition">
                    Place Order
                </button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useCartStore } from "@/stores/cartStore";
import { useRouter } from "vue-router";
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";

const cartStore = useCartStore();
const cart = cartStore.cart;
const totalPrice = cartStore.totalPrice;
const router = useRouter();
const authStore = useAuthStore();

const form = ref({ name: "", city: "", district: "", address: "", phone: "", payment: "" });
const errors = ref({ name: "", phone: "" });

const cities = ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"];
const districts = {
    "台北市": ["中正區", "大同區", "中山區", "松山區"],
    "新北市": ["板橋區", "新莊區", "中和區", "永和區"],
    "桃園市": ["桃園區", "中壢區", "平鎮區"],
};

const validateName = () => {
    errors.value.name = /^[一-龥]{2,}$/.test(form.value.name) ? "" : "姓名需至少2個中文字";
};

const validatePhone = () => {
    errors.value.phone = /^09\d{8}$/.test(form.value.phone) ? "" : "請輸入有效的台灣手機號碼 (09xxxxxxxx)";
};

const placeOrder = async () => {
    if (!authStore.user) return alert("You need to log in to place an order.");
    if (!form.value.payment) return alert("Please select a payment method.");
    if (errors.value.name || errors.value.phone) return alert("請修正表單錯誤");
    
    const orderData = { user_id: authStore.user, ...form.value, items: cart, total: totalPrice };
    await axios.post("/api/place_order", orderData);
    alert("Order placed successfully!");
    cartStore.cart = [];
    router.push("/");
};
</script>
