#!.venv/bin/python3

import yaml  # YAML parsing
from jinja2 import Environment, FileSystemLoader  # Jinja template

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

publications_template = ENV.get_template('src/pug/publications.j2')
papers_template = ENV.get_template('src/pug/papers.j2')
preprints_template = ENV.get_template('src/pug/preprints.j2')

# Opening the data file
with open("src/assets/bib/output.yml") as y:
    with open("src/assets/bib/open.yml") as z:
        # Loading the YAML data
        input = yaml.load(y, Loader=yaml.BaseLoader)
        extras = yaml.load(z, Loader=yaml.BaseLoader)
        # Opening the output file
        f = open('src/pug/publications.pug', 'w', encoding="utf8")
        g = open('src/pug/papers.pug', 'w', encoding="utf8")
        h = open('src/pug/preprints.pug', 'w', encoding="utf8")
        # Rendering the output from data and papers template
        publications_output = publications_template.render(input=input, extras=extras)
        papers_output = papers_template.render(input=input, extras=extras)
        preprints_output = preprints_template.render(input=input, extras=extras)
        # Creating the output file
        f.write(publications_output)
        g.write(papers_output)
        h.write(preprints_output)
        # Closing the output file
        f.close
        g.close
        h.close

presentations_max_template = ENV.get_template('src/pug/presentations_max.j2')

presentations_template = ENV.get_template('src/pug/presentations.j2')

# Opening the data file
with open("src/assets/bib/presentations.yml") as y:
    # Loading the YAML data
    input = yaml.load(y, Loader=yaml.BaseLoader)
    # Opening the output file
    f = open('src/pug/presentations_max.pug', 'w', encoding="utf8")
    g = open('src/pug/presentations.pug', 'w', encoding="utf8")
    # Rendering the output from data and presentations template
    output_max = presentations_max_template.render(input=input)
    output = presentations_template.render(input=input)
    # Creating the output file
    f.write(output_max)
    g.write(output)
    # Closing the output file
    f.close
    g.close