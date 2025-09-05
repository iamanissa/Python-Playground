# Splitting a string
gettysburg_address = """
   Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
"""

print(len(gettysburg_address.split()))

##### With simple text make a dictionary
# sample_text = " a b c A a b"

# word_count = {}

# for word in sample_text.lower().split():
#   if word in word_count:
#     word_count[word] += 1
#   else:
#     word_count[word] = 1

# print(word_count) #--> {'a': 3, 'b': 2, 'c': 1}


##### Now use longer text to do the same
word_count = {}

for word in gettysburg_address.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)
# {'four': 1, 'score': 1, 'and': 6, 'seven': 1, 'years': 1, 'ago': 1, 'our': 2, 'fathers': 1, 'brought': 1, 'forth': 1, 'on': 2, 'this': 3, 'continent,': 1, 'a': 7, 'new': 2, 'nation,': 3, 'conceived': 2, 'in': 4, 'liberty,': 1, 'dedicated': 3, 'to': 8, 'the': 11, 'proposition': 1, 'that': 13, 'all': 1, 'men': 1, 'are': 3, 'created': 1, 'equal.': 1, 'now': 1, 'we': 10, 'engaged': 1, 'great': 3, 'civil': 1, 'war,': 1, 'testing': 1, 'whether': 1, 'or': 2, 'any': 1, 'nation': 2, 'so': 3, 'dedicated,': 1, 'can': 5, 'long': 2, 'endure.': 1, 'met': 1, 'battle-field': 1, 'of': 5, 'war.': 1, 'have': 5, 'come': 1, 'dedicate': 2, 'portion': 1, 'field,': 1, 'as': 1, 'final': 1, 'resting': 1, 'place': 1, 'for': 5, 'those': 1, 'who': 3, 'here': 5, 'gave': 2, 'their': 1, 'lives': 1, 'might': 1, 'live.': 1, 'it': 4, 'is': 3, 'altogether': 1, 'fitting': 1, 'proper': 1, 'should': 1, 'do': 1, 'this.': 1, 'but,': 1, 'larger': 1, 'sense,': 1, 'not': 5, '--': 7, 'consecrate': 1, 'hallow': 1, 'ground.': 1, 'brave': 1, 'men,': 1, 'living': 1, 'dead,': 1, 'struggled': 1, 'here,': 2, 'consecrated': 1, 'it,': 1, 'far': 2, 'above': 1, 'poor': 1, 'power': 1, 'add': 1, 'detract.': 1, 'world': 1, 'will': 1, 'little': 1, 'note,': 1, 'nor': 1, 'remember': 1, 'what': 2, 'say': 1, 'but': 1, 'never': 1, 'forget': 1, 'they': 3, 'did': 1, 'here.': 1, 'us': 3, 'living,': 1, 'rather,': 1, 'be': 2, 'unfinished': 1, 'work': 1, 'which': 2, 'fought': 1, 'thus': 1, 'nobly': 1, 'advanced.': 1, 'rather': 1, 'task': 1, 'remaining': 1, 'before': 1, 'from': 2, 'these': 2, 'honored': 1, 'dead': 2, 'take': 1, 'increased': 1, 'devotion': 2, 'cause': 1, 'last': 1, 'full': 1, 'measure': 1, 'highly': 1, 'resolve': 1, 'shall': 3, 'died': 1, 'vain': 1, 'under': 1, 'god,': 1, 'birth': 1, 'freedom': 1, 'government': 1, 'people,': 3, 'by': 1, 'perish': 1, 'earth.': 1}
