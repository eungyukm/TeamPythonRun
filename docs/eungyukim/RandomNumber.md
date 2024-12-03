# TeamPythonRun
This repository is dedicated to learning Python.

## Number Guessing Game
## Description
This is a simple number guessing gmae implemented in Python.
A random number between 1 an 10 is generated, and the player has three attempts to guess the correct number.
The game provides hints ('UP' or 'Down') after each incorrect guess.

## Features
Each 'Person' object includes attributes such as name, gender, age, and a randomly assigned number.
The gmae begins with a description and allows the player three chances to guess the number.
Hints ('UP' or 'DOWN') guide the player towards the correct answer.

## How to Play
1. Run the script in your Python environment.
2. Enter your name, gender, and age to create a 'Person' object.
3. The gmae will start automatically after diplaying the player's information.
4. Try to guess the random number within three attempts.

## Source Code
````python
import random
# 1 ~ 10까지 랜덤한 숫자를 추출하는 함수
def RandomNumber():
    return random.randint(1, 10)

class Person:
    name = ""
    gender = ""
    age = 0
    randomNum = 0

    def __init__(self, in_name, in_gender, in_age, in_randomNum):
        self.name = in_name
        self.gender = in_gender
        self.age = in_age
        self.randomNum = in_randomNum

    def display(self):
        print("====== Person Information ======")
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Age: ", self.age)
        self.displayRandomNumber()

    def displayRandomNumber(self):
        print("Random Number: ", RandomNumber())

    # 게임의 설명 출력
    def print_game_description(self):
        print("====== Game Description ======")
        print("게임은 1 ~ 10 사이의 숫자를 맞추는 게임입니다.")
        print("3번 안에 맞추지 못하면 게임이 종료됩니다.")
        print("===============================")

    # 게임을 실행하는 함수
    def run_game(self):
        self.print_game_description()
        answer = self.randomNum
        for i in range(3):
            guess = int(input("숫자를 입력하세요: "))
            if guess == answer:
                print("정답입니다.")
                break
            elif guess < answer:
                print("UP")
            elif guess > answer:
                print("DOWN")
        print("게임이 종료되었습니다.")

# 나이, 이름, 성별을 입력받아 Person 객체를 생성하는 함수
def CreatePerson():
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    random_number = RandomNumber()

    person = Person(name, gender, age, random_number)
    return person

# Person 객체를 생성하고 출력하는 함수
person = CreatePerson()
person.display()
person.run_game()
````
