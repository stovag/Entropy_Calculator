import mpmath as m
import math
from tkinter import *
from tkinter import ttk  
from tkinter import StringVar

### function called after button is clicked

def calculate():

    ### the string user typed

    msg = e.get()
    
    ### when the button is clicked again resets the data
    
    listBox.delete(*listBox.get_children())
    depositLabel_total_entropy.pack_forget()
    depositLabel_opt_encoding.pack_forget()
    
    ### Find different characters in input ###

    c_list = []
    for c in msg:
        if c not in c_list:
            c_list.append(c)
    c_num = len(msg)

    ### Find the numer of apearances of each character ###

    c_app = []
    for i in c_list:
        c_app.append([i, 0])

    for i in c_app:
        for j in msg:
            if i[0] == j:
                i[1] = i[1] + 1

    ### Find the probability of each character ###

    c_prob = []
    for i in c_app:
        c_prob.append([i[0], float(i[1])/c_num])

    ### Find the entropy of each character ###
    
    H_c = []

    for i in c_prob:
        num = float(i[1])
        H = -(num * m.log(num, b=2))
        #print(m.log(i[1], b=2))
        H_c.append([i[0], H])

    ### Print the entropy of each character

    for i in H_c:
        listBox.insert("", "end", values=(i[0], float(i[1])))

    ### Print total entropy
    
    H = 0
    for h in H_c:
        H = H + float(h[1])

    labelText_total_entropy.set("Total Entropy: " + str(H))
    depositLabel_total_entropy.pack(padx=5, pady=5)

    ### Calculate and print minimum number of bits needed to encode the string

    bit_size = math.ceil(H)
    min_bits = bit_size * c_num
    labelText_opt_encoding.set("Optimal encoding is possible with " + str(min_bits) + " bits")
    depositLabel_opt_encoding.pack(padx=5, pady=5)
    
### window
root = Tk()

### title 
root.title("Entropy Calculator")

### window not resizable
root.geometry("500x400")
root.resizable(0, 0)

### text that tells to enter the string
enter_string = Label(root, text="Enter a string below")
enter_string.pack(padx=5, pady=5)

### input box
e = Entry(root)
e.pack(padx=2, pady=2)

### calculate button
calculate_btn = Button(root, text="Calculate", command=calculate)
calculate_btn.pack(padx=10, pady=10)

### the tree view that shows the entropy
cols = ('String', 'Entropy')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)  

listBox.pack()

## total entropy text initialized

labelText_total_entropy = StringVar()
depositLabel_total_entropy = Label(root, textvariable=labelText_total_entropy)
depositLabel_total_entropy.pack()

### opt encoding text initialized

labelText_opt_encoding = StringVar()
depositLabel_opt_encoding = Label(root, textvariable=labelText_opt_encoding)
depositLabel_opt_encoding.pack()

### keeps program open
root.mainloop()
