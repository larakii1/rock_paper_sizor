import random
choice = int(input("faire un choix : 1.Papier 2.caillou 3.ciseau"))
result=random.randint(1,3)
if choice == 1 :
    print(''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    
    print("papier")
elif choice == 2 :

    print(''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
          )
    print('caillou')
elif choice == 3 :

    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''' )

    print("ciseau")
else :
    print("wrong choice")

if result == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
           ''')
    
    print("papier")
elif result == 2:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
    
    print ("caillou")
elif result == 3:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          
          ''')
    print("ciseau")

if choice == result :
    print("draw")
elif choice ==1 and result== 2:
     print("vous avez gagné")
elif choice == 2 and result ==3:
    print("vous avez gagné ")
elif choice == 3  and result == 1:
    print("vous avez gagné")
else :
    print("vous avez perdu")

input("Appuie sur Entrée pour fermer...")