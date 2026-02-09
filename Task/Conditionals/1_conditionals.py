# Дані студента
knows_python = True  # чи знає Python (True/False)
knows_math = False    # чи знає математику (True/False)
experience_years = 0  # досвід у роках



knows_python=input("Чи знаєте пайтон True or False: ")
knows_math=input("Чи знаєте математику True or False: ")
experience_years=input("Скільки у вас досвіду на роботах: ")


if  knows_python =="True" and knows_math == "True":
    print("Тобі на курс Data Science")
elif knows_python == "True" and  knows_math == "False":
    print("Тобі на курс Python Web Development")
elif knows_python == "False" and  int(experience_years) > 2 :
    print("Тобі на курс Менеджмент проектів")
else :
    print("Тобі на загальний курс Основи IT")