list_num=[1,2,3,4,5,6,7,8,9,10]
pair=[(list_num[i-1],list_num[-i] )for i in range(1,len(list_num)//2+1)]
print(pair)

