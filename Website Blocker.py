from tkinter import *


# -------------------------------------------------------------------------------
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
color = "pink"
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
wd = Tk()
wd.title('bh')
wd.resizable(True, True)
wd.configure(background = color)
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
label = Label(wd, text='Enter Your Website Link :',background = color)
label.grid(column=0, row=1)
Label(wd, text='',width = 70,background = color).grid(column = 0, row = 0)
Label(wd, text='',width = 70,background = color).grid(column = 0, row = 4)
Label(wd, text='',width = 70,background = color).grid(column = 0, row = 6)
Label(wd, text='',width = 70,background = color).grid(column = 0, row = 2)

# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
Name = Entry(wd, width = 50)
Name.grid(column = 0, row = 3)
Name.focus()
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
def go():
    with open(hosts_path,'r+') as file:
        content=file.read()
        if Name.get() in content:
            pass
        else:
            if Name.get() == '':
                pass
            else:
                file.write(redirect+" "+ Name.get()+"\n")
    file1 = open(hosts_path, 'r')
    Lines = file1.readlines()
    count = 7
    for line in Lines:
        if line.startswith(redirect):
            Label(wd, text=line[9:], width=50, background='white').grid(column=0, row=count)
            print(line[9:])
            count +=1

    btn.configure(background='red',text = "BLOCKED")
    label.configure(text = "DONE")

btn = Button = Button(wd, text='BLOCK', width=10, command=go)
btn.grid(column=0, row=5)
# -------------------------------------------------------------------------------



# -------------------------------------------------------------------------------
wd.mainloop()
# -------------------------------------------------------------------------------
