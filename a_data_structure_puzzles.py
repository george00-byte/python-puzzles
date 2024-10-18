# print("hello")
# x="Shrewd"
# def my_name(x):
#     global y
#     y=" Human"
#     return x+''+y

# def my_home(y):
#     y=y+' '+x
#     return y

# print(my_name("George"))


# print(my_home(y))


import asyncio

# async def print_data(x):
#     print("fetching data...")
#     await asyncio.sleep(2)
#     print(f"fetched data {x}")
    
# asyncio.run(print_data("mine"))


# import asyncio

# async def task1():
#     print("Starting task 1...")
#     await asyncio.sleep(1)
#     return "Task 1 complete"

# async def task2():
#     print("Starting task 2...")
#     await asyncio.sleep(3)
#     return "Task 2 complete"

# async def main():
#     result_one =await task1() 
#     result_two =await task2() # Run tasks concurrently
#     print(result_two,result_one)

# asyncio.run(main())


# import asyncio

# async def task_one():
#     print("waiting....")
#     await asyncio.sleep(2)
#     return [i for i in range(11)] 

# print(asyncio.run(task_one()))

import asyncio
import threading 

import time


# def task_one(name):
#     print("Starting")
#     time.sleep(5)
#     print(f"Hello {name} your time Ended")
    

# thread=threading.Thread(target=task_one, args=(input(str('Enter the Name: ')),))
# thread.start()

    
# import asyncio
# import threading 

# import time


# async def task_one():
#     print("Starting")
#     await asyncio.sleep(3)
#     print("Ended")


# async def main():
#     result = await task_one()
#     return result
 
#  #person class  
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
        
#     def __str__(self,name, age) -> str:
#         return f"{name} ,{age}"
  
  
# global person_one_age
# global person_one_name
# #name of the person
# person_one_name=Person.name="George"


# #age of person
# person_one_age=Person.age=input(str("Enter your age: "))

# #commsnts function
# async def comment(com):
#     print("wait a second..")
#     time.sleep(2)
#     print( f"{com}, {person_one_name}, you are {person_one_age}")




# thread=threading.Thread(asyncio.run(comment('Hello')))
# thread.start()

    
# x=lambda x : f"print {x}"
# print(x(3))


# import threading
# import time

# #function compute

# #take a number

# #sleep for 2 seconds 
# # import threading
# # import time


# # def compute(num):
# #     print(f"Starting {num}")
# #     time.sleep(2)
# #     print(num**2)
    
# # numbers =[1,2,3,4]  

# # for num in numbers:
# #     thread_one=threading.Thread(target=compute,args=(num,))
# #     thread_one.start()


# # Function to test
# def add(a, b):
#     return a + b

# # Unit testing
# import unittest

# class TestDivideFunction(unittest.TestCase):
#     def test_add_equal(self):
#         self.assertEqual(add(2,3),5)
#     def test_add_not_equal(self):
#         self.assertNotEqual(add(2,3), 7)
#     def almost_equal(self):
#         self.assertAlmostEqual(add(2.1,3.2),6)

# unittest.main()


# import unittest


# tup_1= (1,2,3)
# tup_2= (2,2,4)

# x=tup_1+tup_2



# print(tup_1)



# import numpy as np

# x=np.ones((2,3))


# print(x)

# lit =[1,3,3,23,24,24,4]


#stacks

# class Stack():
#     def __init__(self):
#         self.stack = list()
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if len(self.stack) > 0:
#             self.stack.pop()
#         else:
#             return None
#     def peek(self):
#         if len(self.stack) > 0:
#             return self.stack[len(self.stack)-1]
#         else:
#             return None
#     def __str__(self):
#         return str(self.stack)
    
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)


# print(my_stack)

# my_stack.peek()
# print(my_stack.peek())
# my_stack.pop()
# my_stack.pop()
# print(my_stack)



#Queues 

from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)

print(my_queue.popleft())
print(my_queue)


class Queue():
    def __init__(self):
        self.deque =  deque()
    def add (self,item):
        self.deque.append(item)
    def pop_left (self):
        self.deque.popleft()
    def __str__(self):
        return str(self.deque)
my_queue=Queue()

my_queue.add(3)
my_queue.add(4)
print(my_queue.pop_left())
print(my_queue)



# def factorial(num):
#     if num ==1:
#         return 1
#     else:
#         return num*factorial(num-1)

# print(factorial(5))


