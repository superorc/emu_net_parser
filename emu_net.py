
#http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1
# id 1034 is last, Zoop game

import requests, libarchive.public

out = open('./%id.7zip', 'w') , %id
url = "http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1034"
r = requests.get(url)

#save archive
out.write (r.content)
