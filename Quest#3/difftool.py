import os
import difflib

# open the files and store their contents in a list
with open('Release Note OLD.md','r') as old:
    old_lines = old.readlines()

with open('Release Note NEW.md','r') as new:
    new_lines = new.readlines()

# create a generator with unified_diff and compare lines in old and new
d = difflib.unified_diff(old_lines, new_lines, fromfile='Release Note OLD.md', tofile='Release Note NEW.md', lineterm='', n=0)

# store the compared lines of text in a list

lines = list(d)[2:]       #remove before and after control lines

# remove remaning @@ control lines and loop the items in the list to include only additions
added = [line[1:] for line in lines if line[0] == '+']

# write all the lines to a file one at a time to keep format
with open('whatsnew.md','w') as whatsnew:
    for line in added:
        whatsnew.write(line)