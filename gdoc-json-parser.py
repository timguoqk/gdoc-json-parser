import sys
import urllib
import json


def clean_json(raw_data):
    entries = raw_data['feed']['entry']
    cols = [x for x in entries[0] if x.startswith('gsx$')]
    data = []
    for entry in entries:
        row = {}
        for col in cols:
            row[col[4:]] = entry[col]['$t']
        data.append(row)
    return data

if __name__ == '__main__':
    if len(sys.argv) == 0:
        usage_msg = "%prog URL OUTPUT\n" + \
            "Convert spreadsheet in URL to json."
        print(usage_msg)
        return
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print("wrong number of operands")

    url_id = sys.argv[0].split('/')[-1]
    url = "https://spreadsheets.google.com/feeds/list/" + \
        url_id + "/od6/public/values?alt=json"
    try:
        response = urllib.urlopen(url)
    except Exception as e:
        print("failed to open url")
        raise e

    raw_data = json.loads(response.read())
    data = clean_json(raw_data)
    if len(sys.argv) == 1:
        output_file = open('out.json', 'w')
    else:
        output_file = open(sys.argv[1], 'w')
    output_file.write(data)
    output_file.close()
