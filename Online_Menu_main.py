'''
Online Menu Main
'''


from Online_Menu_gui import *


def main() -> None:
    window = Tk()
    window.title('Online Menu')
    window.geometry('710x330')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()
    

if __name__ == "__main__":
    main()