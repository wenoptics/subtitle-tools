import sys
import os

import webvtt


help_txt = """
Combine two vtt subtitle files into one. This may be usageful to make a bi-lingual subtitle file

The files needs to have identical time blocks.
""" 

file1 = sys.argv[1]
file2 = sys.argv[2]
fileOut = file2 + '.BI.vtt'

vtt1 = webvtt.read(file1)
vtt2 = webvtt.read(file2)
vtt_ret = webvtt.WebVTT()

for i in range(len(vtt1)):
    vtt_ret.captions.append(webvtt.Caption(
        vtt1[i].start,
        vtt1[i].end,
        [
            vtt1[i].text,
            vtt2[i].text,
        ]
    ))

print(vtt_ret)


with open(fileOut, 'w', encoding='utf8') as fd:
    vtt_ret.write(fd)
