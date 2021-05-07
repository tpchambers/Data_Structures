class Node():
    
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class CircularLinkedList(object):
    def __init__(self,head = None,end = None):
        self.head = head
        self.end = end
        self.size = 1
    
    def insert_end(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.end = node
            return 
        self.size += 1
        
        if self.head != None:
            node = Node(data)
            self.end.next = node
            self.end = node
            node.next = self.head
        
    def insert_beginning(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.end = node
        if self.head != None:
            node = Node(data)
            self.end.next = node
            node.next = self.head
            self.head = node
        self.size +=1
        return
            
    def traverse(self):
        node_list = []
        curr = self.head
        while curr.next:
            node_list.append(curr.data)
            curr = curr.next
            if curr == self.head: 
                break
        return node_list
        
    def _pop(self):
        return self.head.data

    def insert_mid(self,data):
        if self.getsize() % 2 == 0:
            mid = self.getsize()//2
        else:
            mid = ((self.getsize()+1)//2)
        
        curr = self.head
        node = Node(data)
        for i in range(mid):
            curr = curr.next
        node.next = curr
        prev_node = self.head
        for i in range(mid - 1):
            prev_node = prev_node.next
        prev_node.next = node
        self.size += 1
        
        return 
        
    def _display(self):
        results = self.traverse()
        for i in range(len(results)):
            print(results[i],end='->')
        print(self.head.data)
    
    def getsize(self):
        return self.size
    
    def __len__(self):
        if self.head == None:
            return 0
        size = 1
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
            size += 1
        return size
    
    def remove_beginning(self):
        if self.head:
            new_head = self.head.next
            self.head = new_head
            self.end.next = new_head
        else:
            raise ValueError 
        self.size -= 1
            
    def remove_end(self):
        curr = self.head
        for i in range(self.getsize()-2):
            curr = curr.next
        new_end = curr
        new_end.next = self.head
        self.end=new_end
        self.size -= 1
        return 
        
    def removal(self,value):
        curr = self.head
        prev = self.end
        prev.next = curr
        
        while curr.data != value: 
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.size -= 1
        return curr
    
    def get_count(self, start):
        count = 1
        curr = start
        while curr.next != start:
            count += 1
            curr = curr.next
        return count
        

    def reverse(self):
        curr = self.end.next
        next = curr.next

        while curr != self.end:
            prev = curr 
            curr = next 
            next = curr.next 
            curr.next = prev 
        
        next.next = curr
        curr.next = prev
        self.head = curr
        self.end = next


    def execute(self):
        curr = self.head
        while self.get_count(curr) != 1:
            curr.next = curr.next.next
            curr=curr.next
        return curr
    
    def getJosephus(self,skips):
        curr = self.head
        temp = self.head
        while curr.next != curr:
            count = 1
            while count!= skips:
                temp = curr
                curr=curr.next
                count += 1 
            temp.next = curr.next
            curr=temp.next
        
        return curr.data


       
def main():
    inst = CircularLinkedList()
    n =int(input("number of nodes:"))
    for i in range(n):
        inst.insert_end(i+1)
    skips = int(input("number to skip:"))
    print("Last man standing is prisoner",inst.getJosephus(skips),"!")


if __name__ == '__main__':
    t = CircularLinkedList()
    t.insert_end(5)
    t.insert_end(6)
    t.insert_mid(27)
    t.insert_end(16)
    t.insert_mid(15)
    t.insert_beginning(15)
    t.insert_beginning(15)
    t.remove_beginning()
    t.remove_end()
    t.remove_end()
    t.remove_beginning()
    t.insert_end(16)
    t.insert_mid(15)
    t.insert_beginning(15)
    t.insert_beginning(15)
    t.reverse()
    print(t.traverse())
