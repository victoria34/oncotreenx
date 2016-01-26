##
# imports
import sys
import os
import urllib2
import networkx as nx

## constants.
FILE_URL = "https://raw.githubusercontent.com/cBioPortal/oncotree/master/tumor_tree.txt"

## functions

def build_oncotree(file_path=False):

    # load the file.
    if not file_path:

        # fetch from inter-webs.
        req = urllib2.Request(FILE_URL)
        response = urllib2.urlopen(req)
        the_page = response.read()

        # split into array.
        lines = the_page.strip().split("\n")

    else:

        # just open the file.
        lines = open(file_path, "rb")

    # create a graph.
    g = nx.DiGraph()

    # add root node.
    g.add_node("root", {"text": "root"})
    root = "root"

    # parse the file.
    line_cnt = 0
    for line in lines:

        # skip header.
        if line_cnt == 0:
            line_cnt += 1
            continue

        # tokenize.
        tokens = line.strip().split("\t")
        try:
            metamaintype = tokens[5]
        except IndexError:
            metamaintype = None
        try:
            metacolor = tokens[6]
        except IndexError:
            metacolor = None
        try:
            metanci = tokens[7]
        except IndexError:
            metanci = None
        try:
            metaumls = tokens[8]
        except IndexError:
            metaumls = None

        # set root node.
        prev_n = root

        # build nodes all the way down.
        nodes = list()
        for i in range(4):

            # skip empty.
            if len(tokens) < 2:
                continue

            # check if empty.
            print tokens
            if tokens[i] == "":
                continue

            # split into two.
            tmp = tokens[i].split("(")
            val = tmp[0].strip()
            key = tmp[1].strip().replace("(","").replace(")","")

            # build node.
            g.add_node(key, {
                'text': val,
                'metamaintype': metamaintype,
                'metacolor': metacolor,
                'metanci': metanci,
                'metaumls': metaumls
            })
            n = key

            # add edge.
            g.add_edge(prev_n, n)

            # update previous node.
            prev_n = n

        # increment line count.
        line_cnt += 1

    # return the graph.
    return g

def get_basal(g, source):

    # get ancestors.
    nlist = nx.ancestors(g, source)

    # find the one with predecessor root.
    hit = None
    for n in nlist:

        # get predecessor.
        preds = g.predecessors(n)
        if len(preds) > 0 and preds[0] == 'root':
            hit = n

    # sanity check.
    if hit is None:
        raise StandardError

    # return the basal ancestor.
    return hit
