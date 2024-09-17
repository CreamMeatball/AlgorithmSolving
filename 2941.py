string = str(input())

if "c=" in string:
    string = string.replace("c=", "0")
if "c-" in string:   
    string = string.replace("c-", "0")
if "dz=" in string:
    string = string.replace("dz=", "0")
if "d-" in string: 
    string = string.replace("d-", "0")
if "lj" in string:
    string = string.replace("lj", "0")
if "nj" in string:
    string = string.replace("nj", "0")
if "s=" in string:
    string = string.replace("s=", "0")
if "z=" in string:
    string = string.replace("z=", "0")
    
print(len(string))