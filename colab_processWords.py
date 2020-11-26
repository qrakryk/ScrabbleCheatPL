#@title Podaj litery
letters = 'aoec?'#@param
letters = list(letters)
numLetters = len(letters)
z = 0
yourWords = []
while z < numLetters-1:
  groupNumber = numLetters-z
  current_group = words_groups.get_group(groupNumber)
  i = 0
  while i < len(current_group):
    n = 0
    for letter in letters:
      if letter == '?':
        n = n + 1
      decide = current_group['Word'].iloc[i].find(letter)
      if decide >= 0:
        n=n+1
      if n == numLetters-z:
        yourWords.append(current_group['Word'].iloc[i])
    i=i+1
  z=z+1

yourWordsFrame = pd.DataFrame()
yourWordsFrame['Words'] = yourWords
yourWordsFrame['CharLen'] =  yourWordsFrame['Words'].str.len()
yourWordsFrame
