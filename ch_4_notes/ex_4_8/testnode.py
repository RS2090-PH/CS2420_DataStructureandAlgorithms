"""
File: testnode.py

Tests the Node class.
"""

from node import Node

def length(head):
    count = 0
    probe = head
    while probe != None:
        count += 1
        probe = probe.next
            
    return count

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next
    length(head)
