'''
This scripts partitions the ImageNet train and val data into poison_generation, finetune and val data
to run our backdoor attacks. It creates file lists.

Author: Aniruddha Saha
Date: 02/02/2020
'''


import configparser
import glob
import os
import sys
import random
import pdb

random.seed(10)
config = configparser.ConfigParser()
config.read(sys.argv[1])

options = {}
for key, value in config['dataset'].items():
	key, value = key.strip(), value.strip()
	options[key] = value

if not os.path.exists("ImageNet_data_list/poison_generation"):
	os.makedirs("ImageNet_data_list/poison_generation")
if not os.path.exists("ImageNet_data_list/finetune"):
	os.makedirs("ImageNet_data_list/finetune")
if not os.path.exists("ImageNet_data_list/test"):
	os.makedirs("ImageNet_data_list/test")

DATA_DIR = options["data_dir"]

dir_list = sorted(glob.glob(DATA_DIR + "/train/*"))
# max_list = 0
# min_list = 1300

for i, dir_name in enumerate(dir_list):
	if i%50==0:
		print(i)
	filelist = sorted(glob.glob(dir_name + "/*"))
	random.shuffle(filelist)

	# max_list = max(max_list, len(filelist))
	# min_list = min(min_list, len(filelist))
	with open("ImageNet_data_list/poison_generation/" + os.path.basename(dir_name) + ".txt", "w") as f:
		for ctr in range(int(options["poison_generation"])) if int(options["poison_generation"]) < len(filelist) else range(len(filelist)):
			f.write(filelist[ctr].split("/")[-2] + "/" + filelist[ctr].split("/")[-1] + "\n")
	with open("ImageNet_data_list/finetune/" + os.path.basename(dir_name) + ".txt", "w") as f:
		for ctr in range(int(options["finetune"])) if int(options["finetune"]) < len(filelist) else range(len(filelist)):
			f.write(filelist[ctr].split("/")[-2] + "/" + filelist[ctr].split("/")[-1] + "\n")

dir_list = sorted(glob.glob(DATA_DIR + "/val/*"))

for i, dir_name in enumerate(dir_list):
	if i%50==0:
		print(i)
	filelist = sorted(glob.glob(dir_name + "/*"))
	with open("ImageNet_data_list/test/" + os.path.basename(dir_name) + ".txt", "w") as f:
		for ctr in range(int(options["test"])) if int(options["test"]) < len(filelist) else range(len(filelist)):
			f.write(filelist[ctr].split("/")[-2] + "/" + filelist[ctr].split("/")[-1] + "\n")


# print(max_list, min_list)
