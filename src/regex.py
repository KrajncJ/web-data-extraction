
import json
import re


def parse_overstock(html):
    print('not implemented')


def parse_amazon(html):
    print('not implemented')


def parse_rtvslo(html):
    # Author name
    author = re.findall('<div class="author-name">(.+?)</div>', html)[0]
    # Published time
    pub_time = re.findall('<div class="publish-meta">\n\t\t(.+?). (.+?) ob (.+?)<br>', html)
    pub_time = pub_time[0][0] + ". " + pub_time[0][1] + " ob " + pub_time[0][2]
    # Title
    title = re.findall('<h1>(.+?)</h1>', html)[0]
    # Subtitle
    subtitle = re.findall('<div class="subtitle">(.+?)</div>', html)[0]
    # Lead
    lead = re.findall('<p class="lead">(.+?)</p>', html)[0]
    # Content
    content = re.findall('<article class="article">((.|\n|\r)+)</article>', html)[0]

    return json.dumps({
        "Author": author,
        "PublishedTime": pub_time,
        "Title": title,
        "SubTitle": subtitle,
        "Lead": lead,
        "Content": content,
    }, indent=2)

