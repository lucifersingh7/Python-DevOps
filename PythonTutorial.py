#write a function to find whether a given number is prime number or not.
import os
import shutil

number = int(input("Enter the number to check : "))

def find_Prime_number(num):
     if (num%2==1) :
          print("The number is a prime number")
     elif (num%2==0) :
          print("Number is a composite number")
     else :
          print("Not a prime number")

find_Prime_number(number)

# program to zip and backup a folder to Desktop

def zip_backup(source,dest):
     file_name=os.path.join(dest,"mybackups")
     shutil.make_archive(file_name,'zip',source)

source = r'C:\Users\admin\Downloads\MyResumes'
dest =r'C:\Users\admin\OneDrive\Desktop\PythonBackup'

zip_backup(source,dest)
