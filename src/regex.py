
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
            "Content": cleanhtml(row[25])
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

    ct_arr = re.findall('<[p][^>]*>(.+?)</[p]>', re.findall('<article class="article">[\s\S]*?</article>',html)[0])
    for row in ct_arr:
        cleaned = cleanhtml(row)
        content += cleaned

    return json.dumps({
        "Author": author,
        "PublishedTime": pub_time,
        "Title": title,
        "SubTitle": subtitle,
        "Lead": lead,
        "Content": content,
    }, indent=2, ensure_ascii=False)


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def parse_amazon(html):
    print('not implemented')