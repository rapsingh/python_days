#Sample Input 1 : Welcome to Coding Ninjas

#Sample Output 1: Ninjas Coding to Welcome


def reverseString(str: str) -> str:
    words=[]
    words=str.split()
    l=len(words)
    new_word=[]
    for word in words:
        new_word.insert(0,word)
    my_string=' '.join(new_word)
    return my_string

