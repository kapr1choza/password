#импорт библиотек
import tkinter
import customtkinter as CTk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import password

from PIL import Image

#базовый шаблон графического окна

#основной класс в котором будут элементы графического интерфейса
class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x390") #Размеры окна
        self.title("Password generation") #Название программы
        self.resizable(False, False) #Запрет на изменение размера в ручную

        #размещаю картинку на основном окне программы
        self.logo = CTk.CTkImage(dark_image=Image.open("password.png"), size=(450, 210))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        #фрейм для элементов интерфейса
        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20,20), sticky="nsew")

        #поле вывода пароля
        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        #кнопка генерации пароля
        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                          command=self.set_password)

        #отображаю виджет в том же столбце что и поле пароля, но левее
        self.btn_generate.grid(row=0, column=1)

        #фрейм для элемнтов настройки сложности
        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        #слайдер длины пароля
        self.password_lenght_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_lenght_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        #счетчик длины пароля
        self.password_lenght_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_lenght_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        #чекбоксы настройки сложности пароля
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                         onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                         onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var,
                                        onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3)

        #виджет на изменение цвета интерфейса
        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        #значение по умолчанию для слайдера и значение по умолчанию для темы
        self.password_lenght_slider.set(12)
        self.password_lenght_entry.insert(0, 12)
        self.appearance_mode_option_menu.set("Light")

    #фунцкия изменения фона
    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    #связываем значение слайдера и счетчика
    def slider_event(self, value):
        self.password_lenght_entry.delete(0, "end")
        self.password_lenght_entry.insert(0, int(value))

    #функция для получения символов
    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get()
                       + self.cb_symbol_var.get())
        return chars

    #функция привязывания к кнопке и генерация самого пароля
    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(length=int(self.password_lenght_slider.get()),
                                                          characters=self.get_characters()))


#основное окно программы, цикл обработки скрипта

if __name__ == "__main__":
    app = App()
    app.mainloop()