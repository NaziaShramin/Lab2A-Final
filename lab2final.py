# Course: Data Structure , Author:Nazia Sharmin, assignment:Lab2A,instructor:Professor-Diego Aguirre,
# T.A.:Ms.Anindita Nath, date of last modification:None, purpose of program: Make a linked list from two given files
#  find the duplicate Ids, compare each element with all other element in the list, sort the list bubble sort and merge
#  sort
# sort :comparesort the



class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None

	
	def insert(self, newNode):
		if self.head is None:
			self.head = newNode
		else:
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode
			
	def printList(self):
		if self.head is None:
			print("Empty list")
			return
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			if currentNode.next is None:
				print(currentNode.data)
				return
			followingNode = currentNode.next

			if currentNode.data == followingNode.data:
				print("Duplicate ID:", currentNode.data)
			else:
				print(currentNode.data)
			currentNode = currentNode.next

	def printListForSol4(self, frequency):
		if self.head is None:
			print("Empty list")
			return
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			if currentNode.next is None:
				print(currentNode.data)
				return
			followingNode = currentNode.next

			if frequency[currentNode.data] == True:
				print("Duplicate ID:", currentNode.data)
			else:
				print(currentNode.data)
			currentNode = currentNode.next
	def compareList(self):
		if self.head is None:
			print("Empty list")
			return
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			if currentNode.next is None:
				return
			followingNode = currentNode.next
			while True:
				if followingNode is None:
					break
				if currentNode.data == followingNode.data:
					print("Duplicate ID Found:", currentNode.data)
				followingNode = followingNode.next

			currentNode = currentNode.next

def readFile(fileName):
	file = open(fileName, "r")
	for line in file:
		x = int(line.strip())
		node = Node(x)
		linkedList.insert(node)


def swapped(x,y):
	currentNode=x.data
	x.data=y.data
	y.data=currentNode
def bs(head):
	swap=True
	while swap:
		swap =False
		prevnode=head
		currentNode=head.next
		while currentNode!=None:
			if (prevnode.data <currentNode.data):
				swapped(prevnode,currentNode)
				swap=True
			currentNode=currentNode.next
			prevnode=prevnode.next





# Merge Sort Functions
# Defining function which will sort the linked list using mergeSort
def mergeSort(head):
	if head is None or head.next is None:
		return head
	linkedlist1, linkedlist2 = divideLists(head)
	linkedlist1 = mergeSort(linkedlist1)
	linkedlist2 = mergeSort(linkedlist2)
	head = mergeLists(linkedlist1, linkedlist2)
	return head
	
# Defining function which will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next            
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid
	
# Defining function which will merge two linked lists
def mergeLists(linkedlist1, linkedlist2):
    if linkedlist1== None and linkedlist2==None:
        return None
    if linkedlist1==None:
        return linkedlist2
    if linkedlist2==None:
        return linkedlist1
    if linkedlist1.data > linkedlist2.data:
        tmp = linkedlist1
        linkedlist1=linkedlist1.next
    else:
        tmp=linkedlist2
        linkedlist2=linkedlist2.next
    lastNode=tmp
    while linkedlist1!=None and linkedlist2!= None:
        if linkedlist1.data>linkedlist2.data:
            lastNode.next=linkedlist1
            linkedlist1 = linkedlist1.next
        else:
            lastNode.next=linkedlist2
            linkedlist2=linkedlist2.next
        lastNode=lastNode.next
    if linkedlist1!=None:
        lastNode.next=linkedlist1
    elif linkedlist2!=None:
        lastNode.next=linkedlist2
    return tmp

def solution4(head):
	totalduplicate=0
	seenBefore=[False]*6001
	frequency =[0]*6001
	temp=head
	while temp is not None:

		frequency[temp.data]+=1
		if frequency[temp.data]>1:
			seenBefore[temp.data] = True

		temp=temp.next

	return seenBefore

linkedList = LinkedList()

readFile("activision.txt")
readFile("vivendi.txt")

print("Reading the employee IDs from both files and creating a single liked list")
linkedList.printList()

print("\nSolution 1: Comparing elements using nested loops to find duplicates")
linkedList.compareList()

print("Solution2 Sortbubble")
bs(linkedList.head)
linkedList.printList()

print("\nSolution 3: Merge sort (recursive) and determining if there are duplicates in the list.")

mergeSort(linkedList.head)
linkedList.printList()

print("Solution4")
seenBefore = solution4(linkedList.head)
linkedList.printListForSol4(seenBefore)
