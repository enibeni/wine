import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_age, get_wines


def main():
    parser = argparse.ArgumentParser(description='Сайт-каталог алкогольной продукции')
    parser.add_argument('file', help='Путь к файлу со списком товаров')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=get_age(),
        drinks=get_wines(args.file),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
