import re
import time

from z3 import *

# Function to solve a given skeletal division problem
# Parameters:
#     A string representing a division equation
#     An array including each step of the corresponding long division
#     (optional) An integer representing the maximum number of solutions returned
#        None as default value if not passed into function
# Input Restrictions:
#    No leading zeros except for last value in array
def skeletalDivision(input: str, arr, limit=None):
    start_time  = time.perf_counter()

    input_words = re.findall(r'\b[a-zA-Z0-9]\w*\b', input)
    
    # List of equations that must hold true
    equations = []
    
    # Dictionary containing elements of the original equation
    initial = []
    for word in input_words:
        initial.append(word)
    if len(initial) > 3:
        remain = initial[3]
    else:
        remain = ''
    for w in arr:
        input_words.append(w)

    # Dictionary of words
    words = { w: Int(w) for w in list(input_words) }

    # Dictionary of letters
    letters = { l: Int(l) for l in list("".join(input_words)) }
    for l in list("".join(input_words)):
        numberp = re.match(r'[0-9]', l) 
        if numberp:
            letters.update( { l: float(l) })
    
    # Dictionary of all letters and words
    complete = {}
    complete.update(letters.items())
    complete.update(words.items())
    
    # Useful constants
    dividen = initial[0]
    divisor = initial[1]
    ans = initial[2]
    
    # Constraints: letters must be a number between 0 and 9
    lettersToNum = [ And(0.0 <= v, v <= 9.0) for l,v in letters.items() ]

    # Constraint: first letter of words must not be zero
    # unless it's the remainder or last number in the array
    wordNotZero = [ Or(And(Or(num == arr[len(arr)-1], num == remain), len(num) == 1),
                        letters[num[0]] != 0) for num in words.keys()]
      
    # Constraint: convert words to decimal values
    wordsToNum = [ v == Sum(*[letter_symbol * 10.0**index 
                            for index,letter_symbol in enumerate(
                                reversed([letters[l] for l in list(w)]))]) 
                             for w, v in words.items()]
    
    # Constraint: Remainder
    remainder = dividen + ' % ' + divisor
    if remain != '':
        # Constraint: the remainder must be equivalent to the dividen mod divisor
        equRemain = remain + '== pow(10, ' + str(len(remain)) + ') * (' + remainder + ') / ' + divisor
        equations.append(equRemain)
        print('Remainder Equation: ', equRemain)
    else:
        # Constraint: if there is no remainder the last value of the array has to be 0
        equRemain = arr[len(arr)-1] + ' == 0'
        equations.append(equRemain)
        # Constraint: if there is no remainder the dividen divided by the divisor must
        # have a remainder of 0
        equNoRound = '(' + remainder + ') % 1 == 0'
        equations.append(equNoRound)
        # Constraint: product (controls rounding)
        equProduct = divisor + ' * ' + ans + ' == ' + dividen
        equations.append(equProduct)

    # Constraint: problem as defined by the original input
    equOriginal = dividen + ' / ' + divisor + ' - (' + dividen + ' / ' + divisor  + '%1) == ' + ans 
    equations.append(equOriginal)
    print('Original Equation: ', equOriginal)
    
    # Constraint: Difference between divisor and first member of the array
    # equals the second member of the array
    shift = 10
    powOfTen = len(dividen) - 1 - len(arr[0])
    if len(arr[0]) == len(divisor): 
        powOfTen = powOfTen - 1
    if powOfTen < 0: 
        powOfTen = 0
    if len(dividen) == len(ans): 
        shift = 1
    equDiffBase = '((' + dividen + '-(' + dividen + '%pow(10,' + str(powOfTen) + ')))/pow(10,'  + str(powOfTen) + '))-(' + arr[0] + '*' + str(shift) + ')==' + arr[1]
    equations.append(equDiffBase) 
    print('Base Difference: ', equDiffBase)
    
    # Constraint: check difference of long division steps 
    # loop before decimal
    i = 1
    while i < len(arr)-2 and i < len(dividen):
        if i+2 >= len(dividen)-1:
            x = list("".join(arr[i+2]))
            equDiff = arr[i] + ' - ' + arr[i+1] + ' == ' + x[0]
        else:
            equDiff = arr[i] + ' - ' + arr[i+1] + ' == (' + arr[i+2] + ' - (' + arr[i+2] + '% 10)) / 10' 
        equations.append(equDiff)
        print('Difference Equation (before decimal): ', equDiff)
        i = i + 2  
    # Loop after decimal if applicable
    if remain != '':
        while i < len(arr) - 2:
            x = list("".join(arr[i+2]))
            equDiff = arr[i] + ' - ' + arr[i+1] + ' == ' + x[0]
            equations.append(equDiff)
            i = i + 2
            print('Difference Equation (after decimal): ', equDiff)
            
    # Constraint: dividen times answer equals the corresponding subtrahend
    z = 0
    # Loop over whole number portion of answer
    for x in list("".join(ans)):
        equSub = x + " * " + divisor + " == " + arr[z]
        equations.append(equSub)
        print('Subtrahend Equation: ', equSub)
        z = z+2
    # Loop over decimal portion of answer if present
    if remain != '':
        for x in list("".join(remain)):
            equSub = x + " * " + divisor + " == " + arr[z]
            equations.append(equSub)
            print('Subtrahend (Decimal) Equation: ', equSub)
            z = z+2
    
    # Each constraint equation must hold true
    checkEquations = [ (eval(equ, None, complete) == True) for equ in equations ]
    
    # Initialize Solver
    solver = Solver()
    
    # Dictionary of valid models: solutions
    solutions = []
    
    # Asserts constraints in the solver
    solver.add(lettersToNum + wordsToNum + wordNotZero + checkEquations)
    
    print(input)
    print('SOLVER: \n', solver)
    while str(solver.check()) == 'sat':     
        solutions.append({ str(s): solver.model()[s] for w,s in words.items() })
        print(solutions[-1])
        solver.add(Or(*[ s != solver.model()[s] for w,s in words.items() ]))
        if limit and len(solutions) >= limit: break
         
    run_time = round(time.perf_counter() - start_time, 1)
    print(f'*** {len(solutions)} solutions found in {run_time}s ***\n')
    return solutions

skeletalDivision('1365 / 14 == 97.5',
                         ['126', 
                          '105',
                          '98',    
                          '70',
                          '70',
                          '0'])
skeletalDivision('FGHJ / AB == CD.E',
                         ['KL6', 
                          'MNP',
                          'QR',
                          'ST',
                          'UV',
                          '0'])
pass