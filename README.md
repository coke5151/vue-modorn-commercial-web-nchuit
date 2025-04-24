# AI Commerce Project

## 1. 項目簡介
AI Commerce Project 是一個基於 AI 推薦的現代化電商平台，使用 Vue.js 作為前端框架，Flask 作為後端，並搭配 MySQL 進行數據存儲。該平台旨在提供個性化購物體驗，透過 AI 推薦技術優化用戶體驗。

## 2. 技術棧
本專案採用了以下技術棧：

- **前端**：Vue 3、Vite、Tailwind CSS
- **後端**：Flask、Gemeni Flash
- **資料庫**：MySQL
- **API 請求**：Axios
- **套件管理**：uv (Python 套件管理器)

## 3. 專案結構
```
vue-modorn-commercial-web-nchuit/
│── src/             # 後端伺服器端
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
│   ├── __init__.py  # Python 套件初始化文件
│
│── frontend/        # 前端應用
│   ├── src/         # 核心程式碼
│   │   ├── assets/  # 靜態資源(圖片、CSS、SVG)
│   │   ├── components/ # Vue 元件 (頁面中的小元件設計)
│   │   ├── views/   # 頁面組件 (整個頁面設計)
│   │   ├── router/   # 路由 (每一個頁面的路徑)
│   │   ├── stores/   # Pinia資料存儲庫 (每一個資料表的獲取&儲存 export成全域變數)
│   │   ├── App.vue  # Vue 主體 (整體頁面基底設計)
│   │   ├── main.ts  # Vue 入口 (整體頁面基底掛載邏輯)
│   ├── public/      # 靜態 HTML 資源
│   ├── tests/       # 前端測試文件
│   ├── index.html   # 應用入口
│   ├── package.json # Node.js 依賴管理
│   ├── package-lock.json # 依賴版本鎖定文件
│   ├── vite.config.ts # Vite 配置文件
│   ├── tsconfig.json # TypeScript 配置文件
│
│── .venv/           # uv 建立的虛擬環境 (不納入版本控制)
│── pyproject.toml   # Python 專案配置
│── uv.lock          # uv 依賴鎖定文件
│── ai_commerce.sql  # 資料庫結構和初始數據
│── README.md        # 專案說明文件
│── .gitignore       # Git 忽略文件配置
│── .python-version  # Python 版本指定文件
│── ruff.toml        # Python 代碼檢查配置
```

## 4. 開發與部署步驟

### 4.1 建立專案目錄

```sh
# 克隆專案
git clone https://github.com/asddzxcc1856/vue-modorn-commercial-web-nchuit.git
cd vue-modorn-commercial-web-nchuit
```

### 4.2 建立後端應用

```sh
# 方法一：使用 uv
uv sync # 自動建立虛擬環境並安裝套件

# 方法二：自行建立虛擬環境並使用 pip
pip install -r requirements.txt
```

#### 後端程式結構
- `models/`：定義 MySQL 資料模型
- `routes/`：API 路由設計
- `app.py`：Flask 應用入口

### 4.3 建立前端應用
```sh
# 進入前端目錄
cd ../frontend

# 安裝前端相關套件
npm install
```

### 4.4 啟動應用
#### 啟動後端
```sh
# 方法一：使用 uv 啟動 Python 應用（推薦）
cd src
uv run app.py

# 方法二：自建虛擬環境，然後用你的環境執行
cd src
python src/app.py
```

#### 啟動前端
```sh
cd frontend

# 啟動前端應用
npm run dev
```

## 5. 主要功能
1. **用戶身份驗證**：註冊、登入、JWT 驗證
2. **商品管理**：上架、編輯、刪除商品
3. **個性化推薦**：基於 AI 的推薦系統
4. **購物車與訂單**：用戶購物車與結帳功能
5. **管理後台**：後台控制台管理商品和用戶

## 6. 環境變數設定
### 6.1 後端環境變數 (`.env` 或 `config.py`)
```sh
PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=ai_commerce
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 6.2 管理環境變數
使用 uv 時，可以在虛擬環境中設定環境變數：

```sh
# Linux/MacOS 設定環境變數
export DB_HOST=localhost
export DB_USER=root
# 或在 Windows PowerShell 中
$env:DB_HOST="localhost"
$env:DB_USER="root"
```

## 7. 使用 uv 套件管理器
本專案推薦使用 uv 套件管理器來管理 Python 和 Node.js 依賴，它具有以下優點：

- **速度快**：比傳統的 pip 快數倍
- **跨平台**：支援 Windows、macOS 和 Linux
- **虛擬環境管理**：內建虛擬環境管理功能
- **依賴解析**：更智能的依賴解析和衝突處理