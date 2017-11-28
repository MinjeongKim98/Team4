#import word

class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.guessWord = ''
        self.blank = '_ '*len(self.secretWord)



    def display(self):
        print('Current: '+ str(self.blank))
        print("Tries: " + str(self.numTries))
        print("Already used: " + str(self.guessedChars))


    def guess(self, character): #True or False return
        if character in self.secretWord:
            self.guessWord += character
            self.blank = self.blank[:self.secretWord.index(character)*2] + character + self.blank[self.secretWord.index(character)*2+1:]
            #break

        else:
            self.guessedChars.append(character)
            self.numTries += 1
        if self.guessWord != self.secretWord:
            self.currentStatus = False
            return self.currentStatus
        else:
            self.currentStatus = True
            return self.currentStatus
