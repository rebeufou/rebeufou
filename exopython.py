# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# message = 'Good Morning'
# print(len(message)) #affichier le nb de caractères de 0 à ...
# print(message[11]) #afficher un caractère en particulier
# print(message[0:4]) #afficher un groupe de caractère
# print(message[-2]) #-1 est le dernier caracxtère, ici g, -2 l'avant-dernier
# print(message[ :-1]) # du début jusqu'à la fin
# print(message.upper()) #met en majuscule
# print(message.lower()) #minuscule
# print(message.count('o')) #compte le nb de 'o'
# print(message.find('o')) #renvoie la première position du o, ici 1 car le caractere g est le caract. 0
# new_message = message.replace('Morning','Afternoon')
# print(new_message)
# a = 'cccccct'
# b = 'cccg'
# print(a<b) #ordre alphabétique



    # num = int(input("Enter an interger : "))
    # if num < 5:
    #     print("The number is less than 5.")
    # else:
    #     print("The number is greater than 5.")
    

# num = int(input("Enter the number : "))
# if num%2 ==0:
#     print("The number {} is an even number.".format(num))
# else:
#     print(f"The number {num} is an odd number.")
    

#if
#elif
#else

# grade = float(input("Enter your marks : "))
# if grade < 5:
#     print("Suspended.")
# elif grade >= 5 and grade < 7:
#     print("Approved.")
# elif grade >= 7 and grade < 9:
#     print("Notable.")
# else:
#     print("Excellent.")


# weight = float(input("Enter your weight in kilos : "))
# height = float(input("Enter your height in meters: "))
# bmi = weight/height**2
# if bmi < 18.5:
#     print(f"Underweight, bmi : {bmi}.")
# elif bmi >= 18.5 and bmi < 25:
#     print(f"Normal weight, bmi : {bmi}.")
# elif bmi >= 25 and bmi < 30:
#     print(f"Overweight, bmi : {bmi}.")
# else:
#     print(f"Obesity, bmi : {bmi}")


# temp = input("Enter a temperature in C or F : ")
# degree = int(temp[:-1])
# i_check = temp[-1]

# if i_check.upper() == "C":
#     result = int(round((9*degree)/5 +32))
#     o_check = "Fahrenheit"
# elif i_check.upper() == "F":
#     result = int(round((9*degree - 32)*5/9))
#     o_check = "Celsius"
# else:
#     print("Input proper convention.")
#     quit()
# print("The temperatuyre in ", o_check, " is ", result, " degrees.")


# distance = input("Enter a distance in cm or in m : ")
# dist = int(distance[:-1])
    

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1 % num2 == 0:
#     quotient = int(num1/num2)
#     print(f"{num1} can be divided by {num2} and the quotient is {quotient}")
# else:
#     remainder = num1%num2
#     quotient = num1//num2
#     print(f"{num1} cannot be divided by {num2} ; the quotient is {quotient} and the remainder is {remainder}")
    


# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# minimum = min(num1, num2, num3)
# print(f"The minimum is {minimum}")

# unit = int(input("Enter the number of units : "))
# price = 0
# if unit < 100:
#     print("There is no charge.")
# elif unit >= 100 and unit < 200:
#     price = 5*(unit-100)
#     print(f"The total bill amount is Rs{price}")
# else:
#     price = 10*(unit-200) + 5*100
#     print(f"The total bill amount is Rs{price}")
    

# num = int(input("Enter ab integer value : "))
# while num>0:
#     res = num//3
#     print("The integer division of {} by 3 gives: {}. ".format(num,res))
#     num = int(input("Enter an integer value : "))
# print("We're done.")

# num = int(input("Enter an integer value : "))
# ndiv = 1
# while ndiv < num:
#     res = num//ndiv
#     print("The integer division of {} by {} gives : {}.".format(num, ndiv, res))
#     ndiv = ndiv + 1
    
# print("We're done.")
# print("Total number of divisions : {}.".format(ndiv))

# num=int(input("enter"))
# ndiv=0

# while num>0:
#     res=num//3
#     print("Divion of {} by 3 : {}".format(num,res))
#     ndiv=ndiv+1
#     print("Nb of divions so far : {}".format(ndiv))
#     num=int(input("enter"))
# print("Done")


