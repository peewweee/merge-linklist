class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeLinkedLists(list_1, list_2):
    # Constraints
    if not (0 <= count_nodes(list_1) <= 50 and 0 <= count_nodes(list_2) <= 50):
        raise ValueError("Number of nodes in both lists should be in the range [0,50].")

    dummy = ListNode(0)
    current = dummy

    while list_1 and list_2:
        if not (-100 <= list_1.value <= 100 and -100 <= list_2.value <= 100):
            raise ValueError("Node value should be in the range [-100, 100].")

        if list_1.value <= list_2.value:
            current.next = ListNode(list_1.value)
            list_1 = list_1.next
        else:
            current.next = ListNode(list_2.value)
            list_2 = list_2.next
        current = current.next

    if list_1:
        current.next = list_1
    elif list_2:
        current.next = list_2

    return dummy.next

def count_nodes(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# Example 
list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)

merged_linkedlists = mergeLinkedLists(list_1, list_2)

print("Merged List:")
current_merged = merged_linkedlists
while current_merged:
    print(current_merged.value, end=" -> ")
    current_merged = current_merged.next
print("None")
