class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next=Node(data=data, next=None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data=data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid index")

        if index == 0:
            self.head = None
            return

        count = 0

        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise ValueError("Invalid index")

        if index == 0:
            self.head = Node(data=data, next=None)
            return

        count = 0

        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data=data, next=itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        inserted = False

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data=data_to_insert, next=itr.next)
                itr.next = node
                inserted = True
                break
            itr = itr.next

        if inserted:
            print("value %s inserted after value %s" % (data_to_insert, data_after))
        else:
            print("value not found")

    def remove_by_value(self, data):
        found = False

        itr = self.head
        while itr:
            if itr.next is not None and itr.next.data == data:
                itr.next = itr.next.next
                found = True
                break
            itr = itr.next

        if found:
            print("value %s removed successfully" % data)
        else:
            print("value not found")

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next

        print(listr)


if __name__ == '__main__':
    li = LinkedList()
    li.insert_at_begining(5)
    li.print()
    li.insert_at_begining(89)
    li.print()
    li.insert_at_end(1)
    li.insert_at_end(10)
    li.print()
    li.insert_at_begining(11)
    li.print()
    li.insert_values(data_list=["1","5","3","8"])
    print("Length of linked list is: ", li.get_length())
    li.print()
    li.remove_at(3)
    print("Length of linked list is: ", li.get_length())
    li.print()
    li.insert_at(3, '10')
    li.print()
    li.insert_after_value('5', '55')
    li.print()
    li.insert_after_value('5454', '55')
    li.remove_by_value("3")
    li.print()
    li.remove_by_value("3")
