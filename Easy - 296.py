print(type(3+7))
print(2-1)
print("this is a chunk of text")

a = 20
c = a * 2

if (c<50):
    print(c)
    print("c is less than 50")
else:
    print(c)
    print("c is greater than or = to 50")

print('hello')

### easy DPC

a = ["first", "second", "third", "fourth", "fith", "sixth", "seventh",
     "eighth", "ninth", "tenth", "eleventh", "twelth"]

b = [" Partridge in a Pear Tree",
     " Turtle Doves",
     " French Hens",
     " Calling Birds",
     " Golden Rings",
     " Geese a Laying",
     " Swans a Swimming",
     " Maids a milking",
     " Ladies Dancing",
     " Lords a Leaping",
     " Pipers Piping",
     " Drummers Drumming"]


d = 0

for x in a:
    print("On the " + a[d] + " day of Christmas my true love sent to me:")
    d = d+1
    c = 1
    for i in range(d):
        print(c),b[i]
        c=c+1
    print "\n" 


