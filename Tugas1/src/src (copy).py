import mechanicalsoup
import json
import html
import os
from bs4 import BeautifulSoup
from datetime import timedelta
from datetime import datetime
import copy
fileJson = "hasilJson.json"



def hitungPembagianTahun(fromDate,toDate):
    """
    fromDate: datetime object
    toDate: datetime object
    
    ret: list of list datetime 
    """
    hasil = []
    boundYear = timedelta(365)
    satuHari =  timedelta(1)

    now = datetime(fromDate.year,fromDate.month,fromDate.day)
    while (now<=toDate):
        if( now + boundYear <= toDate ):
            tup = (now,now+boundYear)
            hasil.append(tup)
            now = now + boundYear + satuHari
        else:
            tup = (now,toDate)
            hasil.append(tup)
            now = toDate+satuHari
    return hasil


def getNumberOfPage(soup):
    """
    soup: BeautifulSoup object
    """
    hasilCari  =  soup.find_all('font')
    hasilSplit = (hasilCari[len(hasilCari)-2]).text.split()
    return int(hasilSplit[1])

def openJson(filename):
    """
    filename:  str namafilenya
    ret: jsonObject
    """
    try:
        with open(filename) as json_file:  
            data = json.load(json_file)
            return data
    except Exception as detail:
        data={}
        return data

def saveJson(filename,jsonObj):
    """
    filename: str namafilenya
    jsonObj: dict object json yang ingin disimpan ke filename
    """
    with open(filename, 'w') as outfile:  #open
        json.dump(jsonObj, outfile)


def saveAllDataInSoup(soup):
    """
    soup: BeautifulSoup object
    """
    #Inisiasi Awal
    dataGempa = soup.select("pre + table")[0].select("tr") # Index 0 adalah nama kolom
    data = openJson(fileJson) #buka file jsonnya
    n = len(data) #panjang data sekarang
    ########
    #Build Colom Name
    colomNames = dataGempa[0].find_all("div") #reduce tag html to just text colom name
    for i in range(0,len(colomNames)):
        colomNames[i] = colomNames[i].text
    #################

    #Build Data to json
    for i in range(1,len(dataGempa)):
        dataColoms = dataGempa[i].find_all("div")
        temp = {}
        for j in range(0,len(dataColoms)):
            temp[colomNames[j]] = dataColoms[j].text
        data[i+n] = temp

    #save to json
    saveJson(fileJson,data)

def prettifySaveJson(filename):
    """
    filename: nama file json
    """
    jsonObj = openJson(filename)
    with open(filename, 'w') as outfile:  #open
        hasilString = json.dumps(jsonObj,indent=4)
        outfile.write(hasilString)
    



# Proses Input dari User
print("Jangka Waktu Maksimal 1 tahun")
startDay = input("Starting Day (date/month/year) : ").split("/")
endDay = input("Ending Day (date/month/year) : ").split("/")
topLatitude = input("Top Latitude : ")
rightLongitude = input("Right Longitude : ")
bottomLatitude = input("Bottom Latitude : ")
leftLongitude = input("Left Longitude : ")
minSR = input("Minimum Magnitude SR : ")
maxSR = input("Maximum Magnitude SR : ")
minDepth = input("Minimum Depth(Km) : ")
maxDepth = input("Maximum Depth(Km) : ")
print()
###################################

####Inisiasi Pembagian Tahun
fromDate = datetime(int(startDay[2]),int(startDay[1]),int(startDay[0]))
toDate = datetime(int(endDay[2]),int(endDay[1]),int(endDay[0]))
listTahun = hitungPembagianTahun(fromDate,toDate)
######


for dateE in listTahun:
    #### Initiate Tanggal

    startDay = str(dateE[0].day)
    startMonth = str(dateE[0].month)
    startYear = str(dateE[0].year)

    endDay = str(dateE[1].day)
    endMonth = str(dateE[1].month)
    endYear = str(dateE[1].year)
    tanggal = startDay+"/"+startMonth+"/"+startYear + " to " + endDay+"/"+endMonth+"/"+endYear

    print(tanggal)

    ####Login ke Repo gempa Indonesia
    print("Log in to repogempa .........")

    loginUrl = "http://repogempa.bmkg.go.id/login.php"

    br = mechanicalsoup.StatefulBrowser()
    br.open(loginUrl)

    br.select_form()
    br["userid"] = "bmkg"
    br["passwd"] = "g3mp4Bumi"
    br.submit_selected()
    ##################################




    ####Memasukkan detail data scraping dari use ke form
    print("Input necessary data .........")

    br.select_form()
    br['start_day'] = startDay
    br['start_month'] = startMonth
    br['start_year'] = startYear
    br['end_day'] = endDay
    br['end_month'] = endMonth
    br['end_year'] = endYear
    br['top_lat'] = topLatitude
    br['bot_lat'] = bottomLatitude
    br['right_long'] = rightLongitude
    br['left_long'] = leftLongitude
    br['min_mag'] = minSR
    br['max_mag'] = maxSR
    br['min_depth'] = minDepth
    br['max_depth'] = maxDepth
    br.submit_selected(btnName="Submit")
    ##################################

    ####Ancang2 Scraping:Inisiasi
    counterData = 0
    soup = br.get_current_page()
    totalPage = getNumberOfPage(soup)
    data = {}
    rootUrl = os.path.dirname(br.get_url())+"/"
    ##################################

    print("Mulai Scraping .........")

    ####Mulai Scraping
    for i in range(1,totalPage+1):
        print(tanggal + " Page "+str(i)) #give status
        saveAllDataInSoup(soup)
        #updating browser or br link to next page
        listLink = soup.select("table table table table")[1].select("a")
        nextLink = listLink[len(listLink)-2]['href']
        br.open(rootUrl+nextLink)
        soup = br.get_current_page()
    #################

####Prettify Json
prettifySaveJson(fileJson)