class OrderedDict:
    class ListNode:
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    def __init__(self):
        self.data = {}
        self.queue_dict = {}
        self.head = None
        self.tail = None

    def insert(self, key, value) -> None:
        if key not in self.data:
            new_node = OrderedDict.ListNode(key)
            if self.tail:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                self.head = self.tail = new_node
            self.queue_dict[key] = new_node
        self.data[key] = value

    def delete(self, key) -> None:
        if key in self.data:
            node = self.queue_dict[key]

            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next

            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev

            del self.queue_dict[key]
            del self.data[key]

    def get(self, key):
        return self.data.get(key, None)

    def get_queue(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.key)
            current = current.next
        return result

    def __repr__(self) -> str:
        return f'Словарь: {self.data}\n' \
               f'Порядок ключей: {self.get_queue()}\n' \
               f'HashMap: {list(self.queue_dict.keys())}'


od = OrderedDict()

od.insert('null', 'peach')
od.insert('first', 'banana')
od.insert('second', 'apple')
od.insert('third', 'lychee')
print(od)
print('-' * 50)

od.delete('first')
print(od)
