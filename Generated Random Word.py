from tkinter import *
import random

root=Tk()
root.title("Random Words")
root.configure(bg = "green")
root.geometry("400x400")

label1 = Label(root)

list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(list1)

def random_number():
    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_no5 = random.randint(1, 26)
    print(random_no1)
    random_list1 = list1[random_no1]
    random_list2 = list2[random_no2]
    random_list3 = list3[random_no3]
    random_list4 = list4[random_no4]
    random_list5 = list5[random_no5]
    print("Your Random word is " + random_list1 + random_list2 + random_list3 + random_list4 + random_list5)
    
    label1["text"] = random_list1 + random_list2 + random_list3 + random_list4 + random_list5
    
btn= Button(root, text="Generated Random Word ", command = random_number, bg = "Royal Blue",fg="White")
btn.place(relx= 0.5,rely = 0.4, anchor = CENTER )
label1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()