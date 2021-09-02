
##### writeorg

writeorg stands for write organism

These examples deal with several steps...

Downloading from
[organism example](https://stringdb-static.org/organism_overview.html)
the html file.   
Currently I am doing that with reqwest in the
[rust-examples](https://github.com/stormasm/rust-examples/blob/main/reqwest/examples/exc.rs).  That is actually OK as this only has to be done once or twice a year.

Then the html file is converted to csv.  This work happens in this
repo under
[html](./../html)

From here we convert the actual csv file to its final form using regex
in ex04.
