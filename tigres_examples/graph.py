#!/usr/bin/env python

import os
import sys
import argparse

import pydot



parser = argparse.ArgumentParser(prog='draw',
                                 description="""takes a dot file and creates a pdf representation with the same basename""")
# parser.add_argument( type=str, default=None, required=True, 
parser.add_argument("inputfile", type=str,
                    help="Absolute path to dot file")

args = parser.parse_args()
inputfile = os.path.abspath(args.inputfile)
fname = inputfile.replace('.dot','.pdf')
graph = pydot.graph_from_dot_file(inputfile)
graph.write_pdf(fname)

exit()

