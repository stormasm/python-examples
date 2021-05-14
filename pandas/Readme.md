
### Data Model

| symbol | cashflow | mcap |
| :----: | :------: | :--: |
| symbol 1 | cf1 | mcap1 |
| symbol 2 | cf2 | mcap2 |

stock symbols are always indexes or rows because you may want to display 100 symbols and having the symbols in columns makes no sense.

the series or column is {cashflow, mcap} etc where each column can be a different datatype.  So you can have strings in one column, ints in another, and floats in another.  The key point is that for each column the datatype is the same.

### Pandas Tutorial

This program is a tutorial in how to use pandas.
See the
[Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html) for more details...

The programs in this directory require these files to run...

```python
pathtop = os.environ['BMTOP']
path1 = pathtop + '/python-examples/data/csv'
path2 = pathtop + '/python-examples/data/schema-fun.csv'
```

#### columerge.py
This was the first program written in this repo and eventually
its job will be to merge columns from different data files but
for now it just kicks the ball off...

#### index.py
This is the 2nd program.  Eventually it will go away.  It is
a copy of some of the code from the first program with the ability to filter out
columns from the data frame and indices from the data frame.

It takes as input 2 files, both files are optional...
* the first file is a list of symbols
* the second file is a list of indices

If neither file is provided its run off hardcoded arrays
built into the program...

### References
[How to print all rows and not truncate dataframe](https://thispointer.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/)

[Github Markdown Tables](https://www.pluralsight.com/guides/working-tables-github-markdown)
