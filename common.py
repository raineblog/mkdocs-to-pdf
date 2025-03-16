import requests
import yaml

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        title = file.readline().strip()
    return title[2:] # remove '# '

def load_yaml(file_path):
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().replace('!!', '__').replace('.md', '').replace('.', '-')
        data = yaml.load(text, Loader=yaml.FullLoader)
    return data
