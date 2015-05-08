import sys
import urllib.request
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
    return json.JSONEncoder().encode(data)


def main():
    if len(sys.argv) == 2:
        output_file = open('out.json', 'w')
    if len(sys.argv) == 3:
        output_file = open(sys.argv[1], 'w')
        usage_msg = "gdoc-json-parser URL OUTPUT\n" + \
            "Convert spreadsheet in URL to json."
        print('Wrong number of operands')
        print(usage_msg)
        return

    url_id = sys.argv[1].rstrip('/').split('/')[-1]
    url = "https://spreadsheets.google.com/feeds/list/" + \
        url_id + "/od6/public/values?alt=json"
    try:
        response = urllib.request.urlopen(url)
        raw_data = json.loads(response.read().decode())
    except urllib.error.URLError:
        print('failed to open url')
        return

    data = clean_json(raw_data)
    output_file.write(data)
    output_file.close()
    print('Output to ' + output_file)

if __name__ == '__main__':
    main()
