# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)  

    def test_quality_never_negative_after_multiple_updates(self):
        items = [Item("+5 Dexterity Vest", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
    
    def test_aged_brie_increases_quality_after_sellin_passed(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)  

if __name__ == '__main__':
    unittest.main()
