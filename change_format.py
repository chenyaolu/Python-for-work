import calendar
import re

# 创建日期格式转换 2019-01-20T23:39:03.000-0800 变成 30/Jan/19 11:39 PM
def change_Created(Created):
    date = Created[:10]
    return date
    # newdate = date[2]+"/"+calendar.month_abbr[int(date[1])]+"/"+date[0][2:4]
    # t = Created.split("T")[1][:5]
    # if int(t[:2].zfill(2)) > 12:
    #     return str(newdate) + " " + t + " " + "PM"
    # else:
    #     return str(newdate) + " " + t + " " + "AM"


def change_data(item):
    p = re.compile("name='(.*?)',")
    nl = p.findall(item)
    return nl

# print(change_Created("2019-01-20T23:39:03.000-0800"))
