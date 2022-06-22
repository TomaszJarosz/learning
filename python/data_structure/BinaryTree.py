from typing import Optional, Generic, TypeVar, Any

# https://www.youtube.com/watch?v=yScuF1UgGU0

T = TypeVar('T', bound=Any)


class BinaryTree(Generic[T]):
    value: T
    left: Optional['BinaryTree'] = None
    right: Optional['BinaryTree'] = None

    def __init__(self, value: T):
        self.value = value

    def add(self, value: T) -> None:
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def find(self, value: T) -> Optional[T]:
        if self.value == value:
            return self.value
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def traverse(self, func) -> bool:
        if self.left is not None:
            if not self.left.traverse(func):
                return False
        func(self.value)
        if self.right is not None:
            if not self.right.traverse(func):
                return False
        return True


class Role:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


def main():
    tree = BinaryTree('cbe')
    # tree = BinaryTree(100)
    # tree.add(40)
    # tree.add(50)
    # tree.add(105)
    # tree.add(30)
    # tree.add(35)
    # tree.add(104)
    tree.add('aba')
    tree.add('cba')
    tree.add('aaa')
    tree.add('cbd')
    # tree.add(0.5)
    # tree.add('string')
    print("\n Print Tree:")
    tree.traverse(lambda x: print(x))
    print(tree)


if __name__ == '__main__':
    main()
