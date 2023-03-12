"""This is a second, slightly harder problem on the same theme as the first."""
import html as html_converter


class HtmlPagesConverter:

    def __init__(self, filename):
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        self.filename = filename
        self.breaks = [0]
        self._add_breaks()

    def _add_breaks(self):
        with open(self.filename, "r", encoding="UTF-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    self.breaks.append(f.tell())
            self.breaks.append(f.tell())

    def get_html_page(self, page: int = 0):
        """Return html page with the given number (zero indexed)"""
        page_start = self.breaks[page]
        page_end = self.breaks[page + 1]
        html = ""
        with open(self.filename, "r", encoding="UTF-8") as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                html += html_converter.escape(line, quote=True)
                html += "<br />"
        return html