# class MaxHeap:
#     def __init__ (self, items=[]):
#         super().__init__()
#         self.heap= [0] 
#         for item in items:
#             self.heap.append((item))
#             self.__floatUp(len(self.heap)-1)
#     def push(self, data):
#         self.heap.append(data)
#         self.__floatUp(len(self.heap)-1)
    
#     def peek(self):
#         if self.heap[1]:
#             return self.heap[1]
#         else:
#             return False
#     def pop(self):
#         if len(self.heap) >2:
#             self.__swap(1,len(self.heap) -1)
#             max = self.heap.pop()
#             self.__bubbleDown(1)
#         elif len(self.heap)== 2:
#             max = self.heap.pop()
#         else:
#             max = False
#         return max
#     def __swap(self, i,j):
#         self.heap[i], self.heap[j]= self.heap[j], self.heap[i]
#     def __floatUp(self, index):
#         parent = index//2
#         if index <= 1:
#             return
#         elif self.heap[index] > self.heap[parent]:
#             self.__swap(index,parent)
#             self.__floatUp(parent)
#     def __bubbleDown(self, index):
#         left = index *2
#         right = index *2+1
#         largest = index

#         if len(self.heap) >left and self.heap[largest] < self.heap[left]:
#             largest = left 
#         if len(self.heap) > right and self.heap[largest] < self.heap[right]:
#             largest = right
#         if largest !=index:
#             self.__swap(index, largest)
#             self.__bubbleDown(largest)
            
#     def __str__(self):
#         return str(self.heap)
        
        
# m = MaxHeap([95,3,21])

# m.push(10)

# m.pop()
# m.peek()

# print(m.peek()) 

# print(m)



    
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    def __str__(self):
        return('('+str(self.data)+')')
    

class LinkedList:
    def __init__(self, r=None):
        self.root= r
        self.size = 0
        
    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size+=1
        
    def find(self,d):
        this_node = self.root
        
        while this_node is not None:
            if this_node is not None:
                if this_node.data ==d:
                    return d
                else:
                    this_node = this_node.next_node
        return None
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -=1
                return True
            
            else:
                prev_node = this_node
                this_node = this_node.next_node
            return False
        
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')
        
        
myList = LinkedList()
myList.add(4)
myList.add(5)
myList.add(6)
myList.add(7)

print(str(myList.size))

myList.remove(5)

print(myList.find(4))

print(myList.root)

print(myList)


#check if array is balanced
#method 1
# arr= [1,2,3,4,5]

# def array(arr):
#     if (len(arr)+1) %2 ==0:
#         print('false')
#     else:
#         print('true')
        

# array(arr)

#method 2

# arr = [1,2,33,2]

# def is_balanced(arr):
#     total_sum = sum(arr)
    
#     #if sum is odd it cannot be balance
#     if total_sum % 2 !=0:
#         return False
#     left_sum = 0
    
#     for i in range(len(arr)):
#         left_sum += arr[i]
#         right_sum = total_sum -left_sum
        
#         if left_sum ==right_sum:
#             return True
#     return False
    

# print(is_balanced(arr))

#sum the left only


# x = [4, 5, 6, 7, 4, 6, 8, 7, 9]

# list_to_set=list(set(x))
# print(list_to_set)

# import numpy as np

# x=np.array(list_to_set)
# print(x.mean())

# import pandas as pd
# x=pd.Series(x)
# x['values']=pd.DataFrame(x)
# x=x['values']
# print(x[0].mean())


# def find_missing(arr,n):
#     total =0
#     for i in range(n+1):
#         total+=i
#     total_sum = total
#     # total_sum=n*(n+1)//2
#     missing = total_sum - sum(arr)
#     return missing

# arr= [1,2,4,5]
# n=5
# print(find_missing(arr,n))

# n=5



# def find_two_missing_numbers(arr, n):
#     # Step 1: Calculate the total sum and total sum of squares for numbers 1 to n
#     total_sum = n * (n + 1) // 2
#     total_sum_sq = n * (n + 1) * (2 * n + 1) // 6
    
#     # Step 2: Calculate the sum and sum of squares of the given array
#     arr_sum = sum(arr)
#     arr_sum_sq = sum(x ** 2 for x in arr)
    
#     # Step 3: Calculate the differences (equivalent to x + y and x^2 + y^2)
#     sum_diff = total_sum - arr_sum       # x + y
#     sum_sq_diff = total_sum_sq - arr_sum_sq  # x^2 + y^2
    
