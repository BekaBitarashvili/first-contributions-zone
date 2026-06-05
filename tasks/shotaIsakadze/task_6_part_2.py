#7 თამაში უკუსვლაზე

# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".


# import random
# import time
# number = random.randint(1,21)

# start = time.time()
# answer = int(input("გამოიცანი რიცხვი(1_20): "))

# end = time.time()

# if end - start > 5:
#     print("დრო ამოგეწურა, პასუხი შეიყვანე 5 წამში.")
# else:
#     if answer == number:
#         print("გილოცავ შენ სწორად გამოიცანი რიცხვი")
#     else:
#         print(f"არასწორი რიცხბი. ჩაფიქრებული რიცხვი იყო {number}")



#8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში

# player1 = start + timedelta(seconds=random.randint(5,20))
# player2 = start + timedelta(seconds=random.randint(5,20))
#პირობა ვერ გავიგე


#9 იღბლიანი დაბადების დღე
# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე

# from datetime import date

# bday_input = input("შეიყვანე დაბადების თარიღი (YYYY-MM-DD) ფორმატით: ")
# year, month, day = map(int,bday_input.split("-"))
# birthday = date(year, month, day)
# today = date.today()

# this_year_birthday = birthday.replace(year= today.year)

# if this_year_birthday < today:
#     this_year_birthday  = birthday.replace(year = today.year + 1)

# days_left = (this_year_birthday - today).days
# print(f"შემდეგ დაბადების დღემდე დაგრჩა {days_left} დღე")






#10 საცავი - ჯუნიორ ჰაკერი :)

# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს (შემთხვევითობის პრინციპით) პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და როცა მოხდება კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია", აუცილებელი პირობაა გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.



#git checkout -b shota_task_7_to_10
#git add .
#git commit -m"task 7_10"
#git push origin shota_task_7_to_10