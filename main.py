import re
import customtkinter as ctk

# equation = input("Enter Equation : ")

executed  = False

def function_evaluator(verified_equation,x):

  global executed

   # variables = re.findall(pattern=r"[a-zA-Z]+",string=verified_equation)
   # print("\nVariables -> ",variables)

   

  # result = re.finditer(pattern=r"\d+|[a-zA-Z]+|[+\-]|\*\*|[*\/]|[=]",string=equation)
 
  # prev = 0
 
  # for res in result:
 
 
  #    print(res.group(), end="")
  #    # print(res.start())
  #    # print(res.end())
  
 
  #    gap_start = prev
  #    gap_end = res.start()
 
  #    gap = equation[gap_start:gap_end]
 
  #    prev = res.end()
 
  # if gap:
  
  #  if gap != " ":
  #    print("\nInvalid Equation")
     
 
  #  else:
 
  #   print("\nvalid")
 
  # else:
  
  #  print("\nvalid")
 
  # if gap:
  #    print("[",gap,"]")

  return eval(verified_equation,{"x":x})


def bisection_method(equation):

#  tolerance = 0.0001

 a = float(input_a.get())
 b = float(input_b.get())

 i = 1
 while(i <= 10):

   result_a =  function_evaluator(equation,a)
   result_b = function_evaluator(equation,b)

   if result_a == 0:
     
     root_label = ctk.CTkLabel(right_frame,text=f"Root : {a}",font=("Roboto",40,"bold"))
     root_label.place(x=50,y=50)
     break

   if result_b == 0:
     root_label = ctk.CTkLabel(right_frame,text=f"Root : {b}",font=("Roboto",40,"bold"))
     root_label.place(x=50,y=50)
     break

   c = (a + b)/2

   result_c = function_evaluator(equation,c)

   if result_a * result_c < 0:
     b = c

   if result_a * result_c > 0:
     a = c

   i = i + 1

   if (abs(b - a))/2 < tolerance:
     print("Convergence Successful")
     print("Approximate Root : ",c)
     print("Function Value at Root : ",result_c)
     break
   else:
     print("ERROR : Invalid Interval")
     print("The function values at the given bounds do not have opposite signs.",end="")
     print("No sign change detected between a and b.")
     print("Please provide different bounds.")
     break


app = ctk.CTk()
app.geometry("900x600")
app.title("Equation Solver and Visualizer")

left_frame = ctk.CTkFrame(app,width=300, height=600,fg_color="#0E1214")
left_frame.pack(side="left",fill="y")
left_frame.propagate(False)

my_font = ctk.CTkFont(
    family="Arial",
    size=20,
    weight="bold",      # "bold" or "normal"
     # "italic" or "roman"
    underline=True,     # True / False
    overstrike=False    # True / False
)

input_labels = ctk.CTkLabel(left_frame,text="Input Section",font=my_font)
input_labels.place(x=95,y=20)

equation_input = ctk.CTkEntry(left_frame,placeholder_text="Enter an Equation",width=260,height=40)
# equation_input.pack(padx=20,pady=20)
equation_input.place(x=10, y=100)

input_a = ctk.CTkEntry(left_frame,placeholder_text="Enter 'a' value for f(a)",width=260,height=40)
input_a.place(x=10,y=150)

input_b = ctk.CTkEntry(left_frame,placeholder_text="Enter 'b' value for f(b)",width=260,height=40)
input_b.place(x=10,y=200)

tolerance = ctk.CTkEntry(left_frame,placeholder_text="Enter Tolerance", width=260, height=40)
tolerance.place(x=10,y=250)


equation_button = ctk.CTkButton(left_frame,text="Solve",command=lambda: bisection_method(equation_input.get()),fg_color="#1F2123")
equation_button.place(x=75, y=300)

right_frame = ctk.CTkFrame(app,width=600,height=600,fg_color="#1F2123")
right_frame.pack(side="right",fill="both",expand=True)
right_frame.propagate(False)

# bisection_method(equation)

app.mainloop()
