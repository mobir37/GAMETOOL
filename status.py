astats = [0,0,0,0,0,0]
stats = 0

def getstats():
        return astats
    
def increasestats(statcode,statnumber):
    astats[statcode] = str(int(astats[statcode])+statnumber)
    return astats


def getstats(statnumbers):
    global stats
    stats += statnumbers
    return stats
 