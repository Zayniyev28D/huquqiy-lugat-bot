"""
O'zbekiston Respublikasi Huquqiy Atamalari Izohli Lug'ati
50 ta asosiy huquqiy atama va ularning rasmiy izohlari.
Manbalar:
- O'zbekiston Respublikasi Konstitutsiyasi
- Fuqarolik kodeksi
- Jinoyat kodeksi
- Jinoyat-protsessual kodeksi
- Mehnat kodeksi
- Oila kodeksi
- Ma'muriy javobgarlik to'g'risidagi kodeks
- Fuqarolik protsessual kodeksi
- Amaldagi qonunlar hamda «Yuridik ensiklopediya» (Adliya vazirligi rasmiy nashri)
"""

CATEGORIES = {
    "cat_1": {
        "title": "Davlat va huquq nazariyasi hamda Konstitutsiyaviy huquq",
        "short_title": "🏛 Davlat va Konstitutsiyaviy huquq",
        "icon": "🏛",
        "desc": "Davlat tuzilishi, suverenitet, qonunchilik tizimi va asosiy tamoyillar"
    },
    "cat_2": {
        "title": "Fuqarolik, oila va mehnat huquqi",
        "short_title": "📑 Fuqarolik, oila va mehnat",
        "icon": "📑",
        "desc": "Mulk, shartnomalar, oilaviy munosabatlar va mehnat huquqlari"
    },
    "cat_3": {
        "title": "Jinoyat va maʼmuriy huquq",
        "short_title": "⚖️ Jinoyat va maʼmuriy huquq",
        "icon": "⚖️",
        "desc": "Huquqbuzarliklar, jinoyat tarkibi, jazolar va javobgarlik"
    },
    "cat_4": {
        "title": "Protsessual huquq va odil sudlov",
        "short_title": "🛡 Protsessual huquq va odil sudlov",
        "icon": "🛡",
        "desc": "Sud jarayoni, isbotlash, shikoyat qilish va protsessual kafolatlar"
    }
}

