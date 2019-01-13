import re
import sys

#WARNING: Do not use on all items, only on specific ones
#TODO:find a solution to the lat/long thing when it comes to doing descs
#for now, maybe we should exclude all of them, as the lat/lon may be used in cases where the rest of the desc is the same
LANG = sys.argv[2]#'ceb'
#FILE = 'ceb_labels_descs_v2.tsv'
FILE = sys.argv[1]
new_desc_regex = re.compile("\((.*)\)")
FILTER_WORD = sys.argv[3]
with open(FILE) as infile:
    for line in infile:
        if FILTER_WORD and FILTER_WORD in line:
            segs = line.split('\t')
            item = segs[0]
            label = re.sub(' \(.*\)', '', segs[1])
            existing_desc = segs[2]
            print(item + "\t" + 'L' + LANG + "\t" + label)
            if not existing_desc.strip():
                new_desc = new_desc_regex.search(segs[1]).group(1)
                print(item + "\t" + 'D' + LANG + "\t" + new_desc)
