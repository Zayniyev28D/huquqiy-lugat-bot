# 🏛 SHAROFOVA'S WORD (@lugaviy_word_uz_bot) — Huquqiy Atamalar Izohli Lugʻati

Ushbu bot Oʻzbekiston Respublikasi Konstitutsiyasi, kodekslari, amaldagi qonunlari hamda Adliya vazirligining rasmiy **«Yuridik ensiklopediya»** nashri asosida shakllantirilgan **50 ta asosiy huquqiy atama** va ularning rasmiy izohlarini qulay shaklda taqdim etadi.

- **Bot nomi:** `SHAROFOVA'S WORD`
- **Username:** `@lugaviy_word_uz_bot`

---

## ✨ Botning asosiy imkoniyatlari

1. **🏛 4 ta huquqiy yoʻnalish boʻyicha qulay menyu:**
   - *I. Davlat va huquq nazariyasi hamda Konstitutsiyaviy huquq* (15 ta atama)
   - *II. Fuqarolik, oila va mehnat huquqi* (13 ta atama)
   - *III. Jinoyat va maʼmuriy huquq* (11 ta atama)
   - *IV. Protsessual huquq va odil sudlov* (11 ta atama)
2. **📖 Sahifalangan (Pagination) tugmalar:** Atamalar 5 tadan boʻlib qulay koʻrinishda chiqadi (`⬅️ Oldingi`, `Keyingi ➡️`).
3. **🔍 Aqlli va tezkor qidiruv:**
   - Foydalanuvchi ixtiyoriy soʻzni yozsa (masalan: `Aliment`, `Aksept`, `Huquq`, `Prezump`), bot bir zumda uning huquqiy asosi va izohini topib beradi.
   - Soʻzning bir qismini yozganda ham qidiruv ishlaydi.
4. **🎲 Tasodifiy atama:** Huquqiy bilimlarni mustahkamlash uchun bitta tugma bilan tasodifiy tushunchani koʻrsatadi.
5. **💬 Inline Query rejimi:** Guruh yoki shaxsiy suhbatlarda `@bot_nomi so'z` deb yozib, istalgan atamani doʻstlarga ulashish mumkin.
6. **🌐 24/7 Online va Anti-Sleep (Uxlashga qarshi tizim):**
   - Kompyuter oʻchganda ham bulutli bepul serverlarda (Render, Koyeb, Railway) uzluksiz ishlaydi.
   - Ichki Keep-Alive veb-serveri va avtomatik oʻz-oʻziga ping berish mexanizmi mavjud.

---

## 🚀 1-QADAM: Telegramda Bot ochish va Token olish

