#!/usr/bin/python36

import cgi
import cgitb
cgitb.enable()


print("content-type:text/html")
#print("\n")
form=cgi.FieldStorage()

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as db
from container import Container
from port import Port
from url import URL
import subprocess as sp

email=form.getvalue("email")
service=form.getvalue("service")
#email="tkhandelwal32@gmail.com"
#service="vlc"
con=db.connect(host='localhost',user='root',passwd='123456',db='minor2',port=3306)
cur=con.cursor()
cur.execute("SELECT vlcService,splunkService from serviceDetails where emailId='{}'".format(email))
res=cur.fetchall()
#vlcPath=res[0][0]
#splunkPath=res[0][1]
if service == "vlc":
		req=URL()
		path=req.getVlcUrl()
		print("location:{}".format(path))
		print("\n")
		cur.execute("update serviceDetails  set vlcService='{}'  where emailId='{}'".format(path,email))
		con.commit()
		con.close()
if service == "splunk":
#	if splunkPath == "":
		req=URL()
		path=req.getSplunkUrl()
		print("location:{}".format(path))
		print("\n")
		cur.execute("update serviceDetails  set splunkService='{}'  where emailId='{}'".format(path,email))
		con.commit()
		con.close()
#	else:
	#	print("location:{}".format(splunkPath))
		#print("\n")
#if splunkPath=="":
#	print("path is to be set") #get_url function is to be called
#else:
#	print(splunkPath)
