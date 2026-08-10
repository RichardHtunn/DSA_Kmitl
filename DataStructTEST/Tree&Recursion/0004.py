class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None

def list_to_bst(list_nums):
       
       if len(list_nums) == 0:
           return None

       # หาตัวตรงกลางของ list ที่รับมาก่อน 
       mid = (len(list_nums)) / 2
       mid = int(mid)
       
       # เเล้ว กำหนดให้เป็น root
       root =  TreeNode(list_nums[mid])

       # เอาตัวตรงกลางของฝั่งซ้ายหลังจากเเบ่ง(ก่อนตัว mid) มาเป็น ลูกฝั่งซ้ายของ root
       root.left = list_to_bst(list_nums[:mid])
       
       # เอาตัวตรงกลางของฝั่งขวาหลังจากเเบ่ง(หลังตัว mid) มาเป็น ลูกฝั่งขวาของ root
       root.right = list_to_bst(list_nums[mid+1:])
       return root

def preOrder(node): 

    if not node: 

        return      

    print(node.val)

    preOrder(node.left) 

    preOrder(node.right)   



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)


list_nums = sorted([int(item) for item in input("Enter list : ").split()])

# print(list_nums)

result = list_to_bst(list_nums)

print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)