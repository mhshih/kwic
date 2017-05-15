import csv
from collections import defaultdict

class ItemName:
    def __init__(self,itemname):
        self.wordroot=''
        self.focus=''

#Build word root dictionary.
ItemNames=dict()
d=dict() #d[itemname]=wordroot
for line in csv.reader(open('item_utf8.txt')):
    itemid,itemname,ucode,toda,truku,isroot,notsure,wordroot,focus,todar,trukur,hasbranch,wordclass,mainMeaningWordclass,meaning,meaningEn,sentence=line[:17]
    d[itemname]=wordroot
    It=ItemName(itemname)
    It.wordroot=wordroot
    It.focus=focus
    ItemNames[itemname]=It

#Read text.
from os import listdir
dd=defaultdict(int)
rf=defaultdict(int)
text_dir='text/'
for filename in listdir(text_dir):
    for line in open(text_dir+filename):#,encoding='cp950'):
        for word in line.split():
            itemname=word.lower().strip(',.?!;')
            dd[itemname]+=1
            if itemname in d:
#           wordroot=d[itemname]
                wordroot=ItemNames[itemname].wordroot
                rf[wordroot]+=1

f=open('word_freq_root_freq_focus.tsv','w')
for itemname,item_freq in dd.items():
    if itemname in d:
#       wordroot=d[itemname]
        wordroot=ItemNames[itemname].wordroot
        focus=ItemNames[itemname].focus
        root_freq=rf[wordroot]
    else:
        wordroot='NoRoot'
        focus='NoFocus'
        root_freq=0
    print('%s,%d,%s,%d,%s' % (itemname,item_freq,wordroot,root_freq,focus))
    f.write('%s \t %d \t %s \t %d \t %s\n' % (itemname,item_freq,wordroot,root_freq,focus))
f.close()
