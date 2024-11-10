class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 當前節點的值
        self.next = next    # 指向下一個節點的指標

# 創建節點
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 連結節點
node1.next = node2
node2.next = node3

# 現在我們有一個鏈結串列: 1 -> 2 -> 3

# 初始化指針為鏈結串列的頭部
current = node1

# 遍歷並打印每個節點的值
while current:
    print(current.val)  # 打印當前節點的值
    current = current.next  # 移動到下一個節點
