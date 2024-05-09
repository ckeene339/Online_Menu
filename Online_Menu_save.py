from tkinter import *
import csv
import os
import re
from Online_Menu_gui import *


class SAVE:
    
    '''
    def test_data will check to make sure all sections in the window are filled out properly. The ouctome should either return false or return true.
    If returned false, the program will display the error you are getting in the window telling you how to fix it. If returned true, the program will
    display the name, order, and price of the order in the window.
    '''
    
    def test_data(self, label_order: Label, name: str, selected_item1: str, selected_item2: str, selected_item3: str, tip: int, total: float, total_with_tip: float) -> bool:
        try:
        
            self.tip = tip
            self.total = total
            self.total_with_tip = total_with_tip
            
            self.name = name
            self.nametest = name.strip()
            
            self.maincourse = selected_item1
            self.side = selected_item2
            self.drink = selected_item3
            
            
            '''
            First if statement tests to see if there are any spaces in the input name.
            '''
            
            if ' ' in self.nametest:
                label_order.config(text='Please enter a valid first name with no spaces.', fg='red', font=("Arial", 14))
                return False
            
            elif re.search(r'\d', self.name):
                label_order.config(text='Please enter a valid first name with no numbers.', fg='red', font=("Arial", 14))
                return False
                
            elif self.name:
                if self.maincourse == 'Main Course':
                    label_order.config(text='Please select a Main Course option.', fg='red', font=("Arial", 14))
                    return False
                
                elif self.maincourse != 'Main Course':
                    
                    if self.side == 'Sides':
                        label_order.config(text='Please select a Side option.', fg='red', font=("Arial", 14))
                        return False
                    
                    elif self.side != 'Sides':
                        
                        if self.drink == 'Drinks':
                            label_order.config(text='Please select a Drink option.', fg='red', font=("Arial", 14))
                            return False
                        
                        elif self.drink != 'Drinks':
                            
                            if self.tip == 0:
                                label_order.config(text='Please select a tip amount.', fg='red', font=("Arial", 14))
                                return False
                            
                            elif self.tip > 0:
                                
                                if self.maincourse == 'None' and self.side == 'None' and self.drink == 'None':
                                    label_order.config(text='Must select an item to place an order.', fg='red', font=("Arial", 14))
                                    return False
                                
                                else:
                                    
                                    '''
                                    Code above is successful. Code below is taking information from above and updating label_order
                                    o it displays the order correctly.
                                    '''
                                    
                                    if self.maincourse == 'None':
                                        self.maincourse = 'no main course'
                                    if self.side == 'None':
                                        self.side = 'no side'
                                    if self.drink == 'None':
                                        self.drink = 'no drink'
                                    
                                    label_order.config(text=f'{self.name} ordered {self.maincourse}, {self.side}, with {self.drink}.\n'
                                                            f'Your total is ${self.total_with_tip:.2f}', fg='black', font=("Arial", 14))
                                    
                                    return True
                                
            else:
                label_order.config(text='Please enter a valid first name for the order.', fg='red', font=("Arial", 14))
                return False
        
        except ValueError as e:
            label_order.config(text=str(e), fg='red', font=("Arial", 14))
            return False
        
        return False
        
    
    
    '''
    def save_data creates a csv file within the main path and displays the name, order, total, tip, and total + tip. If csv file already
    exists, this function will append the data to the next available line in the file.
    '''
    
    def save_data(self, radio_answer, dropdown_mainfood, dropdown_side, dropdown_drinks, maincourse_label, side_label, drinks_label,
                  input_name, label_info) -> None:
        
        self.input_name = input_name
        self.radio_answer = radio_answer
        self.dropdown_mainfood = dropdown_mainfood
        self.dropdown_side = dropdown_side
        self.dropdown_drinks = dropdown_drinks
        
        
        try:
            file_exists = os.path.isfile('data.csv')
            
            mode = 'w' if not file_exists else 'a'

            with open('data.csv', mode, newline='') as csv_file:
                writer = csv.writer(csv_file)
                if not file_exists:
                    writer.writerow(['Name', 'Order', 'Total', 'Tip', 'Total + Tip'])
                writer.writerow([self.name, f'{self.maincourse}, {self.side}, {self.drink}', self.total, f'{self.tip}%', f'{self.total_with_tip:.2f}'])
            
            print('Data saved to csv file.')
            
            
            '''
            Code below resets the window so all values and labels go back to default.
            '''
            self.input_name.delete(0, END)
            self.radio_answer.set(0)
            self.dropdown_mainfood.set("Main Course")
            self.dropdown_side.set("Sides")
            self.dropdown_drinks.set("Drinks")
            maincourse_label.config(text='$0.00')
            side_label.config(text='$0.00')
            drinks_label.config(text='$0.00')
            label_info.config(text="$0.00")
        
        except (FileNotFoundError, PermissionError) as e:
            print(f"An error occurred while saving data: {e}")
