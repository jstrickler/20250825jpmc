# generator function
def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # next()
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object
    # return iterator object()


mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in: # next(mary_in)
    print(trimmed_line)

# generator expression
trimmed_lines = (line.rstrip() for line in mary_in)
