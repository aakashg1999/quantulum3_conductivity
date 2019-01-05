import re
from quantulum3 import parser
#defining variable
range_details=[]


def arranging(val1,val2):
    global value_1, value_2
    value_1=(val1)
    value_2=(val2)
    
def adding_info(surface):
    f=re.findall(r' \d+ ?\w',surface)
    
    q=parser.parse(f[0])
    #print(t_range_details)
    print(value_1," to ", value_2," " ,q[0].unit.entity)
    
    range_details.append(value_1)
    range_details.append(value_2)

    

