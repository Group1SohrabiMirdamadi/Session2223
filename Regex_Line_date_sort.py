import re
from datetime import datetime

pattern = r"(?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2})\s*(?P<hour>\d{2})\:(?P<minute>\d{2})\:(?P<sec>\d{2})"

# with open("test.txt", "r") as file:
#     text = file.read()
#     search_date = re.finditer(pattern, text)
text ="""
Neque est adipisci dolor labore numquam temp 1995-01-01 04:42:47 ora etincidunt.
Numquam quaerat dolorem ut sit 1997-11-25 21:10:01 .
Tempora quiquia ipsum numquam quaer 2005-09-06 09:41:28 at.
Sit sit amet amet  1994-08-09 21:11:06 sit quiquia voluptatem adipisci.
Quisquam quaerat tempora ut velit numquam dolo 2006-11-03 03:31:15 r.
Dolor dolorem dolor a 1999-02-20 12:13:08 dipisci.
Amet si 1992-05-28 16:30:26 t quiquia quiquia est labore neque etincidunt.
Sit porro velit dolorem etincidun 1993-04-11 16:21:21 t magnam.
Consectetur ut non non consect 1992-05-24 07:43:16 etur ipsum ut dolorem.
Adipisci dolor temp 1995-02-12 15:55:26 ora quiquia est consectetur quisquam tempora.
Dolore modi etincidunt quaerat d 2009-05-13 10:37:14 olorem.
Amet est ipsu 2001-07-30 22:20:32 m tempora tempora eius.
Dolor porro velit quaerat  2020-09-01 10:54:22 porro modi labore consectetur.
Labore consectetur dolore magnam etin 1992-05-31 10:42:50 cidunt modi velit.
Numquam  1996-01-24 07:11:33 quisquam sed est tempora.
Numqu 2003-04-13 08:41:28 am ipsum porro numquam tempora tempora etincidunt sit.
Am 2003-12-16 07:20:40 et quiquia neque magnam.
Dolor porro etincid 2019-10-04 03:23:32 unt ipsum quaerat neque adipisci.
 2008-02-15 04:52:01 Labore voluptatem quiquia eius velit adipisci.
Consectetur quaerat aliquam velit quaerat la 2001-02-13 20:03:10 bore sed dolorem.
"""

search_date = re.finditer(pattern, text)
date_list = []
for i in search_date:
    date_list.append(datetime(year=int(i.group("year")), month=int(i.group("month")), day=int(i.group("day")),
                              hour=int(i.group("hour")), minute=int(i.group("minute")), second=int(i.group("sec"))))


str_date_list = [date.strftime("%Y-%m-%d %H:%M:%S") for date in sorted(date_list)]

line_list = text.split("\n")

sorted_line_list = []
for sort_line in str_date_list:
    for line in line_list:
        if sort_line in line:
            sorted_line_list.append(line)

with open("SortedList.text", "w") as file:
    for line in sorted_line_list:
        file.write(line)
        file.write("\n")




