import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook

excel = openpyxl.Workbook()
sheet = excel.active

sheet.append(["College Name","Location","State","Entrance Exam","Fees","Rating","College Affiliation","Course Name","Available Courses"])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'}

Hyderabad_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&state=25&city=950%2C1365%2C59%2C97%2C73%2C72%2C1253%2C101%2C25979%2C2358%2C359%2C450%2C128%2C936%2C919&stream=1",headers=headers)
Hyd = BeautifulSoup(Hyderabad_colleges.text, "html.parser")

Andhra_Colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&state=1&city=51%2C142%2C395%2C1357%2C1313%2C70%2C248%2C12%2C346%2C219%2C510%2C143%2C341%2C125%2C1173%2C817%2C979%2C1150%2C1227%2C416&fee=500000&stream=1",headers=headers)
Ap = BeautifulSoup(Andhra_Colleges.text, "html.parser")

Kerala_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&fee=1000000&state=13&city=131%2C6%2C77%2C43%2C340%2C102%2C1032%2C410%2C133%2C80%2C284%2C312%2C318%2C86%2C509&stream=1",headers=headers)
Kerala = BeautifulSoup(Kerala_colleges.text, "html.parser")

Karnataka_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&fee=1000000&state=12&city=715%2C19%2C4347%2C95%2C948%2C711%2C88%2C10858%2C1109%2C1312%2C162%2C24944%2C167%2C26%2C278&stream=1",headers=headers)
Karnataka = BeautifulSoup(Karnataka_colleges.text, "html.parser")

Maharastra_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&fee=1000000&state=15&city=41038%2C110%2C1138%2C96%2C98%2C337%2C14%2C123%2C1156%2C9%2C1210%2C129%2C288%2C432%2C3595&stream=1",headers=headers)
Maharastra = BeautifulSoup(Maharastra_colleges.text, "html.parser")

Delhi_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&fee=1000000&city=48%2C100%2C89%2C124%2C44%2C436%2C67%2C151%2C24%2C402%2C404%2C2553%2C29%2C316%2C361&state=43&stream=1",headers=headers)
Delhi = BeautifulSoup(Delhi_colleges.text, "html.parser")

Uttar_pradesh_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&sort_by=3&degree=2&fee=1000000&city=48%2C89%2C29%2C82%2C927%2C178%2C993%2C7%2C1130%2C1168%2C193%2C1%2C90%2C139%2C5061&state=28&stream=1",headers=headers)
Uttar_pradesh = BeautifulSoup(Uttar_pradesh_colleges.text, "html.parser")

Harayana_colleges = requests.get("https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?entity_type=2&degree=2&fee=1000000&city=124%2C44%2C145%2C347%2C436%2C67%2C905%2C24%2C14%2C934%2C402%2C5405%2C404%2C8%2C122&state=8&stream=1",headers=headers)
Harayana = BeautifulSoup(Harayana_colleges.text, "html.parser")

hyd_colleges = Hyd.find("body").find("div",class_="undefined").find_all("div")

for hyd_college in hyd_colleges:
    try:
        name = hyd_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = hyd_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = hyd_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = hyd_college.find("li").find("a").text

        Fees = hyd_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(hyd_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = hyd_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = hyd_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(hyd_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

ap_colleges = Ap.find("body").find("div",class_="undefined").find_all("div")

for ap_college in ap_colleges:
    try:
        name = ap_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = ap_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[1]

        state = ap_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = ap_college.find("li").find("a").text

        Fees = ap_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(ap_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = ap_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = ap_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(ap_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])

        
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])

    except:
        continue

kerala_colleges_data = Kerala.find("body").find("div",class_="undefined").find_all("div")

for kerala_college in kerala_colleges_data:
    try:
        name = kerala_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = kerala_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = kerala_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = kerala_college.find("li").find("a").text

        Fees = kerala_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(kerala_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = kerala_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = kerala_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(kerala_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

Karnataka_colleges_data = Karnataka.find("body").find("div",class_="undefined").find_all("div")

for Karnataka_college in Karnataka_colleges_data:
    try:
        name = Karnataka_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = Karnataka_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = Karnataka_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = Karnataka_college.find("li").find("a").text

        Fees = Karnataka_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(Karnataka_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = Karnataka_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = Karnataka_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(Karnataka_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

Maharastra_colleges_data = Maharastra.find("body").find("div",class_="undefined").find_all("div")

for Maharastra_college in Maharastra_colleges_data:
    try:
        name = Maharastra_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = Maharastra_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = Maharastra_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = Maharastra_college.find("li").find("a").text

        Fees = Maharastra_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(Maharastra_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = Maharastra_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = Maharastra_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(Maharastra_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

del_colleges = Delhi.find("body").find("div",class_="undefined").find_all("div")

for del_college in del_colleges:
    try:
        name = del_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = del_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = del_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = del_college.find("li").find("a").text

        Fees = del_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(del_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = del_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = del_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(del_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

uttar_colleges = Uttar_pradesh.find("body").find("div",class_="undefined").find_all("div")

for uttar_college in uttar_colleges:
    try:
        name = uttar_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = uttar_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = uttar_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = uttar_college.find("li").find("a").text

        Fees = uttar_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = float(uttar_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = uttar_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = uttar_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = int(uttar_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

Harayana_colleges_data = Harayana.find("body").find("div",class_="undefined").find_all("div")

for Harayana_college in Harayana_colleges_data:
    try:
        name = Harayana_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[0]

        location = Harayana_college.find("div",class_="tupple").find("h3").find("a").text.split(",")[-1]

        state = Harayana_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span").text.split(",")[1]

        entrance_exam = Harayana_college.find("li").find("a").text

        Fees = Harayana_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[1].text.split("₹")[1].split(" ")[0]

        Rating = int(Harayana_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between").find("span",class_="star_text").find("b").text.split("/")[0])

        College_Affiliation = Harayana_college.find("div",class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")\
            .find("div").find_all("span")[1].text

        course = Harayana_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].text.split("(")[0]

        no_course = float(Harayana_college.find("div",class_="snippet_block").find("ul",class_="snippet_list").find_all("li")[2].find("span").text.split("(")[1].split(" ")[0])
   
        print(name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course)
        sheet.append([name,location,state,entrance_exam,float(Fees)*100000,Rating,College_Affiliation,course,no_course])
    except:
        continue

print("Script started...")

# Right before saving
print("Saving file...")

excel.save(r"D:\My Projectss\Educational_Mapping_College_Data_Project.xlsx")

print("✅ Data saved successfully.")



