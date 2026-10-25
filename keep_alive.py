import asyncio
import os
import logging
from aiohttp import web, ClientSession
from datetime import datetime

logger = logging.getLogger(__name__)

START_TIME = datetime.utcnow()

async def handle_home(request):
    uptime_seconds = int((datetime.utcnow() - START_TIME).total_seconds())
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{hours}h {minutes}m {seconds}s"
    
    html_content = f"""<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHAROFOVA'S WORD | 24/7 Online</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }}
        .card {{
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 35px;
            border-radius: 16px;
            max-width: 520px;
            width: 100%;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
            text-align: center;
        }}
        .badge {{
            display: inline-block;
            background: #10b981;
            color: #ffffff;
            font-size: 13px;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 9999px;
            margin-bottom: 16px;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
        }}
        h1 {{
            font-size: 24px;
            margin: 0 0 10px 0;
            color: #ffffff;
        }}
        p {{
            color: #94a3b8;
            font-size: 15px;
            line-height: 1.6;
            margin: 8px 0;
        }}
        .stat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 25px 0;
        }}
        .stat-box {{
            background: rgba(15, 23, 42, 0.6);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .stat-num {{
            font-size: 22px;
            font-weight: bold;
            color: #38bdf8;
        }}
        .stat-label {{
            font-size: 12px;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 4px;
        }}
        .footer {{
            font-size: 12px;
            color: #64748b;
            margin-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 15px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">● TIZIM FAOL (ONLINE)</div>
        <h1>SHAROFOVA'S WORD</h1>
        <p style="color: #38bdf8; font-weight: 500;">@lugaviy_word_uz_bot</p>
        <p>O'zbekiston Respublikasi Konstitutsiyasi va qonunchiligi asosidagi 50 ta asosiy huquqiy atamalar izohli lug'ati.</p>
        
        <div class="stat-grid">
            <div class="stat-box">
                <div class="stat-num">50 ta</div>
                <div class="stat-label">Huquqiy atamalar</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{uptime_str}</div>
                <div class="stat-label">Ishlash vaqti (Uptime)</div>
            </div>
        </div>
        
        <p style="font-size: 13px; color: #10b981;">
            ⚡ Server uxlab qolmaslik (Anti-Sleep) himoyasi yoqilgan.
        </p>
        <div class="footer">
            24/7 Uzluksiz rejim | Cloud Server Ready
        </div>
    </div>
</body>
</html>"""
    return web.Response(text=html_content, content_type="text/html")

async def handle_health(request):
    return web.json_response({
        "status": "ok",
        "service": "huquqiy_lugat_bot",
        "timestamp": datetime.utcnow().isoformat(),
        "terms_count": 50
    })

async def self_ping_loop(target_url: str):
    """
    Bot serveri uxlab qolmasligi uchun (Anti-Sleep) o'z-o'ziga davriy so'rov yuborish.
    Masalan Render.com bepul versiyasi 15 daqiqa faoliyatsizlikdan keyin uxlab qoladi.
    Ushbu tsikl har 9 daqiqada (540 soniya) o'ziga GET so'rov yuborib serverni uyg'oq ushlab turadi.
    """
    logger.info(f"Self-ping xizmati ishga tushdi. Maqsad: {target_url}")
    # Dastlabki 60 soniya kutish (server to'liq ishga tushishi uchun)
    await asyncio.sleep(60)
    
    while True:
        try:
            async with ClientSession() as session:
                url = target_url.rstrip("/") + "/health"
                async with session.get(url, timeout=15) as resp:
                    if resp.status == 200:
                        logger.info(f"Anti-Sleep ping muvaffaqiyatli: {url} (Status: 200)")
                    else:
                        logger.warning(f"Anti-Sleep ping javobi: {resp.status}")
        except Exception as e:
            logger.warning(f"Anti-Sleep ping xatosi (keyingi tsiklda takrorlanadi): {e}")
            
        # Har 9 daqiqada bir marta (540 soniya)
        await asyncio.sleep(540)

def create_web_app():
    app = web.Application()
    app.router.add_get("/", handle_home)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/ping", handle_health)
    return app
