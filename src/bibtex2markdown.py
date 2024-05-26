#!/usr/bin/env python


# Min Xu: generate a bibliograph from a bibtex in a markdown format


from pybtex.database import BibliographyData, parse_file
from collections import OrderedDict
from operator import itemgetter

import re
import pypandoc

bibfile = "./docs/assets/bib/MXPUB.bib"
cslfile = "./docs/assets/csl/american-geophysical-union.csl"

file_md = './docs/publications/index.md'


bibdata = parse_file(bibfile)
bibobjs = BibliographyData(entries=bibdata.entries)



orig_dict = OrderedDict()
for entkey in bibobjs.entries:

    entval = bibobjs.entries[entkey] 

    try:
       pub_yr = entval.fields['year']
    except KeyError:
       pub_yr = 1974
    pub_au = entval.persons['author'][0].last_names[0]
    sortval = str(pub_yr) + pub_au
    sortkey = entkey
    orig_dict[sortkey] = sortval

reorder_dict = OrderedDict(sorted(orig_dict.items(), key = itemgetter(1), reverse = True))


doi_icon_str = "[:simple-doi:]({0})"
bib_icon_str = " (1) \n{ .annotate } \n\n 1. "
#doi_icon_str = "[![Static Badge](https://img.shields.io/badge/DOI-168363?style=flate&logo=doi&logoColor=white)]({})"
#bib_icon_str = "[![Static Badge](https://img.shields.io/badge/BibTeX-168363?style=flate&logo=bibtex&logoColor=white)]({})"


with open (file_md, "w") as fmd:

    fmd.write("---\nicon: material/newspaper-variant-multiple\n---\n\n")
    fmd.write("# Publications\n\n")
    for key in reorder_dict.keys():
    
        ent_org = bibobjs.entries[key]
    

        # extract doi, abstract and web page url
        try:
           doinumber = ent_org.fields.pop('doi')
        except:
           doinumber = 'null'
    
        try:
           abstract = ent_org.fields.pop('abstract')
        except:
           abstract = 'null'
    
        try:
           webpgurl = ent_org.fields.pop('url')
        except:
           webpgurl = 'null'
    
        # remove file and note items
        if 'file' in ent_org.fields.keys():
           ent_org.fields.pop('file')
    
        if 'note' in ent_org.fields.keys():
           ent_org.fields.pop('note')

        bib_str = BibliographyData(entries={key:ent_org}).to_string("bibtex")
        markdown = pypandoc.convert_text(source=bib_str, to="markdown_strict", format="bibtex", extra_args=["--citeproc", "--csl", cslfile])
        markdown = " ".join(markdown.split("\n"))
    
        #print ('key', key)
        #if key == 'durdenAutomatedIntegrationContinentalScale2020':
        #   print ('xxx', bib_str)
        #   print ('yyy', markdown)

        new_md = markdown

        #-repat = re.compile("<[^<,^>]*>")
        #-# doi.org links to DOIs
        #-if repat.findall(markdown) != []:
        #-   for lnk in repat.findall(markdown):

        #-       if 'doi.org' in lnk:
        #-          new_md = markdown.replace(lnk, doi_icon_str.format(lnk))
    
        #-# get the url link not the DOIs for future use
        #-if not 'doi.org' in webpgurl:
        #-   print (webpgurl)

        if doinumber != 'null':
           lnk = "https://doi.org/" + doinumber
           new_md = markdown + doi_icon_str.format(lnk)
    
    
        # put the bibtex icon and annotation in the end of the markdown
        # put additional space after comma in the bib_str, so there will be a new line after comma
        # try to remove all {} pairs with the first {} in bib_str
        istrt = bib_str.find('{') + 1
        istop = bib_str[::-1].find('}') + 1
        bib_fmt = bib_str[0:istrt] + bib_str[istrt:-istop].replace('{','').replace('}','') + bib_str[-istop:-1]
        fmd.write(new_md + bib_icon_str + bib_fmt.replace(',', ',  ') + "\n\n")

fmd.close()
