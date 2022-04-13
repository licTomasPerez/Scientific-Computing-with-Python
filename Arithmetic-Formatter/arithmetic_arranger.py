def arithmetic_arranger(problems, solutions=False):
   ## First we must check that the number of problems in this array is less than five. 
   ## Otherwise, we will not run the program
  if len(problems) > 5:
    return "Error: Too many problems."

  lNo1 = "" ## the initialization of the first line of numbers to be added or subtracted 
  lNo2 = "" ## the initialization of the second line of numbers to be added or subtracted
  lines = "" ## the initialization of the line made up of dashes
  sumX = "" ## the initialization of the line where we will write up the results of the sum or subtraction
  string_Result= "" ## the ending result to be printed will be obtained as a concatenation of the previously initialized lines but previously we must work with them so as to adjust to the exercise's conditions.  
  
  ## we will write here the procedure to generate the lines
  for i, problem in enumerate(problems): ## we generate a tuple. Problem number and problem per sé
    number1, operation, number2 = problem.split() ## we get the numbers to be operated upon by the operator using .split()                                          ## since we are working with an initial list.

    if not operation in ["+", "-"]: 
      return "Error: Operator must be '+' or '-'." ## We will only compute sums or subtractions. Any other operation will not be computed

    # Of course, we can only add or substract numbers. This clause takes care of that by making sure user is inputing real numbers. 
    if not number1.isdigit() or not number2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(number1) > 4 or len(number2) > 4: ## if we get more than 4 problems we will not work.
      return "Error: Numbers cannot be more than four digits."
    
    if operation == "+":
      solution = int(number1) + int(number2) ## we compute the sum
    elif operation == '-':
      solution = int(number1) - int(number2) ## we compute the subtraction

    num_length = len(max([number1,number2], key=len)) ## we return the length of dashes to be written less 2

     ## Here we start to adjust the number of character in each one of the lines to match the required conditions.
    lNo1 += number1.rjust(num_length+2)
    lNo2 += operation + number2.rjust(num_length+1)
    lines += "-" * (num_length + 2)
    sumX += str(solution).rjust(num_length+2)
    
    ## If there are missing characters, we simply separate them with blank spaces.
    if i < len(problems)-1:
      lNo1 += "    "
      lNo2 += "    "
      lines += "    "
      sumX += "    "

  ## At last, we get the final result by concatenating strings ie. concatenating the previously defined lines
  string_Result = lNo1 + "\n" + lNo2 + "\n" + lines

  if solutions: 
    string_Result += "\n" + sumX ## if we want to get the results we have to print them too. 
  return string_Result

## Best regards. 
    ## Tomás Pérez, Ph.D. Fellow at Conicet, Argentina. 


