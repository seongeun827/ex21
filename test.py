#소수 판별 함수 정의
def is_prime(num):
    num= int(num)
    if num != 1:
        for i in range(2,num):
            if num % i == 0:
                return  False
            
    else:        
        return False
    return True
n = 437674
k = 3
code = ''

while n > 0:
    n, mod = divmod(n,k)
    code += str(mod)
code = code[::-1]
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