PersonInfo = {
    "name" : ["Nesil" , "Berke" , "Rıfkı", "Kylo"] ,
    "surName" : ["Uludağ" , "Arman" , "Kuş" , "Kedi" ],
    "id" : [ 1001 , 1002 , 1003 , 1004 ],
    "password" : [1011, 1012, 1013, 1014],
    "balance": [450 , 500, 250, 300]
}

def id_check(id):
   if id in PersonInfo["id"]:
     x = PersonInfo["id"].index(id)
     password = int(input("enter your password: "))
     if password == PersonInfo["password"][x]:
       print("Wellcome" + " " + PersonInfo["name"][x] + " " + PersonInfo["surName"][x])
       print("Account balance: " + str(PersonInfo["balance"][x]))
       print("1 = withdraw money")
       print("2 = deposit money")
       print("3 = send money")
       return True
     else :
       print("wrong password")
       return False
   else :
     print("wrong id")
     return False



def select_operation(operation, id):
  x = PersonInfo["id"].index(id)
  if operation == "1":
    amount = int(input("enter amount: "))
    if amount > PersonInfo["balance"][x]:
      print("insufficient funds")
    else:
     PersonInfo["balance"][x] = PersonInfo["balance"][x] - amount
    #  PersonInfo.update({"balance"[x]:PersonInfo["balance"][x] - amount}) yalnış yazmışsın şunu bi incele sonra + bi kere nasıl çalıştı da sonra çalışmadı onu anla
     print("new balance:" + " " + str(PersonInfo["balance"][x]))

  elif operation == "2":
      amount = int(input("enter amount: "))
      # PersonInfo.update({"balance"[x]:PersonInfo["balance"][x] + amount})
      PersonInfo["balance"][x] = PersonInfo["balance"][x] + amount
      print("new balance:" + " " + str(PersonInfo["balance"][x]))

  elif operation == "3":
     inputId = int(input("Enter ID: "))
     if inputId in PersonInfo["id"]:
      y = PersonInfo["id"].index(inputId)
      if x != y :
       inputName =input("Enter name : ")
       if inputName in PersonInfo["name"]:
        z = PersonInfo["name"].index(inputName)
        if z == y :
         amount = int(input("enter amount: "))
         if PersonInfo["balance"][x] >= amount :
          PersonInfo["balance"][z] = PersonInfo["balance"][z] + amount
          PersonInfo["balance"][x] = PersonInfo["balance"][x] - amount
          print("money sent")
          print("new balance: " + " " + str(PersonInfo["balance"][x])) 
         else:  
          print("insufficient funds")
       else:
        print("wrong name or wrong id")
      else : 
        print("you can not send money to yourself")
     else:
      print("invalid id")
  else:
   print("TRY AGAIN")
  




print("BANK")
personId = int(input("enter your id: "))

while id_check(personId):
    if (id_check == False) :
      break
    user_choice = input("select your operation: ")
    select_operation(user_choice,personId)
    break
    
