class MergeSort(object):
    def __init__(self):
        self.arr = [
            [1,3,343,4,5],
            [23,10,56,89],
            [7,8,24,9,1],
        ]

    def merge_two_sorted_lists(self, list_big, list_small):
        result = []
        runner=0
        runner_small=0
        while runner!=len(list_big) and runner_small!=len(list_small):
            if list_big[runner]<list_small[runner_small]:
                result.append(list_big[runner])
                runner+=1
            else:
                result.append(list_small[runner_small])
                runner_small+=1

        if runner_small<len(list_small):
            while runner_small!=len(list_small):
                result.append(list_small[runner_small])
                runner_small+=1
        else:
            while runner!=len(list_big):
                result.append(list_big[runner])
                runner+=1
        return result

    def mergeSort(self, alist):
        if len(alist) == 1:
            print alist
            return alist
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            lefthalf = self.mergeSort(lefthalf)
            righthalf = self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j+=1
                k+=1

            while i<len(lefthalf):
                alist[k]=lefthalf[i]
                k+=1
                i+=1
            while j<len(righthalf):
                alist[k]=righthalf[j]
                k+=1
                j+=1
        return alist

    def merging_two_unsorted_lists(self):
        result=[]
        for x in self.arr:
            result+=x
            self.mergeSort(result)
        return result

    def caller(self):


        result= self.merging_two_unsorted_lists()
        print result

zron = MergeSort()
zron.caller()
result=zron.mergeSort([54,26,93,17,77,31,44,55,20])
print result
