# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def printList(self):
        """
        This Method prints contents of the linked list
        """

        temp = self.head
        while (temp):
            print(temp.data,sep=' ')
            temp = temp.next

    def __len__(self):
        length = 0
        temp = self.head
        while (temp):
            length += 1
            temp = temp.next
        return length

    def __str__(self):
        """
        Shows a pictorial representation of the Linked List
        Example
        +----+------+   +----+------+   +----+------+
        | 1  |  o------>| 2  |  o------>| 3  | null |
        +----+------+   +----+------+   +----+------+
        """

        # create the output string
        line_top_bottom = ''
        line_middle = ''

        BOX_OUTLINE = '+----+------+\t'
        BOX_NOT_NULL = '| {}  |  o------>'
        BOX_NULL = '| {}  | null |\t'

        # Traverse through the linked list and insert the values
        temp = self.head
        while (temp):
            line_top_bottom = line_top_bottom + BOX_OUTLINE # Outline of the box

            if temp.next != None:
                line_middle = line_middle + BOX_NOT_NULL.format(temp.data)
            else:
                line_middle = line_middle + BOX_NULL.format(temp.data)
            temp = temp.next
        
        # join everything in a single string
        output = ''
        output = line_top_bottom+'\n'+line_middle+'\n'+line_top_bottom

        return output

    # Function to insert a new node at the beginning
    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node

    print(llist)
    llist.push(5)
    print() # to space
    print('Inserting 5 to the start of the Linked List')
    print()
    print(llist)
