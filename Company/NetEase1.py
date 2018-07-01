"""
网易：计算重叠矩形的个数
"""
num = int(raw_input())
left_x = raw_input().strip().split()
left_y = raw_input().strip().split()
right_x = raw_input().strip().split()
right_y = raw_input().strip().split()

x = left_x + right_x
y = left_y + right_y

finalList = []
for i in range(len(x)):
    for j in range(len(y)):
        cnt = 0
        point_x = int(x[i])
        point_y = int(y[j])
        for  m in range(num):
            if(point_x > int(left_x[m]) and point_y > int(left_y[m]) and point_x <= int(right_x[m]) and point_y <= int(right_y[m])):
                cnt += 1
        finalList.append(cnt)
if(max(finalList) == 0):
    print 1
else:
    print max(finalList)
