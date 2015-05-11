def indexing(lister):
    index_product=0
    right_index=left_index=result=0
    for x in range(0,len(lister),1):
        selected_num=lister[x]
        if x == 0:
            left_index=0
        elif x == len(lister)-1:
            right_index=0
        else:
            for y in range(0,len(lister),1):
                if y==x:
                    continue
                if y<x and lister[y]>lister[x]:
                    left_index=y+1
                if y>x and lister[y]>lister[x] and right_index==0:
                    right_index=y+1
            result = left_index*right_index
            right_index=0
        if result>index_product:
            index_product=result
            print index_product
    print index_product

lister=[5, 4, 3, 4, 5]
indexing(lister)
