
#http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1
# id 1034 is last, Zoop game


import requests, subprocess, os

rom_id = 1034
url = "http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=%s" % rom_id
r = requests.get(url)

out_7zip = "%s.7zip" % rom_id
out = open(out_7zip, 'w')

#save archive
out.write (r.content)
out.close()

#mkdir
dir_name = str(rom_id)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

#extract 7zip
cmd = ['7z', 'e', out_7zip, '-o' + dir_name + 'y']
subprocess.call(cmd)
