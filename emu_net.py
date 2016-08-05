
#http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1
# id 1034 is last, Zoop game


import requests, subprocess

out = open('./id.7zip', 'w')
url = "http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1034"
r = requests.get(url)

#save archive
out.write (r.content)
out.close()

#unpack
#subprocess
subprocess.call("mkdir -p f_id", shell=True)
subprocess.call("7z e id.7zip -of_id *[!].gen -y", shell=True)
# -oc:t/ -r"])
