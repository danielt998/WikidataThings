import re
import sys

category_translations=['Category', 'Kaarangay', 'Categori', 'Kategori']
def is_probably_category(line):
    for translation in category_translations:
        if translation in line:
            return True
    return False


#WARNING: Do not use on all items, only on specific ones
#TODO:find a solution to the lat/long thing when it comes to doing descs
#for now, maybe we should exclude all of them, as the lat/lon may be used in cases where the rest of the desc is the same
#FILE = 'ceb_labels_descs_v2.tsv'
FILE = sys.argv[1]
LANG = sys.argv[2]#'ceb'
FILTER_WORD = sys.argv[3]
new_desc_regex = re.compile("\((.*)\)")
with open(FILE) as infile:
    for line in infile:
        if FILTER_WORD and FILTER_WORD in line and not is_probably_category(line):
            segs = line.split('\t')
            item = segs[0]
            label = re.sub(' \(.*\)', '', segs[1])
            existing_desc = segs[2]
            print(item + "\t" + 'L' + LANG + "\t" + label)
            if not existing_desc.strip():
                new_desc = new_desc_regex.search(segs[1]).group(1)
                print(item + "\t" + 'D' + LANG + "\t" + new_desc)
