import re
import customtkinter as ctk
import numpy as np
from matplotlib import pyplot as plt

root=None

def graph_plotter(equation,root):

  plt.clf()

  root_min = root - 2
  root_max = root + 2

  x_range = np.linspace(root_min,root_max,5)

  y_values = []

  for x in x_range:

    y_values.append(function_evaluator(equation,x))

  plt.plot(x_range,y_values)
  plt.scatter(root,0,color="red",s=80,zorder=5)
  plt.xlabel("Value of x")
  plt.ylabel("Corresponding value of y")
  plt.show()

def function_evaluator(verified_equation,x):

  return eval(verified_equation,{"x":x})

def type_writer(label,text,index = 0):

  if index <= len(text):
    label.configure(text=text[:index])
    app.after(50,type_writer,label,text,index+1)

def slide_up(label, y=600, target_y=300):

  if y > target_y:
    label.place(relx = 0.5, y=y, anchor=ctk.CENTER)
    app.after(30,slide_up,label, y-5, target_y)

  else:
    label.place(relx=0.5, y = target_y, anchor=ctk.CENTER)


def bisection_method(equation):

 for widget in right_frame.winfo_children():
   if widget != initial_label:
     widget.destroy()

 global root
 initial_label.destroy()

 a = float(input_a.get())
 b = float(input_b.get())

 itr = int(iterations.get())
 i = 1

 while(i <= itr):

   result_a =  function_evaluator(equation,a)

   result_b = function_evaluator(equation,b)

   if result_a * result_b > 0:

    f_of_a_label = ctk.CTkLabel(right_frame,text=f"f({a}) : {result_a}",font=("Arial",40,"italic"))
    f_of_a_label.place(relx=0.5, y=100, anchor=ctk.CENTER)

    f_of_b_label = ctk.CTkLabel(right_frame,text=f"f({b}) : {result_b}",font=("Arial",40,"italic"))
    f_of_b_label.place(relx=0.5, y=150, anchor=ctk.CENTER)

    not_valid_label = ctk.CTkLabel(right_frame,text=f"f({a}) x f({b}) > 0",font=("Arial",40,"italic"))
    not_valid_label.place(relx=0.5, y=200, anchor=ctk.CENTER)

    error_label = ctk.CTkLabel(right_frame,text="ERROR : Invalid Interval",fg_color="transparent",font=("Helvetica",30),text_color="red")
    error_label.place(relx=0.5, y=300, anchor=ctk.CENTER)

    msg1 = ctk.CTkLabel(right_frame,text="The function values at the given bounds do not have opposite signs.",fg_color="transparent",font=("Roboto",30))
    msg1.place(relx=0.5, y=350, anchor=ctk.CENTER)

    msg2 = ctk.CTkLabel(right_frame,text="No sign change detected between a and b.",fg_color="transparent",font=("Helvetica",30))
    msg2.place(relx=0.5, y=400, anchor=ctk.CENTER)

    msg3 = ctk.CTkLabel(right_frame, text="Please provide different bounds.",fg_color="transparent",font=("Helvetica",30))
    msg3.place(relx=0.5, y=450, anchor=ctk.CENTER)

    return
   
   if result_a == 0:

     f_of_a_label = ctk.CTkLabel(right_frame,text=f"f({a}) : {result_a}",font=("Arial",40,"italic"))
     f_of_a_label.place(relx=0.5, y=100, anchor=ctk.CENTER)

     substituted_equation = equation.replace("x",str(a))
     
     original_equation = ctk.CTkLabel(right_frame,text=f"Equation : \n{equation}",font=("Arial",40))
     original_equation.place(relx=0.5, y=250, anchor=ctk.CENTER)
 
     elaborated_calculation = ctk.CTkLabel(right_frame,text=f"Substituting {a} : \n{substituted_equation}",font=("Arial",40))
     elaborated_calculation.place(relx=0.5, y=350, anchor=ctk.CENTER)

     root_label = ctk.CTkLabel(right_frame,text="",font=("Roboto",40,"bold"),fg_color="#111925",width=300,height=90,corner_radius=20)
     root_label.place(relx=0.5, y=500, anchor=ctk.CENTER)

     root = a
    #  graph_plotter(equation,root)

     type_writer(root_label,f"Root : {a}")

     break

   if result_b == 0:

     f_of_b_label = ctk.CTkLabel(right_frame,text=f"f({b}) : {result_b}",font=("Arial",40,"italic"))
     f_of_b_label.place(relx=0.5, y=100, anchor=ctk.CENTER)

     substituted_equation = equation.replace("x",str(b))

     original_equation = ctk.CTkLabel(right_frame,text=f"Equation : {equation} = 0",font=("Arial",40),fg_color="#111925",corner_radius=20,padx=20,pady=15)
     original_equation.place(relx=0.5, y=250, anchor=ctk.CENTER)

     elaborated_calculation = ctk.CTkLabel(right_frame,text=f"Substituting {b} : {substituted_equation} = 0",font=("Arial",40),fg_color="#111925",corner_radius=20,padx=20,pady=15)
     elaborated_calculation.place(relx=0.5, y=350, anchor=ctk.CENTER)
     
     root_label = ctk.CTkLabel(right_frame,text="",font=("Roboto",40,"bold"),fg_color="#111925",width=300,height=90,corner_radius=20,text_color="white")
     root_label.place(relx=0.5, y=500, anchor=ctk.CENTER)

     type_writer(root_label,f"Root : {b}")

     root = b
    #  graph_plotter(equation,root)

     break

   c = (a + b)/2

   result_c = function_evaluator(equation,c)

   if result_a * result_c < 0:
 
     b_update = ctk.CTkLabel(right_frame,text=f"Since, f({a}) * f({c}) < 0\n -> {result_a} * {result_c} > 0\n So, b = c({c})",font=("Arial",40),fg_color="#111925",corner_radius=20,padx=20,pady=15)
     b_update.place(relx=0.5, y=250, anchor=ctk.CENTER)
     b = c

   if result_a * result_c > 0:

     a_update = ctk.CTkLabel(right_frame,text=f"f({a}) * f({c}) > 0\n -> {result_a} * {result_c} > 0\n So, a = c({c})",font=("Arial",40),fg_color="#111925",corner_radius=20,padx=20,pady=15)
     a_update.place(relx=0.5,y=250,anchor=ctk.CENTER)
     a = c

   i = i + 1

   if (abs(b - a))/2 < float(tolerance.get()):

    convergence_msg = ctk.CTkLabel(right_frame,text="Convergence Successful",fg_color="#111925",width=300,height=90,corner_radius=20)
    # convergence_msg.place(relx=0.5,y=400,anchor=ctk.CENTER)
    slide_up(convergence_msg,y=600, target_y=400)

    root_msg = ctk.CTkLabel(right_frame,text=f"Approximate Root : {c}",fg_color="#111925",width=300,height=90,corner_radius=20)
    # root_msg.place(relx=0.5,y=500,anchor=ctk.CENTER)
    slide_up(root_msg,y=800, target_y=500)

    function_value_msg = ctk.CTkLabel(right_frame,text=f"Function Value : {result_c}",fg_color="#111925",width=300,height=90,corner_radius=20)
    # function_value_msg.place(relx=0.5,y=600,anchor=ctk.CENTER)
    slide_up(function_value_msg,y=1000,target_y=600)

    root = c
    # graph_plotter(equation,root)
    break


