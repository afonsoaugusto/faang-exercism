import unittest
from solution import Solution, ListNode

class MetaSolution:
    def __init__(self, listNode: ListNode):
        self.listNode = listNode
    
    def getList(self) -> list[int]:
        list = []
        listNode = self.listNode
        while True:
            list.append(listNode.val)
            if None == listNode.next:
                break
            listNode = listNode.next
        return list

class TestMetaSolution(unittest.TestCase):

    def test_getListEmpty(self):
        metaSolution = MetaSolution(ListNode())
        self.assertEqual(metaSolution.getList(), [0])

    def test_getListWith_1_Number(self):
        metaSolution = MetaSolution(ListNode(val=1))
        self.assertEqual(metaSolution.getList(), [1])

    def test_getListWith_2_Number(self):
        listNode = ListNode(val=1, next=ListNode(val=2))
        metaSolution = MetaSolution(listNode)
        self.assertEqual(metaSolution.getList(), [1,2])

    def test_getListWith_3_Number(self):
        listNode = ListNode(val=1, next=ListNode(val=2,next=ListNode(val=3)))
        metaSolution = MetaSolution(listNode)
        self.assertEqual(metaSolution.getList(), [1,2,3])        

class TestSolution(unittest.TestCase):

    def test_addTwoNumbers_empty(self):
        metaSolution = MetaSolution(Solution().addTwoNumbers(ListNode(),ListNode()))
        metaSolutionExpected = MetaSolution(ListNode())
        self.assertEqual(metaSolution.getList(), metaSolutionExpected.getList())

    def test_addTwoNumbers_1(self):
        l1 = ListNode(val=2, next=ListNode(val=4,next=ListNode(val=3)))
        l2 = ListNode(val=5, next=ListNode(val=6,next=ListNode(val=4)))
        lr = ListNode(val=7, next=ListNode(val=0,next=ListNode(val=8)))
        metaSolution = MetaSolution(Solution().addTwoNumbers(l1,l2))
        metaSolutionExpected = MetaSolution(lr)
        self.assertEqual(metaSolution.getList(), metaSolutionExpected.getList())        

    def test_addTwoNumbers_2(self):
        l1 = ListNode(val=9, next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9)))))))
        l2 = ListNode(val=9, next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9))))
        lr = ListNode(val=8, next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=0,next=ListNode(val=0,next=ListNode(val=0,next=ListNode(val=1))))))))
        metaSolution = MetaSolution(Solution().addTwoNumbers(l1,l2))
        metaSolutionExpected = MetaSolution(lr)
        self.assertEqual(metaSolution.getList(), metaSolutionExpected.getList())        
