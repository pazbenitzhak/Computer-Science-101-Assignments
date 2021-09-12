#Skeleton file for HW2 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw2_ID.py).


############
# QUESTION 1
############

# 1a
def sum_divisors(n):
    ''' calculate the sum of a number's divisors (not including the number itself) '''
    count = 1
    if n == 1:
        return 0
    for i in range(2, int(n**0.5 + 1)):
        if n % i ==0:
            if n // i != i:
                count += i + (n//i)
            else:
                count += i
    return count

# 1b
def legal_par(st):
    openers = ["(", "{", "<", "["]
    closers = [")", "}", ">", "]"]     #distinguish 2 types of characters
    if (st == "") or (st == len(st)*" "):
        return True
    for i in range(4):
        if st.count(openers[i]) != st.count(closers[i]): # check 1st condition
            return False
    if st[0] in closers:
        return False
    st_list = [k for k in st]
    while any(x in st_list for x in closers): # check 2nd condition
        result = pairings_handler(st_list) # check if there is a relevant closure
        if result == ["w"]:
            return False
    if st_list == []:  # if so, than the string is relevant
        return True
    else:
        return False

def pairings_handler(lst):
    ''' a side function whose goal to locate pairings and erase them from list '''
    openers = ["(", "{", "<", "["]
    closers = [")", "}", ">", "]"]
    for g in range(len(lst)):
        if lst[g] in closers:
            match = openers[closers.index(lst[g])]
            element = lst[g-1]
            if element == match:
                del lst[g-1:g+1]
                break
            else:
                lst = ["w"]
                break
    return lst

# 1c
def spiral_sum(k):
    ''' calculates sum of a 'spiral' method '''
    maximum = k-1
    first = 1 # first number of sum
    suming = 1 # collects the overall sum
    for i in range(2, maximum+2, 2):
        first += i
        adders = [k for k in range(first, (first+3*i)+1, i)] # the relevant adders of each iteration
        suming += sum(adders)
        first = max(adders)
    return suming

############
# QUESTION 2
############

# 2b
def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin:
        if bit == "1":
            result *= a
        a = a*a
    return result

# 2c
def modpower_new(a, b, c):
    """ computes a**b mod c using iterated squaring
        assumes b is nonnegative integer  """

    result = 1 # a**0
    while b > 0:
        if b % 3 == 0:
            result = result % c
            a = a*a*a % c
        if b % 3 == 1:
            result = result*a % c
            a = a*a*a % c
        if b % 3 == 2:
            result = result*a*a % c
            a = a*a*a % c
        b = b // 3
    return result


############
# QUESTION 3
############

# 3a
def inc(binary):
    bin_list = list(binary)
    if int(bin_list[-1]) == 0: # first number is 0
        bin_list[-1] = "1"
        new = ""
        new = new.join(bin_list)
        return new
    if binary == "1":
        return "10"
    if binary == "11":
        return "100"
    if int(bin_list[-1]) == 1: # first number is 1
        bin_list[-1] = "0"
        for i in range(-2, -len(bin_list), -1):
            if int(bin_list[i]) == 0: # second number is 0, change to 1 and end
                bin_list[i] = "1"
                new = ""
                new = new.join(bin_list)
                return new
            if int(bin_list[i]) == 1: # second number is 1, change to 0 and save the 1
                bin_list[i] = "0"
                new_num = int(bin_list[i-1])
                new_num += 1
                if new_num == 1: # if it makes the next number one, than we can finish
                    bin_list[i-1] = str(new_num)
                    new = ""
                    new = new.join(bin_list)
                    return new
                bin_list[i-1] = "1" # else (it makes 2), we'll do the same process for the next number
                if i == -len(bin_list)+1: # to keep order with the first note
                    bin_list[i-1] = 2
        if int(bin_list[0]) == 2: # if all numbers are 1
            new = "1" + len(binary)*"0"
            return new

# 3b
def dec(binary):
    bin_list = list(binary)
    if bin_list[-1] == "1": # if number is odd
        bin_list[-1] = "0"
        new_string = ""
        new_string = new_string.join(bin_list)
        return new_string
    for i in range(-2, -len(bin_list), -1): # if number is even
        if bin_list[i] == "1":
            bin_list[i] = "0"
            for k in range(i+1, 0, 1):
                bin_list[k] = "1"
            new_string = ""
            new_string = new_string.join(bin_list)
            return new_string
    new_string = "1"*(len(bin_list)-1) # covers case of 1 and zeros
    return new_string


# 3c
def sub(bin1, bin2):
    if bin2 == '0':
        return bin1
    while bin2 != "0":
        bin1 = dec(bin1)
        bin2 = dec(bin2)
        if bin1 == "":
            return 'error in input'
    return bin1

# 3d
def leq(bin1, bin2):
    if (sub(bin1, bin2) == 'error in input') or (sub(bin1, bin2) == "0"):
        return True
    return False

# 3e
def div(bin1, bin2):
    count = 0
    while leq(bin2, bin1) == True: # we need the 2nd number to be smaller than the first
        bin1 = sub(bin1, bin2)
        count += 1         # collective variable to count number of times to "add" (actually the numbers of wholes)
    shlemim = "0"
    while count != 0:
        shlemim = inc(shlemim)
        count -= 1
    return shlemim

############
# QUESTION 4
############

# 4a
def has_repeat1(s, k):
    listy = [s[i:i+k] for i in range(len(s)-k+1)]
    for i in range(len(s)-k+1):
        opener = s[i:i+k]
        follower = s[i+k-1:i-1+2*k]
        if (opener in listy) and (follower in listy) and (opener == follower): 
            return True
    return False

# 4b
def has_repeat2(s, k):
    for i in range(len(s)-k+1):
        if s[i:i+k] == s[i+k-1:i-1+2*k]:
            return True
    return False
    
############
# QUESTION 5
############

def reading(n):
    if n == 1:
        return "1" # covers base case
    count = 1
    result = ""
    string = reading(n-1)# a must for this code
    for i in range(len(string)):
        if (i > 0) and (string[i] == string[i-1]): # to avoid "double counting"
                continue
        if i == (len(string)-1): # take care of cases for final note is different than the predecessors
            result += str(count) + string[i]
        for k in range(i+1, len(string)): 
            if string[k] == string[i]: # contributes for the "counting"
                count += 1
                if k == (len(string)-1): # avoid cases where last sequence is not referenced
                    result += str(count) + string[i]
            if string[k] != string[i]: # ensure the counting ends, start a new one and update the string
                result += str(count) + string[i]
                count = 1
                break
    return result

############
# QUESTION 6
############
def max_div_seq(n, k):
    ''' returns max sequence of a digit that is divisible in a number '''
    count = 0
    print(n)
    print(str(n))
    dividors = []
    for i in str(n):
        if int(i) % k == 0:
            count += 1
        else:
            dividors += [count]
            count = 0
    print(str(n))
    print(dividors)
    max_seq = max(dividors)
    return max_seq

########
# Tester
########

def test():
    if sum_divisors(4) != 3 or \
       sum_divisors(220) != 284:
        print("error in sum_divisors")
        
    if not legal_par("<<>>") or legal_par("<{>}"):
        print("error in legal_par")
    if not legal_par("<<{}<>()[<>]>>") or legal_par("{{{]}}"):
        print("error in legal_par")

    if spiral_sum(3) != 25 or spiral_sum(5) != 101:
        print("error in spiral_sum")
        
    if power_new(2,3) != 8:
        print("error in power_new()")

    if modpower_new(3, 4, 5) != pow(3, 4, 5) or \
       modpower_new(5, 4, 2) != pow(5, 4, 2):
        print("error in modpower_new()")
    
    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc()")

    if dec("1") != "0" or \
       dec("10") != "1" or \
       dec("110") != "101" or \
       dec("1000") != "111" or \
       dec(dec("1001")) != "111":
        print("error in dec()")
        
    if sub("0", "0") != "0" or \
       sub("1000", "0") != "1000" or \
       sub("1000", "1000") != "0" or \
       sub("1000", "1") != "111" or \
       sub("101", "100") != "1":
        print("error in sub()")

    if leq("100","11") or not leq("11", "100"):
        print("error in leq")
    if div("1010","10") != "101" or div("11001", "100") != "110":
        print("error in div")
        
    if not has_repeat1("ababa", 3) or \
       has_repeat1("ababa", 4) or \
       not has_repeat1("aba",1):
        print("error in has_repeat1()")

    if not has_repeat2("ababa", 3) or \
       has_repeat2("ababa", 4) or \
       not has_repeat2("aba",1):
        print("error in has_repeat2()")
                
    if [reading(i) for i in range(1, 6)] != ['1', '11', '21', '1211', '111221']:
        print("error in reading")

    if max_div_seq(23300247524689, 2) != 4:
        print("error in max_div_seq()")
    if max_div_seq(1357, 2) != 0:
        print("error in max_div_seq()")        
