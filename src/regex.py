
import json
import re


def parse_overstock(html):

    # Match rows
    matched = re.findall('<tr bgcolor="(#ffffff|#dddddd)">'
                         ' \n<td valign="top" align="center">' 
                         ' \n<table>((.|\n|\r)+?)</table></td>' # unused data
                         '<td valign="top">((.|\n|\r)+?)<b>((.|\n|\r)+?)</b></a><br> \n'  # last value is title
                         '<table>((.|\n|\r)+?)<table> \n<tbody>'
                         '<tr>((.|\n|\r)+?)<td align="left" nowrap="nowrap"><s>((.|\n|\r)+?)</s></td></tr> \n'  # list price
                         '<tr>((.|\n|\r)+?)<td align="left" nowrap="nowrap"><span class="bigred"><b>((.|\n|\r)+?)</b></span></td></tr> \n'  # price
                         '<tr>((.|\n|\r)+?)<td align="left" nowrap="nowrap"><span class="littleorange">((.|\n|\r)+?) \(((.|\n|\r)+?)\)</span></td></tr>'  # you save
                         '((.|\n|\r)+?)'
                         '<td valign="top"><span class="normal">((.|\n|\r)+?)</td>'  # description
                         '((.|\n|\r)+?)'
                         , html)
    parsed_rows = []
    # Process each row
    for row in matched:
        parsed_rows.append({
            "Title": row[5],
            "ListPrice": row[11],
            "Price": row[15],
            "Saving": row[19],
            "SavingPercent": row[21],
            "Content": clean_html(row[25])
        })

    return json.dumps(parsed_rows, indent=2)


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
    content = ""

    ct_arr = re.findall('<[p][^>]*>(.+?)</[p]>', re.findall('<article class="article">(.+?)</article>',html)[0])
    for row in ct_arr:
        cleaned = clean_html(row)
        content += cleaned

    return json.dumps({
        "Author": author,
        "PublishedTime": pub_time,
        "Title": title,
        "SubTitle": subtitle,
        "Lead": lead,
        "Content": content,
    }, indent=2, ensure_ascii=False)


def parse_github(html):
    # Page name
    topic = re.findall('<h1 class="text-normal mb-1">(.+?)</h1>', html)[0]
    description = re.findall('<p>(.+?)</p>', html)[0]
    repos = re.findall('<span class="Counter">(.+?)</span>', html)[0]

    programming_lngs = re.findall('<span itemprop="programmingLanguage">(.+?)</span>', html)
    stars = re.findall('<svg class="octicon octicon-star mr-1" viewBox="0 0 14 16"(?:(?:.|\n|\r)+?)</svg>((?:.|\n|\r)+?)</a>', html)
    descriptions = re.findall('<div class="text-gray mb-3 ws-normal">((?:.|\n|\r)+?)</div>', html)
    repo_links = re.findall('<h3 class="f3">(?:(?:.|\n|\r)+?)<a href="((?:.|\n|\r)+?)">(?:(?:.|\n|\r)+?)</h3>',html)

    repoList = []

    for i in range(len(programming_lngs)):
        repoList.append({
            'RepoLink': repo_links[i],
            'Description': clean_html(descriptions[i].strip()),
            'Stars': stars[i + 1].strip(),
            'ProgrammingLanguage': programming_lngs[i],
        })

    data = {
        "Topic": topic,
        "Description": description,
        "Repositories": repos,
        "RepoList": repoList,
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


