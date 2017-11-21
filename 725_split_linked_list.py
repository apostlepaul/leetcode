# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """ 
        total_node_num = 0
        it = root
        while it != None:
            total_node_num +=1
            it = it.next
        avg = int(total_node_num / k)
        odd = total_node_num % k
        res = []
        it = root
        for i in range(k):
            if it == None:
                res.append(None)
            else:
                new_node = ListNode(it.val)
                res.append(new_node)
                new_node_it = new_node
                sub_len = avg
                if i < odd:
                    sub_len = avg +1
                if sub_len > 0:
                    for i in range(sub_len-1):
                        it = it.next
                        if it != None:
                            new_node_tmp = ListNode(it.val)
                            new_node_it.next = new_node_tmp
                            new_node_it = new_node_tmp
                    it = it.next
                        
        return res
