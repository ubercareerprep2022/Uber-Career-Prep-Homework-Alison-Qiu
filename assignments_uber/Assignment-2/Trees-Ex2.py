# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#similar question on leetcode 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        if root != None: 
            ans.append([root.val])
            queue.append([root])
        while queue != []:
            cur_level = queue.pop(0)
            nxt_level = []
            for cur_node in cur_level:
                if cur_node.left != None:
                    nxt_level.append(cur_node.left)
                if cur_node.right != None:
                    nxt_level.append(cur_node.right)
            if nxt_level != []:
                queue.append(nxt_level)
                ans.append([node.val for node in nxt_level])
        return ans