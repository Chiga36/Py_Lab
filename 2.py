# a
def prime(a,b):
    m=[]
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
a=int(input("Enter the 1st number "))
b=int(input("Enter the 2nd number "))
print("The list of prime numbers are ")
prime(a,b)

# b
subs=['daa','Python Programming lab','DCN','MC IOT','FAFL','Maths']
# 1
for sub in subs:
    print(sub)
# 2
print(f"2nd element is {subs[1]} and 5th element is {subs[4]}")
# 3
print(f"The first four elements are {subs[:4]}")
# 4
print(f"The last four elements are {subs[-1:-5:-1]}")
# 5
if 'Python Programming lab' in subs:
    print(True)
else:
    print(False)
# 6
subs.append('Angular')
print(subs)
subs.insert(3,'R')
print(subs)
# 7
subs.remove('DCN')
print(subs)
subs.pop()
print(subs)
