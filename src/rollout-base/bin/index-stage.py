#!/bin/env python
# -*- coding: utf-8 -*-
___author__ = 'Adam Grigolato'
__version__ = '0'
#IMPORTS
import tarfile
import sys
#
def crprint(data):
    sys.stdout.write('{}\r'.format(str(data)))
    sys.stdout.flush()


def gen_index(filename):
    import hashlib
    index = {}
    hashlist = []
    with tarfile.open(filename, 'r') as tar:
        outloop = 0
        for member in tar:
            outloop += 1
            crprint(str(outloop)+' files processed')
            #print(member.name)
            path = member.name.split('/')
            index_pos = index
            if member.isdir():
                for n in path[1:]:
                    if n not in index_pos:
                        #print(index)
                        index_pos[n] = {}
                        index_pos = index_pos[n]
                    else:
                        index_pos = index_pos[n]
            if member.isfile():
                loop = 0
                for n in path[1:]:
                    loop += 1
                    if n == path[-1]:
                        if n not in index_pos:
                            if not (member.isdev() or member.isfifo() or member.isblk() or member.ischr() or member.islnk() or member.issym() or member.isdir()):
                                hash = hashlib.sha256()
                                f = tar.extractfile(member)
                                hash.update(f.read())
                                digest = hash.digest()
                                hashlist.append(str(member.name)+' '+str(digest))
                                index_pos[n] = (member.size,member.mtime,member.mode,member.type,member.uid,member.gid,member.uname,member.gname,member.isfile(),member.isdir(),member.issym(),member.islnk(),member.ischr(),member.isblk(),member.isfifo(),member.isdev(),digest)
                            else:
                                index_pos[n] = (member.size,member.mtime,member.mode,member.type,member.uid,member.gid,member.uname,member.gname,member.isfile(),member.isdir(),member.issym(),member.islnk(),member.ischr(),member.isblk(),member.isfifo(),member.isdev())
                    else:
                        if n not in index_pos:
                            index_pos[n] = {}
                            index_pos = index_pos[n]
                        else:
                            index_pos = index_pos[n]
    return index, hashlist



if __name__ == '__main__':
    import yaml
    import msgpack
    index, hashlist = gen_index('stage3-latest.tar')
    with open('files.sha256', 'w') as hf:
        for n in hashlist:
            hf.write(n.encode('utf8')+'\n'.encode('utf8'))
    with open('index.msgpack', 'wb') as f:
        f.write(msgpack.packb(index))
        
