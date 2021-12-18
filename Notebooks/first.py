arr = [4, 73, 67, 38, 33]

def multiple_5(number):
    number_aux = number
    for i in range(5):
        if number_aux % 5 == 0:
            break
        number_aux = number_aux + 1      
    
    return number_aux
  
def gradingStudents(grades):
    # Write your code here
    list_grades = []
    for grade in grades:
        if grade < 38:
            list_grades.append(grade)
            continue
        number_hight = multiple_5(grade)
        diff = number_hight - grade
        if (diff < 3): 
            list_grades.append(number_hight)
            continue
        list_grades.append(grade)
        
    return list_grades

def is_leap(year = 2100):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        print("4")
        leap = True
    if year % 100 == 0:
        print("100")
        leap = False
    if year % 400 == 0:
        print("400")
        leap = True
    
    
    return leap

if __name__ == '__main__':
  # list_aux = gradingStudents(arr)
  # print("res", list_aux)
  res = is_leap()
  print(res)
