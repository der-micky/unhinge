#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import run, PIPE
import json

def main():
    command = ['lsblk -J']
    result = run(command,shell=True, stdout=PIPE)

    o_str = result.stdout.decode('utf-8')
    j = json.loads(o_str);

    unhinge = []
    for bl in j['blockdevices']:
        if bl['name'][:2] == 'sd' or bl['name'][:4] == 'nvme':
            mp_present = False
            if 'children' in bl:
                for ch0 in bl['children']:
                    if 'children' in ch0:
                        for ch1 in ch0['children']:
                            if ch1['name'] == 'LUKS_BOOT' and len(ch1['mountpoints']) > 0 and ch1['mountpoints'][0] == '/boot':
                                print("Found boot device %s" % (bl['name'][:3]))
                                mp_present = True
            if not mp_present:
                unhinge.append(bl['name'])

    #remove all other devices other than our stick
    for u in unhinge:
        command = ''
        if u[:2] == 'sd':
            command = ['echo 1 > /sys/block/%s/device/delete' % (u)]
        if u[:2] == 'nv':
            command = ['echo 1 > /sys/block/%s/device/device/remove' % (u)]
        if len(command) > 0:
            print('Removing device %s' % (u))
            result = run(command,shell=True)

if __name__ == '__main__':
    main()
