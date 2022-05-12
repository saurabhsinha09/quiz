def find_sum(a, b):
    for i in range(len(a)):
        c = 0
        temp = []
        print("i:" + str(i))
        for j in a[i : len(a)]:
            c +=j 
            #print("c:" + str(c))
            temp.append(j)
            if c >= b :
                break
        if c == b:
            break
        else :
            temp = []
    return temp

#Q-Find the subset of list for which 
#the sum of list equals to second parameter
#of function.
a = [1, 4, 20, 3, 10, 5]
p = find_sum(a,33)
print(p)

a = [1, 4, 0, 0, 3, 10, 5]
p = find_sum(a,7)
print(p)

a = [1, 4]
p = find_sum(a,0)
print(p)
