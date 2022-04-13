class Category:

    ### First things first: all instances of a class are to have name, a budget and a ledger. 
   def __init__(self, name):
     self.name = name
     self.budget = 0
     self.ledger = list()

    ### Next we define a deposit method which accepts a real amount and a description. We are to construct a dictionary using these input.
   def deposit(self, amount, description = ""):
     self.budget += amount
     self.ledger.append({"amount": amount, "description": description})

    ### Now we are to code a method for excracting a certain amount of money. The catch here is that the user will input a real, positive, number. So we are to substract this as number to the previous amount and generate a control cutoff, should the account have insufficent funds.
   def withdraw(self, subtractAmount, description = ""):
     if self.budget >= subtractAmount:
        self.budget -= subtractAmount
        self.ledger.append({"amount": (subtractAmount*-1), "description": description})
        print('Succesful subtraction.')
        return True
     else:
         print('ERROR: not enough funds in account.')
         return False
        
   ### We write a method for printing the funds in the account without modifying it 
   def get_balance(self):
     return self.budget
   
   ### We define another method that will accept a real number. It will return False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
   
   def check_funds(self, amountTest):
        if self.budget >= amountTest:
            return True
        else:
            return False

   ### We code a method for transfering an amount of money from one instance of the category class to another instance of the category class with a control cutoff if the operation is unsuccesful.
   def transfer(self, amountToTransfer, category):
     ## We give the order to transfer and the destination account.
     if self.check_funds(amountToTransfer): 
       self.withdraw( amountToTransfer, f"Transfer to {category.name}")
       ## Should the operation be succesful we need to readjust the funds in the original account, as follows:
       category.deposit(amountToTransfer, f"Transfer from {self.name}")
       return True
     else:
       return False

   def get_withdrawals(self):
        total = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                total += entry["amount"]

        return round(total, 2)

   ### We define a method for printing the previous information according to the exercise's guidelines. 
   def __title__(self):
     ## A title line of 30 characters where the name of the category is centered in a line of * characters.
     title_num = len(self.name) ## the length of the account's name.
     no_characters = 30-title_num
     centering = int(no_characters / 2)
     show = ("*" * centering) + self.name + ("*"*centering)
     line2 = ""

      ## Now we treat the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters. 
     for item in self.ledger:
       ## setting the amount of characters 
       dscpt = item["description"][:23]
       ## We concatenate the information according to the exercise's guidelines.
       amount = item['amount']
       line2 += f"{dscpt}{amount: >{len(dscpt) - 30}.2f}\n"
       show += "\nTotal: " + "{:.2f}".format(self.get_balance())
     return show

   def get_all_withdrawls(self):
     total = 0
     for entry in self.ledger:
        if entry["amount"] < 0:
           total += entry["amount"]
        return round(total, 2)
             
### This function will take a list of categories as input, and will process it, giving us certain information.              
def create_spend_chart(categories):

    ## This variable will be initialized by a simple string
    output = "Percentage spent by category"
    x = len(categories) ## Amount of elements in the categories list
    y = 100  ## Length of the chart
    percentages = [] ## We start by initializing an empty percentage list.    
    total_spent = 0  ## Then we initialize a real variable 

    for ctg in categories: 
      total_spent += ctg.get_withdrawals()
    for ctg in categories: 
      raw = ctg.get_withdrawals() / total_spent
      percentages.append( int( (raw // .1) * 10 ) )

    title = output + "\n"

    graph = ""
    ## We print the percentages but remember, this function will be tested with up to four categories.
    for interval in range(y, -10, -10):
        graph += str(interval).rjust(3) + "| "
        for percent in percentages:
            if int(percent) >= interval: 
                graph += "o  " + "\n"
            else:
                graph += " " + " " + " " + "\n"
    
    graph += " " * 4 + "-" * ((x * 2) + 4)

    ## We ought to find the maximum name length
    optimal_name_len = 0 ## initialized
    for ctg in categories:
        name = ctg.name ## asigned
        if len(name) > optimal_name_len:
            optimal_name_len = len(name)

    final_result = ""
    for i in range(optimal_name_len):
        if i < optimal_name_len:
            final_result += "\n" + " " * 5
        for ctgy in categories:
            name = ctg.name
            if len(name) > i:
                final_result += name[i] + " " * 2
            else:
                final_result += " " * 3

    final_result = title + graph + final_result.rstrip("\n")

    return final_result