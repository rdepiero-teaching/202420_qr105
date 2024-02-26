from math import factorial

# write all of your function definitions in this cell
def basic_probability(number_of_outcomes, total_outcomes, printer=False):

    probability = number_of_outcomes / total_outcomes
    
    if printer == True:
        print('Number of outcomes: ', number_of_outcomes)
        print('Total outcomes: ', total_outcomes)
        print(f'Probability: {probability:.4f} or {probability:2.2%}')
    else:
        return probability

# calculates the complement probability: 1 - P(A)
def complement_probability(number_of_outcomes, total_outcomes, printer=False):

    probability = 1 - basic_probability(number_of_outcomes, total_outcomes)

    if printer == True:
        print('Number of outcomes: ', number_of_outcomes)
        print('Total outcomes: ', total_outcomes)
        print(f'Complement Probability: {probability:.4f} or {probability:2.2%}')
    else:
        return probability

# calculates the probability P(A and B) = P(A) * P(B)
def probability_both_A_B(probability_A, probability_B, printer=False):
    
    probability = probability_A * probability_B

    if printer == True:
        print('Probability A : ', probability_A)
        print('Probability B: ', probability_B)
        print(f'Probability of A and B: {probability:.4f} or {probability:2.2%}')
    else:
        return probability

# calculates the probability P(A or B) = P(A) + P(B) - P(A) * P(B)
def probability_either_A_B(probability_A, probability_B, printer=False):
    
    probability = probability_A + probability_B - probability_both_A_B(probability_A, probability_B)

    if printer == True:
        print('Probability A : ', probability_A)
        print('Probability B: ', probability_B)
        print(f'Probability of A or B: {probability:.4f} or {probability:2.2%}')
    else:
        return probability

# calculates the conditional probability (A and B not independent: P(A and B) = P(A) * P(B | A)
def conditional_probability(probability_A, probability_B_given_A, printer=False):
    
    probability = probability_A * probability_B_given_A
    
    if printer == True:
        print('Probability A : ', probability_A)
        print('Probability B given A: ', probability_B_given_A)
        print(f'Conditional Probability P(A and B): {probability:.4f} or {probability:2.2%}')
    else:
        return probability


def basic_counting(list_of_options):
    
    num_options = 1
    
    for i in range(len(list_of_options)):
    
        num_options *= list_of_options[i]
    
    return num_options


def combinations(num_of_choices, size_of_set):  
    combos = factorial(num_of_choices) / ( factorial(num_of_choices - size_of_set) * factorial(size_of_set) )
    return combos

def permutations(num_of_choices, size_of_set):  
    perms = factorial(num_of_choices) / ( factorial(num_of_choices - size_of_set) )
    return perms

def expected_value(values, probs, printer=False):
    expected = 0

    for i in range(len(probs)):
        expected = expected + values[i] * probs[i]

    if printer == True:
        print(f'Expected value: {expected:.3f}')
    else:
        return expected
