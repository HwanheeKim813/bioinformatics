import argparse
import pandas as pd
from pubchempy import *


def get_args():
    parser = argparse.ArgumentParser()
    ## positional
    parser.add_argument('drugnameFile', type=str, help="A filepath of drug name data")
    parser.add_argument('smilesFile', type=str, help="A filepath for saving converted smiles data")
    ## optional
    parser.add_argument('-n', metavar='namecolumn', type=str, default='Name', help="A column name of drug name column for reading csv file")
    parser.add_argument('-s', metavar='smilescolumn', type=str, default='smiles', help="A column name of smiles name column")
    parser.add_argument('-t', metavar='smilestype', type=str, default='smiles', help="A column name of smiles name column")
    return parser.parse_args()
    
def main():
    args = get_args()
    namedf = pd.read_csv(args.drugnameFile)
    name = list(namedf[args.n])
    compounds = [get_compounds(n,'name') for n in name]
    smiles = ['' if len(c)==0 else c[0].canonical_smiles for c in compounds]
    out = pd.DataFrame()
    out[args.n] = name
    out[args.s] = smiles
    print(out)
    out.to_csv(args.smilesFile, index=False)
    

if __name__=="__main__":
    main()