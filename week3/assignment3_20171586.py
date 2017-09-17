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
		scdb =  pickle.load(fH)
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
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		try:
			if parse[0] == 'add': #4
			#count = 0
			#	for p in scdb:
			#		if p['Name'] == parse[1]:
			#			print(p['Name'], p['Age'],p['Score'])
			#			record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
			#			scdb += [record]
			#		count += 1
			#if count > 0 :
			#	print("이미 같은 이름의 학생이 존재합니다.")
			#	print("다른 이름 을 사용하여 다시 해주세요.")

				if len(parse) > 4:
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
					scdb += [record]

			elif parse[0] == 'inc':#3

				if len(parse) > 3:
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					for p in scdb:
						if p['Name'] == parse[1]:
							p['Score'] = str(int(p['Score']) + int(parse[2]))

			elif parse[0] == 'del':#2

				if (len(parse) > 2):
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					for l in range(len(parse)):
						for p in scdb:
							if p['Name'] == parse[1]:
								scdb.remove(p)

			elif parse[0] == 'find':#2

				if len(parse) > 2:
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					for p in scdb:
						if p['Name'] == parse[1]:
							print(p['Name'], p['Age'],p['Score'])

			elif parse[0] == 'show':#1
				if len(parse) > 1:
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					sortKey ='Name' if len(parse) == 1 else parse[1]
					showScoreDB(scdb, sortKey)

			elif parse[0] == 'quit' and len(parse) == 1:#1
				if len(parse) > 1:
					print("불필요한 값도 입력 되었습니다. 확인하고 다시시도하십시오 ")
				else:
					break

			else:
				print("Invalid command: " + parse[0])

		except IndexError:
			print("입력되지않은 값이 존재합니다. 입력 후 다시 시도해주십시오.")
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

