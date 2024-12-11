from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Student info handler")
window.geometry("400x400")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nThe button was clicked")
Students = []
#Save Info
def save_info():
    name = name_entry.get()
    grade = grade_entry.get()
    gender = gender_entry.get()
    mobile = mob_entry.get()
    email = email_entry.get()
    if name and grade and gender and mobile and email:
        student = {"Name" : name, "Grade" : grade, "Gender" : gender, "Mobile" : mobile, "Email" : email}
        Students.append(student)
        messagebox.showinfo("Success", "Information saved successfully!")
        name_entry.delete(0, END)
        grade_entry.delete(0, END)
        gender_entry.delete(0, END)
        mob_entry.delete(0, END)
        email_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")
def show_info():
    if Students:
        info_window = Toplevel(window)
        info_window.title("Student Information")
        info_window.geometry("300x200")
        for idx, student in enumerate(Students , start = 1):
            info = f"{idx}. Name: {student["Name"]}, Grade: {student["Grade"]}, Gender: {student["Gender"]}, Mobile: {student["Mobile"]}, Email: {student["Email"]}"
            Label(info_window, text = info).pack(anchor = "w")

#Input fields and labels
Label(window, text = "Name:").pack()
name_entry = Entry(window)
name_entry.pack()
Label(window, text = "Grade:").pack()
grade_entry = Entry(window)
grade_entry.pack()
Label(window, text = "Gender:").pack()
gender_entry = Entry(window)
gender_entry.pack()
Label(window, text = "Mobile:").pack()
mob_entry = Entry(window)
mob_entry.pack()
Label(window, text = "Email:").pack()
email_entry = Entry(window)
email_entry.pack()
#Buttons
save_button = Button(window, text = "Save", relief = GROOVE)
save_button.pack(pady = 5)
save_button.bind("<Button-1>", lambda event: save_info())

show_button = Button(window, text = "Show Info", relief = GROOVE)
show_button.pack(pady = 5)
show_button.bind("<Button-1>", lambda event: show_info())

window.mainloop()