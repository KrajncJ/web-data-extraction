import json
import re
from lxml import html
from lxml import etree
from collections import defaultdict
from random import randint
from bs4 import BeautifulSoup


potential_paths = []
# Potential tag list.
INTERESTING_TAGS = ['p']


def wrapper(base_html, input_html):
    base_tree  = BeautifulSoup(base_html, "html.parser")
    input_tree = BeautifulSoup(input_html, "html.parser")

    # Use only body tags for analysis
    base_body  = base_tree.find('body').findChildren(recursive=False)
    input_body = input_tree.find('body').findChildren(recursive=False)

    res = construct('', {}, base_body, input_body)

    return {
        "Matching_Construction": res,
        "Potential_Paths": potential_paths
    }


def construct(path, map, chlds_first, chlds_sec):
    # Create construction until there are some childs
    if len(chlds_first) == 0:
        return {}
    # We will now iterate though both childs of both DOM nodes. Each node should be at same index
    # If nodes are not on same index, they are not matching same structure, so they will be ignored
    # Save size of childs for second page
    sec_size= len(chlds_sec)
    for i in range(len(chlds_first)):
        # Iterate thorough all childs on base page. But do not proceed if child with same does not exists on other side.
        if i < sec_size:
            # We need both corelated nodes
            base = chlds_first[i]
            comp = chlds_sec[i]
            # Build path name, and pass it to next level of recursion
            curr_path = path+base.name+'/'
            if base.name == comp.name:
                # If nodes are corelated and of same type, then construct inner Tree recursive
                # Add some additional random value, because JSON does not support attributes of same name on same level
                map[base.name+'_'+str(randint(0,1000))] = construct(curr_path,{},base.findChildren(recursive=False), comp.findChildren(recursive=False))
            if base.name in INTERESTING_TAGS:
                # If current path is interesting, then store this in potential path and display at the end
                potential_paths.append(curr_path)

    # Returning generated matching tree with potential paths
    return map

