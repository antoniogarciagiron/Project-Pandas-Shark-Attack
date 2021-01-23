def regeshark (x, pattern):
    import re
    res = re.findall(pattern, x)
    res="".join(res)
    res=res.replace("]", "")
    if "shark" in res:
        return res
    else:
        return "NaN"

def monthattack (x, pattern):
    import re
    res = re.findall(pattern, x)
    if len(res)>1:
        return res[-1]
    elif len(res)==1:
        return res[0]
    else:
        return "NaN"

def daytime (x, pattern):
    import re
    res = re.findall(pattern, x)
    res="".join(res)
    if res in ["06","07","08","09","10","11", "Morning"]:
        return "Morning"
    elif res in ["12","13","14","15","16","17", "Afternoon"]:
        return "Afternoon"
    elif res in ["18","19","20","21","22","23", "Evening"]:
        return "Evening"
    elif res in ["24","01","02","03","04","05", "Night"]:
        return "Night"
    else:
        return "NaN"

def fatal (x, pattern):
    import re
    res = re.findall(pattern, x)
    res="".join(res)
    if len(res)>=1:
        return res
    else:
        return "NaN"
