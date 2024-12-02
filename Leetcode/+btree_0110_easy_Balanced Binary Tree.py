"""
02.12.2024. Topics: Tree, Depth-First Search, Binary Tree
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth
of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10**4 <= Node.val <= 10**4

Let's analyze the problem using the Depth-First Search pattern flowchart.
https://algo.monster/liteproblems/110
Here is a detailed walkthrough:

Is it a graph?

Yes: A binary tree is a type of graph where each node has up to two children.
Is it a tree?

Yes: The given structure is specifically a binary tree.
Does the problem involve performing a Depth-First Search (DFS)?

Yes: We need to verify if the tree is balanced by checking the heights of subtrees,
a task well-suited for DFS as we can explore each branch completely before moving
on to the next one.

Заключение: Блок-схема предлагает использовать шаблон DFS для этой проблемы.
В DFS вы можете использовать рекурсию для вычисления высоты каждого поддерева.
В каждом узле убедитесь, что разница высот левого и правого поддеревьев не превышает 1,
возвращая эту информацию вверх по стеку вызовов.
Если какое-либо поддерево не сбалансировано, все дерево считается несбалансированным

Intuition
Решение этой проблемы включает рекурсивный подход, при котором мы обходим дерево,
чтобы проверить высоту как левого, так и правого поддеревьев для каждого узла и проверить
условие баланса (что разница в высоте не более единицы).
Интуиция, лежащая в основе решения, заключается в выполнении обхода дерева в обратном порядке.
Обход в обратном порядке означает, что мы проверяем поддеревья перед тем,
как работать с текущим узлом, что естественным образом позволяет нам проверить,
сбалансированы ли поддеревья, а также вычислить их высоты.

Если в какой-либо момент мы обнаруживаем, что поддерево не сбалансировано (т. е. разница
в высоте между левым и правым поддеревьями больше 1), мы можем немедленно сделать вывод,
что дерево не сбалансировано по высоте.
Функция height вычисляет высоту дерева, корнем которого является заданный узел.
Если левое или правое поддерево не сбалансировано (представлено высотой -1) или
если высоты поддеревьев текущего узла отличаются более чем на 1, она возвращает -1,
что указывает на то, что дерево не сбалансировано, начиная с этого узла.
Если поддеревья сбалансированы, функция возвращает фактическую высоту, которая равна 1 плюс
максимальная из высот левого и правого поддеревьев.
Функция isBalanced вызывает функцию высоты с корневым узлом и проверяет,
является ли возвращаемое значение неотрицательным.
Неотрицательное возвращаемое значение указывает на то, что дерево сбалансировано,
тогда как значение -1 указывает на то, что это не так. Используя этот подход,
нам нужно обойти каждый узел только один раз, что дает нам эффективный алгоритм со сложностью
по времени O(n), где n — количество узлов в дереве.
"""
from typing import Optional

import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 8 ms Beats 40.60%
# Memory 17.54 MB Beats 6.98%
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of a binary tree rooted at `node`.
        def calculate_height(node):
            # Base case: if the node is None, the height is 0.
            if node is None:
                return 0

            # Recursively find the height of the left and right subtrees.
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            # If either subtree is unbalanced (indicated by a height of -1),
            # or the difference in heights is greater than 1, the tree is unbalanced.
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # If the tree is balanced, return the height of the tree.
            # Height of a node is 1 plus the maximum of the heights of its subtrees.
            return 1 + max(left_height, right_height)

        # The tree is balanced if calculate_height does not return -1.
        return calculate_height(root) >= 0

class Solution2(object):
    def isBalanced(self, root):

        def dfs(node):
            if not node: return [True,0]
            left=dfs(node.left)
            right=dfs(node.right)
            balanced=(left[0] and right[0] and abs(left[1]-right[1])<=1)
            return[balanced,1+max(left[1],right[1])]

        return dfs(root)[0]

if __name__=="__main__":
    s=Solution()
    s.isBalanced()