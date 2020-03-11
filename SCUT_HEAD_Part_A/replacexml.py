import os
import numpy as np
import glob
import xml.etree.ElementTree as ET
#names=glob.glob(os.getcwd()+'/Annotations/*.xml'))
names=glob.glob(os.getcwd()+'/*.xml')
names=sorted(names)
tam=len(names)
for x in range(tam):
	tree=ET.parse(names[x])
	#tree.getroot()
	root=tree.getroot()
	#root[2].text
	#os.getcwd()
	lista=(root[2].text).split('/')
	#folder=""
	photo=""
	splitter=str(names[x])
	splitter=splitter.split("/")
	#print(splitter)
	#print(lista)
	folder=splitter[7]
	photo=lista[7]
	#raiz[2].text=os.getcwd()+'/Annotations/JPEGImages/'+photo
	root[2].text=os.getcwd()+'/'+photo
	#tree.write(os.getcwd()+"/Annotations/JPEGImages/"+folder)
	tree.write(os.getcwd()+"/"+folder)