#     # Step 4: Solve for the missing numbers x and y
#     # We know:
#     # x + y = sum_diff
#     # x^2 + y^2 = sum_sq_diff
#     # From this, we get: x * y = (sum_diff^2 - sum_sq_diff) / 2
    
#     product_diff = (sum_diff ** 2 - sum_sq_diff) // 2  # x * y
    
#     # Step 5: Solve the quadratic equation: x and y are the roots
#     # x and y are the roots of the equation: t^2 - (x + y)t + x * y = 0
#     # or equivalently: t^2 - sum_diff * t + product_diff = 0
#     discriminant = (sum_diff ** 2) - (4 * product_diff)
#     x = (sum_diff + int(discriminant ** 0.5)) // 2
#     y = sum_diff - x
    
#     return x, y

# # Example usage
# arr = [1, 2, 4, 5]
# n = 6
# print(find_two_missing_numbers(arr, n))  # Output: (3, 6)

# from collections import Counter

# def non_repeated_string(s):
#     count=Counter(s)
#     for i in count:
#         if count[i] == 1:
#             print(i)
#     return None
        
# s="adsadsadasdasdawdewg"   
# non_repeated_string(s)



#palindmore in python

#get the string

#print the reverse

#check if reverse equals the actual

# def palindmore(s):
#     reverse_string = s[::-1]
#     if s == reverse_string:
#         return True
#     else:
#         return False
# s='madams'
# print(palindmore(s))



# import numpy as np
# from collections import Counter

# def find_most_occurance(arr):
#     x=[]
#     count= Counter(arr)
#     w=[]
#     print(count)
#     for i in count:
#         z=count[i]
#         w.append(z)
    
#     for i in count:
#         if count[i]== max(w):
#             x.append(i)
#     return x
  


# arr = [1,1,2,23,4,3,3,3]

# print(find_most_occurance(arr))






from collections import Counter


# def maximum_occurance(arr):
#     x= []
    
#     w=[]
   
#     count = Counter(arr)
#     print(count)

#     for i in count:
#         x.append(count[i])
        
#     for i in count:
#         if count[i] == min(x):
#             return i, count[i]
    
        
# arr=[1,1,2,1,2,2,3,3,3,1,3,3,5]
# print(maximum_occurance(arr))
    



# from collections import Counter

# def most_frequent_element(arr):
#     # Count occurrences of each element
#     count = Counter(arr)
    
#     # Find the element with the maximum count
#     most_frequent = max(count, key=count.get)
    
#     # Get the frequency of the most frequent element
#     frequency = count[most_frequent]
    
#     return most_frequent, frequency

# # Example usage:
# arr = [1, 1, 2, 1, 2, 2, 3, 3, 3, 1, 3, 3, 9]
# element, frequency = most_frequent_element(arr)
# print(f"Most frequent element: {element}, Number of occurrences: {frequency}")


# x='sdadasdsaaasdasdsa'
# count= Counter(x)

# x = []
# for i in  count:
#     x.append(count[i])
    
# for i in count:
#     if count[i] > 1 :
#         print(i)



#merge 2 sorted arrays

# x=[1,2,3,3]
# y =[1,2,33,3]

# print(list(set(x+y)))

# x=[1,1,2,2,3]

# from collections import Counter

# x=[1,2,1,3,1,2]

# count = Counter(x)
# print(count)
# for i in count:
#     if count[i] == 1:
#         print(i," appears ",count[i], " times")

# y=[1,2,1,3,1,2]
# counts = {}

# for n in y:
#     if n not in counts:
#         counts[n] =1
#     else:
#         del count[n]
#         print(list(count.keys())[0])



x=[1,2,3,4,4]  #target ==3

# from collections import Counter

# count = Counter(x)


   
# class solution:
#     def two_sum(self, numsa)

# target= 8
# nums= [1,2,3,4,5,5]
# for i in range(len(nums)-1):
#     for j in range(i+1, len(nums)):
#         if nums[i] *nums[j] == target:
#             print([i,j])
        



# class letters:
#     def __init__(self,n):
#         self.n =n
#     def longest_substring(n):
#         return len(set(n))

# letters.n ="bbbbbb"
# n=letters.n
# print(letters.longest_substring(n))


# number = -121
# number_to_str=str(number)
# palindmore = number_to_str[::-1]
# if number_to_str == palindmore:
#     print("true")
# else:
#     print('false')


# input = 'G()(al)'

# input=input.replace('G', 'G')
# input=input.replace('()', 'o')
# input = input.replace('(al)', 'al')



# print(input.replace('()', 'o').replace('(al)', 'al'))

