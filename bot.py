import os
import sys
import random
import logging
import asyncio

# Windows konsolida UTF-8 ni to'g'ri ko'rsatish
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from aiohttp import web

from dictionary_data import (
    CATEGORIES,
    TERMS,
    search_terms,
    get_term_by_id,
    get_terms_by_category
)
from keyboards import (
    get_main_reply_keyboard,
    get_categories_inline_keyboard,
    get_terms_paginated_keyboard,
    get_term_details_keyboard,
    get_search_results_keyboard
)
from keep_alive import create_web_app, self_ping_loop

# .env faylini yuklash
load_dotenv()

# Loggerni sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger("SharofavasWordBot")

BOT_NAME = "SHAROFOVA'S WORD"
BOT_USERNAME = "lugaviy_word_uz_bot"

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
PORT = int(os.getenv("PORT", 8080))
SELF_URL = os.getenv("SELF_URL") or os.getenv("RENDER_EXTERNAL_URL") or ""

dp = Dispatcher()

# =============================================================================
# YORDAMCHI MATN FORMATLASH FUNKSIYALARI
# =============================================================================

def format_term_card(item: dict) -> str:
    """Atama izohini chiroyli va qulay formatda taqdim etish"""
    cat = CATEGORIES.get(item["category_id"], {})
    cat_title = cat.get("title", "Huquqiy atama")
    icon = cat.get("icon", "⚖️")
    
    text = (
        f"{icon} <b>{cat_title}</b>\n\n"
        f"📌 <b>Atama:</b> <u>{item['term']}</u>\n\n"
        f"📖 <b>Mazmuni va izohi:</b>\n"
        f"{item['definition']}\n\n"
        f"🏛 <b>Huquqiy asosi / Manba:</b>\n"
        f"<i>{item['source']}</i>\n\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💡 <i>Qidirish uchun shunchaki istalgan huquqiy so'zni yozib yuboring!</i>"
    )
    return text

def format_start_message(user_name: str) -> str:
    return (
        f"Assalomu alaykum, <b>{user_name}</b>!\n\n"
        f"🏛 <b>«{BOT_NAME}»</b> (@{BOT_USERNAME}) — Huquqiy Atamalar Izohli Lugʻati botiga xush kelibsiz!\n\n"
        f"Ushbu bot Oʻzbekiston Respublikasi Konstitutsiyasi, kodekslari, amaldagi qonunlari hamda "
        f"Adliya vazirligining rasmiy <b>«Yuridik ensiklopediya»</b> nashri asosidagi "
        f"<b>50 ta asosiy huquqiy atama</b> va ularning rasmiy izohlarini oʻz ichiga oladi.\n\n"
        f"⚡ <b>Bot imkoniyatlari:</b>\n"
        f"• 🏛 <b>Boʻlimlar menyusi:</b> Sohalar boʻyicha atamalarni qulay saralash;\n"
        f"• 🔍 <b>Tezkor qidiruv:</b> Istalgan soʻzni (masalan: <i>Huquq</i>, <i>Aliment</i>, <i>Oferta</i>) "
        f"toʻgʻridan-toʻgʻri yozsangiz, bot uning toʻliq maʼnosini chiqarib beradi;\n"
        f"• 🎲 <b>Tasodifiy atama:</b> Bilimlarni mustahkamlash uchun tasodifiy tushunchalar;\n"
        f"• 🌐 <b>24/7 Online:</b> Kompyuter oʻchiq boʻlsa ham serverda uzluksiz ishlaydi.\n\n"
        f"Quyidagi tugmalardan birini tanlang yoki qidirayotgan atamangiz nomini yozing 👇"
    )

