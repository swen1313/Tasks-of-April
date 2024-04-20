min_num = int(input("Введите минимум: "))
max_num = int(input("Введите максимум: "))

def is_simple(min_num, max_num):
    simple_list = []
    for num in range(min_num, max_num +1):
        isSimple = True
        if num < 2:
            return False
            break
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                isSimple = False
                break
        if isSimple:
            simple_list.append(num)
    return simple_list    
       
print(is_simple(min_num, max_num))                   
                


