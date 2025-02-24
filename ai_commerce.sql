-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2025-02-24 05:32:45
-- 伺服器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `ai_commerce`
--

-- --------------------------------------------------------

--
-- 資料表結構 `addresses`
--

CREATE TABLE `addresses` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `subtitle` varchar(255) DEFAULT NULL,
  `content` text NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `news`
--

INSERT INTO `news` (`id`, `title`, `subtitle`, `content`, `image_url`, `created_at`) VALUES
(1, 'AI 商業應用大突破！', '企業如何透過 AI 提升業務效率？', '人工智慧（AI）正在迅速改變商業世界，企業透過 AI 技術提升效率、降低成本，並改善客戶體驗。在 2025 年，全球 AI 市場預計將達到 1 兆美元，許多企業已經將 AI 融入日常業務中，包括自動化流程、數據分析、客服機器人等。  \r\n\r\n許多大型企業，如 **Google、Amazon 和 Microsoft**，已經在其業務中廣泛使用 AI。透過機器學習（ML）技術，這些公司能夠預測市場趨勢，並根據數據調整產品策略。例如，Amazon 透過 AI 驅動的推薦系統提升銷售，根據使用者行為推薦個人化產品，提高轉換率。  \r\n\r\n**AI 在企業應用的三大優勢：**  \r\n1. **提高生產力與自動化**：AI 可以幫助企業減少人工操作，提高工作效率。例如，製造業透過機器視覺（Computer Vision）來檢測產品品質，降低人為誤差。  \r\n2. **數據分析與決策優化**：企業透過 AI 驅動的分析工具，可以更準確地預測市場需求。例如，財務機構使用 AI 來分析投資組合，提供更精準的投資建議。  \r\n3. **客戶體驗提升**：企業透過 AI 聊天機器人（Chatbot）提高客服效率，例如銀行業者利用 AI 提供 24/7 即時回應，提高客戶滿意度。  \r\n\r\n展望未來，隨著 AI 技術的進步，商業應用將更加多元化。企業應該積極導入 AI 技術，以確保在競爭市場中保持領先地位。  ', '/assets/news1.jpg', '2025-02-23 11:28:10'),
(2, '電商市場趨勢報告 2025', '消費者購物習慣的重大變化', '全球電商市場在過去幾年快速增長，根據 **Statista** 的數據，2025 年全球電商市場規模將突破 7.5 兆美元。隨著科技進步，消費者購物習慣正在發生重大變化，這些變化將影響企業的市場策略。  \r\n\r\n**1. 個性化購物體驗**  \r\n消費者越來越期望個性化的購物體驗。**AI 驅動的推薦系統** 透過分析用戶行為，提供個人化的商品推薦。像 Amazon、Shopee 這類電商平台，都已經廣泛使用 AI 來提升用戶體驗，透過大數據分析讓消費者更容易找到自己感興趣的商品。  \r\n\r\n**2. 即時購物與社群電商**  \r\n社群媒體平台（如 Facebook、Instagram、TikTok）已成為電商新戰場。消費者可以直接在社群平台上進行購物，而不需要跳轉至其他網站。這種 **社群電商（Social Commerce）** 已經成為新興趨勢，特別是在中國市場，**直播帶貨** 產業每年創造上百億美元的銷售額。  \r\n\r\n**3. 永續發展與綠色電商**  \r\n消費者越來越關注環保問題，電商企業開始導入永續發展策略。例如，**IKEA 和 Patagonia** 等品牌開始提供「環保包裝」與「二手回收計畫」，減少碳排放，提高品牌形象。  \r\n\r\n未來幾年，電商將持續朝向 **個性化、社群化、環保化** 發展，企業應該提前佈局，以抓住市場機遇。  ', '/assets/news2.jpg', '2025-02-23 11:28:10'),
(3, '科技巨頭進軍 Web3.0', '區塊鏈技術將如何改變未來互聯網？', 'Web3.0 是當前科技界最熱門的話題之一，它以區塊鏈技術為基礎，提供更加去中心化的互聯網架構。與傳統 Web2.0 相比，Web3.0 允許用戶擁有自己的數據，並透過智能合約（Smart Contract）執行去中心化應用（DApp）。  \r\n\r\n**1. Web3.0 的三大核心技術**  \r\n- **區塊鏈技術**：確保交易安全與透明，例如 **Ethereum 和 Solana** 提供去中心化應用平台。  \r\n- **去中心化儲存**：如 **IPFS（星際文件系統）**，允許去中心化存儲，避免傳統伺服器宕機問題。  \r\n- **智能合約**：自動執行合約條款，無需第三方仲介。  \r\n\r\n**2. 科技巨頭的佈局**  \r\n- **Meta（Facebook）**：計畫開發 **去中心化社群平台**，並整合 NFT（非同質化代幣）。  \r\n- **Google Cloud**：推出區塊鏈數據分析服務，幫助企業使用 Web3.0 技術。  \r\n- **Microsoft**：透過 Azure 提供區塊鏈解決方案，推動企業級應用。  \r\n\r\nWeb3.0 被認為是未來網路發展的方向，隨著技術成熟，將顛覆傳統互聯網模式。  ', '/assets/news3.jpg', '2025-02-23 11:28:10'),
(4, '5G 普及化，影響你的生活！', '高速網路如何改變行動裝置使用體驗？', '5G 技術的普及，正在徹底改變行動裝置的使用方式。與 4G 相比，5G 網速提升 **10 倍以上**，延遲降低至 **毫秒級**，為物聯網、智慧城市、自駕車等技術帶來突破性進展。  \r\n\r\n**5G 在不同領域的應用：**  \r\n- **智慧城市**：透過 5G 連接交通燈、監控系統，提升城市運作效率。  \r\n- **雲端遊戲**：玩家可以透過 5G 網路在手機上運行高端遊戲，例如 **NVIDIA GeForce Now**、**Google Stadia**。  \r\n- **遠端醫療**：5G 讓醫生可以透過 **VR/AR 遠端進行手術**，提升醫療可及性。  \r\n\r\n未來，隨著 5G 設備價格下降，這項技術將普及至全球。  ', '/assets/news4.jpg', '2025-02-23 11:28:10'),
(5, '永續發展與綠色科技', '企業如何實現 ESG 目標？', 'ESG（環境、社會、治理）已成為企業發展的重要指標，許多公司開始採取綠色能源、減少碳排放，以達到環境永續發展目標。例如，**Tesla** 正在大力推動太陽能電池板和電動車技術，減少對化石燃料的依賴。  \r\n\r\n隨著各國政府加強環保政策，企業將需要加快綠色轉型，以確保長期競爭力。  ', '/assets/news5.jpg', '2025-02-23 11:28:10');