# num = 0
# ndiv = 0
# while num <= 211:
#     if num % 3 ==0:
#         ndiv += 1
#         print("{} is divisible by 3.".format(num))
#     num += 1
# print("There are {} numbers divisible by 3 between 0 and 211.".format(ndiv))

# sum = 0
# for i in range(1,10):
#     sum += i 
# print(sum)


# sum = 0
# num = 1

# while num <= 10:
#     sum += num
#     num = num + 10

# print(sum)
    
# sum = 0
# nb = 0

# while nb < 10:
#     num = int(input("Enter a number : "))
#     nb += 1
#     sum += num
    
# average = sum/10
# print("The average is : {}".format(average))

# i = 1
# while i <= 4:
#     print("*"*i)
#     i += 1
    
# num = int(input("Enter a number : ")) #factorial
# fact = 1
# while num > 1:
#     fact = fact * num
#     num = num - 1
# print("The result is {}.".format(fact))
    


# name = 'Jesaa29Roy'
# size = len(name)
# i = 0
# while i < size:
#     if name[i].isdecimal():
#         break;
#     print(name[i], end = ' ')
#     i = i + 1
# print("\nThe execution has stopped.")

name = 'Jesaa29Roy'
# size = len(name)
# i = -1
# while i < size-1:
#     i += 1
#     if not name[i].isalpha(): #isalpha pour vérif si c'est une lettre
#         continue
#     print(name[i], end = ' ')

# for i in range(1,10,2): #saut de 2 au lieu de 1

# n = int(input("Enter the value of n : "))
# for i in range(1,n+1,2):
#     q_i = i**2
#     print(q_i)
    

# sum = 0
# for i in range(6):
#     sum = sum + i
#     print(f"The value of sum is in each integration: {sum}")
# print("The sum is : {}".format(sum))

# n = int(input("Enter the value of n : "))
# sum = 0
# for i in range(n+1):
#     sum += i
# print("The sum is equal to : {}".format(sum))

# n = int(input("Enter the value of n : "))
# sum = 0.0
# for i in range(1,n+1):
#     sum+=(i+1)/i**2
# print("The result is : {: .2f}.".format(sum)) #2f pour 2 chiffres décimaux 

# n = int(input("Enter the value of n : "))
# prod = 1
# for i in range(1,n+1):
#     prod *=i
# print("The product is : {}.".format(prod)) 

# for i in range(1,10):
#     for j in range(1,10):
#         print("{}{}".format(i,j))


# for i in range(1,10):
#     for j in range(1,10):
#         if i!=j:
#             print("{}{}".format(i,j))
            

# a = int(input("Enter the number of triangular numbers you want : "))
# for i in range(0, a+1):
#     t = i*(i+1)/2
#     print(t)
    
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print("{}{}{}".format(i,j,k), end = ", ") #end pour les espaces/virgules

# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#                 if i + j + k == 22:
#                     print("{}{}{}".format(i,j,k), end = " ")

# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if i**3 + j**3 + k**3 == i*100 + j*10 + k:
#                 print("{}{}{}".format(i,j,k), end = " ")
                
# n = int(input("Enter a number : "))
# print("The divisors of {} are : ".format(n))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i, end = " ")
        
# n = int(input("Enter a number : "))
# sum = 0
# number = 0
# for i in range(1,2*n+1,2):
#     sum += i
#     print("{}".format(i), end = " ")
# print("The sum is equal to : {}.".format(sum))
                

# n = int(input("Enter a number : "))
# verif = 0
# for i in range(2, n):
#     if n%i==0:
#         verif = 1
#         break;
# if verif == 1:
#     print("The number {} is not prime.".format(n))
# else:
#     print("The number {} is prime.".format(n))

# num1 = 0
# num2 = 1
# print("{} {}".format(num1,num2))
# for i in range(6):
#     num1 +=num2
#     num2 += num1
#     print("{} {}".format(num1,num2)) #fibonacci
    
#liste
# us_president = ['Barack Obama', 'George W. Bush', 'Joe Biden', 'Donald Trump', 'Barack Obama', 'George W. Bush']
# us_president.append('Bill Clinton') #ajouter un élément à la liste
# print(us_president)
# us_president.remove('Bill Clinton')#enlever un élément de la liste, s'il y a 2 valeurs, ça supprime la première
# #.pop() demande à spécifier l'indexe de l'élément à supprimer. 

