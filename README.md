Basic python bioinformatics utiles
=
### In this repository, basic Python codes used for data science in the bio domain are stored.
name_to_smiles.py
--
- convert drug name to smiles.
- use csv format file
- required pubchempy

<pre><code>## install
$ pip install pubchempy
## running
$ python name_to_smiles.py {input}.csv {output}.csv
</code></pre>
### help massage
<pre><code>$ python name_to_smiles.py -h
usage: name_to_smiles.py [-h] [-n namecolumn] [-s smilescolumn]
                         [-t smilestype]
                         drugnameFile smilesFile

positional arguments:
  drugnameFile     A filepath of drug name data
  smilesFile       A filepath for saving converted smiles data

optional arguments:
  -h, --help       show this help message and exit
  -n namecolumn    A column name of drug name column for reading csv file
  -s smilescolumn  A column name of smiles name column
  -t smilestype    A column name of smiles name column
</code></pre>
