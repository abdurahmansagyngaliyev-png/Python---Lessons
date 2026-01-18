#FIRST DAY  "Переменные и типы данных"
#a=int(input("Сколько тебе лет?"))
#print(f"Тебе {a} лет")
#a,b=map(int,input().split())
#print(a+b)
#a,b=map(int,input().split())
#print("Calculator: ")
#print(a+b,a-b,a*b,a//b)
#name="Абдурахман"
#age=14
#print(f"Привет {name} Тебе {age} лет")
#from tkinter.font import names

#import pygame


#SECOND DAY   "УСЛОВИЯ (if/else)"
#a=int(input("Выведи число: "))
#if a%2==0:
    #print("Четное")
#else:
    #print("Нечетное")


#a=int(input("Сколько тебе лет: "))
#if a<12:
    #print("Ребенок")
#elif 12<=a<=17:
    #print("Подросток")
#elif a>=18:
    #print("Взрослый")


#admin=input("Admin: ")
#password=input("Password: ")
#if admin=="admin" and password=="1234":
    #print("Добро пожаловать")
#else:
    #print("Доступ запрещен")


#a=int(input("Введите число: "))
#if a>0:
    #print("Положительно")
#elif a<0:
    #print("Отрицательное")
#else:
    #print("Ноль")



#THIRD DAY "ЦИКЛЫ"
#for i in range(1,10):
    #print(i)

#for i in range(1,20,1):
    #if i%2==1:
        #continue
    #print(i)

#x=int(input())
#while x!=0:
    #print(f"Вы ввели: {x}")
    #x=int(input())
   # if x==0:
        #print("Программа завершена")

#nums = [5, 12, 7, 20, 3, 14]
#for num in nums:
    #if num >10:
        #print(num)

#arr=list(map(int,input("Введите 5 чисел: ").split()))
#print(f"{arr}  Сумма:  {sum(arr)}")



#FOURTH DAY "Строки"
#s = "abdurakhman"
#print(s.isdigit())  # True — все цифры
#print(s.isalpha())  # False — не только буквы
#print(s.isalnum())  # True — буквы или цифры

#a=input("Введите имя: ")
#print(f"Привет,{a.capitalize()}!")

#word=input("Введите слово: ")
#print(f"Длина слова: {len(word)},Первый символ слова: {word[0]},Последний символ слова: {word[-1]}")

#sentence=input("Введите предложение: ")
#print(f"В верхнем регистре: {sentence.upper()},В нижнем регистре: {sentence.lower()}")

#sentence=input("Введите предложение: ")
#print(f"В списке: {sentence.split()}")
#for i in sentence:
    #print(i, end="")

#word=input("Введит слово: ")
#if word.isdigit():
    #print("Это число")
#else:
    #print("Это не число")



#FIFTH DAY "Списки"
#a=[1,2,3,4,5]
#print(f"Summa: {sum(a)},Max: {max(a)},Min: {min(a)}")

#a = input("Введите 5 слов: ").split()
#print(a)


#arr=[10, 15, 20, 25, 30]
#for num in arr:
    #if num>20:
        #print(num)

#for word in input("Введите слова: ").split():
    #print(word)


#arr=["яблоко", "банан", "вишня"]
#arr.remove("банан")
#arr.insert(1,"апельсин")
#print(arr)



#SIXTH DAY "СЛОВАРИ (dict)"
#user={
    #'name': 'Abdurakhman',
    #'age': 14,
    #'city': 'Aktobe'
#}
#print(f"Имя пользователя: {user['name']}")
#print(f"Возраст пользователя: {user['age']}")

#user={
#    'name': 'Abdurakhman',
#    'age': 14,
#    'city': 'Aktobe'
#}
#for key in user:
    #print(f"{key}→{user[key]}")

#user={
    #'name': 'Abdurakhman',
    #'age': 14,
    #'city': 'Aktobe'
#}
#user['age']=15
#user['email']='example@mail.com'
#print(user)

#user={
    #'name': 'Abdurakhman',
    #'age': 14,
    #'city': 'Aktobe'
#}
#print(user.get('phone','Ключ отсутствует'))

#user={
    #'name': 'Abdurakhman',
    #'age': 14,
    #'city': 'Aktobe'
#}
#del user['city']
#print(user)

#SIXTH DAY'S CONTINUE "Множества (set)"
#a = {1, 2, 3}
#b = {3, 4, 5}
#c={6,7,8}

#print(a | b)  # объединение {1, 2, 3, 4, 5}
#print(a & b)  # пересечение {3}
#print(a - b)  # разность {1, 2}

#s={1, 2, 3, 3, 4, 4, 5}
#print(s)

#a = {1, 2, 3}
#b = {2, 3, 4}
#print(a | b)
#print(a & b)
#print(a - b)

#s = input("Введите числа через пробел: ")
#a = set(map(int, s.split()))
#print(a)


#s = {"Али", "Бек", "Дина"}
#print("Бек" in s)  # True


#s=set()
#for i in range(5):
    #s.add(i)
#print(s)



#SEVENTH DAY "Функция (function)"
#def abdu():
    #print("Hello")
#abdu()

#def great():
   # print("Abdurakhman")
#great()

#def add(a,b):
 #   print(a+b)
#a=int(input())
#b=int(input())
#add(a,b)

#def square(a):
 #   print(a**2)
#a=int(input())
#square(a)

#def is_even(a):
  #  if a % 2 == 0:
  #      print(True)
  #  else:
 #       print(False)
#a=int(input())
#is_even(a)

#def max_of_three(a,b,c):
 #   print(max(a,b,c))
#a,b,c=map(int,input().split())
#max_of_three(a,b,c)

#def sum_list(arr):
 #   print(sum(arr))
#arr=[1,2,3,4]
#sum_list(arr)

