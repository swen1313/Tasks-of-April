list1= [int(s) for s in input().split()]

def unique(list1):
    unique_list = []
    for i in list1:
        if list1.count(i) == 1:
            unique_list.append(i)
    return unique_list
    

print(unique(list1))  
            
        
    
