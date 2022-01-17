#!/usr/bin/python
# http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=1
# id 1034 is last, Zoop game


import requests, subprocess, os, time, random
from multiprocessing import Pool

from redis_client import RedisClient



def get_7zip(rom_id):

    url = "http://www.emu-land.net/consoles/genesis/roms?act=getfile&id=%s" % rom_id
    r = requests.get(url)

    t = random.randint(3, 5)
    time.sleep(t)

    out_7zip = "%s.7zip" % rom_id
    out = open(out_7zip, 'w+b')

    #print(r.content)
    binary_format = bytearray(r.content)

    #save archive
    out.write(binary_format)

    RedisClient("id") #(rom_id, url, binary_format)
    out.close()

    return(rom_id, out_7zip)



def get_rom(rom_id, out_7zip):
    #mkdir
    dir_name = str(rom_id)
    path = 'roms/%s' % dir_name
    if not os.path.exists(path):
        os.makedirs(path)

    #extract 7zip , only [!] ROMs
    cmd = ['7z', 'e', '-y', out_7zip, '-o' + path, '*[!].gen', 'r']

    sub_process = subprocess.call(cmd)
    #rc = sub_process.returncode

    #if rc != 0:
    #    print("Failed to save rom file")

    #os.remove(out_7zip)



def get_random_rom_id():
    id_list = []
    for i in range(1, 1035):
        id_list.append(i)
    id = random.choice(id_list)
    id_list.remove(id)
    return str(id)#, len(id_list))



#
#Main execution
#
if __name__ == '__main__':
    p = Pool(2)
    for id in range(1, 1036):
        id = get_random_rom_id()
        out_7zip = get_7zip(id)

        get_rom(out_7zip[0], out_7zip[1])
        #print('Rom saved : %s') % roms
