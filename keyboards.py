from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from dictionary_data import CATEGORIES, TERMS, get_terms_by_category
import math

ITEMS_PER_PAGE = 5

def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """Asosiy pastki doimiy tugmalar menyusi"""
    keyboard = [
        [
            KeyboardButton(text="🏛 Boʻlimlar boʻyicha atamalar"),
            KeyboardButton(text="📚 Barcha 50 ta atama")
        ],
        [
            KeyboardButton(text="🎲 Tasodifiy atama"),
            KeyboardButton(text="🔍 Qidirish qoʻllanmasi")
        ],
        [
            KeyboardButton(text="ℹ️ Bot haqida va Qoʻllanma")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_categories_inline_keyboard() -> InlineKeyboardMarkup:
    """Bo'limlarni tanlash inline menyusi"""
    buttons = []
    for cat_id, cat in CATEGORIES.items():
        count = len(get_terms_by_category(cat_id))
        btn_text = f"{cat['short_title']} ({count} ta)"
        buttons.append([InlineKeyboardButton(text=btn_text, callback_data=f"cat:{cat_id}:0")])
    
    buttons.append([InlineKeyboardButton(text="📚 Barcha atamalar (1-50)", callback_data="all:0")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_terms_paginated_keyboard(items_list: list, prefix: str, page: int = 0) -> InlineKeyboardMarkup:
    """Atamalar ro'yxatini sahifalab (pagination) chiqaruvchi klaviatura"""
    total_items = len(items_list)
    total_pages = max(1, math.ceil(total_items / ITEMS_PER_PAGE))
    page = max(0, min(page, total_pages - 1))
    
    start_idx = page * ITEMS_PER_PAGE
    end_idx = min(start_idx + ITEMS_PER_PAGE, total_items)
    
    buttons = []
    # Sahifadagi atama tugmalari
    for item in items_list[start_idx:end_idx]:
        term_text = f"{item['id']}. {item['term']}"
        buttons.append([InlineKeyboardButton(text=term_text, callback_data=f"term:{item['id']}:{prefix}:{page}")])
        
    # Navigatsiya qatori
    nav_row = []
    if page > 0:
        nav_row.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"page:{prefix}:{page - 1}"))
    else:
        nav_row.append(InlineKeyboardButton(text="⏺ 1-sahifa", callback_data="noop"))
        
    nav_row.append(InlineKeyboardButton(text=f"{page + 1}/{total_pages}", callback_data="noop"))
    
    if page < total_pages - 1:
        nav_row.append(InlineKeyboardButton(text="Keyingi ➡️", callback_data=f"page:{prefix}:{page + 1}"))
    else:
        nav_row.append(InlineKeyboardButton(text="⏺ Oxirgi", callback_data="noop"))
        
    buttons.append(nav_row)
    
    # Orqaga qaytish tugmasi
    buttons.append([
        InlineKeyboardButton(text="🏛 Boʻlimlarga qaytish", callback_data="menu_categories")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_term_details_keyboard(term_id: int, back_prefix: str = "all", back_page: int = 0) -> InlineKeyboardMarkup:
    """Atama izohi ostidagi boshqaruv tugmalari"""
    buttons = [
        [
            InlineKeyboardButton(text="🎲 Boshqa tasodifiy atama", callback_data="random_term"),
            InlineKeyboardButton(text="📤 Ulashish", switch_inline_query=f"{term_id}")
        ],
        [
            InlineKeyboardButton(text="🔙 Roʻyxatga qaytish", callback_data=f"page:{back_prefix}:{back_page}"),
            InlineKeyboardButton(text="🏛 Boʻlimlar", callback_data="menu_categories")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_search_results_keyboard(results: list) -> InlineKeyboardMarkup:
    """Qidiruv natijalarini ko'rsatuvchi inline klaviatura"""
    buttons = []
    # Maksimal dastlabki 8 ta eng yaqin natija
    for item in results[:8]:
        buttons.append([
            InlineKeyboardButton(
                text=f"📌 {item['term']}",
                callback_data=f"term:{item['id']}:search:0"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text="🏛 Boʻlimlar boʻyicha koʻrish", callback_data="menu_categories")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
