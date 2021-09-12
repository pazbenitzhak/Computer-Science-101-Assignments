#Skeleton file for HW5 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to include your ID number (hw5_ID.py).


############
# QUESTION 1
############
class Permutation:
    def __init__(self, perm):
        self.perm = None
        n = len(perm)
        aid = [0 for i in range(n)]
        for i in range(n):
            val = perm[i]
            if val>n-1: #because then it's not a permutation
                return None
            aid[val] += 1
        for item in aid:
            if item!=1: #if so, then we have dups
                return None
        self.perm = perm  # if we don't have dups, it's a permutation
    
    def __getitem__(self, i):
        return self.perm[i]

    def compose(self, other):
        n = len(self.perm)
        comb_perm = []
        for i in range(n):
            item = self[other[i]]
            comb_perm.append(item)
        return Permutation(comb_perm)
        
    def inv(self):
        n = len(self.perm)
        opp = [None for i in range(n)]
        for i in range(n):
            opp[self.perm[i]] = i  # make the opposite
        return Permutation(opp)
    
    def __eq__(self, other):
        return self.perm == other.perm

    def __ne__(self, other):
        return self.perm != other.perm
                    
    def order(self):
        n = len(self.perm)
        rising = [i for i in range(n)]
        identity = Permutation(rising)
        return len(self.make_order(self, [], identity))

    def make_order(self, prod, lst1, idenperm):
        lst1.append(1)
        if prod == idenperm:
            return lst1
        else:
            a = self.compose(prod)
            self.make_order(a, lst1,idenperm)
            return lst1


#This function is not part of the class Permutation
def compose_list(lst):
    if len(lst)==1:
        return lst[0]
    a = lst[-2]
    b = lst[-1]
    prod = a.compose(b) # do permutation by order
    lst[-2] = prod #change the list accordingly
    lst.pop() # delete last item
    compose_list(lst) #make the same for the 'next' perm
    return lst[0] # so in any case we return the 'final' perm   
        



############
# QUESTION 2
############

def printree(t, bykey = True):
        """Print a textual representation of t
        bykey=True: show keys instead of values"""
        #for row in trepr(t, bykey):
        #        print(row)
        return trepr(t, bykey)

def trepr(t, bykey = False):
        """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
        if t==None:
                return ["#"]

        thistr = str(t.key) if bykey else str(t.val)

        return conc(trepr(t.left,bykey), thistr, trepr(t.right,bykey))

def conc(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "|" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """helper for conc"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]==" ":
                i-=1
        return i+1

