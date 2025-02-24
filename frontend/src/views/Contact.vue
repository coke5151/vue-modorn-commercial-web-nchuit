<template>
    <div class="container mx-auto p-6">
      <h1 class="text-3xl font-bold mb-4">聯絡我們</h1>
      <p class="text-gray-700 mb-4">如果您對我們的產品或服務有任何疑問，請隨時聯絡我們。</p>
  
      <div class="bg-gray-100 p-4 rounded-lg">
        <h2 class="text-xl font-semibold">📧 客服信箱</h2>
        <p class="text-gray-700">support@example.com</p>
      </div>
  
      <div class="bg-gray-100 p-4 rounded-lg mt-4">
        <h2 class="text-xl font-semibold">📞 客服專線</h2>
        <p class="text-gray-700">+886 1234 5678</p>
      </div>
  
      <div class="bg-gray-100 p-4 rounded-lg mt-4">
        <h2 class="text-xl font-semibold">🏢 公司地址</h2>
        <p class="text-gray-700">台北市信義區科技路 101 號</p>
      </div>
  
      <h2 class="text-xl font-semibold mt-6">📩 聯絡表單</h2>
      <form @submit.prevent="submitForm" class="mt-4 space-y-4">
        <input v-model="name" type="text" placeholder="您的姓名" class="w-full p-2 border rounded-lg" required />
        <input v-model="email" type="email" placeholder="您的電子郵件" class="w-full p-2 border rounded-lg" required />
        <textarea v-model="message" placeholder="您的訊息" class="w-full p-2 border rounded-lg h-24" required></textarea>
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg">送出</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const name = ref('');
  const email = ref('');
  const message = ref('');
  
  const submitForm = () => {
    alert(`✅ 您的訊息已提交！\n姓名: ${name.value}\nEmail: ${email.value}\n內容: ${message.value}`);
    name.value = '';
    email.value = '';
    message.value = '';
  };
  </script>
  