#-*-coding:utf-8-*-
import re

pattern_text = u'''表白[0-9]+:[\u4e00-\u9fa5，。；？！,.;:：“‘'"?!（）()~0-9]+'''
with open("index.html", "r") as f:
    text = f.read().decode('utf8')
    ans = re.findall(pattern_text, text)
    for s in ans:
        print(re.search(u'''[0-9]+:(.*)''', s).group(1))
pattern_time = r'''publish_time = "[0-9]+-[0-9]+-[0-9]+"'''
time_text = re.findall(pattern_time, text)
time = re.findall('[0-9]+-[0-9]+-[0-9]+', time_text[0])
print(time[0])
