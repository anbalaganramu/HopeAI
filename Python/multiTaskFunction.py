
class SubfieldsInAI:
    
    # Create a class and function, and list out the items in the list
    def Subfields():
        aiTool=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in aiTool:    
            print(temp)
        

class OddEven:
    
    # Create a function that checks whether the given number is Odd or Even
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
        
class EligiblityForMarriage:
    
    # Create a function that tells elegibility of marriage for male and female according
    # to their age limit like 21 for male and 18 for female
            
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

class FindPercent:
    
    # Calculate the percentage of your 10th mark
    def percentage():
        Sub1=int(input("Subject1:"))
        Sub2=int(input("Subject2:"))
        Sub3=int(input("Subject3:"))
        Sub4=int(input("Subject4:"))
        Sub5=int(input("Subject5:"))
        Tot=float(Sub1+Sub2+Sub3+Sub4+Sub5)
        print("Total:", Tot)

        percent=Tot/5
        print("Percentage:",percent)
        fpercentage = "{:.14f}".format(percent)
        print("Percentage:",fpercentage)    
        
class triangle:
    
    # Print area and perimeter of triangle using class and functions
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area_of_traingle=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Traingle:", area_of_traingle)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth2=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        perimeter_of_triangle=(height1+height2+breadth2)
        print("Perimeter of Trianlge:", perimeter_of_triangle)
        
