class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None: # если очередь пуста, возвращаем None
            return None
        
        val = self.start.data # сохраняем значение первого элемента
        if self.start == self.end: # если в очереди один элемент, обнуляем ссылки на начало и конец
            self.start = None
            self.end = None
        else: # если в очереди больше одного элемента, переназначаем ссылку на начало
            self.start = self.start.nref
            self.start.pref = None
        
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val) # создаем новый узел с переданным значением
        
        if self.start is None: # если очередь пуста, новый узел становится началом и концом очереди
            self.start = new_node
            self.end = new_node
        else: # если в очереди есть элементы, добавляем новый узел в конец
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0: # если нужно вставить элемент в начало, вызываем метод push()
            self.push(val)
            return
        
        new_node = Node(val) # создаем новый узел с переданным значением
        
        current = self.start
        for i in range(n-1): # ищем элемент с номером n-1
            if current is None: # если дошли до конца списка и не нашли нужный элемент, выходим из метода
                return
            current = current.nref
        
        if current is None: # если дошли до конца списка и не нашли нужный элемент, добавляем новый узел в конец
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node
        else: # если нашли нужный элемент, вставляем новый узел между ним и предыдущим
            new_node.nref = current.nref
            new_node.pref = current
            current.nref = new_node
            if new_node.nref is not None:
                new_node.nref.pref = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()