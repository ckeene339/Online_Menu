from tkinter import *
from Online_Menu_save import *
from typing import Any

class GUI:
    
    def __init__(self, window: Tk) -> None:
        self.window = window
        
        
        '''
        code below sets label_info that updates every time you place an order.
        '''
        
        self.frame_order = Frame(self.window)
        self.label_order = Label(self.frame_order, text='What would you like to order?', font=("Arial", 14))
        self.label_order.pack(side='left')
        self.frame_order.place(relx=1, rely=1, anchor='sw', x=-700, y=-15)
        
        
        '''
        Code below displays main course and prices when selecting food item.
        '''
        
        self.dropdown_mainfood = StringVar()
        self.dropdown_mainfood.set("Main Course")
        self.dropdown_mainfood.trace('w', self.update_maincourse_label)
        
        main_course = { 
            "Cheeseburger": "$8.99", 
            "Hotdog": "$6.99", 
            "Chili Dog": "$7.99", 
            "Burrito": "$6.59", 
            "Soup": "$2.69", 
            "None": "$0.00"
        }
             
        drop_maincourse = OptionMenu(window, self.dropdown_mainfood, *main_course.keys()) 
        drop_maincourse.place(x=10, y=15)
        drop_maincourse.config(width=12)
        self.main_course_prices = main_course
        self.maincourse_label = Label(window, text="$0.00", font=("Arial", 14))
        self.maincourse_label.place(x=10 + drop_maincourse.winfo_reqwidth() + 10, y=15)
        self.update_maincourse_label()
        
        
        '''
        Code below displays sides and prices when selecting food item.
        '''
        
        self.dropdown_side = StringVar()
        self.dropdown_side.set("Sides")
        self.dropdown_side.trace('w', self.update_side_label)
        
        side = { 
            "French Fries": "$3.99", 
            "Tator Tots": "$3.49", 
            "Apple Slices": "$2.59", 
            "Coleslaw": "$2.99", 
            "None": "$0.00"
        }
             
        drop_side = OptionMenu(window, self.dropdown_side, *side.keys()) 
        drop_side.place(x=10, y=60)
        drop_side.config(width=12)
        self.side_prices = side 
        self.side_label = Label(window, text="$0.00", font=("Arial", 14))
        self.side_label.place(x=10 + drop_side.winfo_reqwidth() + 10, y=60)
        self.update_side_label()
        
        
        '''
        Code below displays drinks and prices when selecting food item.
        '''
        
        self.dropdown_drinks = StringVar()
        self.dropdown_drinks.set("Drinks")
        self.dropdown_drinks.trace('w', self.update_drinks_label)
        
        drink = { 
            "Cherry Coke": "$1.99", 
            "Orange Fanta": "$2.49", 
            "Coffee": "$1.99", 
            "Water": "$1.49", 
            "None": "$0.00"
        }
             
        drop_drinks = OptionMenu(window, self.dropdown_drinks, *drink.keys()) 
        drop_drinks.place(x=10, y=105)
        drop_drinks.config(width=12)
        self.drinks_prices = drink
        self.drinks_label = Label(window, text="$0.00", font=("Arial", 14))
        self.drinks_label.place(x=10 + drop_drinks.winfo_reqwidth() + 10, y=105)
        self.update_drinks_label()
        
        
        '''
        Code below displays tip amounts.
        '''
        
        self.tip_label = Label(window, text="Tip:", font=("Arial", 10))
        self.tip_label.place(x=10, y=155)
        
        self.frame_status = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.tip_10 = Radiobutton(self.frame_status, text='10%', variable=self.radio_answer, value=10, font=("Arial", 10))
        self.tip_15 = Radiobutton(self.frame_status, text='15%', variable=self.radio_answer, value=15, font=("Arial", 10))
        self.tip_20 = Radiobutton(self.frame_status, text='20%', variable=self.radio_answer, value=20, font=("Arial", 10))
        self.tip_10.pack(anchor='w', side='left')
        self.tip_15.pack(anchor='w', side='left')
        self.tip_20.pack(anchor='w', side='left')
        self.frame_status.pack(anchor='w', side='bottom', padx=40, pady=150)
        
        
        '''
        Code below checks when a tip amount is selected and runs def update_price_on_radio_select.
        '''
        
        self.tip_10.bind("<Button-1>", lambda event: self.update_tip_on_radio_select(10))
        self.tip_15.bind("<Button-1>", lambda event: self.update_tip_on_radio_select(15))
        self.tip_20.bind("<Button-1>", lambda event: self.update_tip_on_radio_select(20))
        
        
        '''
        Code below displays textbox to input your name.
        '''
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='First name:', font=("Arial", 10))
        self.input_name = Entry(self.frame_name, width=13, font=("Arial", 10))
        self.label_name.pack(side='left')
        self.input_name.pack(padx=10, pady=10, side='top')
        self.frame_name.place(relx=1, rely=1, anchor='sw', x=-690, y=-105)
        
        
        '''
        Code below displays the Place Order Button
        '''
        
        self.button_pay = Button(self.window, text='Place Order', command=self.submit, font=("Arial", 12), fg='red')
        self.button_pay.config(width=10, height=1)
        self.button_pay.place(relx=1, rely=1, anchor='sw', x=-690, y=-65)
        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text='$0.00', font=("Arial", 14), fg='green')
        self.label_info.pack(side='right')
        self.frame_info.place(relx=1, rely=1, anchor='sw', x=-570, y=-65)
        
        
        '''
        Code below displays the menu on the right side of the window in blue.
        '''
        
        self.menu_maincourse_label = Label(window, text="MAIN COURSE\n\n"
                                             "Cheeseburger      -  $8.99\n"
                                             "Hotdog                  -  $6.99\n"
                                             "Chili Dog               -  $7.99\n"
                                             "Burrito                   -  $6.59\n"
                                             "Soup                      -  $2.69"
                                , fg='darkblue', font=("Arial", 12))
        self.menu_maincourse_label.pack(side='top')
        self.menu_maincourse_label.place(relx=1, rely=1, anchor='n', x=-380, y=-320)
        
        self.menu_sides_label = Label(window, text="SIDES\n\n"
                                             "French Fries            -  $3.99\n"
                                             "Tator Tots                 -  $3.49\n"
                                             "Apple Slices             -  $2.59\n"
                                             "Coleslaw                    -  $2.99\n"
                                , fg='darkblue', font=("Arial", 12))
        self.menu_sides_label.pack(side='top')
        self.menu_sides_label.place(relx=1, rely=1, anchor='n', x=-150, y=-320)
        
        self.menu_drinks_label = Label(window, text="DRINKS\n\n"
                                             "Cherry Coke             -  $1.99\n"
                                             "Orange Fanta            -  $2.49\n"
                                             "Coffee                        -  $1.99\n"
                                             "Water                         -  $1.49\n"
                                , fg='darkblue', font=("Arial", 12))
        self.menu_drinks_label.pack(side='top')
        self.menu_drinks_label.place(relx=1, rely=1, anchor='n', x=-150, y=-190)
        
        
    '''
    update_maincourse_label takes the selected food item given and checks to make sure it is not the default
    value given, in this case, Main Course. The label is then updated to display the selected item. This
    function ends by running the price() function to update pricing changes when a different item is selected.
    '''
    
    def update_maincourse_label(self, *args: Any) -> None:
        self.selected_item1 = self.dropdown_mainfood.get()
        if self.selected_item1 != "Main Course":
            self.maincourse_price = self.main_course_prices[self.selected_item1]
            self.maincourse_label.config(text=f"{self.maincourse_price}")
            self.price()
    
    
    '''
    update_side_label takes the selected food item given and checks to make sure it is not the default
    value given, in this case, Sides. The label is then updated to display the selected item. This function
    ends by running the price() function to update pricing changes when a different item is selected.
    '''
    
    def update_side_label(self, *args: Any) -> None:
        self.selected_item2 = self.dropdown_side.get()
        if self.selected_item2 != "Sides":
            self.side_price = self.side_prices[self.selected_item2]
            self.side_label.config(text=f"{self.side_price}")
            self.price()
    
    
    '''
    update_drinks_label takes the selected food item given and checks to make sure it is not the default
    value given, in this case, Drinks. The label is then updated to display the selected item. This function
    ends by running the price() function to update pricing changes when a different item is selected.
    '''
    
    def update_drinks_label(self, *args: Any) -> None:
        self.selected_item3 = self.dropdown_drinks.get()
        if self.selected_item3 != "Drinks":
            self.drinks_price = self.drinks_prices[self.selected_item3]
            self.drinks_label.config(text=f"{self.drinks_price}")
            self.price()
        
        
    '''
    def below runs self.price() when a radiobutton has been selected so that the
    final price for the order updates.
    '''
        
    def update_tip_on_radio_select(self, tip_percent: int) -> None:
        self.radio_answer.set(tip_percent)
        self.price()
        
    
    '''
    def price updates the total amount when items are selected and tip is selected and
    when order options are switched out.
    '''
        
    def price(self) -> None:
        
        maincourse = float(self.maincourse_label.cget("text")[1:])
        side = float(self.side_label.cget("text")[1:])
        drink = float(self.drinks_label.cget("text")[1:])
        
        tip = self.radio_answer.get() / 100
        
        self.total = maincourse + side + drink
        self.total_with_tip = maincourse + side + drink + (maincourse + side + drink) * tip
        
        self.label_info.config(text=f'${self.total_with_tip:.2f}', fg='green', font=("Arial", 14))
        
    
    '''
    def submit runs Online_Menu_save to check all inputs and saves the data to a csv file.
    '''
    
    def submit(self) -> None:
        
        tip = self.radio_answer.get()
        name = self.input_name.get()
        save = SAVE()
        
        self.price()
        
        if save.test_data(self.label_order, name, self.selected_item1, self.selected_item2, self.selected_item3, tip, self.total, self.total_with_tip):
            save.save_data(self.radio_answer, self.dropdown_mainfood, self.dropdown_side, self.dropdown_drinks, self.maincourse_label,
                           self.side_label, self.drinks_label, self.input_name, self.label_info)
        else:
            print("Test failed. Data not saved.")
        