#opening a function
def HCF(p,q):
    if p==0:
        return q
    return HCF(q%p,p)
#taking input
p=int(input("Please enter the 1st number: "))
q=int(input("Please enter the 2nd number: "))
#printing output
print("The HCF of the 2 enetered numbers is: ",HCF(p,q))