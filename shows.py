import requests
import BeautifulSoup


print("Retrieving show calendars...")
eget = requests.get('http://www.echostage.com')
print("Echostage retrieved!")
sget = requests.get('http://www.baltimoresoundstage.com')
print("Soundstage retrieved!")
nget = requests.get('http://www.930.com/concerts')
print("930 club retrieved!")
#fget = requests.get('http://fillmoresilverspring.com/event-calendar')
#print("Fillmore retrieved!")

if eget.status_code == 200 and sget.status_code == 200 and nget.status_code == 200:
	print("Successfully polled sites.")
else:
	print("Error contacting one or more websites.")

echo = BeautifulSoup.BeautifulSoup(eget.content)
sound = BeautifulSoup.BeautifulSoup(sget.content)
nine = BeautifulSoup.BeautifulSoup(nget.content)
#filmore = BeautifulSoup.BeautifulSoup(fget.content)

ehead = BeautifulSoup.BeautifulSoup(str(echo.findAll('div', { "class" : "eventheadliner" }))).text.split(',')
eopen = BeautifulSoup.BeautifulSoup(str(echo.findAll('div', { "class" : "eventsupporting" }))).text.split(',')
edoors = BeautifulSoup.BeautifulSoup(str(echo.findAll('div', { "class" : "eventdoors" }))).text.split(',') 
edate = BeautifulSoup.BeautifulSoup(str(echo.findAll('div', { "class" : "eventdate" }))).text.replace('2013,',';').replace('2014,',';').split(';')
#edate = edate.replace('2013,',';')

elen = len(ehead)
print "Length:", elen
print "Echostage Shows:\n"
for i in range(0,elen):
	print ehead[i].strip('[]')
	if (eopen[i].strip('[]') != ""):
		print eopen[i].strip('[]')
	else:
		print "***No Opener Announced***"
	print "Doors:", edoors[i].strip('[]')
	print "Date:", edate[i].strip('[],'), "\n"
