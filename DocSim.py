import sys,os,re, math
from collections import Counter


def bubblesort(list, doc):
# Swap the elements to arrange in order
    for j in range(len(list)-1, 0, -1):
        for i in range(j):
             if list[i]>list[i+1]:
                temp = list[i]
                temp1 = doc[i]
                list[i] = list[i+1]
                docs[i] = doc [i+1]
                list[i+1] = temp
                doc[i+1] = temp1

def calculate (Nu_Of_Docs):
 for i in range (1, Nu_Of_Docs):
  global k, vector1, vector2, cosine, vector;
  j=Nu_Of_Docs
  while i < j:
   k = k + 1
   vector1 = vector[i]
   vector2 = vector[j]
   docs[k] = " %s  and  %s "  %(temp[i], temp[j])
   #print (docs [k]) #Test
   cosine[k] = get_cosine(vector1, vector2)
   j = j-1

def get_cosine(vec1, vec2):
    keys = set(vec1.keys()) & set(vec2.keys()) #the keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
    num = sum([vec1[x] * vec2[x] for x in keys]) #arithmiths, x is how many times it has occured
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denom = math.sqrt(sum1) * math.sqrt(sum2) #paronomasths
    if not denom:
        return 0.0
    else:
       # print (denom) #Test
        return float(num) / denom

def find_vector(Nu_Of_Docs):
    global vector, text;
    for i in range (1, Nu_Of_Docs+1):
     vector[i] = split_text(text[i])

def split_text(text):
     words = WORD.findall(text) # or words = re.split( r'\W+',text)
     #print (Counter(words)) #Test
     return Counter(words)

#I am compiling a regular expression, then using it to search for text that matches that regular expression.
#compile a regular expression pattern into a regular expression object, which can be used for matching using findall
#the "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
#WORD = re.compile(r'^[a-zA-Z]+')

def get_NuOfDocs(check):
   global Nu_Of_Docs;
   while (Nu_Of_Docs < 2) and (check==0):
      try:
          Nu_Of_Docs = int(input("Give number of documents: "))  # In case text are blank its 0.0 similarity
          type(Nu_Of_Docs)
          if (Nu_Of_Docs == 0) or (Nu_Of_Docs == 1):
              print ("Wrong Input")
      #print(Nu_Of_Doc) #Test
      except ValueError:
             print("Wrong Input ")
             continue
      else:
             if Nu_Of_Docs >= 2:
                 check=1
                 print("Succeed ")
                 break
             continue

def get_filepath(Nu_Of_Docs):
 for i in range (1, Nu_Of_Docs+1):
    global text;
    text[i] = input('Enter a filepath:\n ')
    while (os.path.exists(text[i]) == False):
     print("Wrong Path ")
     #assert os.path.exists(text[i]), "File not found at, " + str(text[i]) # to stop program
     text[i] = input('Enter a filepath:\n ')
    f = open(text[i], 'r+')
    print("Succeed ")
    f.close()
    type(text[i])
    temp[i]= text[i]
    text[i] = open(text[i], 'r').read().lower() # make all letters lowercase, because we want uppercase to be similar with lowercase letters
   # print (text[i]) #Test

def get_top_k(check):
 global limit, top_k;
 while (top_k < 1) | (check == 0 ) | (top_k >limit):
    try:
       top_k = int (input ("Give top k documents: \n"))
       type(top_k)
    except ValueError:
       print("Wrong Input ")
       continue
    else:
        if top_k >= 1 and top_k <= limit:
            check = 1
            print("Succeed\n ")
            break
        else:
         print("Wrong Input ")

def get_limit(i, Nu_Of_Docs):
 while i < Nu_Of_Docs:
    global limit;
    limit = limit + i
    i=i+1
    #print (limit) #Test

def print_cosine(top_k,k):
 global cosine;
 for j in range (1, top_k+1):
    print('Documents:', docs[k-1], 'are','{:.1%}'.format(cosine[k-1]), 'similar')
    k = k-1


#------------------------------------------------



"""" MAIN """

WORD = re.compile( r'\w+')

#Defines
Nu_Of_Docs=0
check=0
k=0
top_k = 0
limit=0
i=1

docs = list(range(1, 100))
cosine = list(range(2,100)) # we set start range 2 beacause it does one more comparison with an element that does not exist and has 0.00 simularity
temp = list(range(1, 100))
text = list(range(1, 100))
vector = list(range(1, 100))

#start
get_NuOfDocs(check)
get_filepath(Nu_Of_Docs)
find_vector(Nu_Of_Docs)
calculate(Nu_Of_Docs)
get_limit(i, Nu_Of_Docs)
get_top_k(check)
bubblesort(cosine, docs)
print_cosine(top_k, k)

# prev version --> for 1.000002 return --> floating point numbers do wander around a bit in most languages - as they cannot have unlimited precision in digital representations

""" END OF MAIN """

