"""

List Operations

"""
import random

under_10=[x for x in range(10)]
print('under_10 : '+str(under_10))

squares=[x**2 for x in under_10]
print('Squares: ' + str(squares))

odds=[x for x in range(10) if x%2==1]
print('odds : '+ str(odds))

ten_x=[x*10 for x in range(10)]
print('ten_x : ' + str(ten_x))

s='I love 2 go t0 the store 7 times a w3ek.'
nums=[x for x in s if x.isnumeric()]
print('nums : '+ str(nums))

names=['Cosmo', 'Pedro', 'Anu', 'Ray']
idx=[k for k, v in enumerate(names) if v=='Anu']
print('index of specifique value : '+ str(idx))

letters=[x for x in 'ABCDEF']
random.shuffle(letters)
letrs=[a for a in letters if a!='C']
print(letters,letrs)

#nested loop iteration for 2D list
# b is the nested subnets, x is the value
a=[[1,2],[3,4]]
new_list=[x for b in a for x in b]
print(new_list)

