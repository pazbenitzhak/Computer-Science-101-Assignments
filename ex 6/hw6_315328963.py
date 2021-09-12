# Skeleton file for HW6 - Spring 2019/20 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).


############
# QUESTION 1
############

class ImprovedGenerator:
    def __init__(self, g):
        self.gen = g
        self.val = next(self.gen)

    def has_next(self):
        if self.val!=StopIteration:
            return True
        return False

    def peek(self):
        return self.val

    def __iter__(self):
        return self
        # yield next(self)

    def __next__(self):
        try:
            k = self.val
            self.val = next(self.gen)
            return k
        except StopIteration:
            if k != StopIteration:
                self.val = StopIteration
                return k  #last letter case
            else:
                i = 1
        if i == 1:    # iterator ends case
            self.val = StopIteration
            raise StopIteration

    def product(self, other):
        new_gen = ImprovedGenerator((i for i in range(1))) # in order to start 'from scratch'
        union = gen_unify(self.gen, other.gen)
        new_gen.gen = union
        new_gen.val = (self.val,other.val)
        return new_gen

def gen_unify(a, b):
    while True:
        try:
            yield (next(a), next(b))
        except StopIteration:
            return

############
# QUESTION 3
############
def maxmatch(T, p, triple_dict, w=2**12-1, max_length=2**5-1):
    """ finds a maximum match of length k<=2**5-1 in a w long window, T[p:p+k] with T[p-m:p-m+k].
        Returns m (offset) and k (match length) """

    assert isinstance(T,str)
    n = len(T)
    maxmatch = 0
    offset = 0
    if p + 3 > len(T) or T[p:p+3] not in triple_dict:
        return offset, maxmatch
    sequence = T[p:p+3]
    k_list = []
    if T[p:p+3] in triple_dict:
        for m in triple_dict[sequence]:
            k_list.append(m)
    for m in k_list:
        k = 3
        while k <min(n-p, max_length) and T[p+k]==T[m+k]:
            k +=1
        if k > maxmatch:
            maxmatch = k
            offset = p-m
    return offset, maxmatch


def LZW_compress(text, w=2**12-1, max_length=2**5-1):
    """LZW compression of an ascii text. Produces a list comprising of either ascii characters
       or pairs [m,k] where m is an offset and k>=3 is a match (both are non negative integers) """
    result = []
    n = len(text)
    p = 0
    triple_dict = {}

    while p<n:
        m,k = maxmatch(text, p, triple_dict, w, max_length)
        if k<3:
            result.append(text[p])
            add_triple_to_dict(text, p, triple_dict) #it's relevant to add to dict
            p+=1
        else:
            result.append([m,k])
            p+=k
    return result  # produces a list composed of chars and pairs

def add_triple_to_dict(text, p, triple_dict):
    """ Adds to the dictionary mapping from a key T[p:p+2] to a new
        integer in a list p."""
    if p+3 > len(text): return
    triple = text[p:p+3]
    if triple in triple_dict:
        triple_dict[triple].append(p)
    else:
        triple_dict[triple] = [p]



############
# QUESTION 6
############

###### CODE FROM LECTURE - DO NOT CHANGE ######
def fingerprint(text, basis=2 ** 16, r=2 ** 32 - 3):
    """ used to compute karp-rabin fingerprint of the pattern
        employs Horner method (modulo r) """
    partial_sum = 0
    for ch in text:
        partial_sum = (partial_sum * basis + ord(ch)) % r
    return partial_sum


def text_fingerprint(text, m, basis=2 ** 16, r=2 ** 32 - 3):
    """ computes karp-rabin fingerprint of the text """
    f = []
    b_power = pow(basis, m - 1, r)
    list.append(f, fingerprint(text[0:m], basis, r))
    # f[0] equals first text fingerprint
    for s in range(1, len(text) - m + 1):
        new_fingerprint = ((f[s - 1] - ord(text[s - 1]) * b_power) * basis + ord(text[s + m - 1])) % r
        # compute f[s], based on f[s-1]
        list.append(f, new_fingerprint)  # append f[s] to existing f
    return f
##############################################


def is_rotated_1(s, t, basis=2 ** 16, r=2 ** 32 - 3):
    """
    fill-in your code below here according to the instructions
    """
    assert len(s) == len(t)  # entrance condition
    a = fingerprint(s[0], basis=2 ** 16, r=2 ** 32 - 3)
    for i in range(len(t)):
        if fingerprint(t[i], basis=2 ** 16, r=2 ** 32 - 3)==a: # then it's a potential match
            start_index = i
            count = 0
            for k in range(1, len(s)):
                if start_index+k==len(s):  #to nullify index
                    g = k
                    start_index = -g
                if fingerprint(s[k], basis=2 ** 16, r=2 ** 32 - 3)==fingerprint(t[start_index+k], basis=2 ** 16, r=2 ** 32 - 3):
                    count +=1 # if so, they are similar in one note
            if count == len(s)-1: # they are the same in every note
                return True
    return False   # no potential 'turns' found


