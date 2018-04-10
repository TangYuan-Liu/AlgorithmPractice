#这是一道腾讯的编程题。题目：给定一串数字序列，在每个数前可任意添加正负号，使得总和为某一个给定的值，求所有可能的次数。
#例如：序列12345 求所有使其和为2的可能的次数。
"""
                                   sum
                              +1         -1
                            +2 -2     +2   -2
                         +3 -3 +3-3 +3 -3 +3 -3
                        ...       ...     ...     ...
"""


print("Please input the sequence")
seq = raw_input()
print("Please input the value")
value = raw_input()

count = []
total = 0
def search_tree(flag,num,total,count):
   
    if(num <= len(seq) - 1):
        if(flag == 0):
            total += int(seq[num])
            #print seq[num]
        else:
            total -= int(seq[num])
            #print seq[num]
        if(num == len(seq) - 1):
            #print total
            if(total == int(value)):
                count.append(1)
            return
        else:
            search_tree(0,num+1,total,count)
            search_tree(1,num+1,total,count)

search_tree(0,0,total,count)
search_tree(1,0,total,count)

print("Total Number is:")
print len(count)

"""
以下是另一种表达方法：
x是数组，v是规定的和
def find_way(x,v):
    l = len(x)
    if l == 1:
        if x[0] == v:
            return 1
        else:
            return 0
    else:
        N1 = find_way(x[1:],v+x[0])
        N2 = find_way(x[1:],v-x[0])
        return N1 + N2
"""
