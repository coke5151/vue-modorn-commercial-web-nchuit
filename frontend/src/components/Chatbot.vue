<template>
    <div>
        <!-- 🔵 AI 助理懸浮泡泡 -->
        <div @click="toggleChat"
            class="fixed bottom-5 right-5 bg-blue-500 text-white p-4 rounded-full cursor-pointer shadow-lg flex items-center justify-center w-14 h-14">
            💬
        </div>

        <!-- 📌 AI 聊天視窗 (桌機 & 手機版) -->
        <div v-if="isChatOpen" class="chat-container fixed bottom-16 right-5 bg-white shadow-xl rounded-lg border border-gray-300">
            <div class="flex justify-between items-center border-b pb-2 px-4">
                <h2 class="text-lg font-bold">AI 助理</h2>
                <button @click="toggleChat" class="text-gray-500 hover:text-gray-700">✖</button>
            </div>

            <!-- 🗨️ 對話區域 -->
            <div class="chat-box overflow-y-auto px-4 py-2 space-y-3">
                <div v-for="(msg, index) in messages" :key="index" class="flex" :class="msg.isUser ? 'justify-end' : 'justify-start'">
                    <div class="max-w-3/4 p-3 rounded-lg shadow" 
                        :class="msg.isUser ? 'bg-blue-500 text-white self-end' : 'bg-gray-200 text-gray-800 self-start'">
                        
                        <!-- 📝 解析 JSON 內容並顯示 -->
                        <vue-markdown-render v-if="!msg.products" :source="msg.data" />
                        
                        <div v-else>
                            <p class="font-bold">🛒 商品推薦：</p>
                            <ul class="mt-1 space-y-2">
                                <li v-for="product in msg.products" :key="product.id" class="flex items-center gap-2">
                                    <router-link :to="`/product/${product.id}`" class="text-blue-500 hover:underline font-medium">
                                        {{ product.name }}
                                    </router-link>
                                    <span class="text-gray-700">💰 ${{ product.price }}</span>
                                </li>
                            </ul>
                        </div>

                    </div>
                </div>
            </div>

            <!-- 📝 訊息輸入框 -->
            <div class="chat-input flex items-center gap-2 px-4 pb-4">
                <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="輸入訊息..." class="w-full p-2 border rounded-lg" />
                <button @click="sendMessage" class="bg-blue-500 text-white px-4 py-2 rounded-lg">送出</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* 桌機版對話框 */
.chat-container {
    width: 480px;
    height: 600px;
    max-height: 80vh;
    bottom: 20px;
    right: 20px;
}

/* 手機版調整 */
@media (max-width: 640px) {
    .chat-container {
        width: 100vw;
        height: 80vh;
        bottom: 0;
        right: 0;
        border-radius: 0;
    }
    .fixed {
        bottom: 10px;
        right: 10px;
    }
}

/* 聊天內容區域 (最大化滾動範圍) */
.chat-box {
    height: calc(100% - 120px);
}

/* 讓輸入框保持在底部 */
.chat-input {
    position: absolute;
    bottom: 0;
    width: 100%;
    background: white;
    padding-top: 8px;
}

</style>


<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import VueMarkdownRender from "vue-markdown-render";

const isChatOpen = ref(false);
const messages = ref([]);
const userMessage = ref("");
const router = useRouter();

const toggleChat = () => {
    isChatOpen.value = !isChatOpen.value;
};

const sendMessage = async () => {
    if (!userMessage.value.trim()) return;

    messages.value.push({ data: `🧑‍💻 你: ${userMessage.value}`, isUser: true });

    try {
        const response = await axios.post("/api/chat", { message: userMessage.value });

        let responseText = response.data.data;

        // 🛠 1. **使用正則表達式抓取 JSON**
        const jsonMatch = responseText.match(/```json\n([\s\S]*?)\n```/);
        let productList = null;

        if (jsonMatch) {
            try {
                productList = JSON.parse(jsonMatch[1]); // 🛠 2. 確保 JSON 格式正確
            } catch (error) {
                console.error("❌ JSON 解析錯誤:", error);
            }
        }

        // 🛠 3. **移除 Markdown JSON，讓剩下的文字正確顯示**
        responseText = responseText.replace(/```json\n[\s\S]*?\n```/, "").trim();

        messages.value.push({
            data: responseText, // 文字部分
            products: productList, // 商品 JSON
            isUser: false,
        });

    } catch (error) {
        messages.value.push({ data: "❌ 無法連線到 AI 服務！", isUser: false });
    }

    userMessage.value = "";
};

</script>