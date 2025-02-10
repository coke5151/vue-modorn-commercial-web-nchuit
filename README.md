# AI Commerce Project
這是一個基於 AI 推薦的電商平台，使用 Vue.js + Node.js + MySQL。

# 1️⃣ 建立專案目錄
mkdir ai-commerce && cd ai-commerce

# 2️⃣ 建立子目錄
mkdir backend frontend deploy

# 3️⃣ 產生 README.md
echo "# AI Commerce Project" > README.md
echo "這是一個基於 AI 推薦的電商平台，使用 Vue.js + Node.js + MySQL。" >> README.md

# 進入 backend 資料夾
cd backend

# 初始化 Node.js 專案
npm init -y

# 安裝必要套件
npm install express mysql2 redis dotenv axios cors

# 建立基本結構
mkdir models routes services

# 建立 Express.js 入口
cat > app.js <<EOL
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => res.send('AI Commerce Backend Running'));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(\`Server running on port \${PORT}\`));
EOL

# 回到專案根目錄
cd ../frontend

# 初始化 Vue 3 專案
npm create vue@latest .

# 安裝 Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# 設定 Tailwind 內容
cat > tailwind.config.js <<EOL
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts}"],
  theme: { extend: {} },
  plugins: [],
};
EOL

# 加入 Tailwind 到 CSS
mkdir src/assets
echo '@tailwind base;' > src/assets/main.css
echo '@tailwind components;' >> src/assets/main.css
echo '@tailwind utilities;' >> src/assets/main.css

# 更新 main.js 引入 Tailwind
cat > src/main.js <<EOL
import { createApp } from 'vue';
import App from './App.vue';
import './assets/main.css';

createApp(App).mount('#app');
EOL

# 回到專案根目錄
cd ..

# 啟動後端
cd backend && node app.js

# 啟動前端
cd ../frontend && npm run dev
