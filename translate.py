import sys
import os

from utils import grouper

import webvtt
from googletrans import Translator


help_txt = """
Translate a given vtt subtitle file.
"""

file_in = sys.argv[1]
dst_lang = 'zh-cn'
file_out = file_in + '.BI.vtt'

vtt_src = webvtt.read(file_in)
vtt_ret = webvtt.WebVTT()

ori_list = [v.text or "" for v in vtt_src]
translator = Translator()

# # Group lines by some number so the translation payload is not too large
# translated = []
# for g in grouper(ori_list, 100):
#     # print(g)
#     trans = translator.translate(list(g), dest=dst_lang, src='en')
#     translated += [t.text for t in trans]

for i in range(len(vtt_src)):
    ori_text = vtt_src[i].text
    translated_text = translator.translate(vtt_src[i].text, dest=dst_lang, src='en').text
    # translated_text = translated[i]
    print(f'[{i}/{len(vtt_src)}]: {translated_text}')
    
    vtt_ret.captions.append(webvtt.Caption(
        vtt_src[i].start,
        vtt_src[i].end,
        [
            translated_text,
            ori_text
        ]
    ))

print(vtt_ret)


with open(file_out, 'w', encoding='utf8') as fd:
    vtt_ret.write(fd)
