class NewNode():
    def __init__(self,key):
        self.key = key
        self.left=None 
        self.right=None


'''inserting new node to binary Tree'''
def insert(root,data):

    while(root != None):
        if(not root.left):
            root.left = NewNode(data)
            break
        else:
            root = root.left

        if(not root.right):
            root.right = NewNode(data)
            break
        else:
            root = root.right

'''inserting new node to binary Tree'''
def delete(root,data):

    if(root != None):
        if(not root.right or not root.left):
            return None
        if(root.left.key == data):
            temp = root.left
            if(not temp.right or not temp.left):
                print (root.left.key)
                root.left = None
                return None
        elif(root.right.key == data):
            temp = root.right
            if(not temp.right or not temp.left):
                root.right = None
                return None
        else:
            delete(root.left,data)
            delete(root.right,data)
    return None


'''Inorder traversal '''
def Inorder(root):
    if(root != None):
        Inorder(root.left)
        print(root.key,end=" ")
        Inorder(root.right)

'''preorder traversal '''
def preorder(root):
    if(root != None):
        print(root.key,end=" ")
        preorder(root.left)     
        preorder(root.right)

'''postorder traversal '''
def postorder(root):
    if(root != None):
        postorder(root.left)     
        postorder(root.right)
        print(root.key,end=" ")

''' Right View of Tree'''
def rightview(root,current_node,max_mode):
    temp_max_node = max_mode
    if(root != None):
        if(current_node > temp_max_node):
            print (root.key,end=" ")
            temp_max_node = current_node

        temp_max_node = rightview(root.right,current_node+1,temp_max_node)
        temp_max_node = rightview(root.left,current_node+1,temp_max_node)
    return temp_max_node

''' Left View of Tree'''
def leftview(root,current_node,max_mode):
    temp_max_node = max_mode
    # print(root.key)
    if(root != None):
        if(current_node > temp_max_node):
            print (root.key,end=" ")
            temp_max_node = current_node

        temp_max_node = leftview(root.left,current_node+1,temp_max_node)
        temp_max_node = leftview(root.right,current_node+1,temp_max_node)
    return temp_max_node

''' Top View of Tree'''
def topview(root):
    if(root != None):
        print(root.key,end=" ")
        left_temp = root.left
        while (left_temp != None):
            print (left_temp.key,end=" ")
            left_temp = left_temp.left

        right_temp = root.right
        while (right_temp != None):
            print (right_temp.key,end=" ")
            right_temp = right_temp.right
    return 1



root = NewNode(1)
root.left = NewNode(2)
root.left.left = NewNode(3)
root.left.left.left = NewNode(8)
root.left.left.right = NewNode(10)
root.right = NewNode(4)
root.right.left = NewNode(5)
root.right.left.right = NewNode(9)
root.right.right = NewNode(6)

'''        
                           (1)
                           / \
                          /   \
                        (2)   (4)
                        /     / \
                       /     /   \
                     (3)    (5)  (9)
                     / \     \
                    /   \     \
                  (8)   (10)  (9)
                   
                   '''
print("Inorder traversal Before Insert : ",end=" ")
Inorder(root)

insert(root,7)
print()
print("Inorder traversal After Insert : ",end=" ")
Inorder(root)

delete(root,7)
print()
print("Inorder traversal after Delete : ",end=" ")
Inorder(root)


print()
print("right Views : ",end=" ")
rightview(root,0,-1)


print()
print("left Views : ",end=" ")
leftview(root,0,-1)

print()
print("top Views : ",end=" ")
topview(root)



