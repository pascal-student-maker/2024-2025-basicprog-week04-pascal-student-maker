#homework 1c.py
def its_equal(listA,listB):
    result = False
    for x in listA:
        for y in listB:
            if x ==y:
                result = "Equal?: true"
                return result
print(its_equal([10,14,2,4],[-10,3,2,10,14]))   
    