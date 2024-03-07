class Node:
                def __init__(self,data):
                                self.data=data
                                self.left=None
                                self.right=None



def insert(data,root):
                
                if data < root.data:
                                if root.left:
                                                insert(data,root.left)

                                else:
                                                root.left=Node(data)
                else:
                                 if root.right:
                                                 insert(data,root.right)
                                 else:
                                                
                                                root.right=Node(data)
                                                
                                
root=Node(20)
insert(10,root)
insert(30,root)
insert(15,root)
#HW=Check Wether The Thing's Are Inserted Properly
