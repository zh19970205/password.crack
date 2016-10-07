#!usr/bin/env python
import sys
import os

hash_type  = sys.argv[1] # "m" or "b"
hash_file  = sys.argv[2] # file name
hash_slice = sys.argv[3] # sth like 0:1000
dict_file  = sys.argv[4]
dict_slice = sys.argv[5]

hash_slices = map(int,hash_slice.split(":"))
dict_slices = map(int,dict_slice.split(":"))

if hash_type[0] == "m":
    hash_id     = 500
else:
    hash_id     = 3200

this_hash = "this.hash"
this_dict = "this.dict"

hash_file_point = open(hash_file,"r")
dict_file_point = open(dict_file,"r")

this_hash_point = open(this_hash,"w")
this_dict_point = open(this_dict,"w")

for i in range(hash_slices[0]):hash_file_point.readline()
for i in range(dict_slices[0]):dict_file_point.readline()

for i in range(hash_slices[1]-hash_slices[0]):this_hash_point.write(hash_file_point.readline())
for i in range(dict_slices[1]-dict_slices[0]):this_dict_point.write(dict_file_point.readline())

hash_file_point.close()
dict_file_point.close()
this_hash_point.close()
this_dict_point.close()

os.system("./hashcat -a 0 -m %d %s %s"%(hash_id,this_hash,this_dict))
