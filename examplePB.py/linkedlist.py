"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Example 1: Input: head = [1,2,3,4,5], k = 2 Output: [2,1,4,3,5]
Example 2: Input: head = [1,2,3,4,5], k = 3 Output: [3,2,1,4,5]
"""
# Definition for singly-linked list.
emoji_start = 128008
emoji_end = 128060
emoji = emoji_start
emoji_map = {}
emoji_nl = chr(10)
emoji_pd = chr(35)

class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n
        return

    def get_emoji(self):
        global emoji
        i = id(self)
        if not(i in emoji_map):
            if emoji == emoji_end:
                emoji = emoji_start
            emoji_map[i] = "&" + emoji_pd + str(emoji) + ";"
            emoji = emoji + 1
        return emoji_map[i]

    def __repr__(self):
        if not hasattr(self,"value"):
            return "Not initialized yet"
        if not hasattr(self,"next"):
            return "Not initialized yet"
        s = "```html" + emoji_nl
        s += "&nbsp;"
        n = self
        ns = set()
        # make sure to handle circular lists
        # which often happen as intermedite
        # states during list manipulation
        while n != None and not (n in ns):
            ns.add(n)
            s += n.get_emoji()
            s += "<font color='LightSkyBlue'>" 
            s += str(n.value)
            s += "</font>"
            if n.next != None:
                s += "&rarr;"
            n = n.next
        s += "&nbsp;"
        s += "```"
        return s

        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = Node(0, head)
        prev = dummy
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next_head = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = next_head
            prev = tail
            head = tail.next

        return dummy.next


    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
s = Solution()
res = s.reverseKGroup(head, 2)
