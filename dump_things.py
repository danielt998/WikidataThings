from utils import *

DELIMITER='\t'
#FILE='/media/dtm/Seagate Expansion Drive/wikidata-20181231-all.json'
FILE='/media/dtm/wikidata/first1000lines.json'
OUTPUT_FILE_PREFIX='v3_output/'
OUTPUT_FILE_SUFFIX='_labels_descs_v3.tsv'
count=0
#langs=['ceb', 'cy', 'en', 'fr', 'de', 'zh-cn', 'zh', 'zh-hans', 'zh-hant','zh-tw', 'es']
langs=['sv', 'war']

files={}
for lang in langs:
    files[lang] = open(OUTPUT_FILE_PREFIX + lang + OUTPUT_FILE_SUFFIX, 'a+')


def do_filtering(lang_str, desc_str):
    return '(' in lang_str


with open(FILE) as infile:
    for line in infile:
        if line.startswith("[") or line.startswith("]"):
            continue
            if line.startswith("["):
                line = line[1:]
            if line.startswith("]"):
                continue
        i = ''
        line = line.rstrip()
        if line.endswith(","):
            i = json.loads(line[:-1])
        else:
            i = json.loads(line)#TODO:test this works on the last line...
        if i != '':
            continue
        output_string = ''
        for lang in langs:
            lang_str = getLangString(lang, i)
            desc_str = getDesc(lang, i)
            if not do_filtering(lang_str, desc_str):
                continue
            output_string = output_string + getID(i) + DELIMITER + lang_str + DELIMITER + desc_str
            files[lang].write(output_string + '\n')

        #print(str+getDesc('en',i)+DELIMITER+getTypes(line)+DELIMITER+getCountry(line)+DELIMITER+getRegions(line))
            #print(str)
