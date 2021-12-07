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
            print(temp.data, sep=' ')
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
            line_top_bottom = line_top_bottom + BOX_OUTLINE  # Outline of the box

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

    # This function is in LinkedList class.
    # Inserts a new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */
    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # This function is defined in Linked List class
    # Appends a new node at the end. This method is
    # defined inside LinkedList class shown above */
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    def deleteNode(self, k:int):
        
        # Store head node
        temp = self.head
        prev = None

        # If its 1st node
        if k==1:
            self.head=self.head.next
            return
        
        # set temp at xth node to be deleted
        for i in range(1,k):
            prev=temp
            temp=temp.next
        try:
            prev.next=temp.next
            return
        except AttributeError:
            print(f"{k}th node doesn't exist")
            exit()

    
    def deleteFirstOccurNode(self, key:int):
        '''
        Given a reference to the head of a list and a key,
        delete the first occurrence of key in linked list
        '''

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next' 
        # to link both previous and the node after the node that needs to be deleted
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node

    # # Insertion in the start
    # print(llist)
    # llist.push(5)
    # print() # to space
    # print('Inserting 5 to the start of the Linked List')
    # print()
    # print(llist)

    # print()

    # Insertion after a given node
    # print(llist)
    # llist.insertAfter(second, 5)
    # print()  # to space
    # print('Inserting 5 after 2')
    # print()
    # print(llist)

    # print("="*75)

    # Appending in the end
    print(llist)
    llist.append(5)
    print()  # to space
    print('Appending 5')
    print()
    print(llist)

    print("="*75)

    print('deleting 3rd node')
    llist.deleteNode(3)
    print(llist)

    # print("="*75)

    # print('deleting First occurrence of 1')
    # llist.deleteFirstOccurNode(1)
    # print(llist)
