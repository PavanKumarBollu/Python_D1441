# value = "hydearabad Accenture"

# value = "ANP-D1441"
#
# file_write = open("output.txt","w")
# file_write.write(value)
#
# file_write_different_loc = open("C:\\Users\\bpava\\Desktop\\output.txt","w")
#
# file_write_different_loc.write(value)

name = "PK\n"
age = "45\n"
gender = "M"
phone_no = "1234567890\n"
gmail = "PK@gmail.com\n"


file_write_multiline = open("multiOutput.txt", "a")

file_write_multiline.write(name)
file_write_multiline.write(age)
file_write_multiline.write(gender)
file_write_multiline.write(phone_no)
file_write_multiline.write(gmail)

"""
python open() function will provides the support to work with the following file types
.txt plain text files
.csv comma separated values
.tsv tab separated values
.json java script object notation
.xml extendable markup language
.html hypertext markup language
.log files that contains the text data only


Binary format files
-------------------
.jpg 
.png
.mp3
.mp4
.pdf
.word
.zip
.pptx


other files
-----------
.css
.html
.py
.md 
.... etc


"""

"""
r - read the file
rb - read file in binary format
r+ - read and write the file
rb + - read and write the file in binary format
w - write the file
wb - write the file in binary format
w+ - write and read and write the file
wb+ - write and read and write the file in binary format
a - open the file in append mood and the pointer exits at the last line of the file
ab - open the file in append mood and the binary format pointer exists at the last line of the file
a+ - it open a file to append and read  
ab+ it opens a file to append and read in binary format



"""