from datetime import datetime

f = open("oldtime.txt",'r')

def transfertime(oldformat):
	datetimeobject = datetime.strptime(oldformat,'%Y/%m/%d')
	newformat = datetimeobject.strftime('%b %d, %Y')
	return(newformat)

with open("newtime.txt",'w') as g:
	for row in f:
		newdate = transfertime(row.strip())
		g.write(str(newdate)+"\n")
