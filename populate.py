#!.venv/bin/python3

import yaml  # YAML parsing
from jinja2 import Environment, FileSystemLoader  # Jinja template

# Folder with data and templates and do extension
ENV = Environment(loader=FileSystemLoader('.'), extensions=['jinja2.ext.do'])


# jinja2 templates

web_template = ENV.get_template('src/pug/index.j2') # landing page
presentations_max_template = ENV.get_template('src/subfiles/presentations_max.j2') # presentations in landing page
presentations_template = ENV.get_template('src/pug/presentations.j2') # presentations page
publications_template = ENV.get_template('src/subfiles/publications.j2') # preprints and papers in landing page
papers_template = ENV.get_template('src/pug/papers.j2') # papers page
preprints_template = ENV.get_template('src/pug/preprints.j2') # preprints page


# Opening the data files
with open("output.yml") as y:
    with open("data.yml") as z:
        # Loading the YAML data
        biblio = yaml.load(y, Loader=yaml.BaseLoader)
        datos = yaml.load(z, Loader=yaml.BaseLoader)
        # Opening the output files
        f = open('src/pug/index.pug', 'w', encoding="utf8")
        f2 = open('src/subfiles/presentations_max.pug', 'w', encoding="utf8")
        g2 = open('src/pug/presentations.pug', 'w', encoding="utf8")
        f3 = open('src/subfiles/publications.pug', 'w', encoding="utf8")
        g3 = open('src/pug/papers.pug', 'w', encoding="utf8")
        h3 = open('src/pug/preprints.pug', 'w', encoding="utf8")
        # Rendering the output files from data, biblio and jinja2 templates
        output = web_template.render(datos=datos)
        presentations_max_output = presentations_max_template.render(datos=datos)
        presentations_output = presentations_template.render(datos=datos)
        publications_output = publications_template.render(biblio=biblio, datos=datos)
        papers_output = papers_template.render(biblio=biblio, datos=datos)
        preprints_output = preprints_template.render(biblio=biblio, datos=datos)
        # Writing to the output files
        f.write(output)
        f2.write(presentations_max_output)
        g2.write(presentations_output)
        f3.write(publications_output)
        g3.write(papers_output)
        h3.write(preprints_output)
        # Closing the output files
        f.close
        f2.close
        g2.close
        f3.close
        g3.close
        h3.close