def to_upper(s):
  print("UPPERCASE IS :",s.upper())


def to_lower(s):
  print("LOWERCASE IS:",s.lower())


def to_title(s):
  print("TITLECASE IS :",s.title())


def reverse_str(s):
  print("REVERSED STRING IS",s[::-1])


def count_chars(s):
  print("NO OF CHARACTER ARE:",len(s))


def count_words(s):
  print("NO OF WORDS ARE:",len(s.split()))


def count_vowels(s):
  vowels = "aeiouAEIOU"
  count = 0
  for ch in s:
    if ch in vowels:
      count += 1
  print("NO OF VOWELS ARE:",count)

def ch_alpha(s):
  print("Is Alphabet Only:", s.isalpha())


def ch_lower(s):
  print("Is All Lowercase:", s.islower())


def ch_upper(s):
  print("Is All Uppercase:", s.isupper())


def che_digit(s):
  print("Is Digits Only:", s.isdigit())


def ch_alnum(s):
  print("Is Alphanumeric:", s.isalnum())


def ch_space(s):
  print("Is space Only:", s.isspace())

def do_strip(s):
  print("Stripped:", s.strip())
