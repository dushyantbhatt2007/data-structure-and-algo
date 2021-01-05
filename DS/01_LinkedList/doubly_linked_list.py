class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node.prev = itr
        itr.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data=data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid index")

        count = 0

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head

        while itr:
            if count == index - 1:
                node = itr.next.next
                if node is not None:
                    node.prev = itr.next
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise ValueError("Invalid index")

        if index == 0:
            node = Node(data=data)
            self.head.prev = node
            node.next = self.head
            self.head = node

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data=data, prev=itr, next=itr.next)
                itr.next = node
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if data_after == itr.data:
                node = Node(data=data_to_insert, prev=itr, next=itr.next)
                itr.next = node
                print("Inserted successfully")
                break
            itr = itr.next
        print("value not found")

    def remove_by_value(self, data):

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            print("deleted successfully")
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                print("deleted successfully")
                break
            itr = itr.next
        print("value not found")

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        dlistr = ''
        while itr:
            dlistr += str(itr.data) + '<-->'
            itr = itr.next

        print(dlistr)

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        lstr = ''

        while itr:
            lstr += '<-->' + itr.data
            itr = itr.prev

        print(lstr)


if __name__ == '__main__':
    dli = DoublyLinkedList()
    dli.insert_at_begining(5)
    dli.insert_at_begining(35)
    dli.insert_at_begining(52)
    dli.print()
    dli.insert_at_end(43)
    dli.print()
    dli.insert_values(["1", "8", "4", "2", "9"])
    dli.print()
    dli.remove_at(4)
    dli.print()
    dli.remove_at(0)
    dli.print()
    dli.remove_at(2)
    dli.print()
    dli.insert_at(2, "232")
    dli.print()
    dli.insert_at(0, "23")
    dli.print()
    dli.insert_after_value(data_after="232", data_to_insert="213")
    dli.print()
    dli.remove_by_value("213")
    dli.print()
    dli.remove_by_value("23")
    dli.print()
    print("Length of list is: ", dli.get_length())
    dli.print_backward()
