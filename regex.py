import re



LA = [
"1050:0:0:0:5:600:300c:326b",
"1050:0:0:0:5:600:300c:326a",
"1050:0:0:0:5:600:300c:326c",
"1051:0:0:0:5:600:300c:326b",
"22.231.113.64",
"22.231.113.164",
"255.231.111.64",
"253.231.111.64",
"1050:10:0:0:5:600:300c:326b",
"1050:10:0:0:5:600:300c:326a",
"1050:10:0:0:5:600:300c:326c",
"1051:10:0:0:5:600:300c:326b",
"22.21.113.61",
"22.21.113.162",
"255.21.111.63",
"253.21.111.69",
"1050:10:0:0:15:600:300c:326b",
"1050:10:0:10:5:600:300c:326a",
"1050:10:10:0:5:600:300c:326c",
"1051:110:0:0:5:600:300c:326b",
"22.211.113.64",
"22.212.113.164",
"255.213.111.64",
"253.214.111.64",
"1050:10:0:0:15:600:300c:326k",
"1050:10:0:0:15:600:300c:326g",
"1050:10:0:0:15:600:300c:326h",
"1050:10:0:0:15:600:300c:326i",
"22.211.113.364",
"22.212.113.3164",
"255.213.111.464",
"253.214.111.564",
"not an ip address",
"not an ipv4 Address",
"Not an IPv5 Address"]


def internet():
        data = "(77.11112223331, 249.99999999)"
        extract_result = re.findall(r'[0-9]+\.[0-9]+', data)
        print float(datas)

        '''extract_result = re.findall(r'[0-9a-fA-F]+', data)
        if len(extract_result) == 4:
            for x in range(0,len(extract_result),1):
                testcase=re.findall(r'[a-z]+', extract_result[x], re.IGNORECASE)
                if testcase:
                    print "Neither"
                    return
                testcase = int(extract_result[x])
                if testcase>255:
                    print "Neither"
                    return
            print "IPv4"
        elif len(extract_result) == 8:
            print "IPv6"
        else:
            print "Neither"
'''
   
if __name__=='__main__':
    #lines = 35
    #while lines:
    internet()
        #lines-=1
