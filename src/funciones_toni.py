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