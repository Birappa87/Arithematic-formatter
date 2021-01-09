def arithmetic_arranger(problems):
  operators = []



  #limitations
  if len(problems)>5:
    return "Error : Too many problems"

  for problem in problems:
    if "+" in problems[problem]:
      problems[problem] = problems[problem].split("+")
      operators.append("+")
    
    elif "-" in problems[problem]:
      problems[problem] = problems[problem].split("-")
      operators.append("-")
    else:
      return "Error : operators must br '+' or '-'."

  #Each operands will only contain digits 
  for digit in problems:
    if problems[digit].isdigit() = True:
      


  return arranged_problems
