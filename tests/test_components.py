
from googletrans import Translator


def test_translate():
    translator = Translator(service_urls=['translate.google.co.kr'])
    ret = translator.translate(['apple pie', 'orange', 'potato'], dest='zh-cn', src='en')
    assert len(ret) == 3
    assert ret[1].text
    assert ret[1].text != 'orange'
