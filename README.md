# Leetcode_problem2_Add-two-numbers
### 1. Problem description (From Leetcode):
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

- Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

- Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

- Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
### 2. Some details to be noticed:
The Listnode in the code is officially defined as below:
'''class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next'''
This allow us to create nodes as an object and use "next" as a way to make a chain of nodes. Therefore I highly recommend understanding the nodes and how it works as the main key to solution!
### 3. My idea for solution:
 We first need to transform the chain of nodes into numbers...[Writing]
