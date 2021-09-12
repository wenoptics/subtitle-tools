import sys
import os

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
translated = translator.translate(ori_list, dest=dst_lang, src='en')

for i in range(len(vtt_src)):
    ori_text = vtt_src[i].text
    # translated_text = translator.translate(vtt_src[i].text, dest=dst_lang)
    translated_text = translated[i].text
    print(translated_text)
    
    vtt_ret.captions.append(webvtt.Caption(
        vtt_src[i].start,
        vtt_src[i].end,
        [
            translated_text,
            ori_text
        ]
    ))

print(vtt_ret)


with open(fileOut, 'w', encoding='utf8') as fd:
    vtt_ret.write(fd)
