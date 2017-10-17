# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        while l1 or l2:
            print l1.val + l2.val

            l1 = l1.next
            l2 = l2.next

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

if __name__ == "__main__":
    l1 = Solution.makeNodeList([1, 2, 3, 4])
    l2 = Solution.makeNodeList([4, 5, 9, 3])

    res = Solution().addTwoNumbers(l1, l2)

