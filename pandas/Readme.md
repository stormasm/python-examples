
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

#### filter.py
This is the 2nd program.  Eventually it will go away.  It is
a copy of the first program with the ability to filter out
columns from the data frame and indices from the data frame.

It takes as input 2 files, both files are optional...
* the first file is a list of symbols
* the second file is a list of indices
If neither file is provided its run off hardcoded arrays
built into the program...
