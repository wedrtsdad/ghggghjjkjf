from tkinter import *
root=Tk()
root.title("popup")
root.geometry("600x600")
root.config(bg="grey")

month= ("Jan.","Feb.","Mar.","Apr.","May","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec.")
profit= ("10","100","1000","10000","100000","1000000","10000000","100000000","1000000000","10000000000","100000000000","1000000000000")

l1= Label(root)
L2= Label(root)

def h():
       max1= max(profit)
       index1= profit.index(max1)
       print(index1)
       max_pro= month[index1]
       l1["text"]="maximum profit in month of " + str(max_pro) + " is " + str(max1)

def i():
       max2= min(profit)
       index2= profit.index(max2)
       print(index2)
       max_pro2= month[index2]
       L2["text"]="minimum profit in month of " + str(max_pro2) + " is " + str(max2)


btn= Button(root, text= "Show me the maximum profit of the year" , command=h)
btn1= Button(root, text= "Show me the minimum profit of the year" , command=i)

btn.place(relx= 0.5 , rely= 0.6 , anchor=CENTER)
btn1.place(relx= 0.5 , rely= 0.8 , anchor=CENTER)

l1.place(relx= 0.5 , rely= 0.7 , anchor=CENTER)
L2.place(relx= 0.5 , rely= 0.9 , anchor=CENTER)



root.mainloop()