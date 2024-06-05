#!.venv/bin/python3

import yaml  # YAML parsing
from jinja2 import Environment, FileSystemLoader  # Jinja template
import json # JSON parsing

# Folder with data and templates and do extension
ENV = Environment(loader=FileSystemLoader('.'), extensions=['jinja2.ext.do'])

web_template = ENV.get_template('src/pug/index.j2')

# Opening the data file
with open("src/data.yml") as y:
    # Loading the YAML data
    input = yaml.load(y, Loader=yaml.BaseLoader)
    # Opening the output file
    f = open('src/pug/index.pug', 'w', encoding="utf8")
    # Rendering the output from data and web template
    output = web_template.render(input)
    # Creating the output file
    f.write(output)
    # Closing the output file
    f.close

papers_template = ENV.get_template('src/pug/papers.j2')

# Opening the data file
with open("src/assets/bib/output.yml") as y:
    # Loading the JSON data
    input = yaml.load(y, Loader=yaml.BaseLoader)
    # Opening the output file
    f = open('src/pug/papers.pug', 'w', encoding="utf8")
    # Rendering the output from data and papers template
    output = papers_template.render(input=input)
    # Creating the output file
    f.write(output)
    # Closing the output file
    f.close