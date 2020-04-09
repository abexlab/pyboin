import unittest
import pyboin


HIRAGANA = (
        'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔ',
    'アアイイウウエエオオアアイイウウエエオオアアイイウウエエオオアアイイッウウエエオオアイウエオアアアイイイウウウエエエオオオアイウエオアアウウオオアイウエオアオンーヮヰヱヵヶヴ',
)
KATAKANA = (
    'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ',
    'ああいいううええおおああいいううええおおああいいううええおおああいいっううええおおあいうえおあああいいいうううえええおおおあいうえおああううおおあいうえおあおんーゎゐゑゕゖゔ'
)


class Text2Boin(unittest.TestCase):
    def test_hira2kana(self):
        self.assertEqual(pyboin.text2boin(HIRAGANA[0]), HIRAGANA[1])

    def test_kana2hira(self):
        self.assertEqual(pyboin.text2boin(KATAKANA[0], cv='katakana'), HIRAGANA[1])


if __name__ == '__main__':
    unittest.main()
