# AWSCosts

create md with html table extensions from .txt which is modified md
```
  ./table.py cheatsheet.txt > cheatsheet.md
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