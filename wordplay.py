'''
	words_with_length(length) — returns a list of all the words of length length
	starts_with(char1) — returns a list of all the words that start with char1
	ends_with(char2) — returns a list of all the words that end with char2
	palindromes() — returns a list of all the palindromes in the list
	only(str1) — returns a list of the words that contain only those letters in str1
	avoids(str2) — returns a list of the words that contain none of the letters in str2
'''
class Wordplay:
    def __init__(self,l):
        self.word_list=l
    def words_with_length(self,n):
        wl=[]
        for i in self.word_list:
            if len(i)==n:
                wl.append(i)
        print(wl)
    def starts_with(self,s):
        wl=[]
        for i in self.word_list:
            if i[0]==s:
                wl.append(i)
        print(wl)
    def ends_with(self,e):
        wl=[]
        for i in self.word_list:
            if i[-1]==e:
                wl.append(i)
        print(wl)
    def palindrome(self):
        wl=[]
        for i in self.word_list:
            if i==i[::-1]:
                wl.append(i)
        print(wl)
    def only(self,o):
        a=set(o)
        wl=[]
        for i in self.word_list:
            if set(i)==a:
                wl.append(i)
        print(wl)
    def avoids(self,a):
        b=set(a)
        wl=[]
        for i in self.word_list:
            if set(i).intersection(b)==set():
                wl.append(i)
             
        print(wl)

a=Wordplay(['apple', 'banana', 'find', 'dictionary', 'set', 
            'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot'])

a.words_with_length(5)
a.starts_with("a")
a.ends_with("d")
a.only("bna")
a.palindrome()
a.avoids("amkd")