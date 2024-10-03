"""
словарь типа collections ordered dict

поиск / вставка / удаление / получение за o(1)


изменение значения ключа на порядок ключей не влияет


хэш-таблица (или обычный словарь) для порядка эл-тов
"""


class OrderedDict:
    """
    Словарь со списком порядком добавления элементов. Сложность всех функций - O(1).
    """

    def __init__(self):
        self.data = {}
        self.queue = []
        self.queue_dict = {}

    def insert(self, key, value) -> None:
        """
        Добавление элемента словаря.
        :param key: 
        :param value: 
        :return: 
        """
        if key not in self.data:
            self.queue_dict[key] = len(self.queue)
            self.queue.append(key)
        self.data[key] = value

    def delete(self, key) -> None:
        """
        Удаление элемента словаря.
        :param key: 
        :return: 
        """
        if key in self.data:
            index = self.queue_dict[key]
            last = self.queue[-1]

            self.queue[index] = last
            self.queue_dict[last] = index

            self.queue.pop()
            del self.queue_dict[key]
            del self.data[key]

    def get(self, key):
        """
        Получение элемента словаря.
        :param key: 
        :return: 
        """
        return self.data.get(key, None)

    def get_queue(self) -> list:
        """
        Получение порядка добавление элементов.
        :return: 
        """
        return self.queue

    def __repr__(self) -> str:
        return f'Словарь: {self.data}\n' \
               f'Порядок ключей: {self.queue}\n' \
               f'HashMap: {self.queue_dict}'


od = OrderedDict()

od.insert('first', 'banana')
od.insert('second', 'apple')
od.insert('null', 'peach')
print(od)

print('-' * 30)

od.insert('first', 'pear')
od.delete('second')
print(od)

print(od.get_queue())
