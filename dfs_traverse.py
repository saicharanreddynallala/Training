class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    print(root.val)#preorder
    printing(root.left)
    #print(root.val) #inorder
    printing(root.right)
    #print(root.val) #postorder
root=node(1)
root.left=node(2)
root.right=node(3)
printing(root)