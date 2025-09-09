# Lesson 3: Variables - Your Code's Memory! 🧠

## 🎯 Today's Mission
Learn how to store and use information in your programs with variables!

---

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<img src="https://via.placeholder.com/60x60/4CAF50/FFFFFF?text=👩‍💻" alt="Instructor">
<strong>Dr. Pythonia:</strong><br>
"Today we're learning about variables - they're like labeled containers that store information! In my professional work building enterprise systems, variables store everything from user names to complex business data. Think of them as your program's memory!"
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<img src="https://via.placeholder.com/60x60/2196F3/FFFFFF?text=👦" alt="Student">
<strong>Jordan:</strong><br>
"So variables are like backpacks for my data? Can I put anything in them? What happens if I forget what I stored? Can I change what's inside?"
</div>

</div>

---

## 🎒 Understanding Variables: The Digital Backpack

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia explains:</strong><br>
"Perfect analogy! Variables ARE like backpacks. Each has a name (like writing 'MATH' on your backpack) and can hold different things. You can look inside, change contents, or even empty them completely. Python keeps track of everything for you!"
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan discovers:</strong><br>
"Oh! So `player_name = 'Jordan'` is like putting a name tag with 'Jordan' inside a backpack labeled 'player_name'? And I can change it later?"
</div>

</div>

### Variable Types - Different Containers for Different Things

**Text Variables (Strings) 📝**
```python
# Like a label maker - stores words and sentences
player_name = "Jordan"
favorite_color = "Blue"
game_title = "Super Adventure Quest"

print(f"Hello, {player_name}!")
print(f"Your favorite color is {favorite_color}")
```

**Number Variables (Integers) 🔢**
```python
# Like a calculator memory - stores whole numbers
player_age = 11
lives = 3
high_score = 1500

print(f"You are {player_age} years old")
print(f"Lives remaining: {lives}")
```

**Decimal Numbers (Floats) 📊**
```python
# Like a precise scale - stores decimal numbers
player_height = 4.5
temperature = 72.8
game_version = 2.1

print(f"You are {player_height} feet tall")
```

**True/False Values (Booleans) ✅**
```python
# Like a light switch - only True or False
game_over = False
has_key = True
is_winner = False

if has_key:
    print("You can open the door!")
```

---

## 🎮 Activity 1: Build a Player Profile

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's project:</strong><br>
"Let's create a complete player profile system! This is similar to how video games store player information. We'll use different variable types to hold different kinds of data about our character."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's character idea:</strong><br>
"I want to make a space explorer character! Can I store their spaceship name, how many planets they've visited, and whether they've found alien life?"
</div>

</div>

### Step-by-Step Character Creation:

```python
# Character Information (Strings)
character_name = "Captain Nova"
spaceship_name = "Stellar Explorer"
home_planet = "Earth"

# Character Stats (Numbers)
age = 25
planets_visited = 12
alien_encounters = 3
fuel_level = 87.5

# Character Status (Booleans)
has_spacesuit = True
found_alien_life = False
mission_complete = False

# Display Character Profile
print("🚀 SPACE EXPLORER PROFILE 🚀")
print("=" * 30)
print(f"Name: {character_name}")
print(f"Spaceship: {spaceship_name}")
print(f"Home: {home_planet}")
print(f"Age: {age} years")
print(f"Planets Visited: {planets_visited}")
print(f"Alien Encounters: {alien_encounters}")
print(f"Fuel Level: {fuel_level}%")
print(f"Has Spacesuit: {has_spacesuit}")
print(f"Found Alien Life: {found_alien_life}")
print(f"Mission Complete: {mission_complete}")
```

**Your Turn!** Create your own character profile:
- Choose a character type (superhero, wizard, athlete, detective)
- Use at least 5 different variables
- Include text, numbers, and true/false values
- Display it nicely with print statements

---

## 🔄 Activity 2: Changing Variables During the Game

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia reveals:</strong><br>
"The real power of variables is changing them! In games, your score increases, health decreases, and levels advance. Let's simulate a mini-adventure where variables change based on player actions."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan gets excited:</strong><br>
"So I can make my character's stats change as the story goes on? Like gaining experience points or finding treasure?"
</div>