1. Telegramda [@BotFather](https://t.me/BotFather) botini oching.
2. `/newbot` buyrugʻini yuboring.
3. Botingizga nom bering (masalan: `Huquqiy Lug'at Boti`).
4. Botingizga username bering (oxiri `bot` bilan tugashi kerak, masalan: `huquqiy_lugat_uz_bot`).
5. `@BotFather` sizga **API Token** beradi (namuna: `7123456789:AAEjKlMnOpQrStUvWxYz0123456789`). Uni saqlab oling.
6. Inline rejimini yoqish uchun `@BotFather`ga `/setinline` buyrugʻini yuboring, botingizni tanlang va qisqa matn yozing (masalan: `Huquqiy atamani qidiring...`).

---

## 💻 2-QADAM: Kompyuterda sinab koʻrish (Lokal test)

1. Ushbu loyiha papkasiga kiring:
   ```bash
   cd huquqiy_lugat_bot
   ```
2. `.env` faylini oching va bot tokenni yozing:
   ```env
   BOT_TOKEN=7123456789:AAEjKlMnOpQrStUvWxYz0123456789
   PORT=8080
   ```
3. Kutubxonalarni oʻrnating:
   ```bash
   pip install -r requirements.txt
   ```
4. Botni ishga tushiring:
   ```bash
   python bot.py
   ```
5. Telegramda oʻz botingizga kiring va `/start` tugmasini bosing!

---

## ☁️ 3-QADAM: Kompyuter oʻchiq turganda ham 24/7 Online rejimda ishlatish (Render.com da BEPUL)

Botingiz shaxsiy kompyuteringiz oʻchiq boʻlsa ham butunlay bepul ishlab turishi uchun eng oson va qulay usul — **Render.com** bulutli serveridan foydalanish:

### 1-bosqich: Kodni GitHub ga yuklash
1. [GitHub.com](https://github.com) ga kiring va yangi repository oching (masalan: `huquqiy-lugat-bot`).
2. Loyihani GitHub ga yuklang:
   ```bash
   git init
   git add .
   git commit -m "Huquqiy lugat boti v1.0"
   git branch -M main
   git remote add origin https://github.com/SIZNING_PROFILINGIZ/huquqiy-lugat-bot.git
   git push -u origin main
   ```

### 2-bosqich: Render.com ga ulash
1. [Render.com](https://render.com) saytiga bepul roʻyxatdan oʻting (GitHub orqali kirish qulay).
2. Dashboard da **New +** tugmasini bosing va **Web Service** ni tanlang.
3. GitHub dagi `huquqiy-lugat-bot` repozitoriyni tanlang (**Connect**).
4. Sozlamalarni tekshiring:
   - **Name:** `huquqiy-lugat-bot`
   - **Region:** Frankfurt yoki Singapore
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Instance Type:** `Free` ($0/month)
5. Pastroqdagi **Environment Variables** boʻlimiga kiring va qoʻshing:
   - `BOT_TOKEN` = `sizning_telegram_bot_tokeningiz`
   - `PORT` = `10000`
6. **Create Web Service** tugmasini bosing!
7. Render bir necha daqiqada botni ishga tushiradi va sizga bepul havola beradi (masalan: `https://huquqiy-lugat-bot.onrender.com`).

---

## ⚡ 4-QADAM: Bot uxlab qolmasligi uchun mukammallashtirish (Anti-Sleep)

Render.com bepul tarifida 15 daqiqa davomida soʻrov kelmasa server uxlab qoladi (spin-down). Buni bartaraf etish va botni 24/7 doimo uygʻoq va tezkor qilish uchun **2 ta oʻta ishonchli yechim** qilingan:

### 1-yechim: Botning ichki Anti-Sleep tizimi
Render sizga bergan URL manzilni (masalan: `https://huquqiy-lugat-bot.onrender.com`) Render Environment Variables boʻlimiga kirib:
- `SELF_URL` = `https://huquqiy-lugat-bot.onrender.com`
qilib kiriting. Bot har 9 daqiqada oʻz-oʻziga `/health` soʻrovi yuboradi va server hech qachon uxlamaydi!

### 2-yechim: Tashqi bepul monitoring (100% KAFOLAT)
1. [Cron-Job.org](https://cron-job.org) yoki [UptimeRobot.com](https://uptimerobot.com) saytiga bepul kiring.
2. Yangi monitor qoʻshing:
   - **Monitor Type:** `HTTP(s)`
   - **URL:** `https://huquqiy-lugat-bot.onrender.com/ping`
   - **Monitoring Interval:** Har `5 daqiqa` (Every 5 minutes).
3. Saqlang! Endi tashqi xizmat har 5 daqiqada botga signal berib turadi va Render serveringiz 24 soat, 365 kun kompyuteringiz oʻchiq boʻlsa ham uzluksiz ishlaydi.

---

## 🗂 Loyiha fayllari tuzilishi

- `bot.py` — Botning asosiy boshqaruv kodi, komandalar, inline qidiruv va keep-alive integratsiyasi.
- `dictionary_data.py` — Barcha 50 ta huquqiy atama va ularning rasmiy izohlari bazasi hamda qidiruv algoritmi.
- `keyboards.py` — Chiroyli inline va menyu tugmalari, sahifalash (pagination) mantiqi.
- `keep_alive.py` — Bepul bulutli serverlar uchun yengil veb-server va uxlab qolishga qarshi (Anti-Sleep) ping moduli.
- `requirements.txt` — Kerakli Python kutubxonalari roʻyxati.
- `Dockerfile` — Docker konteynerda ishga tushirish uchun (Koyeb, Railway, VPS uchun).
- `render.yaml` — Render.com uchun 1-bosqichli avtomatik deploy konfiguratsiyasi.
- `test_bot.py` — 50 ta atama va qidiruvning toʻgʻri ishlashini tekshiruvchi avtomatlashgan testlar.
