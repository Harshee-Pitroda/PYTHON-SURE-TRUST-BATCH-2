print('*****START THE QUIZ*****')
scr=0
Ques={1:'What is the output of the following code?\n\nls=[1,2,3]\nls.append([9,4,5])\nls.extend(9,4,5)\n\nA.[1,2,3,9,4,5,9,4,5]\nB.[1,2,3,9,4,5,[9,4,5]]\nC.[1,2,3,[9,4,5],[9,4,5]],\nD.[1,2,3,[9,4,5],9,4,5]\n',2:'Which output follows the code?\nx=3\nfor i in range(2):\nfor j in range(4,5):\nif i!=0:\nprint(\'Hello\')\n\nA.Hello\nB.Hello Hello\n',3:'Which keyword can terminate the loop?\n',4:'Dimension of this array is : \narray=np.array([[1,2,3],[4,5,6]])\n',5:'Which is the correct syntax for the declaration of a tuple with a single value 1?\n\nA.(1)\nB.1\nC.1,\nD.(1,)\nE.Both A and D\nF.Both C and D\n'}
while True:
    for i in range(1,6):
        if i==1:
            print(Ques[i],'\n')
            x=input()
            if x=='D':
                scr+=1
        if i==2:
            print(Ques[i],'\n')
            x=input()
            if x=='A':
                scr+=1
        if i==3:
            print(Ques[i],'\n')
            x=input()
            if x=='break':
                scr+=1
        if i==4:
            print(Ques[i],'\n')
            x=int(input())
            if x==2:
                scr+=1
        if i==5:
            print(Ques[i],'\n')
            x=input()
            if x=='F':
                scr+=1
    print(f'Your score is {scr}')
    option=input('Press y to reattempt the QUIZ : x to exit the quiz\n')
    if option =='y':
        continue
    else:
        break

    