def rightspace(row):
        """helper for conc"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]==" ":
                i+=1
        return i






class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"
    
    
    
class Binary_search_tree():

    def __init__(self):
        self.root = None


    def __repr__(self): #no need to understand the implementation of this one
        out = ""
        for row in printree(self.root): #need printree.py file
            out = out + row + "\n"
        return out

    
    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)


    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)


    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node


    def depth(self):
        ''' return depth of tree, uses recursion'''
        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)


    def size(self):
        ''' return number of nodes in tree, uses recursion '''
        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)

    def max_sum(self):
        if self.sum_help(self.root,[], []) == []: # max doesn't function with empty list
            return 0
        else:
            return max(self.sum_help(self.root,[], []))

    def sum_help(self, root, smallist, longlist):
        a = root #for comfort
        if a == None: #we should stop
            longlist.append(sum(smallist)) #add current sum
            return longlist
        smallist.append(a.val) #add current root before recursing
        self.sum_help(a.right, smallist, longlist) #right branch
        self.sum_help(a.left, smallist, longlist) #left branch
        smallist.pop() #we now go 'higher' in the tree
        return longlist #finally return list of sums

    def is_balanced(self):
        if self.root == None:
            return True
        if self.help_balance()==False:
            return False
        return True

    def help_balance(self):
        if self.root == None:
            return 0.5
        if self.root.left==None and self.root.right == None:
            return 1
        lefttree = Binary_search_tree()
        lefttree.root = self.root.left
        righttree = Binary_search_tree()
        righttree.root = self.root.right
        left_rec = lefttree.help_balance()
        right_rec = righttree.help_balance()
        if abs(right_rec-left_rec) >1:
            return False
        if right_rec == False or left_rec == False:
            return False
        return 1+max(left_rec, right_rec)

    def diam(self):
        return max(self.diam_help([])[1]) #to get the longest route

    def diam_help(self, lst):
        if self.root == None: #start counting
            return 0, lst
        if self.root.left==None and self.root.right == None:
            return 1, lst
        lefttree = Binary_search_tree() #left branch
        lefttree.root = self.root.left
        righttree = Binary_search_tree() #right branch
        righttree.root = self.root.right
        left_rec = lefttree.diam_help(lst)
        right_rec = righttree.diam_help(lst)
        item = right_rec[0]+left_rec[0]+1 #longest route for the moment
        lst.append(item)
        return 1+max(left_rec[0], right_rec[0]), lst #go on, remember lst


############
# QUESTION 3
############
def same_tree(lst1, lst2):
    if lst1[0]!=lst2[0]: #because than it's surely ain't the same
                return False
    first_left, first_right = help_same(lst1[1:], lst1[0], [], [])
    second_left, second_right = help_same(lst2[1:], lst2[0], [], [])
    for i in range(len(first_left)): #check left branch
                if first_left[i]!=second_left[i]:
                        return False
    for i in range(len(first_right)):  #check right branch
                if first_right[i]!=second_right[i]:
                        return False
    return True  #everyting is well


def help_same(lst, key, left, right):
        if lst == []:
                return left, right
        if lst[0]>key:
                        right.append(lst[0])
        if lst[0]<key:
                        left.append(lst[0])
        return help_same(lst[1:], key, left, right)



############
# QUESTION 4
############

class Node():
    
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return str(self.value) + "(" + str(id(self))+ ")"
	#This shows pointers as well for educational purposes


class DLList():

    def __init__(self, seq=None):
        self.head = None
        self.tail = None
        self.len = 0
        if seq != None:
            for item in seq:
                self.insert(item)
 
    def __len__(self):
        return self.len
     

    def __repr__(self):
        out = ""
        p = self.head
        while  p != None :
            out += str(p) + ", " # str(p) envokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"
        
            
    def insert(self, val, first = False):
        new = Node(val)
        if self.len ==0: # 1st special case
            self.head = new
            self.tail = new
            self.len+=1
        elif self.len ==1: # special case
            if first == False:
                self.tail = new
                self.head.next = self.tail
                self.tail.prev = self.head
                self.len+=1
            else:
                self.head = new
                self.head.next = self.tail
                self.tail.prev = self.head
                self.len+=1
                return None
        else:  # general case
            if first == False:
                prev_tail = self.tail
                new.prev = prev_tail
                prev_tail.next = new
                self.tail = new
                self.len += 1
            else:
                prev_head = self.head
                new.next = prev_head
                prev_head.prev = new
                self.head = new
                self.len += 1
             
    def reverse(self):
        self.item = self.head
        while self.item!=None: #updating each item accordingly
            prev, forw = self.item.prev, self.item.next
            self.item.next, self.item.prev = prev, forw
            self.item = self.item.prev # it's the 'previous' next item
        head, tail = self.head, self.tail # updating head and tail (reversing them)
        self.head = tail
        self.tail = head
    
    def rotate(self, k):
        if k>=self.len:  #no useless reruns
            k = k%self.len
        if k == 0:  #we want no changes
            return self
        head_index = self.len-k
        head_opposite = k
        new_head = self.head
        new_tail = self.tail
        if head_index <=head_opposite: #in order to acheive the best complexity
            for i in range(head_index):
                new_head = new_head.next
            new_tail = new_head.prev  #new tail accordingly to new head
        else:
            for i in range(head_opposite):
                new_tail = new_tail.prev
            new_head = new_tail.next #new head accordingly to new tail
        new_head.prev = None
        new_tail.next = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.head = new_head #finally switch head and tail to new nodes
        self.tail = new_tail

    def delete_node(self, node):
        if node == self.head:   # special case #1
            forw = node.next
            forw.prev = None
            node.next = None
            self.head = forw
            self.len -=1
            return None
        elif node == self.tail:    # special case # 2
            prev = node.prev
            prev.next = None
            node.prev = None
            self.tail = prev
            self.len -=1
            return None
        else: #general case
            prev, forw = node.prev, node.next
            prev.next = forw
            forw.prev = prev
            node.prev, node.next = None, None
            self.len -=1


############
# QUESTION 6
############
# a
def prefix_suffix_overlap(lst, k):
    res = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if lst[i][:k]== lst[j][-k:]:
                res.append((i,j))
    return res

# c
#########################################
### Dict class ###
#########################################

class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [ [] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])
              
    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key) #hash on key only
        item = [key, value]    #pack into one item
        self.table[i].append(item) 

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        lst = []
        group = hash(key) % len(self.table)
        for tup in self.table[group]:
            if tup[0] == key:
                lst.append(tup[1])
        return lst


#########################################
### End Dict class ###
#########################################    

# d
def prefix_suffix_overlap_hash1(lst, k):
    res = []
    dicty = Dict(3*len(lst))
    for i in range(len(lst)):
        dicty.insert(lst[i][:k], i)
    for j in range(len(lst)):
        match = dicty.find(lst[j][-k:])
        for p in range(len(match)):
            if match[p]!=j:
                res.append((match[p],j))
    return res


# f
def prefix_suffix_overlap_hash2(lst, k):
    res = []
    dicty = {}
    for i in range(len(lst)):
        if lst[i][:k] in dicty:
            dicty[lst[i][:k]].append(i)
        else:
            dicty.update({lst[i][:k]:[i]})
    for j in range(len(lst)):
        if lst[j][-k:] in dicty:
            for m in range(len(dicty[lst[j][-k:]])):
                if dicty[lst[j][-k:]][m]!=j:
                    res.append((dicty[lst[j][-k:]][m],j))
    return res






   
    
########
# Tester
########

def test():
    #Testing Q1
    #Question 1
    p = Permutation([2,3,1,0])
    if p.perm != [2,3,1,0]:
        print("error in Permutation.__init__")
    q = Permutation([1,0,2,4])
    if q.perm != None:
        print("error in Permutation.__init__")
    if p[0] != 2 or p[3] != 0:
        print("error in Permutation.__getitem__")
        
    p = Permutation([1,0,2])
    q = Permutation([0,2,1])
    r = p.compose(q)
    if r.perm != [1,2,0]:
        print("error in Permutation.compose")

    p = Permutation([1,2,0])
    invp = p.inv()
    if invp.perm != [2,0,1]:
        print("error in Permutation.inv")
    
    p1 = Permutation([1,0,2,3])
    p2 = Permutation([2,3,1,0])
    p3 = Permutation([3,2,1,0])
    lst = [p1,p2,p3]
    q = compose_list(lst)
    if q.perm != [1,0,3,2]:
        print("error in compose_list")

    identity = Permutation([0,1,2,3])
    if identity.order() != 1:
        print("error in Permutation.order")
    p = Permutation([0,2,1])
    if p.order() != 2:
        print("error in Permutation.order")
    

    #Testing Q2
    #Question 2
    t = Binary_search_tree()
    if t.max_sum() != 0:
        print("error in Binary_search_tree.max_sum")        
    t.insert('e', 1)
    t.insert('b', 2)
    if t.max_sum() != 3:
        print("error in Binary_search_tree.max_sum")        
    t.insert('a', 8)
    t.insert('d', 4)
    t.insert('c', 10)
    t.insert('i', 3)
    t.insert('g', 5)
    t.insert('f', 7)
    t.insert('h', 9)
    t.insert('j', 6)
    t.insert('k', 5)
    if (t.max_sum() != 18):
        print("error in Binary_search_tree.max_sum")


    t = Binary_search_tree()
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("b", 10) 
    t.insert("d", 10) 
    t.insert("a", 10) 
    t.insert("c", 10) 
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("e", 10) 
    t.insert("f", 10)
    if t.is_balanced() != False:
        print("error in Binary_search_tree.is_balanced")

                
    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("error in Binary_search_tree.diam") 

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("error in Binary_search_tree.diam")



    #Testing Q3
    lst = DLList("abc")
    a = lst.head
    if a == None or a.next == None or a.next.next  == None:
        print("error in DLList.insert")
    else:
        b = lst.head.next
        c = lst.tail
        if lst.tail.prev != b or b.prev != a or a.prev != None:
            print("error in DLList.insert")

    lst.insert("d", True)
    if len(lst) != 4 or lst.head.value != "d":
        print("error in DLList.insert")

    prev_head_id = id(lst.head)
    lst.reverse()
    if id(lst.tail) !=  prev_head_id  or lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.value != "d":
        print("error in DLList.reverse")

    lst.rotate(1)
    if lst.head.value != "d" or lst.head.next.value != "c" or lst.tail.value != "a":
        print("error in DLList.rotate")
    lst.rotate(3)
    if lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.prev.value != "a":
        print("error in DLList.rotate")

    lst.delete_node(lst.head.next)    
    if lst.head.next != lst.tail.prev or len(lst)!= 3:
        print("error in DLList.delete_node")
    lst.delete_node(lst.tail)
    if lst.head.next != lst.tail or len(lst) != 2:
        print("error in DLList.delete_node")


        
    #Question 5
    s0 = "a"*100
    s1 = "b"*40 + "a"*60
    s2 = "c"*50+"b"*40+"a"*10
    lst = [s0,s1,s2]
    k=50
    if prefix_suffix_overlap(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap")
    if prefix_suffix_overlap_hash1(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap_hash1(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash1")
    if prefix_suffix_overlap_hash2(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap_hash2(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash2")

