import json
from jinja2 import Environment, FileSystemLoader
with open('data.json', 'r') as f:
    data = json.load(f)

fileloader = FileSystemLoader('templates')
env = Environment(loader = fileloader)

template = env.get_template('template.html')

output = template.render(data = data)

fileName = 'index.html'

with open(fileName, 'w') as f1:
    f1.write(output)