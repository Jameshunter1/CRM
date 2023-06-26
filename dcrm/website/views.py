from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Home view
def home(request):
	# Get all records
	records = Record.objects.all()
	
	# Check if user is trying to log in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		# Authenticate user
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			# Log in user
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		# Render home template with records
		return render(request, 'home.html', {'records': records})

# Logout view
def logout_user(request):
	# Log out user
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

# User registration view
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			# Save form data
			form.save()
			
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		
	return render(request, 'register.html', {'form': form})

# Customer record view
def customer_record(request, pk): 
	if request.user.is_authenticated:
		# Look up record
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record': customer_record})
	else:
		messages.success(request, "You must be Logged In to view this page")
		return redirect('home')

# Delete record view
def delete_record(request, pk):
	if request.user.is_authenticated:
		# Get record to delete
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

# Add record view
def add_record(request):
	form = AddRecordForm(request.POST or None)
	
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				# Save new record
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form': form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

# Update record view
def update_record(request, pk):
	if request.user.is_authenticated:
		# Get current record to update
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		
		if form.is_valid():
			# Save updated record
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form': form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
