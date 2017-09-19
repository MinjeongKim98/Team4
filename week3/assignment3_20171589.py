import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "":  # if nothing was written -> just pass and make prgram work again
            continue
        parse = inputstr.split(" ")
        # try: #try except -> fix all error
        try:
            if parse[0] == 'add':
                if len(parse) > 4:
                    print("something unnecessary was entered")

                else :
                    record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                    scdb += [record]
        except IndexError:
            print("Index is out of range, check and enter again")

        try:
            if parse[0] == 'del':
                for k in range(len(parse)):
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            scdb.remove(p)
                for j in scdb:
                    if parse[1] != j['Name']:
                        print('check and do it again')
                if len(parse) > 2:
                    print("unnecessary things were entered")
        except IndexError:
                 print("Index error, check and try again")


        try:
            if parse[0] == 'show':
                if len(parse) > 1:
                    print('They are not required')
                else:
                    sortKey ='Name' if len(parse) == 1 else parse[1]
                    showScoreDB(scdb, sortKey)

        except IndexError:
            print("Index Error check and try again")

        try:
            if parse[0] == 'find':
                if len(parse) > 1:
                    print("unnecessary things were written")
                else:
                    for i in scdb:
                        if parse[1] == i['Name']:
                            print(i)

        except IndexError:
            print("Index is out of range check and try again")

        try:
            if parse[0] == 'inc':
                for i in scdb:
                    if i['Name'] == parse[1]: #find name in the list scdb
                        if len(parse) > 2:
                            print("unnecessary things exist")
                        else:
                            i['Score'] = int(parse[2])+int(i['Score']) #list is string so change them as integer
                    else: #enter the word that does not exist
                        print("That name does not exist")

        except IndexError: #tell they are wrong and make program work again
            print("Out of range. try again please")


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

