num_list = [2,4,6]
#use list comprehension to make a new list where each number is n+1
new_list = [num+1 for num in num_list]
print(new_list)

nums = [0, 3, 4, 0, 22, 1]
# create new list w all the non 0 numbers
non_zero_nums = [num for num in nums if num>0]
print(non_zero_nums)

all_classes =['ITEC 2345', 'ENGL 1234', 'ITEC 7654']
#make new list, filtering out non-itec classes
itec_classes = [c for c in all_classes if c.startswith('ITEC')]
print(itec_classes)

num_list_two = [0, 10, 4, 0, 32]
#new list w numbers doubled if num not 0
doubled_not_zero = [n*2 for n in num_list_two if n!=0]
print(doubled_not_zero)