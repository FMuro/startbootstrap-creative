#!/opt/homebrew/bin/python3

import yaml  # YAML parsing
from jinja2 import Environment, FileSystemLoader  # Jinja template

# Folder with data and templates and do extension
ENV = Environment(loader=FileSystemLoader('.'), extensions=['jinja2.ext.do'])

template = ENV.get_template('pug/index.j2')

# Opening the data file
with open("data.yaml") as y:
    # Loading the YAML data
    input = yaml.load(y, Loader=yaml.BaseLoader)
    # Opening the output file
    f = open('pug/index.pug', 'w', encoding="utf8")
    # Rendering the output from data and template
    output = template.render(input)
    # Creating the output file
    f.write(output)
    # Closing the output file
    f.close