# #changer un élément de la liste :
# us_president[4] = "George W. Bush"

# #tuple 

# us_president_tuple = ('Joe', 'Biden', '2021-01-20', 'Democratic')
# #immutable : on ne peut pas remove, add, change

# #set : 
#     #on ne peut pas dupliquer un élément
# us_president = {'Barack Obama', 'George W. Bush', 'Joe Biden', 'Donald Trump'}


# smooth = [3.14, 7, -2 + 3j, 'water', False, [1,2], 5, "Hello", "Hi", '7', 'e'] #une liste
# long_smooth = len(smooth) #longueur de la liste
# # print(long_smooth)
# # print(smooth[::2]) #5 n'est pas compris
# # print(smooth[7] [1])#accès au 7-1ème élément de la liste et au 2ème caractère, donc ne marche que sur des str ou des listes de liste
# print(smooth[-1])
# print(smooth[-2])

# n = int(input("Enter a number : "))
# sum = 0
# for i in range(1,n+1):
#     sum += 1/i
    
# print("The result is : {: .2f}.".format(sum)) #2f pour 2 chiffres décimaux 
    

# n = int(input("Enter a n value : "))
# thelist = []
# for i in range(1, n+1):
#     thelist.append(1/i)
# Sn = sum(thelist)
# print("For n = {} the sum accumulator is equal to {:.2f}".format(n,Sn))
# print(f"For n = {n:.2f} the sum accumulator is equal to {Sn:.2f}")

# line = "Temperature is 298.15 K before combustion"
# words = line.split('i')#crée une liste et sépare lorsqu'il y a un i
# print(words)

# line = input("Enter, in a single line and SEPARATED BY SPACES, the desired temperature values :")
# smooth_txt = line.split()
# print("List is now {}".format(smooth_txt))
# temp = []
# for element in smooth_txt:
#     value = float(element)
#     temp.append(value)
# print("The final list is {}".format(temp))

# a = [1, 3, 5, 7, 11]
# b = [13, 17]
# c = a + b
# print("First instruction print : {}".format(c))
# b[0] = -1
# d = []
# for e in a:
#     d.append(e+1)
# print("Second instruction print : {}".format(d))
# d.append(b[0] + 1)
# d.append(b[-1] + 1)
# print("3 {}".format(d))
# print("4 {}".format(d[-2:]))
# print("5 {}".format(d[:-1]))
# print("6 {}".format(d[1:4]))

# num = int(input("Enter a number : "))
# mylist = []
# for i in range(1,num+1):
#     mylist.append(i**2)
# print(mylist)

# name = "El"
# listename = []
# listegrade = []
# while name != "":
#     name = str(input("Enter a name : ")
#     if(name!=""):
#         listename.append(name)
#         grade = int(input("Enter the grade : "))
#         listegrade.append(grade)
# moyenne = sum(listegrade) / len(grade)
# print("The mean is equal to : {}".format(moyenne))


# nom=[]
# note=[]

# name="aaaa"
# while name!="":
#     name=input("Enter a name : ")
#     if name!="":
#         nom.append(name)
#         x=int(input("Enter his grade : "))
#         note.append(x)
# moyenne = sum(note) / len(note)
# print("The mean is equal to : {}".format(moyenne))


# listvalues = []
# num = "1"
# while num !="":
#     num = str(input("Enter a value : "))
#     if num !="":
#         listvalues.append(num)
# listnombre = []
# sume = 0
# for i in range(len(listvalues)):
#     sume += float(listvalues[i])
# moyenne = sume/len(listvalues)
# print("The arithmetic mean of the list {} bis : {}.".format(listvalues,moyenne))

# name = str(input("Enter the names of people in the same line, separated by blanks : "))
# listname = name.split(" ")
# number = len(listname)
# for i in range(len(listname)):
#     print("Hi {} ".format(listname[i]))
# print("There is {} persons".format(number))

# element = ["H","C","N","O","S","Cl"]
# atomicmass = [1.008,12.011,14.007,15.999,32.065,35.453]
# user = []
# mass = 0.0
# for i in range(len(element)):
#     number = int(input("How many {} do you want ? ".format(element[i])))
#     user.append(number)
#     mass += number*atomicmass[i]
# print("The molecular mass is : {} u.".format(mass))

