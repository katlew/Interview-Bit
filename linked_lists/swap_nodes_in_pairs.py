# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
		res = ListNode(0)
		res.next = A
		root = res

		while root.next and root.next.next:
			root.next = self.swap(root.next, root.next.next)
			root = root.next.next

		return res.next

	def swap(self, p1, p2):
		p1.next = p2.next
		p2.next = p1
		return p2

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""