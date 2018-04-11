"""
给出一组正整数，你从第一个数想最后一个数方向跳跃，每次跳跃至少一个格，每个数的值表示你从这个位置可以跳跃的最大长度。
计算如何以最少的跳跃次数调到最后一个数。

输入描述：
第一行表示有多少个数n
第二行一次是1到n个数，一个数一行

输出描述：
输出一行，表示最少跳跃的次数。

Bingo! Celebrate! :)
"""

import sys

def jump(seq,step_seq,start,total_step):
    
    if(start == len(seq)-1):
        step_seq.append(total_step)
        return 
    else:
        current_position = seq[start]
        for i in range(current_position):
            if(start+i+1 <= len(seq)-1):
                jump(seq,step_seq,start+i+1,total_step+1)
            
    return total_step

def find_min(seq):
    min = seq[0]
    for i in range(len(seq)):
        if(seq[i] < min):
            min = seq[i]
    return min

if __name__ == '__main__':
    
    #step = sys.stdin.readline()
    step = raw_input()
    step = int(step[0])
    seq = []
    step_seq = []
    for i in range(step):
        temp = sys.stdin.readline()
        temp = int(temp[0])
        seq.append(temp)
    
    jump(seq,step_seq,0,0)
    total = find_min(step_seq)
    sys.stdout.write(str(total))
