# AI Commerce Project

## 1. 項目簡介

AI Commerce Project 是一個基於 AI 推薦的現代化電商平台，使用 Vue.js 作為前端框架，Node.js 作為後端，並搭配 MySQL 進行數據存儲。該平台旨在提供個性化購物體驗，透過 AI 推薦技術優化用戶體驗。

## 2. 技術棧

本專案採用了以下技術棧：

- **前端**：Vue 3、Vite、Tailwind CSS
- **後端**：Flask
- **資料庫**：MySQL
- **API 請求**：Axios

## 3. 專案結構

```
ai-commerce/
│── backend/         # 伺服器端
│   ├── models/      # 資料庫模型
│   ├── routes/      # API 路由
│   ├── services/    # 業務邏輯層
│   ├── app.js       # 伺服器入口
│   ├── .env         # 環境變數設定
│
│── frontend/        # 前端應用
│   ├── src/         # 核心程式碼
│   │   ├── assets/  # 靜態資源
│   │   ├── components/ # Vue 元件
│   │   ├── views/   # 頁面組件
│   │   ├── main.js  # Vue 入口
│   ├── public/      # 靜態 HTML
│   ├── index.html   # 應用入口
│
│── deploy/          # 部署相關設定
│── README.md        # 專案說明文件
│── package.json     # 項目依賴管理
```

## 4. 開發與部署步驟

### 4.1 建立專案目錄

```sh
mkdir ai-commerce && cd ai-commerce
```

### 4.2 建立後端應用

```sh
mkdir backend && cd backend
npm init -y
npm install express mysql2 redis dotenv axios cors
```

#### 後端程式結構

- `models/`：定義 MySQL 資料模型
- `routes/`：API 路由設計
- `services/`：封裝業務邏輯
- `app.js`：Express 應用入口

#### 建立 `app.js`

```js
const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());
app.get('/', (req, res) => res.send('AI Commerce Backend Running'));
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### 4.3 建立前端應用

```sh
cd ../frontend
npm create vue@latest .
npm install tailwindcss @tailwindcss/vite
```

#### 配置 Tailwind CSS

修改 `vite.config.ts`：

```js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

建立 `src/assets/main.css`：

```css
@import "tailwindcss";
```

#### 配置 `main.js`

```js
import { createApp } from 'vue';
import App from './App.vue';
import './assets/main.css';
createApp(App).mount('#app');
```

### 4.4 啟動應用

#### 啟動後端

```sh
cd backend && node app.js
```

#### 啟動前端

```sh
cd ../frontend && npm run dev
```

## 5. 主要功能

1. **用戶身份驗證**：註冊、登入、JWT 驗證
2. **商品管理**：上架、編輯、刪除商品
3. **個性化推薦**：基於 AI 的推薦系統
4. **購物車與訂單**：用戶購物車與結帳功能
5. **管理後台**：後台控制台管理商品和用戶

## 6. 版本管理與部署

### 6.1 Git 工作流程

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### 6.2 部署方式

- **本地開發**：`npm run dev`
- **雲端部署**：使用 Docker 或 Vercel/Nginx
- **資料庫**：MySQL 可部署至 AWS RDS 或自建伺服器

## 7. 環境變數設定 (`.env`)

```sh
PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=ai_commerce
REDIS_HOST=localhost
REDIS_PORT=6379
```

## 8. 測試與除錯

- **後端測試**：使用 Postman 測試 API
- **前端測試**：透過 Vue DevTools 進行除錯
- **整合測試**：可使用 Jest 或 Cypress

---

這份 README 概述了專案的開發流程與技術架構，適合全端開發者快速上手。🚀

