import tkinter as tk
from tkfontchooser import Font
import random
from datetime import datetime
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry('800x500')
root.configure(bg = 'black')
wel_label = tk.Label(root, text="Typing Speed Test",bg='black', fg='maroon1', font=Font(family='Arial', size=32, weight='bold'))
wel_label.pack()

text_entry = tk.Entry()
selected_text = ""
is_pressed = 0
text_label = tk.Label()
start_time = 0
end_time = 0
result_label = tk.Label(root)
reset_btn = tk.Button(root)
correct_letter_count = 0

text_font = Font(family='Arial', size=16, weight='bold')
text1 = "He found himself sitting at his computer, typing whatever came to mind."
text2 = "This site tested how fast you were at typing. So he typed."
text3 = "He was currently typing about himself typing, which is odd in a way."
text4 = "He was now describing about how he was typing about himself typing."


def show():
    global selected_text, text_label, text_entry
    text_list = [text1, text2, text3, text4]
    selected_text = text_list[random.randint(0,3)]
    text_label = tk.Label(root, text=selected_text, bg='black', fg='gold', font=text_font, borderwidth=30)
    text_label.pack()

    text_entry = tk.Entry(root, borderwidth=3, justify='center',bg='black', fg='peach puff', font=Font(family='Verdana',
                                                                                                       size=12), width=65)
    text_entry.pack()
    text_entry.focus()

show()
start_time = datetime.now()

def reset():
    global text_entry, result_label, reset_btn, text_label, is_pressed, start_time
    is_pressed = 0
    text_entry.configure(state="normal")
    text_entry.pack_forget()
    result_label.pack_forget()
    reset_btn.pack_forget()
    text_label.pack_forget()
    show()
    start_time = datetime.now()


def show_result(event):
    global text_entry, correct_letter_count, result_label, reset_btn, selected_text, is_pressed, start_time, end_time
    if is_pressed == 0:
        is_pressed = 1
        end_time = datetime.now()
        delta = end_time - start_time
        elapsed_time = delta.total_seconds()
        elapsed_time = "%.2f" % elapsed_time
        correct_letter_list = []
        entered_letter_list = []
        text_entry.configure(state = "disabled")
        for correct_letter in selected_text:
            correct_letter_list.append(correct_letter)
        for entered_letter in text_entry.get():
            entered_letter_list.append(entered_letter)
        length_of_correct_list = len(correct_letter_list)
        length_of_entered_list = len(entered_letter_list)
        count = 0
        correct_letter_count = 0
        try:
            while count < length_of_correct_list:
                if correct_letter_list[count] == entered_letter_list[count]:
                    correct_letter_count += 1
                count += 1
        except IndexError:
            pass
        accuracy = correct_letter_count/length_of_correct_list*100
        accuracy = "%.2f" % accuracy
        word_per_min = int(length_of_entered_list/float(elapsed_time)*60)
        result_label = tk.Label(root, borderwidth=10, text=f"Elasped time: {elapsed_time} seconds, Accuracy:{accuracy}%, WPM: {word_per_min}")
        result_label.pack(pady=80)
        result_label.configure(bg="black", fg="cyan2", font=Font(family="Verdana", size=12))
        reset_btn = tk.Button(root, text="Try again!", font=Font(family="New Times Roman", size=12), command=reset)
        reset_btn.pack()


root.bind('<Return>', show_result)


root.mainloop()