# degree = int(input("The maximum degree n of the polynomial is : "))
# coef = []
# for i in range(degree + 1):
#     value = float(input("What is the value of the coefficient : " + str(i) + " : "))
#     coef.append(value)
# x = float(input("Enter the value of x : "))
# result = 0
# for i in range(len(coef)):
#     result += coef[i]*x**i
# print("For x = {}, the value is : {}.".format(x,result))
 
# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# print(add_sub(5,6))

# def wish(*names):
#     """This function greets all
#     the person in the names tuple."""
# #names is a tuple with arguments
# names = ("MRCET","CSE","SIR","MADAM")
# for name in names:
#     print("Hello",name)
    
# dictionnary

# country_capitals = {"United States": "Washington D.C.", "Italy": "Rome", "England": "London"}
# print(country_capitals)
# type(country_capitals)
# immutable

#dictionnary lenght :
# print(len(country_capitals))

# my_dict = {1: "Hello", (1,2):"Hello Hi", 3:[1,2,3]}
# print(my_dict)

# my_dict1 = {1: "Hello", [1,2]:"Hello Hi"}
# print(my_dict1) #erreur car la key ne peut pas être une liste

#méthode dict()
# Dict = dict({1: "Geeks", 2: "For", 3: "Geeks"})
# print("\nDictionnary with the use of dict() :")
# print(Dict)

# Dict = dict([(1,"Geeks"),(2,"For")])
# print("Dictionary with each item as pair :")
# print(Dict)

# Dict = {1: "Geeks", 2: "For",3: {"A" : "Welcome", "B" : "To", "C" : "Geeks"}}

# print(Dict[1])#accès au premier élément
# Dict={"Dict1": {1:"Geeks"}, "Dict2": {"Name": "For", "City": "Nanterre"}}
# print(Dict["Dict1"][1])
# print(Dict["Dict2"]["City"])

#values mutable but key immutable

# country_capitals = {"United States": "Washington D.C.", "Italy": "Rome", "England": "London"}
# print(country_capitals)
# country_capitals["Italy"] = "Venise"
# print(country_capitals)
# country_capitals["Germany"] = "Berlin" #add a value
# print(country_capitals)
# country_capitals["Mehdi"] = 1,2,3 #ajouter un groupe de valeurs
# print(country_capitals)
# del country_capitals["Mehdi"] #supprimer une key + ses valeurs
# print(country_capitals)

# for country in country_capitals:
#     print(country)
#     print(country_capitals[country])
    
#update() : add or change
#clear() remove all
#popitem() : remove the last
#copy() : return a copy of the dictionary
#keys() : returns all the dictionary's keys
#values() : returns all the dictionnary values
#pop : remove the item with the specified key
#get() : returns the value of the specified key

# country_capitals("Russia") = "Moscow"
# print(country_capitals)

# my_list = {1: "Hello", "Hi": 25, "Howdy": 100}
# print(1 in my_list) #true

# print("Howdy" not in my_list) #false
# print("Hello" in my_list) #false, pas de key "Hello"

# for keys,values in country_capitals.items():
#     print(country_capitals.keys())
#     print(country_capitals.values())
    
# dict2 = country_capitals.copy()
# print(dict2)

# dict2.clear()
# print(dict2)

# print(country_capitals.get("Italy"))

# print(country_capitals.items())

# print(country_capitals.values())

# country_capitals.update({"Algeria" : "Alger"})
# print(country_capitals)

#sequence of string
# cities = ("Paris","Athènes","Madrid")
# continent = "Europe"

# my_dictionary = dict.fromkeys(cities,continent)
# print(my_dictionary)

# my_dictionary1 = dict.fromkeys(cities)
# print(my_dictionary1)

# keys = ['Ten', 'Twenty', 'thirty']
# values = [10,20,30]
# my_dic = dict(zip(keys,values))
# print(my_dic)
# # my_dic = dict.formkeys(keys,values)
# # print(my_dic)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1,**dict2} #additionner 2 dictionnaires sans doublons 
# print(dict3)

# sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics" : 70, "history": 80}}}}

