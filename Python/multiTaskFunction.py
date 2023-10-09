class multiTaskFunction:
    
    def Subfields():
        aiTool=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in aiTool:    
            print(temp)
    
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
            
    def Eligible(gender,age):
        print("Your gender:", gender)
        print("Your age:", age)
        if(gender=="male") and (age>=21):
            print("Eligible")
        elif(gender=="male") and (age<21):
            print("Not Eligible")
        elif(gender=='female') and (age<18):
            print("Not Eligible")
        elif(gender=='female') and (age>18):
            print("Eligible")
    
    def Percentage():
        sub1=[98,87,95,95,93]
        for mark in sub1:
            print(mark)        