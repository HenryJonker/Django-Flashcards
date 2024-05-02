from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})

def add(request):
	from random import randint

	num_1 = randint(0,10) 
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1= request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']

		if not answer:
			my_answer = "Hey you forgot to fill in the form"
			return render(request,'divide.html',{
				'my_answer':my_answer,
				'answer':answer,
				'num_1':num_1,
				'num_2':num_2,
				})

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer)==correct_answer:
			my_answer="Correct! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_answer)
			color='warning'
		else : 
			my_answer = "Incorrect " + old_num_1 + " + " + old_num_2 + " is not " + str(answer)
			color='success'

		return render(request,'add.html',{
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	return render(request,'add.html',{
		'num_1':num_1,
		'num_2':num_2,
		})

def subtract(request):
	from random import randint

	num_1 = randint(0,10) 
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1= request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']

		if not answer:
			my_answer = "Hey you forgot to fill in the form"
			return render(request,'divide.html',{
				'my_answer':my_answer,
				'answer':answer,
				'num_1':num_1,
				'num_2':num_2,
				})

		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer)==correct_answer:
			my_answer="Correct! " + old_num_1 + " - " + old_num_2 + " = " + str(correct_answer)
			color='warning'
		else : 
			my_answer = "Incorrect " + old_num_1 + " - " + old_num_2 + " is not " + str(answer)
			color='success'

		return render(request,'subtract.html',{
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	return render(request,'subtract.html',{
		'num_1':num_1,
		'num_2':num_2,
		})
	

def multiply(request):
	from random import randint

	num_1 = randint(0,10) 
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1= request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']

		if not answer:
			my_answer = "Hey you forgot to fill in the form"
			return render(request,'divide.html',{
				'my_answer':my_answer,
				'answer':answer,
				'num_1':num_1,
				'num_2':num_2,
				})

		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer)==correct_answer:
			my_answer="Correct! " + old_num_1 + " * " + old_num_2 + " = " + str(correct_answer)
			color='warning'
		else : 
			my_answer = "Incorrect hallo " + old_num_1 + " * " + old_num_2 + " is not " + str(answer)
			color='success'

		return render(request,'multiply.html',{
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	return render(request,'multiply.html',{
		'num_1':num_1,
		'num_2':num_2,
		})
	

def divide(request):
	from random import randint

	num_1 = randint(0,10) 
	num_2 = randint(0,10)




	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1= request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']

		if not answer:
			my_answer = "Hey you forgot to fill in the form"
			return render(request,'divide.html',{
				'my_answer':my_answer,
				'answer':answer,
				'num_1':num_1,
				'num_2':num_2,
				})


		correct_answer = int(old_num_1) / int(old_num_2)
		if int(answer)==correct_answer:
			my_answer="Correct! " + old_num_1 + " / " + old_num_2 + " = " + str(correct_answer)
			color='warning'
		else : 
			my_answer = "Incorrect hallo " + old_num_1 + " / " + old_num_2 + " is not " + str(answer)
			color='success'

		return render(request,'divide.html',{
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	return render(request,'divide.html',{
		'num_1':num_1,
		'num_2':num_2,
		})



# Create your views here.