def format_about_message() -> str:
    return (
        f"ℹ️ <b>«{BOT_NAME}» (@{BOT_USERNAME}) haqida:</b>\n\n"
        f"Mazkur bot yurisprudensiya yoʻnalishidagi 50 ta fundamental huquqiy atamalarning "
        f"aniq va rasmiy tushuntirishlarini oʻrganish uchun maxsus yaratilgan.\n\n"
        f"📚 <b>Atamalar quyidagi 4 ta asosiy sohaga ajratilgan:</b>\n"
        f"1. 🏛 Davlat va huquq nazariyasi hamda Konstitutsiyaviy huquq (15 ta atama)\n"
        f"2. 📑 Fuqarolik, oila va mehnat huquqi (13 ta atama)\n"
        f"3. ⚖️ Jinoyat va maʼmuriy huquq (11 ta atama)\n"
        f"4. 🛡 Protsessual huquq va odil sudlov (11 ta atama)\n\n"
        f"📖 <b>Asosiy huquqiy manbalar:</b>\n"
        f"• Oʻzbekiston Respublikasi Konstitutsiyasi\n"
        f"• Fuqarolik, Mehnat, Oila, Jinoyat va Protsessual kodekslar\n"
        f"• «Yuridik ensiklopediya» (Adliya vazirligi rasmiy nashri)\n\n"
        f"🌐 <b>Uzluksiz 24/7 ishlash:</b> Cloud Server texnologiyasi va Anti-Sleep tizimi orqali taʼminlangan."
    )

def format_search_help() -> str:
    return (
        f"🔍 <b>Qidiruvdan foydalanish boʻyicha qoʻllanma:</b>\n\n"
        f"1. <b>Oddiy qidiruv:</b> Botga shunchaki oʻzingiz qiziqqan soʻzni yozib yuboring.\n"
        f"Masalan:\n"
        f"👉 <code>Huquq</code>\n"
        f"👉 <code>Shartnoma</code>\n"
        f"👉 <code>Aybsizlik prezumpsiyasi</code>\n"
        f"👉 <code>Aliment</code>\n\n"
        f"2. <b>Qisman moslik:</b> Soʻzning bir qismini yozsangiz ham bot uni topadi (masalan: <i>prezump</i>, <i>kolliz</i>, <i>retsidiv</i>).\n\n"
        f"3. <b>Inline qidiruv:</b> Istalgan guruh yoki doʻstingiz bilan yozishayotganda "
        f"<code>@{BOT_USERNAME} so'z</code> deb yozsangiz, toʻgʻridan-toʻgʻri chatda yuridik izohni ulasha olasiz!"
    )

# =============================================================================
# BUYRUQLAR (COMMAND HANDLERS)
# =============================================================================

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.first_name if message.from_user else "Foydalanuvchi"
    await message.answer(
        text=format_start_message(user_name),
        reply_markup=get_main_reply_keyboard(),
        parse_mode="HTML"
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        text=format_search_help(),
        reply_markup=get_main_reply_keyboard(),
        parse_mode="HTML"
    )

@dp.message(Command("random"))
async def cmd_random(message: Message):
    term = random.choice(TERMS)
    text = format_term_card(term)
    await message.answer(
        text=text,
        reply_markup=get_term_details_keyboard(term["id"], "all", 0),
        parse_mode="HTML"
    )

@dp.message(Command("categories"))
async def cmd_categories(message: Message):
    await message.answer(
        text="🏛 <b>Kerakli huquq sohasini tanlang:</b>",
        reply_markup=get_categories_inline_keyboard(),
        parse_mode="HTML"
    )

# =============================================================================
# ASOSIY MENYU TUGMALARI ISHLOVCHILARI (REPLY BUTTONS)
# =============================================================================

@dp.message(F.text == "🏛 Boʻlimlar boʻyicha atamalar")
async def btn_categories(message: Message):
    await message.answer(
        text="🏛 <b>Quyidagi huquq sohalaridan birini tanlang:</b>",
        reply_markup=get_categories_inline_keyboard(),
        parse_mode="HTML"
    )

@dp.message(F.text == "📚 Barcha 50 ta atama")
async def btn_all_terms(message: Message):
    await message.answer(
        text=f"📚 <b>Barcha huquqiy atamalar roʻyxati (Jami: {len(TERMS)} ta):</b>\n\n"
             f"<i>Kerakli atamani tanlash uchun uning ustiga bosing:</i>",
        reply_markup=get_terms_paginated_keyboard(TERMS, "all", 0),
        parse_mode="HTML"
    )

@dp.message(F.text == "🎲 Tasodifiy atama")
async def btn_random(message: Message):
    term = random.choice(TERMS)
    text = format_term_card(term)
    await message.answer(
        text=text,
        reply_markup=get_term_details_keyboard(term["id"], "all", 0),
        parse_mode="HTML"
    )

