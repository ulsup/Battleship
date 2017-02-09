def read_field(filename):
    '''
    (str) -> (data)
    Reads element from file and writes it down to the data format.
    '''
    f = open(filename, 'r', encoding='utf-8')
    sequence = f.readlines()
    sequence = [w.strip('\n') for w in sequence]  # creates a list with strings in it (1 string = 1 line)
    f.close()
    return sequence
print(read_field('field.txt'))

def has_ship(sequence, point):
    '''
    (data, tuple) -> (bool)
    Checks if field has a ship or its part in this point (coordinates).
    '''
    import string
    letters = [i for i in string.ascii_uppercase[:10]]
    numbers = [i for i in range(1,11)]
    tuples = [(a,b) for a in letters for b in numbers]  # creates all possible coordinates in tuples
    pairs = [(c,letters.index(c)+1) for c in letters]  # to create tuple of letters and its indexes
    for i in pairs:  # its easier to switch letter to number and number to letter
        if point[0] in i:
            poryadok = i[1] - 1
    if point in tuples:
        if sequence[point[1]-1][poryadok] == '*':
            return True
        else:
            return False
    else:
        return 'You should enter uppercase letters between A and J and numbers between 1 and 10'
print(has_ship(read_field('field.txt'), ('B', 4)))

def ship_size(sequence, point):
    '''
    (data, tuple) -> (int)
    Checks the lenght of the ship using the coordinates of its part.
    '''
    import string
    letters = [i for i in string.ascii_uppercase[:10]]
    numbers = [i for i in range(1, 11)]
    tuples = [(a, b) for a in letters for b in numbers]
    pairs = [(c, letters.index(c) + 1) for c in letters]
    for i in pairs:
        if point[0] in i:
            poryadok = i[1] - 1
            break
    line = point[1] - 1
    ryadok = sequence[line]
    if point in tuples:
        if ryadok[poryadok] == '*':  # checks if on this area placed ship or its part
            count = 1
            right = 0
            left = 0
            up = 0
            down = 0
            lst = []
            lst.append((point[0], line + 1))  # addes coordinates of current point
            if ryadok[poryadok + 1] == '*' or ryadok[poryadok - 1] == '*':  # checks if ship has more parts on the right
                try:  # or on the left sides. if it hasn't, it checks whether ship has parts below or under its part
                    while ryadok[poryadok + 1] == '*':  # switches positions within one line
                        count += 1
                        poryadok += 1
                        right += 1  # this variable is to count how many positions we moved on
                        if right != 0:
                            for i in pairs:
                                if (poryadok + 1) in i:
                                    new_point = i[0]
                                    break
                            lst.append((new_point, line + 1))  # addes coordinate of '*' until not ''
                except IndexError:
                    pass
                poryadok -= right  # to get back previous value of variable poryadok
                try:
                    while ryadok[poryadok - 1] == '*':
                        if poryadok == 0:  # if index of '*' is 0, we don't need to go to the last element (index -1)
                            break  # so it finishes counting the length
                        count += 1
                        poryadok -= 1
                        left -= 1
                        if left != 0:
                            for i in pairs:  # switches number to the letter
                                if (poryadok + 1) in i:
                                    new_point = i[0]
                            lst.append((new_point, line + 1))
                except IndexError:
                    pass
                poryadok += left
            elif sequence[line + 1][poryadok] == '*' or sequence[line - 1][poryadok] == '*':  # checks whether ship has
                try:  # parts below or under its part
                    while sequence[line + 1][poryadok] == '*':  # switches lines but moves on the same position
                        count += 1
                        line += 1
                        down += 1
                        if down != 0:
                            for i in pairs:
                                if (poryadok + 1) in i:
                                    new_point = i[0]
                                    break
                            lst.append((new_point, line + 1))
                except IndexError:
                    pass
                line -= down
                try:
                    while sequence[line - 1][poryadok] == '*':
                        count += 1
                        line -= 1
                        up += 1
                        if up != 0:
                            for i in pairs:
                                if (poryadok + 1) in i:
                                    new_point = i[0]
                                    break
                            lst.append((new_point, line - 1))
                except IndexError:
                    pass
                line += up
        else:
             return 'There is no ship in this area.'
        return (count, lst)
    else:
        return 'You should enter uppercase letters between A and J and numbers between 1 and 10'

print(ship_size(read_field('field.txt'), ('B', 7)))

def is_valid(sequence):
    '''
    (data) -> (bool)
    Checks if the field is correct including sizes of ships and intersection, size of field.
    '''
    for line in sequence:
        for element in line:
            if element == '*':
                pass

print(is_valid(read_field('field.txt')))

def field_to_str(sequence):
    return '\n'.join(sequence)
print(field_to_str(read_field('field.txt')))

def generate_field():
    pass