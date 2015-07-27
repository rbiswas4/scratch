#!/usr/bin/env python

import os
import sys
import argparse

import pydot



parser = argparse.ArgumentParser(prog='draw',
                                 description="""takes a dot file and creates a pdf representation with the same basename""")
parser.add_argument("--inputfile", type=str, default=None, required=True, 
                    help="Absolute path to dot file")

args = parser.parse_args()
inputfile = os.path.abspath(args.inputfile)
#location, fname = os.path.split(inputfile)
fname = inputfile.replace('.dot','.pdf')


graph = pydot.graph_from_dot_file(inputfile)
graph.write_pdf(fname)

exit()

graph = pydot.graph_from_dot_file('HelloWorldParallel.dot')
graph.write_pdf('HelloWorldParallel.pdf')
g = pydot.graph_from_file('HelloWorldParallelSplitMerge.dot')
g = pydot.graph_from_dot_file('HelloWorldParallelSplitMerge.dot')
g.write_pdf('HelloWorldParallel.pdf')
g.write_pdf('HelloWorldParallel_split_merge.pdf')
get_ipython().magic(u'logstart ')
