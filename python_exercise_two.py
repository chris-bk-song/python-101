# Step 0: Document the problem
# Prompt user to input their name and print out welcome mesage with their name

# Step 1: Setup/Configuration
name = input('What is your name? ')
name_length = len(name)

# Step 2: Result/Output
greeting = f'Welcome, {name.upper()}! \n YOUR NAME HAS {name_length} LETTERS IN IT! AWESOME!' 

# Step 3: Do the work
print(greeting)