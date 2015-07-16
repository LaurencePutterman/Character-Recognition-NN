from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
import numpy as np

layout = GridLayout(rows = 8, cols = 8)
inputString = ""
inArray = np.array([[]])
X = np.array([])
y = np.array([[]])
np.random.seed(1)
syn0 = 2*np.random.random((64,5)) - 1
syn1 = 2*np.random.random((5,1)) - 1
inputCount = 0
text = TextInput()
class MyApp(App):
    
    def build(self):
        parent = Widget()
        global layout
        global text
        for x in range(0,64):
            btn = Button(background_color = (1,1,1,1), text="0")
            btn.bind(on_press=callback)
            layout.add_widget(btn)
        btn = Button(text="Add")
        btn.bind(on_press=add)
        gLayout = GridLayout(size = (1680, 1050), cols = 2)
        gLayout2 = GridLayout(rows = 4)
        gLayout2.add_widget(btn)
        text = TextInput(multiline=False)
        text.bind(on_text_validate=on_enter)
        gLayout2.add_widget(text)
        learn = Button(text="Learn", on_press=learnn)
        gLayout2.add_widget(learn)
        isA4 = Button(text="Is a 4?", on_press=isAFour)
        gLayout2.add_widget(isA4)
        gLayout.add_widget(layout)
        gLayout.add_widget(gLayout2)

        parent.add_widget(gLayout)
        return parent

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

def callback(instance):
    print('button <%s> ' % (instance))
    text = ""
    text = instance.text
    if text == "0":
        instance.background_color = (0,0,0,1)
        instance.text = "1"
    else :
        instance.background_color = (1,1,1,1)
        instance.text = "0"

def add(self):
    global layout
    s = ""
    global inArray
    inArray = np.array([[]])
    for btn in layout.children:
        s = s+btn.text
        print(btn)
        a = np.array([[float(btn.text)]])
        inArray= np.append(inArray,a)
    print s
    print inArray
    global X
    X = np.append(X,inArray)
    print X
    global inputCount 
    inputCount = inputCount+1
    

def on_enter(instance):
    global y
    a = np.array([[float(instance.text)]])
    y = np.append(y,a)
    print y
    Clock.schedule_once(focusText)

def focusText(instance):
    global text
    text.focus = True
    text.text = ""

def isAFour(instance):
    global syn0
    global syn1
    global layout
    arr = np.array([[]])
    for x in xrange(inputCount):
        for btn in layout.children:
            a = np.array([[float(btn.text)]])
            arr = np.append(arr,a)

    arr = np.reshape(arr,(inputCount,-1))
    l0 = arr
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    mean = np.mean(np.abs(l2))
    print mean
    if mean > 0.9:
        print "is a four!"
    else:
        print "not a four."



def learnn(instance):
    print("go")
    global inputCount
    global X
    global y
    print y
    print inputCount
    y = np.reshape(y,(inputCount,-1))
    X = np.reshape(X,(inputCount,-1))
    print y
    print X
    global syn0
    global syn1
    syn0 = 2*np.random.random((64,inputCount)) - 1
    syn1 = 2*np.random.random((inputCount,1)) - 1

    for j in xrange(60000):

    # Feed forward through layers 0, 1, and 2
        l0 = X
        l1 = nonlin(np.dot(l0,syn0))
        l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
        l2_error = y - l2
    
        if (j% 10000) == 0:
            print "Error:" + str(np.mean(np.abs(l2_error)))
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
        l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
        l1_error = l2_delta.dot(syn1.T)
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
        l1_delta = l1_error * nonlin(l1,deriv=True)

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

    print l2
    print l1
   


if __name__ == '__main__':
    MyApp().run()