# employees = ['Kelly', 'Emma']
# defaults = {"designer": 'Developper', "salary": 8000}
# dict1 = dict.fromkeys(employees,defaults)
# print(dict1)

# sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New-York"}

# keys = ["name", "salary"]
# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# keys = ['a','b','c']
# for i in keys:
#     if sample_dict[i]==200:
#         print("200 present in a dict")
        
# #méthode 2
# if 200 in sample_dict.values():
#     print("...")


#3
# sample_dict= {'emp1': {'name': 'Jhon', 'salary': 7500},
#               'emp2': {'name': 'Emma', 'salary': 8000},
#               'emp3': {'name': 'Brad', 'salary': 500}}
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)

# #Problem1
# periodictable = {"H": {"atomicnumber":1,"meltingPoint":14,"boilingPoint":20},
#                   "He": {"atomicnumber":2,"meltingPoint":1,"boilingPoint":4},
#                   "Li": {"atomicnumber":3,"meltingPoint":453,"boilingPoint":1603},
#                   "Be": {"atomicnumber":4,"meltingPoint":1560,"boilingPoint":2742},
#                   "B": {"atomicnumber":5,"meltingPoint":2349,"boilingPoint":4200},
#                   "C": {"atomicnumber":6,"meltingPoint":3915,"boilingPoint":3915},
#                   "N": {"atomicnumber":7,"meltingPoint":63,"boilingPoint":77},
#                   "O": {"atomicnumber":8,"meltingPoint":54,"boilingPoint":90},
#                   "F": {"atomicnumber":9,"meltingPoint":53,"boilingPoint":85},
#                   "Ne": {"atomicnumber":10,"meltingPoint":25,"boilingPoint":27}}
# value = str(input("What is the element ? "))
# temp = int(input("What's the temperature ? "))
# if temp < periodictable[value]["meltingPoint"]:
#     print("{} is solid".format(value))
# elif (temp < periodictable[value]["boilingPoint"]) and (temp > periodictable[value]["meltingPoint"]):
#     print("{} is liquid".format(value))
# else:
#     print("{} is gas".format(value))
    
# #Problem2
# interestrates = {
#     "ANZ": {"year1and2": 2.3, "year3": 4.1},
#     "Bank of Australia": {"year1and2": 0.1, "year3": 5.0},
#     "Commonwealth Bank": {"year1and2": 3.5, "year3": 3.8},
#     "Westpac": {"year1and2": 3.7, "year3": 3.7}}


# names = str(input("What's the name of the bank ? "))
# years = int(input("How many years do they stay ? "))
# principal = int(input("What's the value of the payment ? "))
# if names:
#         if years <= 2:
#             interest_rate = interestrates[names]["year1and2"]/100
#         else:
#             interest_rate = interestrates[names]["year3"]/100
            
# #        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)
#         monthly_payment = (principal + principal*interest_rate)/(years*12)

#         print(f"For {principal} $ at the bank {names} in {years} years :")
#         print(f"The mortgage repayments {monthly_payment:.2f} $")

# else:
#         print("The bank doesn't exist.")
        
# def functionn(*kids): #plusieurs éléments en attribut
#     print("The youngest child is " + kids[2])
    
# functionn("Emil", "Tobias", "lucas", "Noé")

# def func2(**kids): #** = dictionnary et *arguments : tuple, list, number, str sauf dico
#     print("The last name is " + kids["lname"])
    
# func2(fname = "Tobias", lname = "Refsnes")

# def biggest(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# print( biggest(5,6))

# liste = [9,2,5,10,1]


# def func4():
#     liste = []
#     for i in range(5):
#         num1 = int(input("enter a number : "))
#         liste.append(num1)
#     print("The max is {} and the min is {}".format(max(liste),min(liste)))

# print(func4())

# def func5():
#     liste = []
#     for i in range(5):
#         num1 = int(input("enter a number : "))
#         liste.append(num1)
#     for i in range(5):
#         max1 = liste[0]
#         min1 = liste[0]
#         if max1 < liste[i]:
#             max1 = liste[i]
#         if min1 > liste[i]:
#             min1 = liste[i]
#     print("The max is {} and the min is {}.".format(max1,min1))
# print(func5())