def is_rotated_2(s, t):
    """
    fill-in your code below here according to the instructions
    """
    assert len(s) == len(t)
    a = fingerprint(s[0], basis=2 ** 16, r=2 ** 32 - 3)
    start_indexes= []
    for i in range(len(t)):
        if fingerprint(t[i], basis=2 ** 16, r=2 ** 32 - 3)==a:
            start_indexes.append(i)
    for i in start_indexes:
        new_string = t[i:] + t[:i]
        if text_fingerprint(s, len(s))==text_fingerprint(new_string, len(new_string)):
            return True
    return False


############
# QUESTION 7
############

from matrix import Matrix

# (1)
def had(n):
    mat = Matrix(pow(2,n), pow(2,n))
    for i in range(pow(2,n)):
        for j in range(pow(2,n)):
            mat[i,j] = had_local(n,i,j)
    return mat

def had_local(n, i, j):
    ''' finds the ith row, jth column number in Hadamard's n matrix '''
    if n==0: #base case
        return 0
    if i < 2**(n-1) and j<2**(n-1): #upper left
        return had_local(n-1, i, j)
    if i <2**(n-1) and j>=2**(n-1): #lower left
        return had_local(n-1, i, j-2**(n-1))
    if i>=2**(n-1) and j<2**(n-1): #upper right
        return had_local(n-1,i-2**(n-1),j)
    if i>=2**(n-1) and j>=2**(n-1):  #lower right
        return 1-had_local(n-1,i-2**(n-1), j-2**(n-1))
        
had_complete = lambda n : \
               [[had_local(n,i,j) for j in range(2**n)] for i in range(2**n)]


# (2)
def disj(n):
    mat = Matrix(pow(2,n), pow(2,n))
    for i in range(pow(2,n)):
        for j in range(pow(2,n)):
            larger = max(len(bin(i)), len(bin(j)))
            smaller = min(len(bin(i)), len(bin(j)))
            count = 0
            for k in range(-1,-smaller+1,-1):
                if bin(i)[k] == bin(j)[k]=='1':
                    mat[i,j]=0
                    break
                else:
                    count +=1
                    if count == smaller-2:
                        mat[i,j] = 1
    return mat

# (3)
def id_image():
    """
         fill-in your code below here according to the instructions
         use Matrix.load() to load the images
    """
    image = Matrix(30, 300)
    ID = "315328963"
    k = 0
    for number in ID:
        num_mat = Matrix.load('./'+str(number)+'.bitmap')
        for i in range(20):
            for j in range(20):
                image[i,j+k] = num_mat[i,j]
        k +=20
    for i in range(20,30):
        for j in range(300):
            image[i,j] = 255
    for i in range(0,20):
        for j in range(180,300):
            image[i,j] = 255
    return image

########
# Tester
########

def test():

    # Question 1

    g = (i for i in range(5))
    g2 = ImprovedGenerator(g)
    for i in range(5):
        if g2.peek() != i:
            print("error in peek")

        if next(g2) != i:
            print("error in next")

        if (i != 4 and (not g2.has_next())) or (i == 4 and g2.has_next()):
            print("error in has_next")

    try:
        next(g2)
        print("should throw stopiteration")
    except StopIteration:
        print("GOOD: raises StopIteration as should")
    except:
        print("not the correct exception")

    g1 = (i for i in range(3))
    g2 = (i for i in range(3))

    g3 = ImprovedGenerator(g1)
    g4 = ImprovedGenerator(g2)
    g5 = g3.product(g4)

    for i in range(3):
        if next(g5) != (i, i):
            print("error in product")

    # Question 3

    # first convert to tuple to make easy comparison
    compressed = tuple([el if isinstance(el, str) else tuple(el) for el in LZW_compress("abcdabc")])
    if compressed != ('a', 'b', 'c', 'd', (4, 3)):
        print("error in LZW_compress")

    # Question 6
    for func in [is_rotated_1, is_rotated_2]:
        if func("amirrub", "rubamir") != True or \
                func("amirrub", "bennych") != False or \
                func("amirrub", "ubamirr") != True:
            print("error in", func.__name__)

    # Question 7

    # (1)
    had1 = Matrix(2, 2)
    had1[1, 1] = 1
    if had(1)!=had1:
        print("error in had")

    # (2)
    disj1 = Matrix(2, 2, 1)
    disj1[1, 1] = 0
    if disj(1) != disj1:
        print("error in disj")
