# AI Commerce Project

## 1. 項目簡介

AI Commerce Project 是一個基於 AI 推薦的現代化電商平台，使用 Vue.js 作為前端框架，Flask 作為後端，並搭配 MySQL 進行數據存儲。該平台旨在提供個性化購物體驗，透過 AI 推薦技術優化用戶體驗。

## 2. 技術棧

本專案採用了以下技術棧：

- **前端**：Vue 3、Vite、Tailwind CSS
- **後端**：Flask、Gemeni Flash
- **資料庫**：MySQL
- **API 請求**：Axios

## 3. 專案結構

```
ai-commerce/
│── backend/         # 伺服器端
│   ├── models/      # 資料庫模型
│   │   ├── database.py  # 資料庫連線&登入
│   │   ├── product.py # 產品資料表
│   │   ├── user.py # 使用者資料表
│   ├── routes/      # API 路由
│   │   ├── auth.py # 登入&註冊功能API
│   │   ├── chatbot.py # AI客服功能API
│   │   ├── news.py # 最新消息功能API
│   │   ├── orders.py # 訂貨單功能API
│   │   ├── product.py # 產品列表功能API
│   │   ├── user.py # 使用者資料功能API
│   ├── app.py       # 伺服器入口
│   ├── config.py    # 環境變數設定(資料庫帳密)
│
│── frontend/        # 前端應用
│   ├── src/         # 核心程式碼
│   │   ├── assets/  # 靜態資源(圖片、CSS、SVG)
│   │   ├── components/ # Vue 元件 (頁面中的小元件設計)
│   │   ├── views/   # 頁面組件 (整個頁面設計)
│   │   ├── routes/   # 路由 (每一個頁面的路徑)
│   │   ├── stores/   # Pinia資料存儲庫 (每一個資料表的獲取&儲存 export成全域變數)
│   │   ├── App.vue  # Vue 主體 (整體頁面基底設計)
│   │   ├── main.ts  # Vue 入口 (整體頁面基底掛載邏輯)
│   ├── public/      # 靜態 HTML ()
│   ├── index.html   # 應用入口
│
│── deploy/          # 部署相關設定
│── README.md        # 專案說明文件
│── package.json     # 項目依賴管理
```

## 4. 開發與部署步驟

### 4.1 建立專案目錄

```sh
#此指令是初始化安裝的人使用
mkdir ai-commerce && cd ai-commerce
#請使用我的檔案
git clone https://github.com/asddzxcc1856/vue-modorn-commercial-web.git
```

### 4.2 建立後端應用

```sh
#此指令是初始化安裝的人使用
mkdir backend && cd backend
#請使用我的檔案(上面打過可以跳過此指令)
git clone https://github.com/asddzxcc1856/vue-modorn-commercial-web.git
#請安裝python的環境(二選一)
pip install flask flask_cors flask_jwt_extended google.generativeai requests pymysql
# python原生的pip套件管理或者miniconda套件管理去下載所有需要的套件(packages)
conda install flask flask_cors flask_jwt_extended google.generativeai requests pymysql

# 如果上述方法有問題請用以下方法(此方法使用miniconda+pip)
conda create -n flask_env python=3.12
conda activate flask_env
conda install -c conda-forge flask requests pymysql
pip install flask_cors flask_jwt_extended google.generativeai
```

#### 後端程式結構

- `models/`：定義 MySQL 資料模型
- `routes/`：API 路由設計
- `app.py`：Flask 應用入口

#### 建立 `app.js`

```python
from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.product import product_bp
from routes.news import news_bp
from routes.user import user_bp
from routes.chatbot import chatbot_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["JWT_SECRET_KEY"] = "your_secret_key"
app.config["JWT_IDENTITY_CLAIM"] = "sub"

jwt = JWTManager(app)  # 啟動 JWT

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(news_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(chatbot_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
```

### 4.3 建立前端應用

```sh
#此指令是初始化安裝的人使用
cd ../frontend
npm create vue@latest .
npm install tailwindcss @tailwindcss/vite

#請使用下列方法可以把 package.json 的套件所有都裝近來(沒裝不能動，因為github上面沒有那些套件)
npm install
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

#### 配置 `main.ts`

```ts
import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.min.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

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

