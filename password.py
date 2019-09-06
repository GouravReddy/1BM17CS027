import string
from random import sample,choice
length=8
char=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
var=''
password=var.join(sample(char,length))
#var.join[choice(char) for i in range(length)]
print(password)
