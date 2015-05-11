class Overlap(object):
    def __init__(self):
        self.interval = [[1,4],[3,6],[5,9],[12,14]]

    def aggregate(self):
        result=[]
        for x in self.interval:
            if result == []:
                result = x
            else:
                if result[1]>=x[0]:
                    result[1]=x[1]
        print "Aggregated interval =",result




a = Overlap()
a.aggregate()