-- --------------------------------------------------------

--
-- 資料表結構 `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `order_items`
--

CREATE TABLE `order_items` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `category` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `discounted_price` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `connection_type` varchar(50) DEFAULT NULL,
  `gaming_certified` tinyint(1) DEFAULT 0,
  `combo_set` tinyint(1) DEFAULT 0,
  `product_type` varchar(100) DEFAULT NULL,
  `BSMI` varchar(50) DEFAULT NULL,
  `NCC` varchar(50) DEFAULT NULL,
  `shipping_location` varchar(255) DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `products`
--

INSERT INTO `products` (`id`, `name`, `category`, `price`, `discounted_price`, `stock`, `brand`, `connection_type`, `gaming_certified`, `combo_set`, `product_type`, `BSMI`, `NCC`, `shipping_location`, `image_url`, `created_at`, `updated_at`) VALUES
(1, 'Gaming Mouse 1', 'Pet Food', 999, 799, 179, 'Logitech', 'Wireless', 1, 0, 'Standard', 'R41126', 'CCAI23LP0120T2', 'Kaohsiung, Taiwan', '/assets/00001.jpg', '2025-02-22 07:00:11', '2025-02-23 13:18:25'),
(2, 'Gaming Mouse 2', 'Pet Food', 799, 599, 373, 'Logitech', 'Wired', 1, 0, 'Special Edition', 'R41127', 'CCAI23LP0120T3', 'Taipei, Taiwan', '/assets/00002.jpg', '2025-02-22 07:00:11', '2025-02-23 08:40:14'),
(3, 'Gaming Mouse Pro', 'Gaming Accessories', 1299, 1099, 50, 'Razer', 'Wireless', 1, 0, 'Standard', 'R51128', 'CCAI23LP0121T4', 'Kaohsiung, Taiwan', '/assets/00003.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(4, 'Gaming Mouse X', 'Gaming Accessories', 899, 799, 100, 'SteelSeries', 'Wired', 1, 0, 'Special Edition', 'R51129', 'CCAI23LP0122T5', 'Taipei, Taiwan', '/assets/00004.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(5, 'Mechanical Keyboard V1', 'Gaming Accessories', 2499, 2199, 30, 'Corsair', 'Wired', 1, 0, 'RGB', 'R61130', 'CCAI23LP0123T6', 'Tainan, Taiwan', '/assets/00005.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(6, 'Mechanical Keyboard Lite', 'Gaming Accessories', 1799, 1599, 60, 'Logitech', 'Wireless', 1, 0, 'Compact', 'R61131', 'CCAI23LP0124T7', 'Taichung, Taiwan', '/assets/00006.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(7, 'Gaming Headset Elite', 'Gaming Accessories', 1999, 1799, 40, 'HyperX', 'Wireless', 1, 0, 'Surround Sound', 'R71132', 'CCAI23LP0125T8', 'Kaohsiung, Taiwan', '/assets/00007.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(8, 'Gaming Headset X', 'Gaming Accessories', 1399, 1199, 75, 'Razer', 'Wired', 1, 0, 'Noise Cancelling', 'R71133', 'CCAI23LP0126T9', 'Taipei, Taiwan', '/assets/00008.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(9, 'Gaming Monitor 27\"', 'Gaming Accessories', 5999, 5499, 25, 'ASUS', 'Wired', 1, 0, '144Hz', 'R81134', 'CCAI23LP0127T10', 'Tainan, Taiwan', '/assets/00009.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(10, 'Gaming Monitor 32\"', 'Gaming Accessories', 7499, 6999, 14, 'Acer', 'Wired', 1, 0, '165Hz', 'R81135', 'CCAI23LP0128T11', 'Taichung, Taiwan', '/assets/00010.jpg', '2025-02-23 08:44:21', '2025-02-23 13:18:25'),
(11, 'Gaming Controller Pro', 'Gaming Accessories', 2999, 2599, 35, 'Sony', 'Wireless', 1, 0, 'DualSense', 'R91136', 'CCAI23LP0129T12', 'Kaohsiung, Taiwan', '/assets/00011.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21'),
(12, 'Gaming Controller X', 'Gaming Accessories', 1999, 1699, 50, 'Microsoft', 'Wireless', 1, 0, 'Elite', 'R91137', 'CCAI23LP0130T13', 'Taipei, Taiwan', '/assets/00012.jpg', '2025-02-23 08:44:21', '2025-02-23 08:44:21');

-- --------------------------------------------------------

--
-- 資料表結構 `reviews`
--

CREATE TABLE `reviews` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `addresses`
--
ALTER TABLE `addresses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- 資料表索引 `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- 資料表索引 `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- 資料表索引 `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `addresses`
--
ALTER TABLE `addresses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `order_items`
--
ALTER TABLE `order_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `addresses`
--
ALTER TABLE `addresses`
  ADD CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- 資料表的限制式 `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- 資料表的限制式 `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);

--
-- 資料表的限制式 `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
