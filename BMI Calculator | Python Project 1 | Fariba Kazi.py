#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator (PROJECT)

# In[ ]:


weight = input()


# In[2]:


weight = input("Enter your weight in pounds: ")


# In[3]:


print(weight)


# In[4]:


weight = input("Enter your weight in pounds: ")

height = input("Enter your height in inches: ")



# In[5]:


weight = input("Enter your weight in pounds: ")

height = input("Enter your height in inches: ")

BMI = (weight * 703) / (height * height)


# In[6]:


type(height)


# In[7]:


weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)


# In[8]:


weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)


# In[ ]:


# BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[9]:


if BMI>0: 
    if (BMI<18.5):
        print("You are underweight.")
    else:
        print("Enter valid inputs")


# In[11]:


if BMI>0: 
    if (BMI<=18.5):
        print("You are underweight.")
    elif (BMI<=24.9):
        print("You are normal weight.")
    elif (BMI<=29.9):
        print("You are overweight.")
    else:
        print("Enter valid inputs")


# In[12]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)


# In[15]:


if BMI>0: 
    if (BMI<=18.5):
        print(name + ", you are underweight.")
    elif (BMI<=24.9):
        print(name + ", you are normal weight.")
    elif (BMI<=29.9):
        print(name + ", you are overweight.")
    elif (BMI<=34.9):
        print(name + ", you are obese.")
    elif (BMI<=39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese")


# In[ ]:


if BMI>0: 
    if (BMI<=18.5):
        print(name + ", you are underweight.")
    elif (BMI<=24.9):
        print(name + ", you are normal weight.")
    elif (BMI<=29.9):
        print(name + ", you are overweight.")
    elif (BMI<=34.9):
        print(name + ", you are obese.")
    elif (BMI<=39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese")
else:
    print("Enter valid input")


# In[16]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0: 
    if (BMI<=18.5):
        print(name + ", you are underweight.")
    elif (BMI<=24.9):
        print(name + ", you are normal weight.")
    elif (BMI<=29.9):
        print(name + ", you are overweight.")
    elif (BMI<=34.9):
        print(name + ", you are obese.")
    elif (BMI<=39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese")
else:
    print("Enter valid input")


# In[18]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0: 
    if (BMI<=18.5):
        print(name + ", you are underweight.")
    elif (BMI<=24.9):
        print(name + ", you are normal weight.")
    elif (BMI<=29.9):
        print(name + ", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif (BMI<=34.9):
        print(name + ", you are obese.")
    elif (BMI<=39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese")
else:
    print("Enter valid input")

