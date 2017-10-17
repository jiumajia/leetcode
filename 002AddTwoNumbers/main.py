# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# for commit code ###
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        flag = 0
        while l1 or l2 or flag:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0
            val = c1 + c2 + flag

            res.append(val % 10 )
            flag = val // 10

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return Solution.makeNodeList(res)

    @classmethod
    def makeNodeList(self, l_list):
        """
        :param l_list:  turn python list to listnode
        :return: listnode
        """
        colloction = []
        for i in l_list[::-1]:
            s = ListNode(i)
            if len(colloction) > 0:
                s.next = colloction[-1]
            colloction.append(s)

        return colloction[-1]
# for commit code ###

    @classmethod
    def interNodeList(clsself, n):
        res = []
        while n:
            res.append(n.val)
            n = n.next
        print res

if __name__ == "__main__":
    l1 = Solution.makeNodeList([1])
    l2 = Solution.makeNodeList([9, 9])

    res = Solution().addTwoNumbers(l1, l2)
    Solution.interNodeList(res)
