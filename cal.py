a,b=map(int,input().split())
print("Enter the number for operation : \n 1)1->addition \n 2)2->substration \n 3)3->multiplication \n 4)4->division")
c=int(input())
match(c):
    case 1:
        print(a+b)
        
    case 2:
        print(a-b)
        
    case 3:
        print(a*b)
        
    case 4:
        print(a/b)
        
    case default:
        print("\nplease enter a valid number:")
        
    
    
