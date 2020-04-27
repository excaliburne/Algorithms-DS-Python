def reverse_list(head):
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head 
        head = head.next
        current.next = prev 
        prev = current 

    return prev

