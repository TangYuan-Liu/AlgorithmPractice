"""
Flatten List
"""

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        def my_func(input_list):
            my_list = []
            for i in range(len(input_list)):
                if(type(input_list[i]) != type(my_list)):
                    my_list.append(input_list[i])
                    continue
                else:
                    my_list.extend(my_func(input_list[i]))
            return my_list
        
        
        final_list = []
        if type(nestedList) != type(final_list):
            final_list.append(nestedList)
            return final_list
        for i in range(len(nestedList)):
            if(type(nestedList[i]) != type(final_list)):
                final_list.append(nestedList[i])
            else:
                final_list.extend(my_func(nestedList[i]))
            
        
        
        
        return final_list
