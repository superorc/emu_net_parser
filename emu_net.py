#!/usr/bin/python
# http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1
# id 1034 is last, Zoop game


import requests, subprocess, os, time, random



def get_7zip(rom_id):

    time.sleep(0.5)

    url = "http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=%s" % rom_id
    r = requests.get(url)

    out_7zip = "%s.7zip" % rom_id
    out = open(out_7zip, 'w')

    #save archive
    out.write (r.content)
    out.close()

    return(rom_id, out_7zip)



def get_rom(rom_id, out_7zip):
    #mkdir
    dir_name = str(rom_id)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    #extract 7zip , only [!] ROMs
    cmd = ['7z', 'e', '-y', out_7zip, '-o' + dir_name, '*[!].gen', 'r']
    #print ("CMD= " + str(cmd))
    subprocess.call(cmd)

    os.remove(out_7zip)



def get_random_rom_id():
    id_list=[]
    for i in range(1, 1035):
        id_list.append(i)
    id = random.choice(id_list)
    id_list.remove(id)
    return(str(id))#, len(id_list))



#
#Main execution
#

for roms in range(1, 1036):
    roms = get_random_rom_id()
    out_7zip = get_7zip(roms)
    #print(out_7zip[0], out_7zip[1])
    get_rom(out_7zip[0], out_7zip[1])

#print type(get_random_rom_id())

print(get_random_rom_id())
