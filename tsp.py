#!/usr/bin/env python
"""
SYNOPSIS

    An 2-approximate algorithm for metrix-TSP.

DESCRIPTION
    

EXAMPLES
    
    python tsp.py


EXIT STATUS
    
    0 program exit normal
    1 program had problem on execution


AUTHOR

    Theofilis George <theofilis.g@gmail.com>

LICENSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    1
"""

import sys, os, traceback, optparse
import time
import re
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

from myUtility import *

def apprAlgorithm(G):
    # Find a minimum spanning tree T of G
    T=nx.minimum_spanning_tree(G, weight='weight')

    dfs = nx.dfs_preorder_nodes(T, '0');
    listnode = [];
    for item in dfs:
        listnode += [item]

    # Create the hamiltonian tour
    L =nx.Graph()
    L.add_nodes_from(G.nodes(data=True))

    cost = 0
    weight = nx.get_edge_attributes(G,'weight')
    for index, item in enumerate(listnode):
        if index < len(G) - 1:
            L.add_edge(item, listnode[index+1])
            cost += G[str(item)][str(listnode[index+1])]['weight']  
        else:
            L.add_edge(item, listnode[0])
            cost += G[str(item)][str(listnode[0])]['weight'] 
            
    return(cost, T, L, listnode) 

def main ():

    global options, args

    G = nx.read_graphml(args[0] + ".graphml")

    save(G, "problem-"+args[0]+".png")
    initgraph(G)

    (cost,T, L, path) = apprAlgorithm(G)

    print "The cost of this tour:",cost
    print "The tour:", path

    save(T, "minimum-spanning-tree-kruskal-"+args[0]+".png")
    save(L, "2-approximate-tour-"+args[0]+".png")
    #draw(G, L)
    


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print(time.asctime())
        main()
        if options.verbose: print(time.asctime())
        if options.verbose: print('TOTAL TIME IN MINUTES:'),
        if options.verbose: print ((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
    except SystemExit as e: # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)