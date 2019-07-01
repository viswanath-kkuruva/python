# identify middle element in a list

import sys

def middle(lst):
	lst_length = len(lst)
	if lst_length % 2 == 0:
		start = (lst_length - 1) // 2
		end = start + 1
		return lst[start:end+1]
	else:
		indx = lst_length / 2 - 0.5
		return lst[int(indx)]

print(middle([1,2,3]))
print(middle([1,2,3,4]))
print(middle([1,2,3,4,5]))
print(middle([1,2]))
print(middle([]))


# identify occurance of each item and print if occurances count is greater than len(list)/2

from collections import Counter
import random
import time

lst = []
for i in range(1000000):
	lst.append(int(random.random()*10))

def counter_method(lst, matching_count):
	repetitions = Counter(lst)
	for item in repetitions.items():
		if item[1] > matching_count:
			print('{} is having {} crossing matching_count : {}'
				.format(item[0], item[1], matching_count))
			break

def dict_method(lst, matching_count):
	repetitions = {}
	for item in lst:
		if item not in repetitions:
			repetitions[item] = 1
		repetitions[item] += 1
	
	for item, count in repetitions.items():
		if count > matching_count:
			print('{} is having {} crossing matching_count : {}'
				.format(item, count, matching_count))
			break			

start = time.time()
counter_method(lst, 2)
end = time.time()
print(end-start)

start = time.time()
dict_method(lst, 2)
end = time.time()
print(end-start)


# Reverse each word in a string

string = 'each word in this string to be reversed'

reversed_string = ' '.join([word[::-1] for word in string.split(' ')])
print(reversed_string)

reversed_string = ' '.join(string[::-1].split(' ')[::-1])
print(reversed_string)