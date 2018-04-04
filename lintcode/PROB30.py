"""
Insert Interval
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    
    def insert(self, intervals, newInterval):
        NewList = []
        if(len(intervals) == 0):
            NewList.append(newInterval)
            return NewList
        
        
        # write your code here
        temList = []
        myinsert = newInterval
        flag = 0
        for i in range(len(intervals)):

            tem = intervals[i]

            if(i == len(intervals) - 1):
                if(tem.start <= myinsert.start):
                    temList.append(tem)
                    temList.append(myinsert)
                else:
                    temList.append(myinsert)
                    temList.append(tem)
            else:
                if(myinsert.start <= tem.start):
                    temList.append(myinsert)
                    temList.append(tem)
                    flag = i+1
                    for j in range(flag,len(intervals)):
                        temList.append(intervals[j])
                    break
                else:
                    temList.append(tem)
                    continue
            
        for i in range(len(temList)):
            if(i == len(temList)-2):
                if(temList[i].end < temList[i+1].start):
                    NewList.append(temList[i])
                    NewList.append(temList[i+1])
                    break
                else:
                    if(temList[i].end <= temList[i+1].end):
                        myinsert = Interval(temList[i].start,temList[i+1].end)
                        NewList.append(myinsert)
                        break
                    else:
                        myinsert = Interval(temList[i].start,temList[i].end)
                        NewList.append(myinsert)
                        break
            
            if(temList[i].end < temList[i+1].start):
                NewList.append(temList[i])
                continue
            else:
                if(temList[i].end <= temList[i+1].end):
                    myinsert = Interval(temList[i].start, temList[i+1].end)
                    temList[i+1] = myinsert
                    continue
                else:
                    myinsert = Interval(temList[i].start,temList[i].end)
                    temList[i+1] = myinsert
                    continue
           
        return NewList
            
            
