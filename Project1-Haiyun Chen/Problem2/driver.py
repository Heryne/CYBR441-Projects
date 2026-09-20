
# @Author: Haiyun Chen
# @Date  : 2026/9/20 13:27
# @File  : driver.py

from BinarySearchTree import BinarySearchTree

def main():
    bst = BinarySearchTree()

    print("\n--------------- insertion ---------------")
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)
    print(bst)

    print("\n--------------- search ---------------")
    print(f"Search -> 40: {bst.search(40)}")
    print(f"Search -> 99: {bst.search(99)}")

    print("\n--------------- traversal ---------------")
    print(f"inorder -> {bst.inorder()}")
    print(f"preorder -> {bst.preorder()}")
    print(f"postorder -> {bst.postorder()}")

    print("\n--------------- deletion ---------------")
    print(f"Delete -> 20: {bst.delete(20)}")
    print(f"Delete -> 50: {bst.delete(50)}")
    print(f"After: inorder -> {bst.inorder()}")


if __name__ == '__main__':
    main()