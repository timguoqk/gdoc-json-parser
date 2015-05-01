import sys
import urllib
import json
from optparse import OptionParser

if __name__ == '__main__':
    version_msg = "%prog 0.1"
    usage_msg = "%prog [OPTION] URL OUTPUT\n" + \
        "Convert spreadsheet in URL to json."
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)

    options, args = parser.parse_args(sys.argv[1:])
    if len(args) != 1 and len(args) != 2:
        parser.error("wrong number of operands")

    url_id = args[0].split('/')[-1]
    url = "https://spreadsheets.google.com/feeds/list/" + \
        url_id + "/od6/public/values?alt=json"
    response = urllib.urlopen(url)
    # TODO: try and catch
    data = json.loads(response.read())

    # TODO: clean data
    output_file = open(args[1], 'w')
    output_file.write(data)
    output_file.close()
