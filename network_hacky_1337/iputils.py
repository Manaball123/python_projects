

ff = 255

def int2ip(i):

    s1 = str((i >> 24) & ff)
    s2 = str((i >> 16) & ff)
    s3 = str((i >> 8) & ff)
    s4 = str((i >> 0) & ff)
    return s1 + "." + s2 + "." + s3 + "." + s4




def ip2int(s):
    sl = s.split(".")
    i = 0
    i += (int(sl[0]) << 24)
    i += (int(sl[1]) << 16)
    i += (int(sl[2]) << 8)
    i += (int(sl[3]) << 0)
    return i


def get_range_enum(start, stop, mode = "ip", rtype = "ip"):
    """
    returns every ip in set range(inclusive)
    start: start of ip range
    stop: end of ip range
    mode: data type of start/stop, defaults to ip string
    rtype: return type, defaults to list of ip strings
    """
    s = start
    e = stop
    if(mode == "ip"):
        s = ip2int(start)
        e = ip2int(stop)
    rlist = []
    for i in range(s,e):
        rlist.append(i)
        
    rlist.append(e)
    if(rtype == "ip"):
        for it in range(len(rlist)):
            rlist[it] = int2ip(rlist[it])
    

    return rlist

    