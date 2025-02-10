<template>
    <div class="bg-gray-900 text-gray-300 py-6">
        <div class="container mx-auto px-6">
            <div class="flex flex-wrap justify-between items-center">
                <!-- 左側 - 版權資訊 -->
                <div class="mb-4 md:mb-0">
                    <h2 class="text-lg font-semibold text-white">AI Commerce</h2>
                    <p class="text-sm">&copy; 2025 AI Commerce. All rights reserved.</p>
                </div>

                <!-- 中間 - 導覽連結 -->
                <div class="flex gap-x-6">
                    <router-link to="/about" class="hover:text-white">About Us</router-link>
                    <router-link to="/contact" class="hover:text-white">Contact</router-link>
                    <router-link to="/privacy" class="hover:text-white">Privacy Policy</router-link>
                </div>

                <!-- 右側 - 社群媒體 -->
                <div class="flex gap-x-6">
                    <a href="https://facebook.com" target="_blank" class="hover:text-white">
                        <i class="fab fa-facebook"></i>
                    </a>
                    <a href="https://twitter.com" target="_blank" class="hover:text-white">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="https://instagram.com" target="_blank" class="hover:text-white">
                        <i class="fab fa-instagram"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
</script>

<style scoped>
i {
    font-size: 1.5rem;
}
</style>