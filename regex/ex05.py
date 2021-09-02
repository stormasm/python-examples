## See the html directory in this repo

import re

def get_name_and_number(input):
    m = re.match(r"(?P<x0>Organism) (?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
    r1 = m.group("x1") + " " + m.group("x2")
    r2 = m.group("x4")
    mytuple = (r1, r2)
    return mytuple

"Organism Enterococcus sp. 8G7_MSG3316 has 2625 proteins with network connections.,overview.1834191.html"
"Organism Lachnoclostridium sp. YL32 has 4965 proteins with network connections.,overview.1834196.html"
"Organism Hungateiclostridiaceae bacterium KB18 has 2724 proteins with network connections.,overview.1834198.html"
"Organism Burkholderiales bacterium YL45 has 2039 proteins with network connections.,overview.1834205.html"
"Organism Erysipelotrichaceae bacterium I46 has 3171 proteins with network connections.,overview.1834207.html"
"Organism Frankia sp. BMG5.36 has 6664 proteins with network connections.,overview.1834512.html"
"Organism Frankia asymbiotica has 5603 proteins with network connections.,overview.1834516.html"
"Organism Fibrella sp. ES10-3-2-2 has 4013 proteins with network connections.,overview.1834519.html"
"Organism Saccharothrix sp. CB00851 has 6645 proteins with network connections.,overview.1835005.html"
"Organism Polynucleobacter duraquae has 1813 proteins with network connections.,overview.1835254.html"
"Organism Penicillium arizonense has 6768 proteins with network connections.,overview.1835702.html"
"Organism secondary endosymbiont of Trabutina mannipara has 231 proteins with network connections.,overview.1835721.html"
"Organism Arthrobacter sp. OY3WO11 has 3385 proteins with network connections.,overview.1835723.html"
"Organism Maribacter sp. T28 has 3118 proteins with network connections.,overview.1836467.html"
"Organism Phytoplasma sp. Vc33 has 369 proteins with network connections.,overview.1836886.html"
"Organism Shewanella colwelliana has 3467 proteins with network connections."
print(get_name_and_number(org01))
