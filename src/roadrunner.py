import json
import re
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup


def wrapper(base_html, input_html):
    base_tree  = BeautifulSoup(base_html, "html.parser")
    input_tree = BeautifulSoup(input_html, "html.parser")
    base_body  = base_tree.find('body').findChildren()
    input_body = base_tree.find('body').findChildren()



    ret_map = {"body":{}}
    for i in range(len(base_body)):
        if base_body[i].name == input_body[i].name:
            ret_map["body"][base_body[i].name] = {}

    print("asd")




    # [print(str(tag.name)) for tag in base_body]

# def rf(base,cmp):
#     if base.name != cmp.name:
#         return