@dp.message(F.text == "🔍 Qidirish qoʻllanmasi")
async def btn_search_help(message: Message):
    await message.answer(
        text=format_search_help(),
        parse_mode="HTML"
    )

@dp.message(F.text == "ℹ️ Bot haqida va Qoʻllanma")
async def btn_about(message: Message):
    await message.answer(
        text=format_about_message(),
        parse_mode="HTML"
    )

# =============================================================================
# INLINE TUGMALAR ISHLOVCHILARI (CALLBACK QUERIES)
# =============================================================================

@dp.callback_query(F.data == "noop")
async def cb_noop(callback: CallbackQuery):
    await callback.answer()

@dp.callback_query(F.data == "menu_categories")
async def cb_menu_categories(callback: CallbackQuery):
    await callback.message.edit_text(
        text="🏛 <b>Quyidagi huquq sohalaridan birini tanlang:</b>",
        reply_markup=get_categories_inline_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data == "random_term")
async def cb_random_term(callback: CallbackQuery):
    term = random.choice(TERMS)
    text = format_term_card(term)
    await callback.message.edit_text(
        text=text,
        reply_markup=get_term_details_keyboard(term["id"], "all", 0),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("cat:"))
async def cb_show_category(callback: CallbackQuery):
    parts = callback.data.split(":")
    cat_id = parts[1]
    page = int(parts[2]) if len(parts) > 2 else 0
    
    items = get_terms_by_category(cat_id)
    cat_info = CATEGORIES.get(cat_id, {})
    title = cat_info.get("title", "Boʻlim")
    
    await callback.message.edit_text(
        text=f"{cat_info.get('icon', '📌')} <b>{title}</b>\n\n"
             f"<i>Ushbu boʻlimda {len(items)} ta atama mavjud. "
             f"Kerakli atamani tanlang:</i>",
        reply_markup=get_terms_paginated_keyboard(items, cat_id, page),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("all:"))
async def cb_show_all(callback: CallbackQuery):
    parts = callback.data.split(":")
    page = int(parts[1]) if len(parts) > 1 else 0
    
    await callback.message.edit_text(
        text=f"📚 <b>Barcha huquqiy atamalar roʻyxati (Jami: {len(TERMS)} ta):</b>\n\n"
             f"<i>Kerakli atamani tanlash uchun ustiga bosing:</i>",
        reply_markup=get_terms_paginated_keyboard(TERMS, "all", page),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("page:"))
async def cb_pagination(callback: CallbackQuery):
    parts = callback.data.split(":")
    prefix = parts[1]
    page = int(parts[2])
    
    if prefix == "all":
        items = TERMS
        title = f"📚 <b>Barcha huquqiy atamalar roʻyxati (Jami: {len(TERMS)} ta):</b>"
    elif prefix == "search":
        items = TERMS
        title = "🔍 <b>Qidiruv natijalari:</b>"
    else:
        items = get_terms_by_category(prefix)
        cat_info = CATEGORIES.get(prefix, {})
        title = f"{cat_info.get('icon', '📌')} <b>{cat_info.get('title', 'Boʻlim')}</b>"
        
    await callback.message.edit_text(
        text=f"{title}\n\n<i>Kerakli atamani tanlang:</i>",
        reply_markup=get_terms_paginated_keyboard(items, prefix, page),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("term:"))
async def cb_term_details(callback: CallbackQuery):
    parts = callback.data.split(":")
    term_id = int(parts[1])
    prefix = parts[2] if len(parts) > 2 else "all"
    page = int(parts[3]) if len(parts) > 3 else 0
    
    term = get_term_by_id(term_id)
    if not term:
        await callback.answer("Kechirasiz, atama topilmadi!", show_alert=True)
        return
        
    text = format_term_card(term)
    await callback.message.edit_text(
        text=text,
        reply_markup=get_term_details_keyboard(term_id, prefix, page),
        parse_mode="HTML"
    )
    await callback.answer()

# =============================================================================
# QIDIRUV VA FOYDALANUVCHI MATNLARI (TEXT SEARCH HANDLER)
# =============================================================================

