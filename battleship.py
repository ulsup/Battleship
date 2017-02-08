def read_field(filename):
    '''
    (str) -> (data)
    Read element from file and write it down to any data format.
    '''
    f = open(filename, 'r', encoding='utf-8')
    sequence = f.readlines()
    sequence = [w.strip('\n') for w in sequence]
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
    tuples = [(a,b) for a in letters for b in numbers]
    pairs = [(c,letters.index(c)+1) for c in letters]
    for i in pairs:
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
    ryadok = sequence[point[1] - 1]
    if point in tuples:
        if ryadok[poryadok] == '*':
            count = 1
            while True:
                if ryadok[poryadok + 1] == '*':
                    count += 1
                    poryadok += 1
                break
            while True:
                if ryadok[poryadok - 1] == '*':
                    count += 1
                    poryadok -= 1
                break
            while True:
                if sequence[point[1]] == '*':
                    count += 1
                    point[1] += 1
                break
            while True:
                if sequence[point[1] - 2] == '*':
                    count += 1
                    point[1] -= 1
                break
            return count
        else:
             return 'There is no ship in this area.'
        return count
    else:
        return 'You should enter uppercase letters between A and J and numbers between 1 and 10'

print(ship_size(read_field('field.txt'), ('E', 7)))

def is_valid(sequence):
    '''
    (data) -> (bool)
    Checks if the field is correct including sizes of ships and intersection, size of field.
    '''
    import collections
    new_seq = sum([i.split(' ') for i in sequence], [])
    counter = collections.Counter(new_seq)
    if counter['*'] == 4 and counter['**'] == 3 and counter['***'] == 2 and counter['****'] == 1:
        return True
    else:
        return False

print(is_valid(read_field('field.txt')))

def field_to_str(sequence):
    return '\n'.join(sequence)
print(field_to_str(read_field('field.txt')))

def generate_field():
    pass