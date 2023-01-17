while True:
    try:
        fname = input('Enter file name: ')

        if fname != 'done':
            t = []

            with open(fname) as file:
                for line in file:
                    for word in line.rstrip().split():
                        if word not in t:
                            t.append(word)

            sorted(t)
            print(t)
        else:
            print('See ya!')
            break
    except:
        print('Invalid file name or error')