@dp.message(F.text)
async def handle_user_text(message: Message):
    query = message.text.strip()
    
    # Qidiruvni amalga oshirish
    results = search_terms(query)
    
    if not results:
        await message.answer(
            text=f"🔍 «<b>{query}</b>» soʻzi boʻyicha hech qanday atama topilmadi.\n\n"
                 f"Iltimos, soʻzning toʻgʻri yozilganligini tekshiring yoki "
                 f"boʻlimlar roʻyxatidan qidiring.",
            reply_markup=get_categories_inline_keyboard(),
            parse_mode="HTML"
        )
        return
        
    # Agar faqat 1 ta aniq natija topilsa, to'g'ridan-to'g'ri izohini chiqaramiz
    if len(results) == 1:
        term = results[0]
        text = format_term_card(term)
        await message.answer(
            text=text,
            reply_markup=get_term_details_keyboard(term["id"], "all", 0),
            parse_mode="HTML"
        )
        return
        
    # Agar bir nechta natija topilsa, tanlash uchun ro'yxat chiqaramiz
    await message.answer(
        text=f"🔍 «<b>{query}</b>» boʻyicha <b>{len(results)} ta</b> mos atama topildi.\n"
             f"<i>Oʻzingizga keraklisini tanlang:</i>",
        reply_markup=get_search_results_keyboard(results),
        parse_mode="HTML"
    )

# =============================================================================
# INLINE REJIM (TELEGRAM INLINE QUERY)
# =============================================================================

@dp.inline_query()
async def inline_search(inline_query: InlineQuery):
    query = inline_query.query.strip()
    if query:
        matches = search_terms(query)[:20]
    else:
        matches = TERMS[:20]
        
    articles = []
    for item in matches:
        card_text = format_term_card(item)
        short_def = item["definition"][:100] + ("..." if len(item["definition"]) > 100 else "")
        articles.append(
            InlineQueryResultArticle(
                id=str(item["id"]),
                title=f"📌 {item['term']}",
                description=short_def,
                input_message_content=InputTextMessageContent(
                    message_text=card_text,
                    parse_mode="HTML"
                )
            )
        )
        
    await inline_query.answer(results=articles, cache_time=10)

# =============================================================================
# ASOSIY ISHGA TUSHIRISH (MAIN WITH KEEP-ALIVE SERVER)
# =============================================================================

async def main():
    if not BOT_TOKEN:
        logger.error("XATOLIK: .env faylida yoki muhit o'zgaruvchilarida BOT_TOKEN topilmadi!")
        print("\n" + "="*60)
        print("XATOLIK: BOT_TOKEN kiritilmagan!")
        print("Iltimos, .env faylini oching va bot tokenni yozing:")
        print("BOT_TOKEN=1234567890:ABCdefGhIJKlmNoPQRsTUVwxyZ")
        print("="*60 + "\n")
        return

    bot = Bot(token=BOT_TOKEN)
    
    # 1. Web serverni (keep-alive) fon rejimida ishga tushirish
    web_app = create_web_app()
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=PORT)
    await site.start()
    logger.info(f"Keep-Alive veb-serveri ishga tushdi: http://0.0.0.0:{PORT}")
    
    # 2. Agar SELF_URL berilgan bo'lsa, Anti-Sleep ping vazifasini ishga tushirish
    ping_task = None
    if SELF_URL:
        logger.info(f"Anti-sleep avto-ping yoqildi: {SELF_URL}")
        ping_task = asyncio.create_task(self_ping_loop(SELF_URL))
    else:
        logger.info("SELF_URL belgilanmagan. Agar Render.com bepul tarifida ishlatsangiz, SELF_URL yoki UptimeRobot sozlash tavsiya etiladi.")
        
    try:
        # Eski kutilayotgan xabarlarni tozalash va pollingni boshlash
        await bot.delete_webhook(drop_pending_updates=True)
        bot_info = await bot.get_me()
        global BOT_USERNAME
        if bot_info.username:
            BOT_USERNAME = bot_info.username
        logger.info(f"Bot muvaffaqiyatli ishga tushdi: @{bot_info.username}")
        print("\n" + "="*60)
        print(f"🚀 Bot ishga tushdi: @{bot_info.username}")
        print(f"🌐 Keep-Alive server porti: {PORT}")
        print(f"📚 Lug'atdagi atamalar soni: {len(TERMS)} ta")
        print("="*60 + "\n")
        
        await dp.start_polling(bot)
    finally:
        if ping_task:
            ping_task.cancel()
        await runner.cleanup()
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi.")
