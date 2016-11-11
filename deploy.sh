#!/bin/bash

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