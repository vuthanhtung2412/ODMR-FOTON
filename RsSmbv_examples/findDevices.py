from RsSmbv import *

print("dmm")
# Use the instr_list string items as resource names in the RsSmbv constructor
instr_list = RsSmbv.list_resources("?*")
print(instr_list)