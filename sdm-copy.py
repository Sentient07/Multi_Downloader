#!/usr/bin/python
import re
import getpass
import os
import urllib2
import pycurl
import cStringIO
from threading import Thread
def authentication(user_id,passwd,ips):
 buffer1 = cStringIO.StringIO()
 c = pycurl.Curl() #object c is assigned the curl object
 c.setopt(c.URL, "https://10.1.0.10:8090/httpclient.html") 
 c.setopt(c.WRITEFUNCTION, buf.write)  #writes the out after running this code into that string buffer
 c.setopt(c.CONNECTTIMEOUT, 30)
 c.setopt(c.INTERFACE, ips) #sets the interface i.e IP address to bind the login
 c.setopt(c.TIMEOUT, 150)
 c.setopt(c.MAXREDIRS, 10)
 c.setopt(c.POSTFIELDS, 'username='+user_id+'&password='+passwd+'&mode=191')  #sets to the login field password and username
 c.setopt(c.COOKIEFILE, 'cookies.txt')
 c.setopt(c.USERAGENT ,"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0")  #Setting the browser
 c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8']) #setting the required header
 c.setopt(c.FAILONERROR, True) 
 c.setopt(c.VERBOSE, True) # sets into verbose mode
 c.perform()
 print buf.getvalue()
 buffer1.close()
 key = "Authenicated"
 return key
def downloads(ips,url,ri,rf):
 buf1 = cStringIO.StringIO()
 c1 = pycurl.Curl() #see line 10
 c1.setopt(c1.INTERFACE, ips) #selects interface
 c1.setopt(c1.USERAGENT ,"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0 ") #see line 11
 c1.setopt(c1.URL , url)
 c1.setopt(c1.RANGE,str( ri) +  "-" + str(rf)) #sets the range
 c1.setopt(c1.NOSIGNAL, 1)
 c1.setopt(c1.NOPROGRESS, 0) #not to shut off the progress bar
 c1.setopt(c1.WRITEFUNCTION, buf1.write) 
 c1.setopt(c1.VERBOSE, 1) 
 c1.setopt(c1.COOKIEFILE, 'cookie.txt')
 c1.perform()
 return 1
def file_size(url):
 #size = urllib2.urlopen(url).info()
 opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
 read = opener.open(url)
 headers = read.info()
 meta = headers.getheaders("Content-Length")[0]
 return meta
def main():
 try:
  os.system("sudo sh add_ip.sh")
 except:
  print("Error in excecution of the script")
 url = raw_input("enter the URL of the file to be downloaded: ")
 size_actual = int(file_size(url))
 print("The total size of the file to be downloaded is: ")
 print(size_actual)
 split = 7
 flag = 0
 size = size_actual/split
 print(size)
 while flag<split:
  params = raw_input("enter the IP address: ")
  uname = raw_input("Enter userID: ") #getting userID and password
  pwd = raw_input("Password: ")
  authentication(uname,pwd,params)
  flag = flag+1
 ranges = [] #list for setting the range of different download
 i = 1
 j = 0
 while j<=split:
  ranges.append(j)
  j = j+1
 while i<=split: #setting ranges to download in this array
  ranges[i] = ranges[i-1] + size 
  i = i+1
 thread1 = Thread(downloads('10.3.12.230',url,ranges[0],ranges[1]-1))
 thread2 = Thread(downloads('10.3.12.231',url,ranges[1],ranges[2]-1))
 thread3 = Thread(downloads('10.3.12.232',url,ranges[2],ranges[3]-1))
 thread4 = Thread(downloads('10.3.12.233',url,ranges[3],ranges[4]-1))
 thread5 = Thread(downloads('10.3.12.234',url,ranges[4],ranges[5]-1))
 thread6 = Thread(downloads('10.3.12.235',url,ranges[5],ranges[6]-1))
 thread7 = Thread(downloads('10.3.12.236',url,ranges[6],ranges[7]-1))
 thread1.start()
 thread2.start()
 thread3.start()
 thread4.start()
 thread5.start()
 thread6.start()
 thread7.start()
 thread1.join()
 thread2.join()
 thread3.join()
 thread4.join()
 thread5.join()
 thread6.join()
 thread7.join()
if __name__ == "__main__":
 main()
