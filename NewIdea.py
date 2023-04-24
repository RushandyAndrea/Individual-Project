import tkinter as tk
import random
from PIL import ImageTk, Image

# Define the types of light aircraft to identify
aircraft_types = ['Acro Sport', 'GA-7 Cougar', 'DA-2', 'GB1 GameBird', 'Glasair 3', 'LearJet', 'Merlin', 'Phenom 100',
                  'Sportsman', 'Super Viking']

# Define the number of questions to ask in the drill
num_questions = 10

# Define a dictionary to store the correct answers
correct_answers = {}


# Define a function to generate a random aircraft and perspective
def generate_question():
    aircraft = random.choice(aircraft_types)
    return aircraft


# Define a function to display the question
def display_question():
    global current_question
    aircraft = generate_question()
    current_question = aircraft
    question_text.set(f"What type of aircraft is this?")
    image_filename = f"{aircraft}.jpg"
    image = Image.open(image_filename)
    image = image.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    answer_entry.delete(0, tk.END)  # clear the answer entry widget


# Define a function to check the answer
def check_answer():
    global num_correct
    global num_asked
    aircraft = current_question
    answer = answer_entry.get().strip()
    if answer.lower() == aircraft.lower():
        result_text.set("Correct!")
        num_correct += 1
        answer_entry.delete(0, tk.END)  # clear the answer entry widget
        if num_asked < num_questions:
            next_button.pack_forget()  # hide the "Next" button
            display_question()
        else:
            result = f"You got {num_correct} out of {num_questions} correct!"
            accuracy_text.set(result)
            check_button.config(state=tk.DISABLED)  # disable the "Check" button
    else:
        result_text.set(f"Incorrect. That is a {aircraft}.")
    num_asked += 1
    accuracy_text.set(f"Accuracy: {num_correct}/{num_asked}")
    answer_entry.delete(0, tk.END)  # clear the answer entry widget


# Define the main window
root = tk.Tk()
root.title("Aircraft Identification Drill")

# Define the question frame
question_frame = tk.Frame(root)
question_frame.pack(pady=10)

question_text = tk.StringVar()
question_label = tk.Label(question_frame, textvariable=question_text, font=('Arial', 14))
question_label.pack()

image_label = tk.Label(question_frame)
image_label.pack(pady=10)

# Define the answer frame
answer_frame = tk.Frame(root)
answer_frame.pack(pady=10)

answer_label = tk.Label(answer_frame, text="Your answer:", font=('Arial', 14))
answer_label.pack(side=tk.LEFT)

answer_entry = tk.Entry(answer_frame, font=('Arial', 14))
answer_entry.pack(side=tk.LEFT)

check_button = tk.Button(answer_frame, text="Check", font=('Arial', 14), command=check_answer)
check_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(answer_frame, text="Next", font=('Arial', 14), command=display_question)
next_button.pack(side=tk.LEFT, padx=10)

result_text = tk.StringVar()
result_label
