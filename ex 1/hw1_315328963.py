#Skeleton file for HW1 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw1_ID.py).

from primes_lst import  * #loading the list of primes into a variable named primes


#Question 3
def max_word_len(filename):
    ''' writes the length of the longest word in a row (of a text) in a new file '''
    inFile = open(filename, "r")
    outFile = open("output.txt", "w")
    for line in inFile:
        new_list = line.split() #make the line into a list of words
        if new_list == []:
            longest_word = "" # to cover cases of empty lines
        else:
            longest_word = max(new_list, key=len) # in order to find the longest word
        num = str(len(longest_word)) # 'size' of longest word        
        outFile.write(num + "\n")
    inFile.close()
    outFile.close()
    return None

    




#
#Question 5
def k_boom(start, end, k):
    ''' The function presents the classic 'k-boom' game,
         done between 2 chosen numbers and a chosen k '''
    my_string = "" # will collect all of the numbers/booms
    for num in range(start, end +1):
        nums = str(num)
        count = nums.count(str(k)) # for numbers with 7 in them
        if num % 7 == 0:
            if count == 0:
                my_string += "boom! "
            else:
                my_string += "bada-boom! "
        else:
            if count == 0:
                my_string += str(num) + " "
            else:
                my_string += (count-1)*"boom-" + "boom! "
    last_string = my_string.rstrip() # get rid of last space
    return (last_string)






#
#Question 6

# 6a
def check_goldbach_for_num(n, primes_lst):
    ''' checks the goldbach conjecture for a natural number and a list of primes '''
    for i in range(len(primes_lst)):
        for k in range(len(primes_lst)):
            if primes_lst[i] + primes_lst[k] == n: # immediately ends the loops since correct
                return(True)
    return(False)

# 6b
def check_goldbach_for_range(limit, primes_lst):
    ''' checks goldbach conjecture for a range of even numbers '''
    new_list = []
    new_primes = [numb for numb in primes_lst if numb < limit] # in order to check only relevant primes
    for i in range(len(new_primes)):
        for k in range(len(new_primes)):
            summing = new_primes[i] + new_primes[k]
            new_list.append(summing) # new list of all sums in primes_lst
    for n in range(4, limit, 2):
        if n not in new_list:
            return False # beacause if so, the conjecture for the whole range is not true
    return True

# 6c
def check_goldbach_for_num_stats(n, primes_lst):
    ''' checks how many couples of numbers from the list sum to n '''
    count = 0
    new_primes = [numb for numb in primes_lst if numb < n] # in order to check only relevant primes
    for i in range(len(new_primes)):
        for k in range(len(new_primes)):
            if new_primes[i] + new_primes[k] == n:
                count += 1
    div = n /2
    if div in primes:
        count = (count// 2) + 1 # in order to avoid duplicates
    else:
        count = count//2 # in order to avoid duplicates
    return(count)





########
# Tester
########

