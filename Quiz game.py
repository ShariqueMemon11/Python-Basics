print('Hello Welcome to the game')

playing = input('do yo want to play this game? ')

if playing.lower() != 'yes' :
    quit()

print('okay lets play=> ')   

count=0

ans=input('what is 6*5? ')
if ans == '30':
    print('correct :)')
    count+=1
else:
    print('incorrect :(')

ans=input('what is the full form of PC? ')
if ans.lower() == 'personal computer' :
    print('correct :)')
    count+=1
else:
    print('incorrect :(')

ans=input('what is 5+12? ')
if ans == '17':
    print('correct :)')
    count+=1
else:
    print('incorrect :(')
    
ans=input('what 1 kilogram in grams? ')
if ans == '1000':
    print('correct :)')
    count+=1
else:
    print('incorrect :(')

ans=input('what does RAM stand  for? ')
if ans.lower() == 'random access memory':
    print('correct :)')
    count+=1
else:
    print('incorrect :(')
print('your final score is')
if count == 5:
    print('5 perfect :)')
if count == 4:
    print('4 thats good :)')
if count == 3:
    print('3 not bad but you can do better :)')    
if count == 2:
    print('2 not good enough :(')
if count == 1:
    print('1 try harder :(')
if count == 0:
    print('0 you need to practice :( ')

print('you got '+ str((count/5)*100) + '%')

 


