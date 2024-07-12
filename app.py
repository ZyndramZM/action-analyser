from tkinter import *
import customtkinter as ct
from pathlib import Path
from plotter import Plotter

import pandas as pd

ct.set_appearance_mode('System')
ct.set_default_color_theme('green')

OBLIGATORY_INDEXES = []
PLOT_TYPES = ["Linear", "Candle", "OHLC"]


class App(ct.CTk):
    def __init__(self):
        super().__init__()

        # Initialize plotter
        self.plot = Plotter()

        # Main config
        self.title("Action Analyser")
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

        self.file_info = ct.CTkLabel(self.top_frame, text='Choose data file:', width=180)
        self.file_info.pack(side=LEFT)

        self.get_file = ct.CTkButton(self.top_frame, text='No file chosen.', command=self.UploadTxt, width=400)
        self.get_file.pack(side=LEFT)

        # Plot options frame
        self.options_frame = ct.CTkFrame(self, corner_radius=0)
        self.options_frame.grid(row=1, column=0, sticky="nsew", pady=20)
        self.options_label = ct.CTkLabel(self.options_frame, text='Plot indicators',
                                         font=ct.CTkFont(size=16, weight='bold'))
        self.options_label.grid(padx=20, pady=10)

        self.SMA_v = IntVar()
        self.EMA_v = IntVar()
        self.RSI_v = IntVar()

        self.SMA_switch = ct.CTkSwitch(self.options_frame, text='SMA', variable=self.SMA_v)
        self.SMA_switch.grid(padx=25, pady=5, sticky='w')
        self.EMA_switch = ct.CTkSwitch(self.options_frame, text='EMA', variable=self.EMA_v)
        self.EMA_switch.grid(padx=25, pady=5, sticky='w')
        self.RSI_switch = ct.CTkSwitch(self.options_frame, text='RSI', variable=self.RSI_v)
        self.RSI_switch.grid(padx=25, pady=5, sticky='w')

        # Include options
        self.include_frame = ct.CTkFrame(self, corner_radius=0)
        self.include_frame.grid(row=1, column=1, sticky="nsew", pady=20)
        self.include_label = ct.CTkLabel(self.include_frame, text='Plot settings',
                                         font=ct.CTkFont(size=16, weight='bold'))
        self.include_label.grid(padx=20, pady=10)

        self.VOL_v = IntVar()
        self.VOL_v.set(1)
        self.plot_t_v = StringVar()
        self.plot_t_v.set(PLOT_TYPES[0])

        self.VOL_switch = ct.CTkSwitch(self.include_frame, text='Volume plot',
                                       variable=self.VOL_v)
        self.VOL_switch.grid(padx=25, pady=5, sticky='w')

        self.plot_type_option_label = ct.CTkLabel(self.include_frame, text="Plot type:")
        self.plot_type_option_label.grid(padx=25, pady=(5, 0), sticky='w')
        self.plot_type_option = ct.CTkOptionMenu(self.include_frame, values=PLOT_TYPES,
                                                 variable=self.plot_t_v, command=None)
        self.plot_type_option.grid(padx=25, pady=(0, 5), sticky='w')

        # Generate plot
        self.plot_frame = ct.CTkFrame(self, corner_radius=0)
        self.plot_frame.grid(row=2, column=0, columnspan=2, sticky="sew", )

        self.generate_bt = ct.CTkButton(self.plot_frame, text='Generate plot!',
                                        font=ct.CTkFont(size=14, weight='bold'), command=self.generate_plot, width=200)
        self.generate_bt.pack(side=BOTTOM, pady=10)

    def UploadTxt(self, event=None):
        filename = ct.filedialog.askopenfile(filetypes=[('Data file', '*.txt *.csv')])
        if filename is None:
            return
        filepath = Path(filename.name)
        filename.close()

        self.plot.load_data(pd.read_csv(filepath))

        self.get_file.configure(text=f'Chosen file: {filepath.name}')
        self.file_info.configure(bg_color='transparent', font=ct.CTkFont(weight='normal'))

    def generate_plot(self):
        if not self.plot.ready:
            self.file_info.configure(bg_color='red', font=ct.CTkFont(weight='bold'))
            return
        self.plot.setup(
            sma=self.SMA_v.get(),
            ema=self.EMA_v.get(),
            rsi=self.RSI_v.get(),
            volume=self.VOL_v.get(),
            plot_type=self.plot_t_v.get()
        )
        self.plot.generate()



if __name__ == '__main__':
    app = App()
    app.mainloop()
