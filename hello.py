#experiment  7: Write a program to demonstrate working with dictionaries in
# #creating a dictionary
student={
    "name":"priya",
    "age":20,
    "curse":"b.tech",
    "marks":88
}
  #printing tthe  whole dictniory 
print("pappu dictinory :",student)
  #accesing the value using keys 
print("/n Name:",student ["name"])
print("age:",student["age"])
   

#adding the new value key valu pair 

student["university"]="gulzar group of insititution"
#updated 
print("/nafter addding 'university':",student)
   

   #updated an exisiting value 
student["marks"]=92 
print("/nAfter updating 'marks':",student)
  
  #remove 
student ["curse"]
print("/nafter removing 'course':",student)

#lterating through dictionary keys and valuess 
print("/nAll key value pairs:")

for key, value in student .items ():
     print (key,":",value)