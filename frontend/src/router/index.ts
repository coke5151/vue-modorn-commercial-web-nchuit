import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ShopView from "../views/ShopView.vue"; // Ensure this file exists at the specified path
import ProductDetail from "../views/ProductDetail.vue";
import CartView from "../views/CartView.vue";
import CheckoutView from "../views/CheckoutView.vue";
import UserProfile from "../views/UserProfile.vue";

const routes = [
  { path: "/", component: HomeView },
  { path: "/shop", component: ShopView },
  { path: "/product/:id", component: ProductDetail },
  { path: "/cart", component: CartView },
  { path: "/checkout", component: CheckoutView },
  { path: "/profile", component: UserProfile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
