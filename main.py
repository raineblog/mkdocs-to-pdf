import sys
import os
import download
import common

hints = {
    'default': 'Usage: python main.py [path]',
    'notExists': 'The path does not exist!'
}

def download_mkdocs(path, target, subject):
    lists = []
    
    def process(present, item):
        if isinstance(item, dict):
            for section, content in item.items():
                print("Fetch section:", section)
                process(os.path.join(present, section), content)
        elif isinstance(item, list):
            for element in item:
                process(present, element)
        elif isinstance(item, str):
            file_path = os.path.join('https://raineblog.github.io/whk/', item, 'index.html').replace('index\\index.html', 'index.html')
            title = common.get_title(os.path.join(path, 'docs', item + '.md'))
            print("Fetch content:", file_path, title)
            lists.append([file_path, os.path.join(present, title + '.pdf')])
        else:
            raise ValueError(f"Unsupported item type: {item}")

    process(target, subject)
    download.convertHtmlToPdf(lists)
    # print(lists)

def Main():
    argv = sys.argv
    if len(argv) < 3:
        print(hints['default'])
        return
    elif len(argv) == 3:
        path = os.path.abspath(argv[1])
        target = os.path.abspath(argv[2])
        print(path, target)
        if not os.path.exists(path):
            print(hints['notExists'])
            return
        data = common.load_yaml(os.path.join(path, 'mkdocs.yml'))
        for subject in data['nav']:
            download_mkdocs(path, target, subject)
        # print(nav)
    else:
        print(hints['default'])

if __name__ == "__main__":
    Main()
