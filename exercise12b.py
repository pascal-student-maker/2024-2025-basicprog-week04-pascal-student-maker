#exercise12b
def are_totally_different(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x ==y:
                result = "at least list1 and list2 element in common"
                return result
print(are_totally_different([4,5,6,4], [89,79,4]))   
print(are_totally_different([4,5,6,4], [89,79,4]))           
    