# #modèle d'un code
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# try:
#     f = open('/content/testfile.txt')
# except Exception:
#     print("Sorry, this file does not exist.")

# try:
#     f = open('/content/test_file.txt')
#     var 
# except FileNotFoundError:
#     print("File error")
# except NameError:
#     print("Name error")

# while True:   
#     try:
#         num = int(input("Enter an integer : "))
#     except :
#         print("Error.")
#     num = int(input("Enter an integer please : "))
#     if(num%2 == 0):
#         print("{0} is Even".format(num))
#     else:
#         print("{0} is Odd".format(num))
        
# def estpremier(num):
#     verif = True
#     for i in range(num):
#         if num%i == 0:
#             verif = False

# while True:
#     try:
#         num = int(input("Enter a number "))
#         while(num == 1 or num==0 or num<0):
#             print("Enter a propper number, the input is wrong : ")
#             num = int(input("Enter a number "))
#         if (num%2) == 0:
#             print("{} is Even".format(num))
#             break
#         else:
#             print("{} is Odd".format(num))
#     except ValueError as e:
#         print(e)


import numpy as np #calcul sur des listes, matrices... AN
# a = np.array([1,3,5]) #+ rapide que les listes
# b = np.array([2,6,9])
# print(a*b) #possible avec np
# a = np.array([1,2,3], dtype = 'int32') #
# #b = np.array([9,8,7],[6,5,4])

# #get dimension :
# a.ndim

# #get shape
# b.shape

#get type 
# a.dtype

# #get item size
# a.itemsize

# #get total size
# a.nbytes

# #get number of elements
# a.size

# a = np.array([1,2,3,4,5,6,7],[8,9,10,11,12,13,14])
#  #get specific element 
# print(a[1,3])

# #get a specific row 

# a[0,:]

# #get a specific column
# a[:,2]

# #getting a little more fancy [startindex:endindex:stepsize]
# a[0, 1:-1:2] #résultat : [2,4,6] ; on se place sur la ligne
# a[1:-1:2,0] #on se place sur la colonne

# #créer une matrice avec des zéros dedans 
# np.zeros((2,3))

# #créer une matrice avec des 1 dedans 
# np.ones((4,2,2),dtype = 'int32')

# #créer une matrice avec n'importe quelle nombre 
# np.full((2,2),(99))
# np.full_like(a,4)

# #random decimal number 
# np.random.rand(4,2)
# np.random.randint(-4,8, size = (3,3)) #-4 et 8 sont les mins et max des nombresrandom pouvant être pris

# #matrice identité
# np.identity(4)

#repeat an array 
# arr = np.array([[1,2,3]])
# # r1 = np.repeat(arr, 3, axis = 0)
# # print(r1)
        
# output = np.ones((5,5))
# print(output)

# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)

# output[1:-1,1:-1] =  z #créer une matrice 
# print(output)    

# #copy une matricz 
# b = output.copy()
# a = b.copy()

# # b + 2 #ajouter 2 à tous les nombres de la matrice
# # b - 2
# # b*2
# # b/2
# # b**2

# np.cos(b)
# np.matmul(a,b)
# # c = np.random.rand(-5,5,size=(3,2)) #renverra des float car rien sinon randint
# print(np.matmul(a,b))

# f = np.random.randint(-10,10,size=(4,4))
# g = np.random.randint(-4,10,size=(3,3))
# print(np.linalg.det(f))
# print(np.linalg.det(g))#déterminant

# stats = np.array([[1,2,3],[4,5,6]]) #axis correspond à la colonne
# np.min(stats, axis=1)
# np.max(stats)
# np.sum(stats, axis = 0) #faire la somme entre les termes de chaque ligne 

# #Repeat an array
# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3,axis=0) #3 lignes, 3 colonnes
# print(r1)
# r2 = np.repeat(arr,3,axis =1)#1 ligne, 9 colonnes

# angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
# angles = np.array(angles)
# sin_ang = np.sin(angles)

# npoints = 21
# values = np.linspace(-2.0,2.0,npoints) #renvoie 21 points à équidistances entre -2 et 2, number of division
# print(values)

# y = np.arange(10,31)
# #y = np.linspace(10,30,21)
# y[4] = 1
# print(y)

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,101)
y =x**2
print(x)

plt.plot(x,y)
plt.show()



    
