import sys

def zero_one(number, multiplier_list=[]):
    '''
    #if multiplier_list[:-1] < (sys.maxint)/10:
    digit_place=0
    if len(multiplier_list)==0:
        digit_place=0
        multiplier_list = [0]
    else:
        digit_place = len(str(multiplier_list[0]))

    for selection in multiplier_list:
        new_multiplier_list=[]
        build_new_list=[]
        #build_new_list = [number*(i*10**digit_place + selection) for i in range(1,10,1)]

        for i in range(1,10,1):
            build_new_list.append(number*(i*(10**digit_place)) + selection)

        for x in range(len(build_new_list)):
            remainder = build_new_list[x]%(10**digit_place + selection)
            if check_num(remainder):
                new_multiplier_list.append(10**digit_place + selection)


        for x in new_multiplier_list:
            if check_num(x*number%(10**digit_place)):
                return x
    zero_one(number, new_multiplier_list)
    #else:
    #    print('Number too big')
    '''
    x = 1
    while x<sys.maxint-10:
        if check_num(number*x):
            return x
        x+=1
    print "too big"




def check_num(number):
    number_str = str(number)
    number_hash = dict(zip(number_str,number_str))
    check_list = ['0','1']
    if sorted(number_hash.keys())==check_list or number_hash.keys()==['1'] or number_hash.keys()==['0']:
        return True
    return False


print zero_one(15)

