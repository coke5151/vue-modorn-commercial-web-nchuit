<template>
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-3xl font-bold">Your Cart</h1>

        <div v-if="cart.length" class="mt-6">
            <div v-for="item in cart" :key="item.id"
                class="flex items-center justify-between p-4 border rounded-lg mb-4">
                
                <div class="flex items-center">
                    <img :src="item.image" alt="cart item" class="w-20 h-20 object-cover rounded-lg mr-4" />
                    <div>
                        <h2 class="text-lg font-semibold">{{ item.name }}</h2>
                        <p class="text-gray-500">${{ item.price }} x {{ item.quantity }}</p>
                        <p class="text-gray-500"><strong>Brand:</strong> {{ item.brand }}</p>
                        <p class="text-gray-500"><strong>Connection:</strong> {{ item.connectionType }}</p>
                        <p class="text-gray-500"><strong>Gaming Certified:</strong> {{ item.gamingCertified ? 'Yes' : 'No' }}</p>
                        <p class="text-gray-500"><strong>Stock Left:</strong> {{ item.stock }}</p>
                        <p class="text-gray-500"><strong>BSMI:</strong> {{ item.BSMI }}</p>
                        <p class="text-gray-500"><strong>NCC:</strong> {{ item.NCC }}</p>
                    </div>
                </div>
                
                <button @click="removeFromCart(item.id)" class="text-red-500 hover:underline">Remove</button>
            </div>

            <!-- 🧾 總金額 -->
            <div class="text-right mt-6">
                <h2 class="text-xl font-bold">Total: ${{ totalPrice }}</h2>
                <router-link to="/checkout">
                    <button class="bg-blue-500 text-white px-4 py-2 rounded-lg mt-2 hover:bg-blue-600 transition">
                        Proceed to Checkout
                    </button>
                </router-link>
            </div>
        </div>

        <p v-else class="text-center text-gray-500 mt-6">Your cart is empty.</p>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useCartStore } from "@/stores/cartStore";

const cartStore = useCartStore();
const cart = computed(() => cartStore.cart);
const totalPrice = computed(() => cartStore.totalPrice);
const removeFromCart = cartStore.removeFromCart;
</script>
