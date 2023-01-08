from tkinter import *
import customtkinter as ct
from pathlib import Path

ct.set_appearance_mode('System')
ct.set_default_color_theme('green')


class App(ct.CTk):
    def __init__(self):
        super().__init__()

        # Main config
        self.title("Analiza kursu akcji")
        self.geometry('600x300')
        self.resizable(width=False, height=False)

        # Configure app grid
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=0, minsize=50)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        # File selection frame
        self.top_frame = ct.CTkFrame(self, height=50, corner_radius=0)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.file_info = ct.CTkLabel(self.top_frame, text='Wybierz plik z danymi:', width=140)
        self.file_info.pack(side=LEFT)

        self.get_file = ct.CTkButton(self.top_frame, text='Plik nie został wybrany', command=self.UploadTxt, width=450)
        self.get_file.pack(side=LEFT)

        # Plot options frame
        self.options_frame = ct.CTkFrame(self, corner_radius=0)
        self.options_frame.grid(row=1, column=0, sticky="nsew", pady=20)
        self.options_label = ct.CTkLabel(self.options_frame, text='Wskaźniki na wykresie',
                                         font=ct.CTkFont(size=16, weight='bold'))
        self.options_label.grid(padx=20, pady=10)

        self.SMA_switch = ct.CTkSwitch(self.options_frame, text='SMA')
        self.SMA_switch.grid(padx=25, pady=5, sticky='w')
        self.EMA_switch = ct.CTkSwitch(self.options_frame, text='EMA')
        self.EMA_switch.grid(padx=25, pady=5, sticky='w')
        self.RSI_switch = ct.CTkSwitch(self.options_frame, text='RSI')
        self.RSI_switch.grid(padx=25, pady=5, sticky='w')

        # Include options
        self.include_frame = ct.CTkFrame(self, corner_radius=0)
        self.include_frame.grid(row=1, column=1, sticky="nsew", pady=20)
        self.include_label = ct.CTkLabel(self.include_frame, text='Uwzględnij na wykresie',
                                         font=ct.CTkFont(size=16, weight='bold'))
        self.include_label.grid(padx=20, pady=10)

        self.VOL_switch = ct.CTkSwitch(self.include_frame, text='Wykres woluminu')
        self.VOL_switch.grid(padx=25, pady=5, sticky='w')
        self.VOL_switch.select()

        # Generate plot
        self.plot_frame = ct.CTkFrame(self, corner_radius=0)
        self.plot_frame.grid(row=2, column=0, columnspan=2, sticky="sew", )

        self.generate_bt = ct.CTkButton(self.plot_frame, text='Wygeneruj wykres!',
                                        font=ct.CTkFont(size=14, weight='bold'), command=None, width=200)
        self.generate_bt.pack(side=BOTTOM, pady=10)

    def UploadTxt(self, event=None):
        filename = ct.filedialog.askopenfile(filetypes=[('Plik z opisem wykresu', '*.txt *.csv')])
        if filename is None:
            return
        filepath = Path(filename.name)
        filename.close()

        # TODO: Create empty plot
        self.get_file.configure(text=f'Wybrany plik: {filepath.name}')


#
# button.pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()
