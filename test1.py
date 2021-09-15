
def is_prime(num):
    num= int(num)
    if num != 1:
        for i in range(2,num):
            if num % i == 0:
                return  False
            
    else:        
        return False
    return True
n = 110011
k = 10

numb=[]
m= str(n)
for i in range(len(m)):
    numb.append(i)
maxnum = max(numb)
code = 0
for idx, number in enumerate(m[::-1]):
    code += int(m) * ((int(maxnum))** idx)
# code = str(n)
code= str(code)
index = 0
zeroloc=[]
while index > -1:
    index = code.find('0',index)
    if index > -1:
        zeroloc.append(index)
        # print(index)
        index += len('0')
confirnum = []
j=0
for i in zeroloc:
    confirnum.append(code[j:i])
    j=i+1
if zeroloc[-1] < len(code):
        confirnum.append(code[zeroloc[-1]+1:])
print(confirnum)
answer = 0
for num in confirnum:
    if is_prime(num):
        answer +=1
    
print(answer)