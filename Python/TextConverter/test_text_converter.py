import unittest
from pathlib import Path
from text_converter import UnicodeFileToHtmlTextConverter
from html_pages import HtmlPagesConverter


class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):

    def test_foo(self):
        converter = UnicodeFileToHtmlTextConverter("foo")
        self.assertEqual("foo", converter.full_filename_with_path)

    def test_convert(self):
        path = Path(__file__).parent.joinpath('mock_file')
        converter = UnicodeFileToHtmlTextConverter(path)
        html = converter.convert_to_html()
        self.assertEqual(html, 'test<br />')


class HtmlPagesConverterTest(unittest.TestCase):

    def test_get_html_page(self):
        path = Path(__file__).parent.joinpath('mock_pagination_file')
        converter = HtmlPagesConverter(path)
        html = converter.get_html_page(1)
        self.assertEqual(html, 'test1<br />')


if __name__ == "__main__":
    unittest.main()
