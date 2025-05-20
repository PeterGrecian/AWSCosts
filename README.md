# AWSCosts

Markdown lacks rowspan and github lacks styles too.  Converting to html allows rowspan for github and more generally allows styles.

Create html table from .txt which is modified md.  A comment containing the rowspan directive in the first column can be used.  There's quite a bit of hard coding to get this written quickly and "table.py" which uses styles not supported by github gists.
```
  ./gist-table.py cheatsheet.txt > cheatsheet.md
```

create secret gist from the md
```
  gh gist create cheatsheet.md -w  
```

delete a load of gists

```
name="cheatsheet.md"  # be careful!
yes="--yes"
for g in $(gh gist list | grep $name$ | cut -f 1); do gh gist delete $yes $g; done
```