#1 მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)

# from itertools import permutations
# word = "ABCD"
# variants = [''.join(p) for p in permutations(word)]

# print("Total variants: ",len(variants))



#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

# from datetime import date, timedelta

# today = date.today()
# #სამშაბათი = 1
# while today.weekday() != 1:
#     today += timedelta(days = 1)

# print(f"შემდეგი სამშაბათი არის {today}") 



#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი

# import calendar
# year = int(input("შეიყვანე წელი: "))

# if calendar.isleap(year):
#      print(f"{year} ნაკიანი წელია")
# else:
#      print(f"{year} არ არის ნაკიანი წელი")




#4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
# import datetime

# today = date.today()
# new_year = date(2027,1,1)
# # days_left = (new_year - today).weeks
# days_left = (new_year - today).days
# weeks = days_left // 7

# print(f"ახალ  წლამდე დარჩა {weeks} კვირა")



#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

# from itertools import combinations

# numbers = [1,2,3,4,5]

# all_combinations = list(combinations(numbers, 3))

# for x in all_combinations:
#      print(x)




#6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე

from itertools import combinations

string = "shota"


for x in range (1, len(string)+1):
    for c in combinations(string, x):
        print(''.join(c))

#მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.


# git commands
# git status
# git checkout -b shota
# git pull origin main
# git add .
# git commit -m"task 1_6"
# git push origin shota