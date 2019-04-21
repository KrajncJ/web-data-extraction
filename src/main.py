
import regex
import os
from selenium import webdriver


# Not used currently, may use if content will be displayed with JS. Then we have to render page with browser
def open_page(path):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("file:///" + os.path.abspath(path))

    return driver.page_source


def get_rtvslo_data():
    # Get HTML content
    rtvslo_01 = open('../data/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html').read()
    rtvslo_02 = open(
        '../data/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html').read()

    parsed_rtvslo01 = regex.parse_rtvslo(rtvslo_01)
    parsed_rtvslo02 = regex.parse_rtvslo(rtvslo_02)

    return [parsed_rtvslo01, parsed_rtvslo02]


def get_overstock_data():
    # Get HTML content
    overstock_01 = open('../data/overstock.com/jewelry01.html').read()
    overstock_02 = open('../data/overstock.com/jewelry02.html').read()

    parsed_overstock_01 = regex.parse_overstock(overstock_01)
    parsed_overstock_02 = regex.parse_overstock(overstock_02)

    return [parsed_overstock_01, parsed_overstock_02]


def print_rtvslo_data():
    [print(x) for x in get_rtvslo_data()]


def print_overstock_data():
    [print(x) for x in get_overstock_data()]


if __name__ == '__main__':
    print_overstock_data()

