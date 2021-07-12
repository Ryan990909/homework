score = [] 
score.append(100)
score.append(97)
score.append(95)
score.append(93)
score.append(80)
score.append(77)
print(score)
name=[]
name.append('Eric') 
name.append('Jack')
name.append('Piter')
name.append('Jash') 
name.append('Nick')
name.append("Tommey")
print (name)
scoresum=0 
for i in score:
    scoresum=scoresum+i
print(scoresum/6)
max=0
namemax=' ' 
for s in range(6):
    if score[s]>max:
        max=score[s]
        namemax=name[s]
print(max,namemax)
min=10000
namemin=''
for n in range(6):
    if score[n] <min:
        min=score[n]
        namemin=name[n]
print(min)
print(namemin)