app = ctk.CTk()
app.geometry("900x600")
app.title("Equation Solver and Visualizer")

top_frame = ctk.CTkFrame(app, height=80,fg_color="#1D2427")
top_frame.pack(side="top",fill="x")

heading_label = ctk.CTkLabel(top_frame,text="Equation Solver and Visualizer",font=("Arial",50,"bold"),fg_color="transparent")
heading_label.place(relx=0.5, rely=0.5, anchor="center")  

left_frame = ctk.CTkFrame(app,width=300, height=600,fg_color="#0E1214",corner_radius=15)
left_frame.pack(side="left",fill="y")
left_frame.propagate(False)

my_font = ctk.CTkFont(
    family="Arial",
    size=25,
    weight="bold",      # "bold" or "normal"
    underline=True,     # True / False
    overstrike=False    # True / False
)

input_labels = ctk.CTkLabel(left_frame,text="Input Section",font=my_font)
input_labels.place(x=65,y=50)

equation_input = ctk.CTkEntry(left_frame,placeholder_text="Enter an Equation",width=260,height=40)
equation_input.place(x=10, y=100)

input_a = ctk.CTkEntry(left_frame,placeholder_text="Enter 'a' value for f(a)",width=260,height=40)
input_a.place(x=10,y=150)

input_b = ctk.CTkEntry(left_frame,placeholder_text="Enter 'b' value for f(b)",width=260,height=40)
input_b.place(x=10,y=200)

tolerance = ctk.CTkEntry(left_frame,placeholder_text="Enter Tolerance", width=260, height=40)
tolerance.place(x=10,y=250)

iterations = ctk.CTkEntry(left_frame,placeholder_text="Enter Minimum Iterations", width=260, height=40)
iterations.place(x=10,y=300)

equation_button = ctk.CTkButton(left_frame,text="Solve",command=lambda: bisection_method(equation_input.get()),fg_color="#1F2123")
equation_button.place(x=75, y=400)

graph_button = ctk.CTkButton(left_frame,text="Put it on Graph",command=lambda: graph_plotter(equation_input.get(),root),fg_color="#1F2123")
graph_button.place(x=75, y=460)

right_frame = ctk.CTkFrame(app,width=600,height=600,fg_color="#1F2123",corner_radius=15)
right_frame.pack(side="right",fill="both",expand=True)
right_frame.propagate(False)

initial_label = ctk.CTkLabel(right_frame,text="Calculations and Results will appear here",font=("Arial",40),fg_color="#111925",corner_radius=20,padx=20,pady=15)
initial_label.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

app.mainloop()
