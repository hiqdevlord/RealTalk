
from urllib.request import urlopen
from urllib.error import URLError

#get the first word between two strings
def get_first_btwn(str_start, str_end, str_full):
    if str_full.find(str_start) == -1 or str_full.find(str_end) == -1:
        return ""
    size_start = len(str_start)
    size_end = len(str_end)
    cur_text_bracket = str_full[int(str_full.find(str_start)):int(str_full.find(str_end) + size_start)]
    return cur_text_bracket[size_start:len(cur_text_bracket)-size_end]

#get all the words between two strings
def get_multi_btwn(str_start, str_end, str_full):
    out = []
    str_start = str(str_start)
    str_end = str(str_end)
    str_full = str(str_full)
    size_start = len(str_start)
    size_end = len(str_end)
    while str_start in str_full:
        cur_text_bracket = str_full[int(str_full.find(str_start)):int(str_full.find(str_end) + size_start)]
        cur_text = cur_text_bracket[size_start:len(cur_text_bracket)-size_end]
        str_full = str_full.replace(cur_text_bracket, ' ', 1)
        out.append(cur_text)
    return out

#get website source
def get_src(url):
    try:
        return urlopen(url).read()
    except URLError as e:
        print('Error, could not read file:', e)
        return ""

# region Test_Bot
#example bot to find front page headlines from reddit

full_website = get_src('https://www.reddit.com/')
results_full = get_multi_btwn('<p class="title">', '</p>', full_website)
results = []
for i in range(0,len(results_full)):
    results.append(get_first_btwn('>','</a>',results_full[i]))

for i in range(0,len(results)):
    print(results[i],"\n")

# endregion



