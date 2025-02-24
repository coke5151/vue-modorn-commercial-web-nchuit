<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <main class="flex-grow">
      <router-view />
    </main>
    <Chatbot />
    <Footer />
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
import Chatbot from "./components/Chatbot.vue";
import { useProductStore } from "@/stores/productStore";

const productStore = useProductStore();
productStore.fetchData();
</script>
