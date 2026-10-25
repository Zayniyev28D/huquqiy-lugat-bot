"""
Huquqiy Lug'at Boti testlari
"""
import unittest
from dictionary_data import (
    TERMS,
    CATEGORIES,
    search_terms,
    get_term_by_id,
    get_terms_by_category
)

class TestDictionary(unittest.TestCase):
    def test_term_count(self):
        """Jami 50 ta atama mavjudligini tekshirish"""
        self.assertEqual(len(TERMS), 50, f"Atamalar soni 50 ta bo'lishi kerak, lekin {len(TERMS)} ta topildi.")

    def test_unique_ids(self):
        """Har bir atamaning ID raqami unikal bo'lishi kerak"""
        ids = [t["id"] for t in TERMS]
        self.assertEqual(len(ids), len(set(ids)), "ID raqamlarda takrorlanish mavjud!")
        self.assertEqual(set(ids), set(range(1, 51)), "ID lar 1 dan 50 gacha ketma-ket bo'lishi kerak.")

    def test_categories(self):
        """Barcha 4 ta kategoriya to'g'ri bog'langanligini tekshirish"""
        cat_ids = set(CATEGORIES.keys())
        self.assertEqual(cat_ids, {"cat_1", "cat_2", "cat_3", "cat_4"})
        
        c1 = get_terms_by_category("cat_1")
        c2 = get_terms_by_category("cat_2")
        c3 = get_terms_by_category("cat_3")
        c4 = get_terms_by_category("cat_4")
        
        self.assertEqual(len(c1), 15, f"1-bo'limda 15 ta bo'lishi kerak, {len(c1)} ta chiqdi.")
        self.assertEqual(len(c2), 13, f"2-bo'limda 13 ta bo'lishi kerak, {len(c2)} ta chiqdi.")
        self.assertEqual(len(c3), 11, f"3-bo'limda 11 ta bo'lishi kerak, {len(c3)} ta chiqdi.")
        self.assertEqual(len(c4), 11, f"4-bo'limda 11 ta bo'lishi kerak, {len(c4)} ta chiqdi.")
        self.assertEqual(len(c1) + len(c2) + len(c3) + len(c4), 50)

    def test_required_fields(self):
        """Har bir atama maydonlari to'liqligini tekshirish"""
        for t in TERMS:
            self.assertTrue(t["term"].strip(), f"Atama nomi bo'sh: ID {t['id']}")
            self.assertTrue(t["definition"].strip(), f"Izoh bo'sh: ID {t['id']}")
            self.assertTrue(t["source"].strip(), f"Manba bo'sh: ID {t['id']}")
            self.assertIn(t["category_id"], CATEGORIES)

    def test_search_exact_and_fuzzy(self):
        """Qidiruv funksiyasini turli so'zlar bilan sinash"""
        # Aniq so'z
        res = search_terms("Huquq")
        self.assertTrue(len(res) > 0)
        self.assertEqual(res[0]["term"], "Huquq")
        
        # Aliment
        res_aliment = search_terms("Aliment")
        self.assertEqual(len(res_aliment), 1)
        self.assertEqual(res_aliment[0]["term"], "Aliment")
        
        # Qisman yozish: "prezump"
        res_prezump = search_terms("prezump")
        self.assertTrue(any(t["term"] == "Aybsizlik prezumpsiyasi" for t in res_prezump))
        
        # Qisman yozish: "retsidiv"
        res_retsidiv = search_terms("retsidiv")
        self.assertTrue(any(t["term"] == "Retsidiv jinoyat" for t in res_retsidiv))
        
        # Qisman yozish: "kolliz"
        res_kolliz = search_terms("kolliz")
        self.assertTrue(any("Kolliziya" in t["term"] for t in res_kolliz))

if __name__ == "__main__":
    unittest.main()
