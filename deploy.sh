#!/bin/bash
set -ex

# Generate schema documentation
pip install rdflib
pip install arrow
#python3 ./schema_page_gen/brick_tagset_page_gen.py

# build site
hugo

# attempt to add changes
git add -A
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master
git subtree push --prefix=public git@github.com:BuildSysUniformMetadata/BrickSchemaSite.git gh-pages
