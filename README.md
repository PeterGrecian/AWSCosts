# AWSCosts
There are tools such as Cost Explorer which can be used to study AWS costs incurred, however it is also very useful to have an easy to use value for the cost of a resource to use for developing designs.  

The costs do vary with region, but in most cases the costs are within a 10% margin. Bulk discounts are usually quite small, and there is the effect of the "always free" quotas which deserve a separate discussion.  Substantial discounts can be obtained for compute, particularly using Reserved Instances in the case of EC2 and RDS, or Compute Savings Plans to a lesser degree for Fargate or Lambda. The completeness or "coverage" of the Reservations is an important factor in how accurately resources can be costed and 2 significant figures is ample.



## AWS Costs Cheatsheet


### Tables in the Cheatsheet for gist markdown and more generally

Markdown lacks rowspan and github lacks styles too.  Converting to html allows rowspan for github and more generally allows styles.

Create html table from .txt which is modified md.  A comment containing the rowspan directive in the first column can be used.  There's quite a bit of hard coding to get this written quickly and "table.py" which uses styles not supported by github gists.
```
  ./gist-table.py cheatsheet.txt > cheatsheet.md
```

create secret gist from the md and view in browser
```
  gh gist create cheatsheet.md -w  
```

delete a load of gists

```
name="cheatsheet.md"  # be careful!
yes="--yes"
for g in $(gh gist list | grep $name$ | cut -f 1); do gh gist delete $yes $g; done
```