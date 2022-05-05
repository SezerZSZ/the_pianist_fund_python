n = int(input())
pieces_collection = {}

for i in range(n):
    line = input().split("|")
    key = line[2]
    piece = line[0]
    composer = line[1]

    if piece not in pieces_collection.keys():
        pieces_collection[piece] = {key: composer}

line = input()
while line != 'Stop':
    data = line.split("|")
    cmd = data[0]
    if cmd == "Add":
        piece = data[1]
        composer = data[2]
        key = data[3]

        if piece not in pieces_collection.keys():
            pieces_collection[piece] = {key: composer}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif cmd == "Remove":
        piece = data[1]

        if piece not in pieces_collection.keys():
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            del pieces_collection[piece]
            print(f'Successfully removed {piece}!')

    elif cmd == 'ChangeKey':
        piece = data[1]
        new_key = data[2]

        if piece not in pieces_collection.keys():
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            value = pieces_collection.get(piece)  # {'C# Minor: 'Beethoven'}
            for k in value.copy():
                old_key = k
                value[new_key] = value.pop(old_key)  # {'C# Major': 'Beethoven'}

            pieces_collection[piece].update(value)  # we're literally 'putting' the updated value to the piece
            print(f"Changed the key of {piece} to {new_key}!")

    line = input()

# printing...
for key, value in sorted(pieces_collection.items()):
    piece = key
    for k, v in value.items():  # here we separate the key and composer, assigning variables to them...
        key = k
        composer = v
        # then we print them in the order we wish...
        print(f"{piece} -> Composer: {composer}, Key: {key}")







