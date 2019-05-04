import json
import re
from lxml import html


def parse_rtvslo(html_in):
    tree = html.fromstring(html_in)

    # # Author name
    author   = tree.xpath('//div[@class="author-name"]/text()')[0]
    # # Published time
    pub_time = tree.xpath('//div[@class="publish-meta"]/text()')[0]
    pub_time = re.findall('\n\t\t(.+?). (.+?) ob (.+)', pub_time)
    pub_time = pub_time[0][0] + ". " + pub_time[0][1] + " ob " + pub_time[0][2]
    # # Title
    title = tree.xpath('//h1/text()')[0]
    # # Subtitle
    subtitle = tree.xpath('//div[@class="subtitle"]/text()')[0]
    # # Lead
    lead = tree.xpath('//p[@class="lead"]/text()')[0]
    # Content
    content_list = tree.xpath('//article/p/text()')
    content = ""
    for p_txt in content_list:
        content = content + p_txt

    return json.dumps({
        "Author": author,
        "PublishedTime": pub_time,
        "Title": title,
        "SubTitle": subtitle,
        "Lead": lead,
        "Content": content,
    }, indent=2, ensure_ascii=False)



def parse_overstock(html_in):
    tree = html.fromstring(html_in)

    title      = tree.xpath('//tr/td[@valign="top"]/a/b/text()')
    list_price = tree.xpath('//table/tbody/tr/td[@align="left"]/s/text()')
    price      = tree.xpath('//table/tbody/tr/td[@align="left"]/span/b/text()')
    save       = tree.xpath('//table/tbody/tr/td[@align="left"]/span/text()')
    content    = tree.xpath('//td[@valign="top"]/span[@class="normal"]/text()')
    for i in range(len(content)):
        content[i] = content[i].replace("\n", " ")
        save[i] = re.findall("(.*) \((.*)\)",save[i])
    parsed_rows = []
    for i in range(len(title)):
        parsed_rows.append({
                "Title": title[i],
                "ListPrice": list_price[i],
                "Price": price[i],
                "Saving": save[i][0][0],
                "SavingPercent": save[i][0][1],
                "Content": content[i]
            })
    return json.dumps(parsed_rows, indent=2)



def parse_github(html_in):
    tree = html.fromstring(html_in)

    repo_links_names        = tree.xpath('//h3[@class="f3"]/a/@href')
    descriptions            = tree.xpath('//article[@class="border-bottom border-gray-light py-4"]/div[@class="text-gray mb-3 ws-normal"]')
    stars                   = tree.xpath('//a[@class="d-inline-block link-gray"]')
    programming_languages   = tree.xpath('//span[@itemprop="programmingLanguage"]/text()')
    parsed_rows = []
    for i in range(len(descriptions)):
        descriptions[i] = descriptions[i].xpath("normalize-space()")
    for i in range(len(stars)):
        stars[i]        = stars[i].xpath("normalize-space()")

    for i in range(len(programming_languages)):
        parsed_rows.append({
            "RepoLink" :            repo_links_names[i],
            "Description":          descriptions[i],
            "Stars":                stars[i],
            "ProgrammingLanguage":  programming_languages[i],
        })


    return json.dumps(parsed_rows, indent=2)


