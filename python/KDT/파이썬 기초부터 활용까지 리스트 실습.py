f = open('sung1.txt','r', "utf-8")
basedata = f.read()
f.close()

data = basedata.split('\n')
for oneRec in range(len(data)):
    data[oneRec] = data[oneRec].split(',')


f= open('sung2.txt','w')

for k in range(len(data)):
    sum = 0
    for j in range(1,len(data[k])):
        sum += int(data[k][j])

    data[k].append(str(sum))
    av = int(sum/3)
    data[k].append(str(av))
    data2 = ', '.join(data[k]) + '\n'

    f.write(data2)

f.close
print("작업 성공")

