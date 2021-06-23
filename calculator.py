import tkinter as t

app = t.Tk()
app.title('calculator')
app.geometry('300x300')


result = t.Variable(app)
t.Entry(app, textvariable=result,width=40).place(x=30,y=60)

p =''

def operate(e):
    global p
    p = p+e
    result.set(p)

def clr():
    global p
    p=''
    result.set(p)

def ans():
    global p
    result.set(eval(p))

t.Button(app, text='+',width=2, command = lambda:operate('+')).place(x=230,y=100)
t.Button(app, text='-',width=2, command = lambda:operate('-')).place(x=230,y=150)
t.Button(app, text='X',width=2, command = lambda:operate('*')).place(x=230,y=200)
t.Button(app, text='%',width=2, command = lambda:operate('/')).place(x=230,y=250)
t.Button(app, text='9',width=2, command = lambda:operate('9')).place(x=150,y=100)
t.Button(app, text='6',width=2, command = lambda:operate('6')).place(x=150,y=150)
t.Button(app, text='3',width=2, command = lambda:operate('3')).place(x=150,y=200)
t.Button(app, text='=',width=2, command = lambda:ans()).place(x=150,y=250)
t.Button(app, text='8',width=2, command = lambda:operate('8')).place(x=90,y=100)
t.Button(app, text='5',width=2, command = lambda:operate('5')).place(x=90,y=150)
t.Button(app, text='2',width=2, command = lambda:operate('2')).place(x=90,y=200)
t.Button(app, text='0',width=2, command = lambda:operate('0')).place(x=90,y=250)
t.Button(app, text='7',width=2, command = lambda:operate('7')).place(x=40,y=100)
t.Button(app, text='4',width=2, command = lambda:operate('4')).place(x=40,y=150)
t.Button(app, text='1',width=2, command = lambda:operate('1')).place(x=40,y=200)
t.Button(app, text='.',width=2, command = lambda:operate('.')).place(x=40,y=250)
t.Button(app, text='clr',width=4, command = lambda:clr()).place(x=30,y=20)

app.mainloop()
