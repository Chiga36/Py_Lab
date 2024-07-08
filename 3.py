# a
dic={'hii':'hallo','coffee':'kaffee','thanks':'danke','gern':'like','mag':'like'}
c=int(input('''Enter the option '''))
if c==1:
    key=input("Enter the key ")
    value=input("Enter the value ")
    dic.update({key:value})
    print(dic)
elif c==2:
    search=input("Enter the word ")
    if search in list(dic.keys()):
        print(dic[search])
    else:
        print("Not found")
elif c==3:
    mean=input("Enter the meaning")
    a=[word for word,meaning in dic.items() if meaning==mean]
    print(a)
elif c==4:
    delete=input("Enter the word to be deleted ")
    del dic[delete]
    print(dic)
elif c==5:
    print("Sorted in alphabetically")
    sorted_words=sorted(dic.keys())
    for word in sorted_words:
        print(word,"-",dic[word])

# b
arr=[10,2,5,10,22,90,110,30]
arr.sort()
print("The min of array is ",arr[0],'and max of the array is ',arr[-1])
m1=max(arr)
arr.remove(m1)
print(f"The 2nd largest number is {max(arr)}")
