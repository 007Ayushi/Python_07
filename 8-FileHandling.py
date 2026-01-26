""" Files - You all know what are files - any name with an extension is file"""
""" Now that extension can be .py ,.txt , .mp3 etc and when we want to handle 
these files we will use file handling.
"""


"""
File Handling - Means creating , Reading ,Updating and Deleting(CRUD)
operation that we can perform in files.
"""

# a = open(r"C:\Users\411ay\Downloads\fff.txt")
# print(a.read())
# a.close()

#Modes in File Handling- 'r','w','a','x'
# 'r'-Read (default) -File must exist
# 'w'-Write - Creates file or overwrites.
# 'a'-append- adds to the end of file
# 'x'- Create - Create a new file, fails if it exists.

#Default Mode is r- read mode
# r=open("super.txt",'w')

#r.write("Hello This is ayushi and I am writing inside this file")


#close - closes the file which is open , otherwise it will leave the opened file as open.
# r.write("Super.txt has created and the text I am writing has show in the file")
# r.close()

# r=open("super.txt",'a')
# r.write("and now i am appending some content inside the file");
# r.close()


# new_file=open("demo.txt","x")
# new_file.close()

# a=open("demo.txt","x")
# a.close() #FileExistsError: [Errno 17] File exists: 'demo.txt'

