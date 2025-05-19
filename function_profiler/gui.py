import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import random
import sys
import inspect


sys.path.append(os.path.dirname(__file__))
from loader import FunctionLoader
from plotter import plot_results, export_results
from decorators import measure_time  

class ProfilerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Extended Function Profiler')
        self.geometry('900x700')

        self.filepath = tk.StringVar()
        self.configpath = tk.StringVar()
        self.plot_var = tk.BooleanVar()
        self.csv_var = tk.StringVar()
        self.html_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text='Python File:').grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.filepath, width=50).grid(row=0, column=1)
        tk.Button(frame, text='Browse', command=self.browse_file).grid(row=0, column=2)

        tk.Label(frame, text='Config JSON:').grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.configpath, width=50).grid(row=1, column=1)
        tk.Button(frame, text='Browse', command=self.browse_config).grid(row=1, column=2)

        tk.Checkbutton(frame, text='Show Plot', variable=self.plot_var).grid(row=2, column=1, sticky='w')

        tk.Label(frame, text='Export CSV:').grid(row=3, column=0)
        tk.Entry(frame, textvariable=self.csv_var, width=30).grid(row=3, column=1)

        tk.Button(frame, text='Run Profiling', command=self.run_profiling).grid(row=5, column=1, pady=5)

        tk.Label(self, text='Results:').pack(anchor='w', padx=10)
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=25)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')])
        if filepath:
            self.filepath.set(filepath)

    def browse_config(self):
        configfile = filedialog.askopenfilename(filetypes=[('JSON Files', '*.json')])
        if configfile:
            self.configpath.set(configfile)

    def run_profiling(self):
        pyf = self.filepath.get()
        cfg = self.configpath.get()
        if not os.path.isfile(pyf):
            messagebox.showerror('Error', 'Select a valid Python file')
            return

        funcs = FunctionLoader.load_functions_from_file(pyf)
        tests = []
        if cfg and os.path.isfile(cfg):
            tests = FunctionLoader.load_tests_from_config(cfg)

        self.text_area.delete('1.0', tk.END)
        results = {}

        for name, func in funcs.items():
            
            decorated_func = measure_time(func)

            sig = inspect.signature(func)
            needs_arg = len(sig.parameters) > 0

            data = None
            for t in tests:
                if t.get('function') == name:
                    size = t.get('size', 1000)
                    population = max(size * 10, size)
                    data = random.sample(range(population), size)

            if needs_arg:
                result = decorated_func(data or [])
            else:
                result = decorated_func()

            elapsed_time = result['time']  


            results[name] = elapsed_time
            line = f"{name}: {elapsed_time:.2f} ms"+"\n"
            self.text_area.insert(tk.END, line)

        if self.plot_var.get() and results:
            plot_results(results)
        if self.csv_var.get() or self.html_var.get():
            export_results(results, self.csv_var.get() + ".csv" or None, self.html_var.get() or None)


if __name__ == '__main__':
    ProfilerGUI().mainloop()