# city_destinations = [["London",'New York'],["New York",'Lima'], ['Lima','Sao Paulo']]


# count=dict(city_destinations)
# z=[]
# for i in count:
#     z.append(count[i])
# print(z[-1])


# city_destinations = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

# # Extract starting and destination cities
# starting_cities = set()
# destination_cities = set()

# for route in city_destinations:
#     starting_cities.add(route[0])
#     destination_cities.add(route[1])

# # The destination city is the one that is only in destination_cities, not in starting_cities
# final_destination = destination_cities - starting_cities

# print(final_destination)


# city_destinations = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

# destinations =set()
# starting_point = set()


# for i in city_destinations:
#     destinations.add(i[0]) 
#     starting_point.add(i[1])

# print(starting_point-destinations)





# def solution(digits: str, num: str) -> int:
#     # Create a dictionary to map each digit in 'digits' to its index
#     digit_to_index = {digit: idx for idx, digit in enumerate(digits)}
    
#     # Initialize the total time to 0
#     total_time = 0
    
#     # Start at the position of the first digit in 'num'
#     current_pos = digit_to_index[num[0]]
    
#     # Loop through the digits in 'num' and calculate the movement time
#     for i in range(1, len(num)):
#         next_pos = digit_to_index[num[i]]
#         total_time += abs(current_pos - next_pos)
#         current_pos = next_pos
    
#     return total_time

# digits = "8459761203"
# num = "5439"
# output = solution(digits, num)
# print(output)  # This should correctly print 17




# def solution(digits: str, num: str) -> int:
#     # Create a dictionary to map each digit in 'digits' to its index
#     digit_to_index = {digit: idx for idx, digit in enumerate(digits)}
    
#     # Initialize the total time to 0
#     total_time = 0
    
#     # Start at the position of the first digit in 'num'
#     current_pos = digit_to_index[num[0]]
    
#     # Loop through the digits in 'num' and calculate the movement time
#     for i in range(1, len(num)):
#         next_pos = digit_to_index[num[i]]
#         total_time += abs(current_pos - next_pos)
#         current_pos = next_pos
    
#     return total_time

# digits = "8459761203"
# num = "5439"
# output = solution(digits, num)
# print(output)  # This should correctly print 17




# def solution(digits: str, num: str) -> int:
#     total_time = 2 #moving from the the last index to the first and back
    
#     # Start at the index of the first digit in 'num'
#     current_pos = digits.index(num[0])
    
#     # Loop through the digits in 'num' and calculate the movement time
#     for i in range(1, len(num)):
#         next_pos = digits.index(num[i])
#         total_time += abs((current_pos) - next_pos)
#         current_pos = next_pos
    
#     return total_time

# digits = "8459761203"
# num = "5439"
# output = solution(digits, num)
# print(output)  # This should correctly print 17




# from typing import List

# def solution(morsecode: str) -> List[str]:
#     ans = []
    
#     # Loop through the string and find pairs of consecutive dots ".."
#     for i in range(len(morsecode) - 1):
#         if morsecode[i:i+2] == "..":  # Check for ".." substring
#             # Replace the found ".." with "-" and append to the results list
#             new_code = morsecode[:i] + "-" + morsecode[i+2:]
#             ans.append(new_code)
    
#     return ans

# morsecode = "...."
# print(solution(morsecode))  # Output: ['--..', '.--.', '..--']



class solution:
    def __init__(self,N):
        self.N = N
        
    def fib(self,N:int)->int:
        if N == 0:
            return 0
        if N== 1:
            return 1
        
        return self.fib(N-1)+ self.fib(N-2)

sol = solution(9)
print(sol.fib(sol.N))


# class solution:
#     def fib(self,N:int)->int:
#         if N == 0:
#             return 0
#         if N== 1:
#             return 1
        
#         return self.fib(N-1)+ self.fib(N-2)

# sol = solution()
# print(sol.fib(9))


# class solution:
#     @staticmethod
#     def fib(N:int)->int:
#         if N == 0:
#             return 0
#         if N== 1:
#             return 1
        
#         return solution.fib(N-1)+ solution.fib(N-2)

# sol = solution()
# print(sol.fib(9))


# class goat:
#     def __init__(self, Name):
#         self.Name = Name
#     def age(self,x):
#         return x*2
  
# g= goat("name")  
# print(g.age(2))



# def fib(N:int)->int:
#     if N == 0:
#         return 0
#     if N== 1:
#         return 1
    
#     return (fib(N-1)+fib(N-2))


# print(fib(5))