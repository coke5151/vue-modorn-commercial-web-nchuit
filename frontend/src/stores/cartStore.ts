import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useCartStore = defineStore("cart", () => {
  // 🛒 購物車列表
  const cart = ref<
    {
      id: number;
      name: string;
      price: number;
      image: string;
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

  // 🛒 新增商品
  const addToCart = (product: typeof cart.value[0]) => {
    const item = cart.value.find((p) => p.id === product.id);
    if (item) {
      item.quantity += product.quantity;
    } else {
      cart.value.push({ ...product });
    }
  };

  // ❌ 移除商品
  const removeFromCart = (productId: number) => {
    cart.value = cart.value.filter((p) => p.id !== productId);
  };

  // 📊 計算總價
  const totalPrice = computed(() =>
    cart.value.reduce((sum, p) => sum + p.price * p.quantity, 0)
  );

  return { cart, addToCart, removeFromCart, totalPrice };
});
