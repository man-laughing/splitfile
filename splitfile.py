#!/usr/bin/python

import argparse
from Queue import Queue
import sys
import os

def main(file,size=1048576,outdir="/tmp/"):
    FILE_SIZE    = os.path.getsize(file)
    SPLIT_SIZE   = size 
    if FILE_SIZE % SPLIT_SIZE:
        PART_NUMBER = FILE_SIZE / SPLIT_SIZE + 1
    else:
        PART_NUMBER = FILE_SIZE / SPLIT_SIZE
    OUT_PREFIX   = "parts_" 
    if outdir[-1] != "/":outdir = outdir+"/"
    OUT_DIR      = outdir
    if bool(os.path.exists(OUT_DIR)) == False:os.mkdir(OUT_DIR)
    q1 = Queue()
    x = [ x for x in range(PART_NUMBER)]
    for v in x:q1.put(v)
    with open(file,'rb') as f:
        while True:
            zl = f.read(SPLIT_SIZE)
            if bool(zl) == False:
                break
                sys.exit()
            with open(OUT_DIR+OUT_PREFIX+str(q1.get()),'w') as c:
                c.write(zl)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",dest="file",type=str,help="Specify the target file.")
    parser.add_argument("-b",dest="size",type=int,help="Specify the size of the file to be split.(unit:bytes)")
    parser.add_argument("-o",dest="outdir",type=str,default="/tmp/",help="Specify the output directory.(default:/tmp/)")
    options = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
    else:    
        main(**vars(options))
