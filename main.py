import os
import requests
import json
import time
import matplotlib.pyplot as plt
import math
import gc

s=requests.session()
spl=[0]
bpl=[0]
tim=['0']
plt.ion()
fig=plt.figure()
asp=fig.add_subplot(211)
spline, = asp.plot(tim,spl)
abp=fig.add_subplot(212)
bpline, =abp.plot(tim, bpl)

first=0
while 1:
	if len(tim)>=5:
		tim.pop(0)
	tim.append(str(os.popen('date +"%H:%M:%S"').read().strip()))
	os.popen('exit')
	res=json.loads(s.get('https://paytm.com/papi/v2/gold/product-portfolio').content.decode())
	if len(spl)>=5:
		spl.pop(0)
	tspl=res['portfolio']['product_level'][0]['sell_price_per_gm']
	spl.append(math.floor(float(tspl)))
	if len(bpl)>=5:
		bpl.pop(0)
	tbpl=res['portfolio']['product_level'][0]['price_per_gm']
	bpl.append(math.floor(float(tbpl)))
	# plt.subplot(2,1,1)
	# print('tim: '+str(tim)+' spl: '+str(spl))
	# plt.plot(tim,spl)
	# plt.title('Selling Price')
	# plt.subplot(2,1,2)
	# plt.plot(tim,bpl)
	# plt.title('Buying Price')
	# plt.show()
	# print('working')
	#spl.sort()
	#bpl.sort()
	asp.cla()
	abp.cla()
	fig.suptitle('Buying Price: '+str(bpl[-1])+"\nSelling Price: "+str(spl[-1]))
	spline, = asp.plot(tim,spl)
	bpline, =abp.plot(tim, bpl)
	# spline.set_xdata(tim)
	# spline.set_ydata(spl)
	# bpline.set_xdata(tim)
	# bpline.set_ydata(bpl)
	#print(first)
	#print('sel: '+str(spl)+' time: '+str(tim))
	fig.canvas.draw()
	gc.collect()
	if first==0:
		first=1
	else:
		time.sleep(2)