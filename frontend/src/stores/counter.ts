import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useCartStore = defineStore("cart", () => {
  const cart = ref([]);

  // 🛒 新增商品
  const addToCart = (product) => {
    const item = cart.value.find((p) => p.id === product.id);
    if (item) {
      item.quantity += product.quantity;
    } else {
      cart.value.push(product);
    }
  };

  // ❌ 移除商品
  const removeFromCart = (productId) => {
    cart.value = cart.value.filter((p) => p.id !== productId);
  };

  // 📊 計算總價
  const totalPrice = computed(() => cart.value.reduce((sum, p) => sum + p.price * p.quantity, 0));

  return { cart, addToCart, removeFromCart, totalPrice };
});
