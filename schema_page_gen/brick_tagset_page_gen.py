import json
import os
from os.path import isfile, join
import sys
import pdb
from collections import defaultdict, OrderedDict
from operator import itemgetter
import subprocess

import rdflib
from rdflib import Namespace, OWL, RDF, RDFS
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
import arrow

# Helper functions
    
def uri_list_to_md_str(uri_list):
    res = list()
    for uri in uri_list:
        name = uri.split('/')[-1].split('#')[-1]
        res.append('[{0}]({1})'.format(name, str(uri)))
#        res.append('[{0}]({1})'.format(name, '../'+name))
    return ', '.join(res)

def adder(x,y):
    return x + y



version_list = ['1.0.1']

commit_dict = {
        '1.0.1': '0b47efe87dad04c758b7571035dffba2012dea12',
        }


base_template = """
<a name="{0}"></a>
## [{0}](#{0})
### Definition: {1}

### Relationships:
"""

header_template = """
---
date: {0}
title: {1} version {2}
menu: {2}
---

"""

for version in version_list:
    schema_content_dir = 'content/schema/{0}/'.format(version)

    try:
        os.mkdir(schema_content_dir)
    except:
        pass
    
    # clean existing entity files
    files = [f for f in os.listdir(schema_content_dir) \
            if isfile(join(schema_content_dir, f)) and "index.md" not in f ]
    for filename in files:
        os.remove(join(schema_content_dir, filename))

    BRICK = Namespace('https://brickschema.org/schema/{0}/Brick#'.format(version))
    BF = Namespace('https://brickschema.org/schema/{0}/BrickFrame#'.format(version))

    relationship_dict ={
            'Brick': [RDFS.subClassOf, 
                        RDFS.label, 
                        BF.usesTag, 
                        BF.usesMeasurement,
                        SKOS.definition],
            'BrickFrame': [OWL.inverseOf, 
                        RDFS.range, 
                        RDFS.domain],
            }

    root_query_dict = {
            'Brick': 'select ?tagset \
            where{?tagset rdfs:subClassOf+ <%s>}'%str(BF.TagSet),
            'BrickFrame': 'select ?prop where{?prop a owl:ObjectProperty.}'
            }

    os.chdir('schema_page_gen/Brick')
    subprocess.call(['git', 'reset', '--hard', commit_dict[version]])
    os.chdir('../..')
    
    schema_file_dir = 'schema_page_gen/Brick/dist/'
    schema_file_dict = {
            'Brick': schema_file_dir + 'Brick.ttl',
            'BrickFrame': schema_file_dir + 'BrickFrame.ttl'
            }

    for schema_type, schema_filename in  schema_file_dict.items():
        header = header_template.format(str(arrow.get()), schema_type, version)
        doc_dict = dict()
        g = rdflib.Graph()
        #g.parse('raw_src/Brick/dist/Brick.ttl', format='turtle')
        #g.parse('raw_src/Brick/dist/BrickFrame.ttl', format='turtle')
        g.parse(schema_filename, format='turtle')
        root_query = root_query_dict[schema_type]
        display_relationships = relationship_dict[schema_type]

        qres = g.query(root_query)

        for row in qres:
            entity_uri = str(row[0])
            (schema_name, entity_name)= entity_uri.split('/')[-1].split('#')
            
            # Get all relationships
            q = 'select ?p ?o where {<%s> ?p ?o.}'%entity_uri
            qres = g.query(q)
            
            rel_dict = defaultdict(list)
            for row in qres:
                if row[0] in display_relationships:
                    rel_dict[row[0]].append(row[1])
            rel_dict = dict(rel_dict)

            definition = rel_dict.get(SKOS.definition)
            if not definition:
                definition = 'TODO'
            else:
                definition = str(definition[0])
                del rel_dict[SKOS.definition]

            prop_doc = base_template.format(entity_name, definition)
            for p, o_list in rel_dict.items():
                p_name = p.split('#')[-1]
                if p in [RDFS.label]:
                    o_str = o_list[0]
                else:
                    o_str = uri_list_to_md_str(o_list)
                prop_doc += '* [{0}]({1}): {2}\n'.format(p_name, p, o_str)
            doc_dict[entity_name] = prop_doc
        doc_dict = OrderedDict(sorted(doc_dict.items(), key=itemgetter(0)))
        doc_str = reduce(adder, doc_dict.values(), '')

        filename = schema_content_dir + schema_type + '.md'
        with open(filename, 'w') as fp:
            fp.write(header + doc_str)
