# Definition for singly-linked list:
class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array1 = []
        array2 = []
        # Change to array:

        while l1.next!= None:
            array1.append(l1.val)
            l1 = l1.next
        array1.append(l1.val)

        while l2.next!= None:
            array2.append(l2.val)
            l2 = l2.next
        array2.append(l2.val)

        

        # Reformat into numbers:
        def getnum(array):
            sum=0
            for i in range(len(array)):
                sum+=array[i]*(10**i)
            return sum

        # Calculate:
        result=getnum(array1)+getnum(array2)
        
        if result == 0:
            return ListNode(0)

        dummy = ListNode(0)  
        curr = dummy          

        while result > 0:
            digit = result % 10          
            curr.next = ListNode(digit)  
            curr = curr.next             
            result //= 10                

        return dummy.next  