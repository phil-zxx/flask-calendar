
class Cell:
    def __init__(self, label: str | int, html_tag: str, class_name: str, styles: str = ""):
        self.label      = label if isinstance(label, str) else str(label)
        self.html_tag   = html_tag
        self.class_name = class_name
        self.styles     = styles

    def to_html(self, extra_class: str) -> str:
        return f'<{self.html_tag} class="{extra_class} {self.class_name}" style="{self.styles}">{self.label}</{self.html_tag}>'


class Table:
    def __init__(self, headers: list[Cell], rows: list[list[Cell]], class_name: str, styles: str):
        self.headers = headers
        self.rows = rows
        self.class_name = class_name
        self.styles = styles

    def to_html(self, extra_cell_class: str) -> str:
        return f"""
            <table class="{self.class_name} mb-0" style="{self.styles}">
                <thead>
                    <tr>{"".join([cell.to_html(extra_cell_class) for cell in self.headers])}</tr>
                </thead>
                <tbody>
                    {"".join(["<tr>" + "".join([cell.to_html(extra_cell_class) for cell in row]) + "</tr>\n" for row in self.rows])}
                </tbody>
            </table>
        """
