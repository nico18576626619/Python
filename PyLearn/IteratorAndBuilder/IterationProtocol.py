class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]

    def __repr__(self):
        return "node({!r})".format(self._value)


    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_fisrt(self):
        yield self
        for c in self:
            yield from c.depth_fisrt()

if __name__=='__main__':
    root=Node(0)
    child1=Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child3=Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child1.add_child(child3)
    child1.add_child(child4)
    child2.add_child(child5)
    child3.add_child(Node(6))
    child5.add_child(Node(7))

    for ch in root.depth_fisrt():
        print(ch)