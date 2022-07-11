#mutable
my_list=['1','2','3']
another_list=['one','two','Three']
new_list=my_list+another_list
print(new_list)
new_list[0]='ONE'
print(new_list)
new_list.append('eleven')
print(new_list)
new_list.pop()#pop will reomve last item and also print it
new_list.pop(0)#will pop the element in index 0
new_list.reverse()#to reverse

