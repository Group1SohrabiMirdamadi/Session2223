import requests
import re


# response = requests.request('GET' , "http://ma-web.ir/maktab52/" , params={"name" : "akbar"})
response = requests.request('GET' , "https://en.wikipedia.org/wiki/akbar" )
text1 =response.text

with open("wiki.html" , 'w' , encoding= 'UTF-16') as f:
    f.write(text1)
    print("done!!!!!")

pattern= r"(<h[1-6]>)(?P<content>.*)(</h[1-6]>)"
pattern1= r"(<p>)(?P<content>.*)(</p>)"

res = re.finditer(pattern , text1)
res1 = re.finditer(pattern1 , text1)

# for i in res :
#     print(i.group("content"))
# print ("____________________________")
# print ("____________________________")
# print ("____________________________")
# print ("____________________________")
#
# for i in res1:
#     print(i.group("content"))

with open("header.txt" ,'w') as f :
    for i in res:
        f.write(str(i.group("content").encode("UTF-8"))+ "\n")

with open("paragraph.txt" , 'w') as f:
    for i in res1:
        f.write(str(i.group("content").encode("UTF-8")) + "\n")

# pattern = r"(\<\h\d{}\>)("

