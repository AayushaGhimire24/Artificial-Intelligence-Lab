from itertools import permutations


def solve_cryptarithmetic():
    # Letters involved in the puzzle
    letters = 'TWOFRU'
    digits = '0123456789'


    # Check all possible permutations of the digits for the letters
    for perm in permutations(digits, len(letters)):
        # Create a mapping of letters to digits
        mapping = {letters[i]: int(perm[i]) for i in range(len(letters))}
        
        # Ensure that the leading digits are non-zero
        if mapping['T'] == 0 or mapping['F'] == 0:
            continue
        
        # Calculate TWO, TWO and FOUR
        TWO = 100 * mapping['T'] + 10 * mapping['W'] + mapping['O']
        FOUR = 1000 * mapping['F'] + 100 * mapping['O'] + 10 * mapping['U'] + mapping['R']
        
        # Check if the equation holds true
        if 2 * TWO == FOUR:
            return mapping, TWO, FOUR


    return None


# Find and print the solution
solution = solve_cryptarithmetic()
if solution:
    mapping, TWO, FOUR = solution
    print(f"Mapping: {mapping}")
    print(f"TWO: {TWO}")
    print(f"FOUR: {FOUR}")
else:
    print("No solution found.")
