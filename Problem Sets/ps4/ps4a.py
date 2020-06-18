# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

permutations = '123'

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    global permutations 
    permutations = []


    def write_permutation(string):
        global permutations
        permutations += (string,)


    def permutation (string, step = 0):
        if step == len (string):
            permutationsString = ''
            for char in string:
                permutationsString += char
            write_permutation (permutationsString)
            #print ('Writing ' + permutationsString + '\n')
        else:
            for i in range (step, len(string)):
                string_copy = [character for character in string]
                # swap the current index with the step
                string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
                permutation(string_copy, step + 1)
    
    permutation (sequence, 0)
    return permutations



if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

