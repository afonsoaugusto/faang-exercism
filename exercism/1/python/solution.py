from copy import deepcopy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def _getStringFromListNode(self, listNode: ListNode) -> list[int]:
        string  = "" 
        listNode = deepcopy(listNode)
        while True:
            string += str(listNode.val)
            if None == listNode.next:
                break
            listNode = listNode.next
        return string

    def _createListNodeFromString(self, string: str) -> ListNode:
        listNodes = []
        for i in string:
            listNodes.append(ListNode(val=int(i)))
        for i in range(0,len(listNodes)-1):
            listNodes[i].next = listNodes[i+1]
        return listNodes[0]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sl1 = self._getStringFromListNode(l1)
        sl2 = self._getStringFromListNode(l2)
        slr = str(int(sl1[::-1]) + int(sl2[::-1]))[::-1]
        return self._createListNodeFromString(slr)
