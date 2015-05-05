class Solution:  
    # @return a ListNode  
    def addTwoNumbers(self, l1, l2):  
        head = ListNode(0)
        node = head
        sum = 0
        #carry = 0
        while True:
            if l1.next != None:
                sum  += l1.val
                l1 = l1.next
            if l2.next != None:
                sum += l2.val 
                l2 = l2.next
            #sum %= 10
            node.val = sum % 10
            sum /= 10
            
            if l1 != None or l2 != None or sum != 0:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        return head
