import requests
import datetime

#data gathering
#todo read in a list of stock symbols from a json file
#todo show date range for all symbol data based on existing downloads
#todo provide link to download fresh data files then refresh list
#todo parse all symbol data files into a big python dictionary



Symbol = "AAPL"
YearsOfData = 1

OutFile = Symbol + ".csv"

StopDate = str(datetime.date.today())

Year = datetime.date.today().year - YearsOfData
Month = datetime.date.today().month
Day = datetime.date.today().day

StartDate = str.format(f"{Year:04d}-{Month:02d}-{Day:02d}")

NasdaqURL = str.format("https://www.nasdaq.com/api/v1/historical/{}/stocks/{}/{}", Symbol, StartDate, StopDate)

print("Downloading from: " + NasdaqURL)

# Open the URL and save the contents

####
#### THIS IS WHERE IT HANGS ....
####

WebData = requests.get(NasdaqURL)


f = open(OutFile, 'w')
f.write(WebData.content)
f.close()
