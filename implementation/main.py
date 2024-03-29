
import regex
import os
from selenium import webdriver
from implementation import xpath
from implementation import roadrunner
import regex
import json


# Not used currently, may use if content will be displayed with JS. Then we have to render page with browser
def open_page(path):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("file:///" + os.path.abspath(path))

    return driver.page_source


def get_rtvslo_data():
    # Get HTML content
    rtvslo_01 = open('../input/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html', encoding='utf-8').read()
    rtvslo_02 = open( '../input/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html', encoding='utf-8' ).read()

    parsed_rtvslo01 = regex.parse_rtvslo(rtvslo_01)
    parsed_rtvslo02 = regex.parse_rtvslo(rtvslo_02)

    return [parsed_rtvslo01, parsed_rtvslo02]


def get_overstock_data():
    # Get HTML content
    overstock_01 = open('../input/overstock.com/jewelry01.html').read()
    overstock_02 = open('../input/overstock.com/jewelry02.html').read()

    parsed_overstock_01 = regex.parse_overstock(overstock_01)
    parsed_overstock_02 = regex.parse_overstock(overstock_02)

    return [parsed_overstock_01, parsed_overstock_02]


def get_github_data():
    # Get HTML content
    github_01 = open('../input/github.com/Topic_google.html', encoding='utf-8').read()
    github_02 = open('../input/github.com/Topic_react-native.html', encoding='utf-8').read()

    parsed_github_01 = regex.parse_github(github_01)
    parsed_github_02 = regex.parse_github(github_02)

    return [parsed_github_01, parsed_github_02]



def get_rtvslo_data_xpath():
    # Get HTML content
    rtvslo_01 = open('../input/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html', encoding='utf-8' ).read()
    rtvslo_02 = open( '../input/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html', encoding='utf-8' ).read()
    parsed_json1 = xpath.parse_rtvslo(rtvslo_01)
    parsed_json2 = xpath.parse_rtvslo(rtvslo_02)
    return [parsed_json1,parsed_json2]

def get_overstock_data_xpath():
    # Get HTML content
    overstock_01 = open('../input/overstock.com/jewelry01.html').read()
    overstock_02 = open('../input/overstock.com/jewelry02.html').read()

    parsed_overstock_01 = xpath.parse_overstock(overstock_01)
    parsed_overstock_02 = xpath.parse_overstock(overstock_02)

    return [parsed_overstock_01, parsed_overstock_02]

def get_github_data_xpath():
    # Get HTML content
    github_01 = open('../input/github.com/Topic_google.html', encoding='utf-8').read()
    github_02 = open('../input/github.com/Topic_react-native.html', encoding='utf-8').read()

    parsed_github_01 = xpath.parse_github(github_01)
    parsed_github_02 = xpath.parse_github(github_02)

    return [parsed_github_01, parsed_github_02]

def get_roadrunner_suggestion():
    # github_01 = open('../input/test/test1.html', encoding='utf-8').read()
    # github_02 = open('../input/test/test2.html', encoding='utf-8').read()

    github_01 = open('../input/github.com/Topic_google.html', encoding='utf-8').read()
    github_02 = open('../input/github.com/Topic_react-native.html', encoding='utf-8').read()

    return roadrunner.wrapper(github_01,github_02)
    # parsed_github_01 = xpath.parse_github(github_01)
    # parsed_github_02 = xpath.parse_github(github_02)
    # return [parsed_github_01, parsed_github_02]



def print_rtvslo_data():
    [print(x) for x in get_rtvslo_data()]

def print_overstock_data():
    [print(x) for x in get_overstock_data()]

def print_github_data():
    [print(x) for x in get_github_data()]

def print_roadrunner_data():
    print(json.dumps(get_roadrunner_suggestion(),indent=2))

if __name__ == '__main__':
    #get_rtvslo_data_xpath()
    #get_overstock_data_xpath()
    # get_github_data_xpath()
    # get_roadrunner_suggestion()
    #[print(x) for x in get_rtvslo_data_xpath()]
    #print_rtvslo_data()
    #print_overstock_data()
    #print_github_data()
     print_roadrunner_data()