#def auth():
    #def check_pass():
    #    password=int(input("Парольди енгиз: "))
    #    if password == 1234:
    #        print("YES")
    #    else:
    #        print("NO")
    #check_pass()
#auth()

#def positive():
   # arr=[-2, 0, 5, -7, 10]
  #  for i in arr:
  #      if i>0:
 #           print(i,end=" ")
#positive()

#def main():
 #   a=int(input("Enter a number: "))
  #  if a%3==0:
    #    print(True)
   # else:
     #   print(False)
#main()

#def main():
  #  a,b=map(int,input("Enter a and b numbers: ").split())
 #   print(a-b)
#main()

#def main():
  #  a=str(input())
 #   print(a[::-1])
#main()

#def words():
  #  a=str(input())
 #   print(a.count("a, e, i, o, u, ә, ө, ү, ы, и, о"))
#words()

#def main():
  #  arr=[1,2,3,4,5]
 #   minimum=arr[0]
   # for i in arr:
    #    if i<minimum:
     #       minimum=i
      #      print(minimum)
#main()

#def main():
    #a=[1,2,3,4,5,6]
   # for i in a:
  #      if i%2==0:
 #           print(i)
#main()

#def main():
   # a=["level","hello"]
   # for i in a:
    #    if i[::-1]==i:
   #         print(True)
 #       else:
  #          print(False)
#main()

#def main():
    #a=["apple","banana"]
    #print(max(a,key=len))
#main()

#def main():
   # a=[1,2,3]
  #  for i in a:
 #       print(i**2)
#main()

#def main():
    #a=int(input("Enter your password: "))
    #if a==7777:
   #     print(True)
  #  else:
 #       print(False)
#main()



#EIGHTH DAY "файлмен жұмыс"
#with open("names.txt", "w") as f:
 #   f.write("Hello, Abdurahman!\n")
  #  f.write("Python file practice!\n")

#with open("names.txt",'a') as b:
 #   b.write("Hello, Abdurahman!\n")
  #  b.write("Python file practice!")

#with open("names.txt",'r') as a:
 #   print(a.read())


# words.txt файлына 5 сөз жазайық
#with open("words.txt", "w") as f:
    #f.write("apple\n")
    #f.write("banana\n")
   # f.write("kiwi\n")
  #  f.write("pineapple\n")
 #   f.write("pear\n")

# Файлдан оқып, ең ұзын сөзді табу
#with open("words.txt", "r") as f:
 #   words = f.read().splitlines()  # әр жолды тізімге айналдырады
#longest = max(words, key=len)
#print("Ең ұзын сөз:", longest)


#with open("log.txt", "w") as f:
 #   for i in range(3):
 #       msg = input("Лог хабарламасын енгіз: ")
 #       f.write(msg + "\n")
#
#with open("log.txt", "r") as f:
#    print(f.read())








#NINTH DAY "try/except"
#try:
 #   x=int(input("Enter a number: "))
#    print(f'The answer: {x/10}"')
#except:
   # print("Error")

#try:
  #  a=input(f"Me: \n-Zhalantos, Did you do your home works ?")
#    b=input("Did you suck?")
  #  with open('names.txt','r') as names:
   #     print(names.read())
#except FileNotFoundError:
  #  print(f"He: \n-Your jokes are shit.")
#else:
    #print(f"Me: \n-Good Boy...")

#try:
  #  a,b=map(int,input("Enter a number: ").split())
   # print(a+b)
#except ValueError:
   # print("Please enter a number")
#finally:
    #print("Program has been finished")






#TENTH DAY "JSON"
#import json

#data={
#    "name": "...",
#    "age": ...,
#    "city": "...",
#    "email": "example@gmail.com"
#}


#with open("user.json","w") as f:
#    json.dump(data,f,indent=4)
#with open("user.json","r") as a:
    #print(json.load(a))



#ELEVENTH "Modules"
#def hello(name):
 #   print(f"Hello, {name}!")


#def add():
#    a,b=map(int,input().split())
#    print(a+b)
#add()

#def minus():
#    a,b=map(int,input().split())
#    print(a-b)
#minus()

#def multiply():
#    a,b=map(int,input().split())
#    print(a*b)
#multiply()

#def divide():
  #  a,b=map(int,input().split())
 #   print(a/b)
#divide()


#import random
#def abdu():
 #   for i in range(5):
#        print(random.randint(1,10000))
#abdu()


# from math import sqrt
#b=0
#while b==0:
 #   try:
  #      a = int(input("Enter a number: "))
   #     print(sqrt(a))
   # except AttributeError:
      #  print("Please enter a number again,because object has no attribute 'sqrt'")
    #else:
       # print("Good boy...")
        #break


#def text():
 #   a={"Bugin men dalaga zhyktym,dala suyk boldy,men uige baryp zhyly kiynyp aldym,elif men auyryp kalamyn"}
 #   print(a.reverse)
 #   print(a.upper())
#text()

#def abdu(example):
    #a="Bugin men dalaga zhyktym,dala suyk boldy,men uige baryp zhyly kiynyp aldym,elif men auyryp kalamyn"
    #with open(example,"w") as f:
        #f.write(a)

#def save_user(user_dict):
    #import json
    #with open("user.json", "w") as f:
    #    json.dump(user_dict, f, indent=4)


#def double():
    #n=int(input("Enter a number: "))
  #  print(n*2)
#double()



#TWELFTH DAY "class/OOP"
#class Cat:
#    def set_data(self,name , age , isHappy):
#        self.name = name
#        self.age = age
#        self.isHappy = isHappy
#    def abdu(self):
#        print(self.name)
#        print(self.age)
#        print(self.isHappy)
#cat1=Cat()
#cat1.set_data("Barsik",5,True)
#cat1.abdu()