#-*-coding:utf-8-*-
import os
import re
pattern_text = u'''表白[0-9]+:[\u4e00-\u9fa5，。；  ？！,.;:：“‘'"?!（）()~0-9A-Za-z\n]+'''
pre = os.getcwd()
sum = 0
for suf in os.listdir(pre):
    if suf == "todo.list" or suf == "getText.py" or suf == "list.txt":
        continue
    sum += 1
    dirr = pre + "/" + suf
    print(dirr)
    with open(dirr+"/index.html", "r") as f:
        text = f.read().decode('utf8')
        ans = re.findall(pattern_text, text)
        for s in ans:
            with open(pre +"/list.txt", "a") as fw:
                fw.write(re.search(u'''[0-9]+:(.*)''', s).group(1).encode("utf-8")+"\n")
    pattern_time = r'''publish_time = "[0-9]+-[0-9]+-[0-9]+"'''
    time_text = re.findall(pattern_time, text)
    try:
        time = re.findall('[0-9]+-[0-9]+-[0-9]+', time_text[0])
    except IndexError:
        pass
    print(time[0])
print(sum)