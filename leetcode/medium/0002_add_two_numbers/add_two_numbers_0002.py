#2024-11-10
#add two numbers
#ex:[2, 4, 3] and [1, 2, 3] => 342+321=663 =>output:[3, 6, 6] (ListNode!!!)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 當前節點的值
        self.next = next    # 指向下一個節點的指標

def main(x_array : ListNode, y_array : ListNode):
    x_num = array_to_num(x_array)
    y_num = array_to_num(y_array)
    sum_num = x_num + y_num
    sum_array = num_to_array(sum_num)
    print(sum_array)

def array_to_num(data : ListNode):  #ListNode to num
    j = 1
    if data != None:
        num = data
    while data.next != None:
        num = num + data * (10 ** j)
    return num

def num_to_array(num : int):
    data = []
    num_str = str(num)
    length = len(num_str)
    data.append(num % 10)
    for i in range(1, length):
        data.append(int(num/(10**i)) % 10)
    return data

main([2, 4, 3], [5, 6, 4])