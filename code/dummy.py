#This script is for testing certain scripts, not necessarily important!!
import sys
import torch

print("------------------------------------------------------------")
print("yo lets go!!!")
print(torch.cuda.is_available())

print(torch.cuda.device_count())

print("yo lets go is complete@@@@")
print(sys.version)
print(sys.version_info)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o','--open-file', help='Description', required=False)
parser.add_argument('-s','--save-file', help='Description', required=False)

args = parser.parse_args()

print(args.open_file)
print(args.save_file)

print()
print(len(sys.argv))