</div>

### Interactive Adventure Simulator:

```python
# Starting Stats
hero_name = input("Enter your hero's name: ")
health = 100
gold = 50
experience = 0
level = 1
has_sword = False

print(f"\nWelcome, {hero_name}! Your adventure begins...")
print(f"Health: {health} | Gold: {gold} | Level: {level}")

# Adventure Scene 1: Find a treasure chest
print("\n🗃️ You found a treasure chest!")
gold = gold + 25  # Add gold
experience = experience + 10  # Gain experience
print(f"You gained 25 gold and 10 experience!")
print(f"New totals - Gold: {gold}, Experience: {experience}")

# Adventure Scene 2: Battle a monster
print("\n👹 A monster appears!")
health = health - 30  # Take damage
experience = experience + 20  # Battle experience
print(f"You fought bravely but lost 30 health and gained 20 experience!")
print(f"Health: {health}, Experience: {experience}")

# Adventure Scene 3: Find a weapon
print("\n⚔️ You discovered a magical sword!")
has_sword = True
print(f"Sword equipped: {has_sword}")

# Check for level up
if experience >= 25:
    level = level + 1
    health = 100  # Full health restore
    print(f"\n🎉 LEVEL UP! You are now level {level}!")
    print(f"Health restored to {health}")

# Final Status
print(f"\n📊 FINAL STATS FOR {hero_name.upper()}")
print(f"Level: {level}")
print(f"Health: {health}")
print(f"Gold: {gold}")
print(f"Experience: {experience}")
print(f"Has Sword: {has_sword}")
```

---

## 🧮 Activity 3: Variable Math & Operations

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia teaches:</strong><br>
"Variables can do math! In my enterprise software, we calculate totals, averages, and percentages all the time. Let's explore how Python handles mathematical operations with variables."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan wonders:</strong><br>
"Can I make a calculator with variables? Or maybe figure out batting averages for my baseball team? What about calculating how much allowance I'll have after saving?"
</div>

</div>

### Math Operations with Variables:

```python
# Basic Math Operations
a = 15
b = 4

print("🧮 VARIABLE MATH PLAYGROUND")
print(f"a = {a}, b = {b}")
print()

# Addition
sum_result = a + b
print(f"{a} + {b} = {sum_result}")

# Subtraction  
difference = a - b
print(f"{a} - {b} = {difference}")

# Multiplication
product = a * b
print(f"{a} × {b} = {product}")

# Division
quotient = a / b
print(f"{a} ÷ {b} = {quotient}")

# Remainder (Modulo)
remainder = a % b
print(f"{a} mod {b} = {remainder}")

# Exponentiation (Powers)
power = a ** 2
print(f"{a} squared = {power}")
```

### Real-World Application: Grade Calculator

```python
# Grade Calculator
print("📚 GRADE CALCULATOR")
student_name = input("Enter student name: ")

# Get test scores
test1 = float(input("Enter test 1 score: "))
test2 = float(input("Enter test 2 score: "))
test3 = float(input("Enter test 3 score: "))

# Calculate average
total_points = test1 + test2 + test3
average = total_points / 3

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print(f"\n📊 RESULTS FOR {student_name.upper()}")
print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
print(f"Total Points: {total_points}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter_grade}")
```

---

## 🎯 Challenge Activities

### Challenge 1: Variable Guessing Game

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's challenge:</strong><br>
"Create a guessing game where the computer picks a secret number and the player tries to guess it. Use variables to track the secret number, the guess, and the number of attempts!"
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's approach:</strong><br>
"I'll need variables for the secret number, the player's guess, and how many tries they've used. Maybe I can add hints like 'too high' or 'too low'!"
</div>

</div>

```python
import random

# Game Setup
secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5
game_won = False

print("🎯 NUMBER GUESSING GAME")
print(f"I'm thinking of a number between 1 and 20")
print(f"You have {max_attempts} attempts to guess it!")

# Game Loop
while attempts < max_attempts and not game_won:
    guess = int(input("\nEnter your guess: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        game_won = True
        print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts!")
    elif guess < secret_number:
        print("📈 Too low!")
    else:
        print("📉 Too high!")
    
    remaining = max_attempts - attempts
    if remaining > 0 and not game_won:
        print(f"Attempts remaining: {remaining}")

if not game_won:
    print(f"\n💔 Game Over! The number was {secret_number}")
```

