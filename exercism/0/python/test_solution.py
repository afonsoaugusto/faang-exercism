import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_simpleSmash(self):
        solution = Solution()
        self.assertEqual(solution.smash([]), "")
        self.assertEqual(solution.smash(["hello"]), "hello")
        self.assertEqual(solution.smash(["hello", "world"]), "hello world")
