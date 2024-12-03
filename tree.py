
class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.count = 0
        self.root = None
    
    def contains_helper(self, value, node: Node):
        if value == node.value:
            return True
        if node == None:
            return False
        if value < node.value and node.left is not None:
            return self.contains_helper(value,node.left)
        elif value > node.value and node.right is not None:
            return self.contains_helper(value, node.right)

    def __contains__(self, value):
        if self.root is not None:
            return self.contains_helper(value, self.root)        

    def index_check(self, index):
        if type(index) != int:
            raise TypeError(f"Index is not an integer. INDEX = {index}")
        if index < 0:
                index += self.count
        if index < 0:
            raise IndexError(f'Negative index out of range. INDEX = {index}')
        elif index >= self.count:
            raise IndexError(f'Index larger than range. INDEX = {index}')
        else:
            return index
    def __len__(self):
        return self.count
    
    def insert_helper(self, value, node:Node):
        if value < node.value: #case: value less than root (go left)
            if node.left is not None: #keep going down tree
                self.insert_helper(value,node.left)
            else: #arrived at bottom
                node.left = Node(value)
        elif value > node.value:
            if node.right is not None:
                self.insert_helper(value,node.right)
            else:
                node.right = Node(value)

    def insert(self, value):
        if self.root is None: #case: nothing in tree
            self.count += 1
            self.root = Node(value) 
            return 1
        elif value not in self: #if the value is already in the tree, do nothing
            self.count += 1
            self.insert_helper(value, self.root)
            return 1
        else:
            return 0
         
    def clear(self):
        save_the_counter = int(self.count)
        self.root = None
        self.count = 0
        return save_the_counter
    
    def str_helper(self, node: Node):
        string = ''
        
        if node is not None: #base case
            if node.left is None and node.right is None:
                string += f"{node.value}" #no child case
            elif node.left is None:
                string += '(-' #one child case
                string += f" {node.value} "
                string += f"{self.str_helper(node.right)})"
            elif node.right is None: #one child case
                string += f"({self.str_helper(node.left)}"
                string += f" {node.value} "
                string += '-)'
            else: # 2 child case
                string += f"({self.str_helper(node.left)}"
                string += f" {node.value} "
                string += f"{self.str_helper(node.right)})"

        return string
        
    def __str__(self):
        if self.root is None:
            return '-'
        else:
            return self.str_helper(self.root)

    def getitem_helper(self, node):
        string = ''
        if node is not None:
            string += f"{self.getitem_helper(node.left)}"
            string += f" {node.value} "
            string += f"{self.getitem_helper(node.right)}"
            
        return string

    def __getitem__(self, index):
        index = self.index_check(index) #check valid index + convert to positive 
        item_list = self.getitem_helper(self.root).split()
        return item_list[index]
            
    def successor(self, node): #use for finding right most node 
        curr = node.left
        while curr is not None and curr.right is not None:
            curr = curr.right #just return the right most node
        return curr

    def remove_helper(self, node, item):
        if node is None:
            return None
        if node.value > item: #navigate to node
            node.left = self.remove_helper(node.left, item)
        elif node.value < item:
            node.right = self.remove_helper(node.right, item)
        elif node.value == item:
            if node.left == None and node.right == None: #no child case
                return None
            elif node.left is None: # one child case
                return node.right
            elif node.right is None: #one child case
                return node.left
            else: #2 child case
                succ = self.successor(node) #find the right most node
                node.value = succ.value
                node.left = self.remove_helper(node.left, succ.value)
        return node
  
    def remove(self, item):
        if self.root == None:
            return 0
        if item not in self: #case: value not in tree
            return 0
        else:
            self.count -= 1
            self.root = self.remove_helper(self.root, item)
            return 1
            #case: node.left = None and node.right = None (no child)
            #case: node.left = none or node.right = none (1 child)
            #case: two child, else
        


#fxns to write: __str__()
# remove()
#code case for insert: what if value is already in tree?
#use getitem to check

if __name__ == '__main__':
    def assertNodeclass():
        try:
            c = Node()
            pass
        except:
            raise TypeError('node class does not exist.')
    assertNodeclass()
    
    c = Tree()
    c.insert(12)
    c.insert(0)
    c.insert(14)
    c.insert(13)
    c.insert(7)
    c.insert(13)
    c.insert(500)
    c.insert(200)
    c.insert(-200)
    c.insert(-13)                                                                           
    
    c.insert(9)
    print(str(c))
    print(9 in c)
    print(f"get item test: {c[2]}")
    print(len(c))
    c.remove(12)
    print(str(c))
    print(c.clear())
    print(len(c))

    
    

      