### Challenge 2: Personal Finance Tracker

Create a simple allowance and spending tracker:

```python
# Personal Finance Tracker
print("💰 ALLOWANCE TRACKER")

# Starting values
total_allowance = float(input("Enter your weekly allowance: $"))
weeks_saved = int(input("How many weeks have you been saving? "))

# Calculate savings
current_savings = total_allowance * weeks_saved

print(f"\nYour current savings: ${current_savings:.2f}")

# Track a purchase
purchase = float(input("Enter amount you want to spend: $"))

if purchase <= current_savings:
    remaining = current_savings - purchase
    print(f"✅ You can afford this!")
    print(f"Remaining after purchase: ${remaining:.2f}")
else:
    needed = purchase - current_savings
    weeks_needed = needed / total_allowance
    print(f"❌ Not enough money yet!")
    print(f"You need ${needed:.2f} more")
    print(f"Save for {weeks_needed:.1f} more weeks")
```

---

## 🐛 Common Variable Mistakes & Debugging

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's debugging wisdom:</strong><br>
"Everyone makes variable mistakes - even professional programmers! The key is learning to spot and fix them. Common errors include typos in variable names, using variables before defining them, and mixing up data types."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's debugging experience:</strong><br>
"I keep typing 'plyer_name' instead of 'player_name' and getting errors! And sometimes I forget if I stored a number or text in my variable."
</div>

</div>

### Common Errors and Solutions:

**Error 1: Undefined Variable**
```python
# ❌ WRONG - using before defining
print(player_name)
player_name = "Jordan"

# ✅ CORRECT - define before using
player_name = "Jordan"
print(player_name)
```

**Error 2: Case Sensitivity**
```python
# ❌ WRONG - different cases
Player_Name = "Jordan"
print(player_name)  # Error! Undefined

# ✅ CORRECT - consistent case
player_name = "Jordan" 
print(player_name)
```

**Error 3: Data Type Mixing**
```python
# ❌ WRONG - adding text to number
score = 100
message = "Your score is " + score  # Error!

# ✅ CORRECT - convert or use f-strings
score = 100
message = f"Your score is {score}"
# or
message = "Your score is " + str(score)
```

---

## 🏆 Mastery Checklist

Check off what you've mastered:

### Basic Understanding:
- [ ] I know what variables are (containers for data)
- [ ] I can create variables with meaningful names
- [ ] I understand different data types (text, numbers, true/false)
- [ ] I can display variable contents with print()

### Practical Skills:
- [ ] I can change variable values during program execution
- [ ] I can perform math operations with number variables
- [ ] I can get user input and store it in variables
- [ ] I can use variables in if statements for decisions

### Advanced Applications:
- [ ] I can build programs with multiple related variables
- [ ] I can debug common variable errors
- [ ] I can plan which variables I need before coding
- [ ] I can explain variables to someone else

---

## 🏠 Take Home Projects

### Project 1: Family Member Profiles
Create profiles for your family members using variables:
- Name, age, favorite food, hobby
- Calculate total family age
- Display everyone's information nicely

### Project 2: Sports Statistics
Track statistics for your favorite sport:
- Games played, wins, losses
- Calculate win percentage
- Track improvement over time

### Project 3: Dream Vacation Calculator
Plan a vacation with variables:
- Destination, cost per day, number of days
- Calculate total cost
- Figure out how long to save allowance

---

## 🔮 Next Lesson Preview

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia teases:</strong><br>
"Next time, we'll learn about functions - your own custom commands! Functions let you create reusable blocks of code, just like creating your own custom LEGO pieces that you can use over and over."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan anticipates:</strong><br>
"So I can create my own commands like 'level_up()' or 'calculate_score()'? That sounds like creating my own magic spells for programming!"
</div>

</div>

---

**Excellent work today! You now have the power to give your programs memory! 🧠✨**