TERMS = [
    # =========================================================================
    # I. Davlat va huquq nazariyasi hamda Konstitutsiyaviy huquq (15 ta)
    # =========================================================================
    {
        "id": 1,
        "term": "Huquq",
        "category_id": "cat_1",
        "definition": (
            "Davlat tomonidan oʻrnatiladigan yoki maʼqullanadigan, umumiy majburiy "
            "xulq-atvor qoidalari (normalari) tizimi boʻlib, ularning bajarilishi "
            "davlatning majburlov kuchi bilan taʼminlanadi."
        ),
        "source": "Davlat va huquq nazariyasi, Yuridik ensiklopediya"
    },
    {
        "id": 2,
        "term": "Konstitutsiya",
        "category_id": "cat_1",
        "definition": (
            "Davlatning Asosiy qonuni boʻlib, inson va fuqarolarning huquq va erkinliklarini, "
            "jamiyat va davlat tuzilishining asoslarini, davlat hokimiyati organlari tizimini "
            "belgilab beruvchi oliy yuridik kuchga ega hujjat."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasi"
    },
    {
        "id": 3,
        "term": "Normativ-huquqiy hujjat",
        "category_id": "cat_1",
        "definition": (
            "Qonunchilik hujjatlariga muvofiq qabul qilingan, umumiy majburiy davlat koʻrsatmalari "
            "sifatida huquqiy normalarni belgilashga, oʻzgartirishga yoki bekor qilishga qaratilgan rasmiy hujjat."
        ),
        "source": "«Normativ-huquqiy hujjatlar toʻgʻrisida»gi Qonun"
    },
    {
        "id": 4,
        "term": "Qonun",
        "category_id": "cat_1",
        "definition": (
            "Oʻzbekiston Respublikasi Oliy Majlisi tomonidan yoki referendum yoʻli bilan qabul qilinadigan, "
            "ijtimoiy munosabatlarning eng muhim masalalarini tartibga soluvchi oliy yuridik kuchga ega normativ-huquqiy hujjat."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasi"
    },
    {
        "id": 5,
        "term": "Qonunosti hujjatlari",
        "category_id": "cat_1",
        "definition": (
            "Qonunlar asosida va ularni ijro etish uchun vakolatli davlat organlari (Prezident, Vazirlar Mahkamasi, "
            "vazirliklar, mahalliy hokimiyat organlari) tomonidan qabul qilinadigan normativ-huquqiy hujjatlar "
            "(farmonlar, qarorlar, buyruqlar)."
        ),
        "source": "Yuridik ensiklopediya"
    },
    {
        "id": 6,
        "term": "Kodeks",
        "category_id": "cat_1",
        "definition": (
            "Ijtimoiy munosabatlarning muayyan bir sohasini yagona tizimga solingan va kompleks tarzda "
            "tartibga soluvchi qonun hujjati."
        ),
        "source": "Qonunchilik texnikasi qoidalari"
    },
    {
        "id": 7,
        "term": "Suverenitet (Davlat suvereniteti)",
        "category_id": "cat_1",
        "definition": (
            "Davlat hokimiyatining mamlakat ichida ustuvorligi va tashqi munosabatlarda toʻla mustaqilligi."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasi"
    },
    {
        "id": 8,
        "term": "Hokimiyatlar boʻlinishi prinsipi",
        "category_id": "cat_1",
        "definition": (
            "Davlat hokimiyatining qonun chiqaruvchi, ijro etuvchi va sud hokimiyatiga boʻlinishi "
            "hamda ularning oʻzaro tiyib turish va manfaatlar muvozanati asosida faoliyat yuritishi."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasining 11-moddasi"
    },
    {
        "id": 9,
        "term": "Referendum",
        "category_id": "cat_1",
        "definition": (
            "Davlat va jamiyat hayotining eng muhim masalalari boʻyicha qonunlar va boshqa qarorlarni "
            "qabul qilish maqsadida oʻtkaziladigan umumxalq ovoz berishi."
        ),
        "source": "«Oʻzbekiston Respublikasining referendumi toʻgʻrisida»gi Qonun"
    },
    {
        "id": 10,
        "term": "Huquqiy munosabat",
        "category_id": "cat_1",
        "definition": (
            "Huquq normalari bilan tartibga solingan, ishtirokchilari oʻzaro subyektiv huquq va "
            "yuridik majburiyatlarga ega boʻlgan ijtimoiy munosabat."
        ),
        "source": "Davlat va huquq nazariyasi"
    },
    {
        "id": 11,
        "term": "Huquq layoqati",
        "category_id": "cat_1",
        "definition": (
            "Shaxsning fuqarolik huquq va burchlariga ega boʻlish qobiliyati. "
            "U inson tugʻilgan paytdan eʼtiboran vujudga keladi va vafot etishi bilan tugaydi."
        ),
        "source": "Fuqarolik kodeksi, 17-modda"
    },
    {
        "id": 12,
        "term": "Muomala layoqati",
        "category_id": "cat_1",
        "definition": (
            "Fuqaroning oʻz harakatlari bilan huquqlarga ega boʻlish va ularni amalga oshirish, "
            "oʻzi uchun burchlar vujudga keltirish va ularni bajarish qobiliyati. "
            "Toʻliq muomala layoqati 18 yoshga toʻlganda vujudga keladi."
        ),
        "source": "Fuqarolik kodeksi, 22-modda"
    },
    {
        "id": 13,
        "term": "Huquqbuzarlik",
        "category_id": "cat_1",
        "definition": (
            "Muomala layoqatiga ega boʻlgan subyekt tomonidan sodir etilgan, huquq normalariga zid boʻlgan, "
            "jamiyatga zarar yetkazuvchi aybli qilmish (harakat yoki harakatsizlik)."
        ),
        "source": "Davlat va huquq nazariyasi"
    },
    {
        "id": 14,
        "term": "Yuridik javobgarlik",
        "category_id": "cat_1",
        "definition": (
            "Huquqbuzarlik sodir etgan shaxsga nisbatan qonunda nazarda tutilgan davlat majburlov choralarining "
            "qoʻllanilishi (intizomiy, moddiy, maʼmuriy, fuqarolik-huquqiy va jinoiy javobgarlik turlari mavjud)."
        ),
        "source": "Yuridik ensiklopediya"
    },
    {
        "id": 15,
        "term": "Kolliziya (Huquqiy kolliziya)",
        "category_id": "cat_1",
        "definition": (
            "Bir xil masalani tartibga soluvchi ikki yoki undan ortiq normativ-huquqiy hujjatlar oʻrtasidagi "
            "qarama-qarshilik yoki nomuvofiqlik."
        ),
        "source": "Davlat va huquq nazariyasi"
    },

    # =========================================================================
    # II. Fuqarolik, oila va mehnat huquqi (13 ta)
    # =========================================================================
    {
        "id": 16,
        "term": "Jismoniy shaxs",
        "category_id": "cat_2",
        "definition": (
            "Huquqiy munosabatlar ishtirokchisi boʻlgan Oʻzbekiston Respublikasi fuqarolari, "
            "chet el fuqarolari hamda fuqaroligi boʻlmagan shaxslar."
        ),
        "source": "Fuqarolik kodeksi, 16-modda"
    },
    {
        "id": 17,
        "term": "Yuridik shaxs",
        "category_id": "cat_2",
        "definition": (
            "Oʻz mulkida, xoʻjalik yuritishida yoki operativ boshqaruvida alohida mol-mulkka ega boʻlgan, "
            "oʻz majburiyatlari yuzasidan ushbu mol-mulk bilan javob beradigan, oʻz nomidan huquqlarga "
            "ega boʻla oladigan hamda sudda daʼvogar va javobgar boʻla oladigan tashkilot."
        ),
        "source": "Fuqarolik kodeksi, 39-modda"
    },
    {
        "id": 18,
        "term": "Bitim",
        "category_id": "cat_2",
        "definition": (
            "Fuqarolar va yuridik shaxslarning fuqarolik huquq va burchlarini belgilash, "
            "oʻzgartirish yoki bekor qilishga qaratilgan harakatlari."
        ),
        "source": "Fuqarolik kodeksi, 101-modda"
    },
    {
        "id": 19,
        "term": "Shartnoma",
        "category_id": "cat_2",
        "definition": (
            "Ikki yoki bir necha shaxsning fuqarolik huquqlari va burchlarini vujudga keltirish, "
            "oʻzgartirish yoki bekor qilish haqidagi kelishuvi."
        ),
        "source": "Fuqarolik kodeksi, 353-modda"
    },
    {
        "id": 20,
        "term": "Oferta",
        "category_id": "cat_2",
        "definition": (
            "Bir yoki bir necha muayyan shaxsga yuborilgan, shartnoma tuzish haqidagi yetarli darajada "
            "aniq ifodalangan va taklif kiritgan shaxsning oʻzini shartnoma tuzgan deb hisoblash xohishini bildiradigan taklif."
        ),
        "source": "Fuqarolik kodeksi, 367-modda"
    },
    {
        "id": 21,
        "term": "Aksept",
        "category_id": "cat_2",
        "definition": (
            "Oferta yuborilgan shaxsning uni qabul qilganligi haqidagi toʻliq va pisandasiz javobi."
        ),
        "source": "Fuqarolik kodeksi, 370-modda"
    },
    {
        "id": 22,
        "term": "Mulk huquqi",
        "category_id": "cat_2",
        "definition": (
            "Shaxsning oʻziga qarashli mol-mulkka oʻz xohishi bilan va oʻz manfaatlarini koʻzlab "
            "egalik qilish, undan foydalanish va uni tasarruf etish huquqi."
        ),
        "source": "Fuqarolik kodeksi, 164-modda"
    },
    {
        "id": 23,
        "term": "Majburiyat",
        "category_id": "cat_2",
        "definition": (
            "Fuqarolik-huquqiy munosabat boʻlib, unga asosan bir shaxs (qarzdor) boshqa shaxs (kreditor) "
            "foydasiga muayyan harakatni amalga oshirishi yoki muayyan harakatdan oʻzini tiyishi shart, "
            "kreditor esa qarzdordan oʻzining majburiyatini bajarishni talab qilish huquqiga ega."
        ),
        "source": "Fuqarolik kodeksi, 234-modda"
    },
    {
        "id": 24,
        "term": "Ishonchnoma",
        "category_id": "cat_2",
        "definition": (
            "Bir shaxs (ishonch bildiruvchi) tomonidan ikkinchi shaxsga (ishonchli vakilga) "
            "uchinchi shaxslar oldida vakillik qilish uchun berilgan yozma vakolat."
        ),
        "source": "Fuqarolik kodeksi, 134-modda"
    },
    {
        "id": 25,
        "term": "Daʼvo muddati",
        "category_id": "cat_2",
        "definition": (
            "Shaxs oʻzining buzilgan huquqini daʼvo qoʻzgʻatish yoʻli bilan himoya qilishi mumkin boʻlgan muddat. "
            "Umumiy daʼvo muddati — 3 yil."
        ),
        "source": "Fuqarolik kodeksi, 149-150-moddalar"
    },
    {
        "id": 26,
        "term": "Vasiyatnoma",
        "category_id": "cat_2",
        "definition": (
            "Fuqaroning oʻziga tegishli mol-mulkni yoki bu mol-mulkka nisbatan huquqini "
            "vafot etgan taqdirda tasarruf etish xususidagi xohish-irodasining qonunda belgilangan shaklda ifodalanishi."
        ),
        "source": "Fuqarolik kodeksi, 1120-modda"
    },
    {
        "id": 27,
        "term": "Mehnat shartnomasi",
        "category_id": "cat_2",
        "definition": (
            "Xodim bilan ish beruvchi oʻrtasida muayyan mutaxassislik, malaka, lavozim boʻyicha "
            "ishni ichki mehnat tartibiga boʻysungan holda haq evaziga bajarish haqidagi kelishuv."
        ),
        "source": "Mehnat kodeksi, 103-modda"
    },
    {
        "id": 28,
        "term": "Aliment",
        "category_id": "cat_2",
        "definition": (
            "Qonunda belgilangan hollarda oilaning bir aʼzosi boshqa muhtoj va mehnatga layoqatsiz "
            "oila aʼzosiga (masalan, ota-onaning voyaga yetmagan farzandlariga) taʼminot sifatida toʻlashi shart boʻlgan mablagʻ."
        ),
        "source": "Oila kodeksi"
    },

    # =========================================================================
    # III. Jinoyat va maʼmuriy huquq (11 ta)
    # =========================================================================
    {
        "id": 29,
        "term": "Jinoyat",
        "category_id": "cat_3",
        "definition": (
            "Jinoyat kodeksi bilan taqiqlangan, aybli ijtimoiy xavfli qilmish (harakat yoki harakatsizlik) boʻlib, "
            "jazo qoʻllash tahdidi bilan sodir etilishi man etilgan xatti-harakat."
        ),
        "source": "Jinoyat kodeksi, 14-modda"
    },
    {
        "id": 30,
        "term": "Jinoyat tarkibi",
        "category_id": "cat_3",
        "definition": (
            "Qilmishni jinoyat deb topish uchun zarur boʻlgan, Jinoyat kodeksida nazarda tutilgan "
            "obyektiv va subyektiv belgilar yigʻindisi (jinoyat obyekti, obyektiv tomoni, subyekti va subyektiv tomoni)."
        ),
        "source": "Jinoyat huquqi nazariyasi"
    },
    {
        "id": 31,
        "term": "Ayb",
        "category_id": "cat_3",
        "definition": (
            "Shaxsning oʻzi sodir etgan ijtimoiy xavfli qilmishga va uning oqibatlariga nisbatan "
            "qasddan yoki ehtiyotsizlik shaklidagi ruhiy munosabati."
        ),
        "source": "Jinoyat kodeksi, 20-modda"
    },
    {
        "id": 32,
        "term": "Qasd (Toʻgʻri va egri qasd)",
        "category_id": "cat_3",
        "definition": (
            "Shaxs oʻz qilmishining ijtimoiy xavfli xususiyatini anglagan, uning oqibatlariga koʻzi yetgan "
            "va shu oqibatlar kelib chiqishini istagan (toʻgʻri qasd) yoki bunga ongli ravishda yoʻl qoʻygan "
            "(egri qasd) holda jinoyat sodir etishi."
        ),
        "source": "Jinoyat kodeksi, 21-modda"
    },
    {
        "id": 33,
        "term": "Ehtiyotsizlik",
        "category_id": "cat_3",
        "definition": (
            "Oʻz-oʻziga ishonish (oqibatlarning oldini olishga asossiz umid bogʻlash) yoki "
            "beparvolik (oqibatlarga koʻzi yetishi lozim va mumkin boʻlgan holda buni anglamaslik) "
            "oqibatida jinoyat sodir etish."
        ),
        "source": "Jinoyat kodeksi, 22-modda"
    },
    {
        "id": 34,
        "term": "Zaruriy mudofaa",
        "category_id": "cat_3",
        "definition": (
            "Shaxsning oʻzini yoki boshqa fuqarolarni, jamiyat va davlat manfaatlarini gʻayriqonuniy "
            "tajovuzdan tajovuz qiluvchiga zarar yetkazish yoʻli bilan himoya qilishi. "
            "Mudofaa chegarasidan chetga chiqilmagan boʻlsa, qilmish jinoyat hisoblanmaydi."
        ),
        "source": "Jinoyat kodeksi, 37-modda"
    },
    {
        "id": 35,
        "term": "Jazo",
        "category_id": "cat_3",
        "definition": (
            "Davlat nomidan sud hukmi bilan jinoyat sodir etishda aybli deb topilgan shaxsga nisbatan "
            "qoʻllaniladigan va uni muayyan huquq hamda erkinliklardan mahrum qilish yoki ularni cheklashdan iborat majburlov chorasi."
        ),
        "source": "Jinoyat kodeksi, 42-modda"
    },
    {
        "id": 36,
        "term": "Retsidiv jinoyat",
        "category_id": "cat_3",
        "definition": (
            "Ilgari qasddan sodir etgan jinoyati uchun sudlangan shaxs tomonidan yangidan qasddan jinoyat sodir etilishi."
        ),
        "source": "Jinoyat kodeksi, 34-modda"
    },
    {
        "id": 37,
        "term": "Amnistiya",
        "category_id": "cat_3",
        "definition": (
            "Oliy Majlis Senati tomonidan qabul qilinadigan, muayyan toifadagi jinoyat sodir etgan "
            "shaxslarni jinoiy javobgarlikdan yoki jazodan ozod qilish yoxud jazoni yengillashtirish toʻgʻrisidagi insonparvarlik akti."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasining 95-moddasi"
    },
    {
        "id": 38,
        "term": "Afv etish",
        "category_id": "cat_3",
        "definition": (
            "Oʻzbekiston Respublikasi Prezidenti tomonidan muayyan mahkumga (aniq bir shaxsga) nisbatan qoʻllaniladigan, "
            "uni jazodan toʻliq yoki qisman ozod qilish yoxud tayinlangan jazoni yengilrogʻi bilan almashtirish akti."
        ),
        "source": "Oʻzbekiston Respublikasi Konstitutsiyasining 109-moddasi"
    },
    {
        "id": 39,
        "term": "Maʼmuriy huquqbuzarlik",
        "category_id": "cat_3",
        "definition": (
            "Qonunchilikka binoan maʼmuriy javobgarlikka tortish nazarda tutilgan, shaxsga, "
            "fuqarolarning huquq va erkinliklariga, mulkchilikka, davlat va jamoat tartibiga tajovuz qiluvchi "
            "gʻayrihuquqiy, aybli harakat yoki harakatsizlik."
        ),
        "source": "Maʼmuriy javobgarlik toʻgʻrisidagi kodeks, 10-modda"
    },

    # =========================================================================
    # IV. Protsessual huquq va odil sudlov (11 ta)
    # =========================================================================
    {
        "id": 40,
        "term": "Aybsizlik prezumpsiyasi",
        "category_id": "cat_4",
        "definition": (
            "Jinoyat sodir etganlikda ayblanayotgan har bir shaxsning ishi sudda qonuniy tartibda, "
            "oshkora koʻrib chiqilib, uning aybi aniqlanmaguncha va sudning qonuniy kuchga kirgan "
            "hukmi bilan tasdiqlanmaguncha u aybsiz hisoblanishi haqidagi konstitutsiyaviy prinsip."
        ),
        "source": "Konstitutsiyaning 28-moddasi; JPKning 23-moddasi"
    },
    {
        "id": 41,
        "term": "Daʼvo (Daʼvo arizasi)",
        "category_id": "cat_4",
        "definition": (
            "Manfaatdor shaxsning (daʼvogarning) oʻz buzilgan yoki nizolashilayotgan huquqi "
            "yoxud qonun bilan qoʻriqlanadigan manfaatini himoya qilish toʻgʻrisida sudga qilgan yozma murojaati."
        ),
        "source": "Fuqarolik protsessual kodeksi"
    },
    {
        "id": 42,
        "term": "Dalillar",
        "category_id": "cat_4",
        "definition": (
            "Sud, prokuror, tergovchi va surishtiruvchi qonunda belgilangan tartibda ish uchun "
            "ahamiyatli boʻlgan holatlar mavjud yoki mavjud emasligini aniqlaydigan har qanday haqiqiy maʼlumotlar."
        ),
        "source": "Jinoyat-protsessual kodeksi, 81-modda"
    },
    {
        "id": 43,
        "term": "Ehtiyot choralari",
        "category_id": "cat_4",
        "definition": (
            "Ayblanuvchi yoki sudlanuvchining surishtiruv, dastlabki tergov va suddan boʻyin tovlashining oldini olish, "
            "uning jinoiy faoliyatini toʻxtatish maqsadida qoʻllaniladigan protsessual majburlov choralari "
            "(masalan, qamoqqa olish, uy qamogʻi, garov, munosib xulq-atvorda boʻlish haqida tilxat)."
        ),
        "source": "Jinoyat-protsessual kodeksi, 236-modda"
    },
    {
        "id": 44,
        "term": "Gumon qilinuvchi",
        "category_id": "cat_4",
        "definition": (
            "Jinoyat sodir etganlikda gumon qilinayotganligi toʻgʻrisida maʼlumotlar mavjud boʻlib, "
            "ayblanuvchi tariqasida ishda ishtirok etishga jalb qilish uchun yetarli asoslar boʻlmagan taqdirda, "
            "ushbu maqomda eʼtirof etilgan shaxs."
        ),
        "source": "Jinoyat-protsessual kodeksi, 47-modda"
    },
    {
        "id": 45,
        "term": "Ayblanuvchi",
        "category_id": "cat_4",
        "definition": (
            "Qonunda belgilangan tartibda ayblov eʼlon qilish haqida qaror chiqarilgan shaxs. "
            "Ish sudga oshirilgandan soʻng u sudlanuvchi, hukm chiqarilgandan keyin esa mahkum (yoki oqlangan shaxs) deb ataladi."
        ),
        "source": "Jinoyat-protsessual kodeksi, 45-modda"
    },
    {
        "id": 46,
        "term": "Jabrlanuvchi",
        "category_id": "cat_4",
        "definition": (
            "Jinoyat (yoki maʼmuriy huquqbuzarlik) oqibatida maʼnaviy, jismoniy yoki mulkiy zarar yetkazilgan shaxs."
        ),
        "source": "Jinoyat-protsessual kodeksi, 54-modda"
    },
    {
        "id": 47,
        "term": "Sanksiya",
        "category_id": "cat_4",
        "definition": (
            "1) Huquq normasining qoidani buzganlik uchun javobgarlik chorasini belgilovchi tarkibiy qismi;\n"
            "2) Prokuror yoki sud tomonidan shaxsning huquqlarini cheklovchi protsessual harakatlarni "
            "(masalan, tintuv, telefon soʻzlashuvlarini eshitish) oʻtkazishga beriladigan ruxsat."
        ),
        "source": "Jinoyat-protsessual kodeksi, Davlat va huquq nazariyasi"
    },
    {
        "id": 48,
        "term": "Apellyatsiya",
        "category_id": "cat_4",
        "definition": (
            "Birinchi instansiya sudining hali qonuniy kuchga kirmagan hal qiluv qarori yoki hukmidan "
            "norozi boʻlgan taraflarning yuqori turuvchi sudga ishni qayta koʻrib chiqish haqida beradigan shikoyati (protesti)."
        ),
        "source": "Protsessual qonunchilik"
    },
    {
        "id": 49,
        "term": "Kassatsiya",
        "category_id": "cat_4",
        "definition": (
            "Birinchi instansiya sudining qonuniy kuchga kirgan hal qiluv qarori, hukmi yoki ajrimining "
            "qonuniyligi va asosliligini yuqori instansiya sudi tomonidan tekshirish tartibi."
        ),
        "source": "Protsessual qonunchilik"
    },
    {
        "id": 50,
        "term": "Yurisdiksiya",
        "category_id": "cat_4",
        "definition": (
            "Tegishli davlat organlari va sudlarning huquqiy nizolarni hal qilish, "
            "huquqbuzarliklar toʻgʻrisidagi ishlarni koʻrib chiqish va huquqiy baho berish boʻyicha "
            "qonunda belgilangan vakolatlari doirasi (taalluqliligi)."
        ),
        "source": "Yuridik ensiklopediya"
    }
]

def normalize_text(text: str) -> str:
    """Qidiruv uchun matnni harflar va belgilardan tozalash va kichraytirish"""
    t = text.lower()
    t = t.replace("ʻ", "'").replace("ʼ", "'").replace("`", "'").replace("'", "")
    t = t.replace("g‘", "g").replace("o‘", "o").replace("sh", "s").replace("ch", "c")
    return t.strip()

def search_terms(query: str):
    """Qidiruv so'ziga mos keluvchi atamalarni topish"""
    q_norm = normalize_text(query)
    if not q_norm:
        return []
    
    results = []
    for item in TERMS:
        term_norm = normalize_text(item["term"])
        def_norm = normalize_text(item["definition"])
        
        # 1. Aniq mos kelish (eng yuqori ball)
        if q_norm == term_norm:
            results.append((100, item))
        # 2. Atama nomi shu so'z bilan boshlansa
        elif term_norm.startswith(q_norm):
            results.append((80, item))
        # 3. Atama nomi ichida qidiruv so'zi bo'lsa
        elif q_norm in term_norm:
            results.append((60, item))
        # 4. Izoh ichida so'z uchrasa
        elif q_norm in def_norm:
            results.append((30, item))
            
    # Ball bo'yicha saralash
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results]

def get_term_by_id(term_id: int):
    """ID bo'yicha atamani olish"""
    for item in TERMS:
        if item["id"] == term_id:
            return item
    return None

def get_terms_by_category(category_id: str):
    """Bo'lim ID bo'yicha atamalar ro'yxatini olish"""
    return [t for t in TERMS if t["category_id"] == category_id]
