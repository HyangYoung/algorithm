class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        # currentNode는 임시로 만든 포인터
        currentNode = self.head
        while True:
            # 해당 노드가 마지막인 경우 멈추고
            if currentNode.next is None:
                break
            # 그렇지 않은 경우 계속 다음 노드를 탐색
            currentNode = currentNode.next
        # 포인터의 바로 다음이 새로운 노드일 경우 앞 뒤 연결
        currentNode.next = newNode
        newNode.previous = currentNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        print("Printing from the beginning")
        # head => nodeOne -> nodeTwo -> nodeThree
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            if currentNode.next is None:
        # reverseTraversalNode는 반대방향으로 움직이는 새로운 포인터
                reverseTraversalNode = currentNode
            currentNode = currentNode.next
        print("Printing from end")
        while True:
            if reverseTraversalNode is None:
                break
            print(reverseTraversalNode.data)
            reverseTraversalNode = reverseTraversalNode.previous



nodeOne = Node('Joe')
nodeTwo = Node('Mary')
nodeThree = Node('Grace')
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.printList()
