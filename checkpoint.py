#!/usr/bin/python3
import os
import requests
import json
import time

s=requests.session()
try:
	f=open('checkpoint.txt', 'r').read()
except Exception as e:
	raise e

val=f.split('\n')
try:
	sellchk=val[0]
except Exception as e:
	sellchk=''
try:
	buychk=val[1]
except Exception as e:
	buychk=''

run=0
while run==0:
	res=json.loads(s.get('https://paytm.com/papi/v2/gold/product-portfolio').content.decode())
	tspl=float(res['portfolio']['product_level'][0]['sell_price_per_gm'])
	tbpl=float(res['portfolio']['product_level'][0]['price_per_gm'])
	mssg=''
	os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Today Gold Price' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"\nWaiting amount:"+str(int(sellchk)-int(tspl))+"\nBuying Checkpoint: "+str(buychk)+"\nWaiting amount:"+str(int(tbpl)-int(buychk))+"'")
	if sellchk=='':
		sellchk=int(tspl)+100
	if tspl>=float(sellchk):
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Gold Price Hiked!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Gold Price Hiked Sell the gold!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Sell the Gold Sir!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")

	if buychk=='':
		buychk=0.0
	if tbpl<=float(buychk):
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'LOW GOLD PRICE!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Gold Price Drained Buy the gold!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")
		os.popen("/usr/bin/notify-send -t 1000000 -u critical 'Buy the Gold Sir!!' 'Buying Price: "+str(tbpl)+"\nSelling Price: "+str(tspl)+"\nSelling checkpoint: "+str(sellchk)+"'")
	run=1