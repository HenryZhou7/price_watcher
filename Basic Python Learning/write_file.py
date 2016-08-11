
#writing the files

text_file = open("text.txt", "w")

hello = "www.amazon.com"
num = 100.3

text_file.write("%s %f\n" % (hello, num))

hello = "www.nike.ca"
num = 34.23
text_file.write("%s %f\n" % (hello, num))


text_file.close()

#Read from a file

with open("text.txt") as f:
    content = f.readlines()
    
total_commodity = len(content)

for x in range(0, total_commodity):
    the_word = content[x].split()
    print the_word[0]
    print the_word[1]
    
    
#convert a string to a floating point

value = float(the_word[1])
value = value * 10
print value

