# In indeed where we search the job and its location then the URL becomes something like this https://in.indeed.com/jobs?q=”+job+”&l=”+Location
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.indeed.com/jobs?q=Data%20Engineer&l&vjk=460cce461bec5669")
soup = BeautifulSoup(page.content, 'html.parser')

dejob = soup.find(id= 'resultsBodyContent')

dejob.prettify()

detitle = [deti.get_text() for deti in dejob.select(".tapItem .jobTitle")]

desdesc = [desd.get_text() for desd in dejob.select(".tapItem .job-snippet")]

desal = [desa.get_text() for desa in dejob.select(".tapItem .salaryOnly")]

deloc = [delo.get_text() for delo in dejob.select(".tapItem .companyLocation")]

deconame = [deco.get_text() for deco in dejob.select(".tapItem .companyName")]

# print(detitle)
# print(desdesc)
# print(desal)
# print(deloc)
# print(deconame)

dataengineeringjobs = pd.DataFrame({
    "Title": detitle,
    "Short Description": desdesc,
    "Salary": desal,
    "Location": deloc,
    "Company Name": deconame
})
print(dataengineeringjobs)


"""Save as .csv file"""
dataengineeringjobs.to_csv("dataengineeringjobs.csv", index=False)























