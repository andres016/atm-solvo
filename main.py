"""
Atm -Solvo
Andres Lopez
1. Falta arreglar el print de la transaccion
"""
print("Welcome to bank")
pin=1234
choice = 0
log=[]
def withdraw():
      Transaction = []
      Bills= [10000,5000,2000]
      amount= int(input('Enter the amount you want to withddraw: $'))
      number_transaction = len(log)+1
      Transaction.append(number_transaction)
      for Bills in Bills:
            if amount >= Bills:
                  number_bills = amount // Bills
                  amount -= number_bills * Bills
                  Transaction.append(f'{number_bills} ${Bills} Bills')
      if amount == 0:
            log.append(Transaction)
            print('The Transaction was'+ str(Transaction[1:]))
      else:
            print('Insufficent bills for your transaction')

while choice != 3:
      print('***Menu***')
      print("1 = log")
      print("2 == withdraw")
      print("3 == leave")

      choice = int(input('Enter your option: '))
      if choice == 1:
            pin_ingresado = int(input('Enter pin: '))
            if pin_ingresado == pin:
                  print("Welcome to log")
                  print(log)
            else:
                  print("Pin incorrect  Try again")
      if choice == 2:
            withdraw()
      if choice == 3:
            print('Goodbye!')



