class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None
        self.prev = None
        self.metadata = {
            'song_name': None,
            'artist': None,
            'album': None,
        }

    def __repr__(self):
        return f'| PREV: {self.prev} | DATA: {self.data} | NEXT: {self.next} |'


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def __repr__(self) -> str:
        nodes = ['START']

        for node in self:
            nodes.append(str(node.data))

        nodes.append('NIL')

        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        length = 0

        for _ in self:
            length += 1

        return length

    def insert_at_beginning(self, element: Node) -> None:
        if self.start is None:
            self.start = element
            self.end = element
            return

        element.next = self.start
        self.start.prev = element
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        if self.start is None:
            self.start = element
            self.end = element
            return

        element.prev = self.end
        self.end.next = element
        self.end = element

    def insert_after_node(self, element: Node, node_reference: any) -> None:
        for node in self:
            if node.data == node_reference:
                element.next = node.next
                element.prev = node

                if node.next is not None:
                    node.next.prev = element
                else:
                    self.end = element

                node.next = element
                return

    def delete_node(self, element_data: any) -> None:
        if self.start is None:
            return

        for node in self:
            if node.data == element_data:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.start = node.next

                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.end = node.prev

                return

    def search(self, element_data: any) -> Node | None:
        for node in self:
            if node.data == element_data:
                return node

        return None