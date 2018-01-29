

#Jennifer Gilbert - Homework 1
#1/21/18
#Q1 part 1
print("Question 1")
y1 = 17
y2 = 17.0
y3 = "17"
y4 = y2<18
print(y1)
print(y2)
print(y3)
print(y4)
print(type(y1))
print(type(y2))
print(type(y3))
print(type(y4))

#Q1 part 2
text = "The value of x is " + y3+"."
print(text)

#Q2
print("\nQuestion 2")
text1 = "I"
text2 = "love"
text3 = "learning"
text4 = "how"
text5 = "to"
text6 = "code"
text7 = "!"
text = text1 +" "+ text2 +" "+ text3 +" "+ text4 +" "+ text5 +" "+ text6 +text7
print(text)

#Q3 part 1
print("\nQuestion 3")
#iterative function
n = int(input("Type a value for n for this ITERATIVE FUNCTION (hint - pick 100 for this assignment)... "))

def iterative(q):
	mysum = 0
	for i in range(1,q+1):
		mysum += i
	return(mysum)

print(iterative(n))

#recursive function
n = int(input("Type a value for n for this RECURSIVE FUNCTION (hint - pick 100 for this assignment)... "))

i=1
def recursive(q):
	if q==0:
		return 0
	else:
		return q + recursive(q-1)
		
print(recursive(n))


#Q4
print("\nQuestion 4")
yours = ["Yale","MIT","Berkeley"]
mine =["Boston University", "Yale", "Bunker Hill Community College"]
ours1 = yours + mine
ours2 = []
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)
print("The ours1 list is different than the ours2 list because the ours1 list joins our two lists together, while the ours2 list provides a list of the two lists instead of joining them together.")
yours[1]="Virginia Commonwealth University"
print(ours1)
print(ours2)
print("The ours1 list did not change because we did not redefine it after changing the second element of the list, so the ours1 list is still saved with MIT. For the ours2 element, it uses a list of the lists and therefore recalls the new value for the 'yours list', including it in the output.")

#Q5
print("\nQuestion 5")
months = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12, '1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
print("The sixth month is " + str(months['6']))
print("February is month " + str(months['February']))
