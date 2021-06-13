import tkinter as _Tkinter
from win32api import GetSystemMetrics

from logging import _is_log_on
from global_variables import GlobalVariables


# ----------------------------------------------- Logging window ---------------------------------------------------- #


class LoggingWindow:
    # position and size
    WINDOW_SIZE = {"width": 400, "height": 120}
    WINDOW_POSITION = "%dx%d" % (WINDOW_SIZE["width"], WINDOW_SIZE["height"])
    # images sizes
    CB_IMAGE_SIZE = (300, 80)
    MERIT_LOGO_SIZE = (78, 30)

    # child windows
    pWindow = None
    eWindow = None
    iWindow = None

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.title("Logging Window")
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=False, height=False)
        # execute sub-functions
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        # loop the window to keep it open until close event
        self.window.mainloop()

    def __del__(self):
        del self.pWindow
        del self.eWindow
        del self.iWindow

    def _create_widgets(self):
        self.label_name = _Tkinter.Label(master=self.window, text="Username:")
        self.entry_name = _Tkinter.Entry(master=self.window)
        self.entry_name.insert(0, GlobalVariables.Username)
        self.label_password = _Tkinter.Label(master=self.window, text="Password:")
        self.entry_password = _Tkinter.Entry(master=self.window, show="*")
        self.button_log_in = _Tkinter.Button(master=self.window, text="Process logging", command=self.log_in_button_event, font=("Times", 12, "normal"))
        self.label_merit_text = _Tkinter.Label(master=self.window, text="Leszaj paint by num", font=("Times", 8, "italic"))

    def _place_widgets(self):
        self.label_name.grid(row=1, column=0, sticky=_Tkinter.W)
        self.entry_name.grid(row=1, column=1, ipadx=40, padx=10)
        self.label_password.grid(row=2, column=0, sticky=_Tkinter.W)
        self.entry_password.grid(row=2, column=1, ipadx=40, padx=10)
        self.button_log_in.grid(row=3, column=0, columnspan=2, pady=5)
        self.label_merit_text.grid(row=4, column=0, columnspan=2, sticky=_Tkinter.S + _Tkinter.W)

    def _define_binds(self):
        self.window.bind("<Return>", self.log_in_button_event)
        self.window.bind("<Control-KeyPress-a>", self._bind_ctr_a)
        self.window.bind("<Control-KeyPress-A>", self._bind_ctr_a)

    def _bind_ctr_a(self, event):
        if event.widget in (self.entry_name, self.entry_password):
            None

    def log_in_button_event(self, *_args):
        self.button_log_in.config(text="Logging...", font=("Times", 12, "italic"))
        self.button_log_in.update()

        if _is_log_on(self.entry_name.get(), self.entry_password.get()):
            self.window.destroy()
            self.pWindow = ProjectWindow()
            self.eWindow = EtiquetteWindow()
            self.iWindow = ImageParseWindow()
            self.window.mainloop()   # loop the window to keep it open until close event
        else:
            self.button_log_in.config(text="Logging...", font=("Times", 12, "normal"))
            self.button_log_in.update()


# ------------------------------------------------ Imgage parse window ---------------------------------------------- #


class ImageParseWindow():
    # position and size
    WINDOW_SIZE = {"width": 800, "height": 800, }
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["height"]) // 2,
                                 (GetSystemMetrics(1) - WINDOW_SIZE["width"]) // 2)
    WINDOW_DIMENTIONS = "%dx%d" % (WINDOW_SIZE["width"], WINDOW_SIZE["height"])
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)
    CB_LOGO_SIZE = (50, 50)
    VECTOR_LOGO_SIZE = (80, 30)
    VTESTSTUDIO_LOGO_SIZE = (50, 50)

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.title("Image Parse Window")
        self.window.geometry(self.WINDOW_DIMENTIONS)
        self.window.resizable(width=False, height=False)
        # import previously saved settings
        #self._import_settings_file()
        # execute sub-functions
        self._define_variables()
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        self._config_widgets()

    def _define_variables(self):
        self.var_project = _Tkinter.StringVar(master=self.window)
        self.var_tracker = _Tkinter.StringVar(master=self.window)
        self.var_test_run = _Tkinter.StringVar(master=self.window)
        self.var_test_results_path = _Tkinter.StringVar(master=self.window)
        self.var_progress = _Tkinter.DoubleVar(master=self.window, value=0.0)
        self.test_runs = {"": ""}

    def _create_widgets(self):

        #self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        #self.img_cb_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_CODEBEAMER_LOGO).resize(self.CB_LOGO_SIZE, Image.ANTIALIAS))
        #self.img_vector_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_VECTOR_LOGO).resize(self.VECTOR_LOGO_SIZE, Image.ANTIALIAS))
        #self.img_vteststudio_logo = ImageTk.PhotoImage(master=self.window,image=Image.open(IMAGE_VTESTSTUDIO_LOGO).resize(self.VTESTSTUDIO_LOGO_SIZE, Image.ANTIALIAS))

        self.label_output = _Tkinter.Label(master=self.window, text="OUTPUT:", font=("Times", 20, "bold"))
        self.label_project = _Tkinter.Label(master=self.window, text="Choose project:")
        self.label_tracker = _Tkinter.Label(master=self.window, text="Choose tracker:")
        self.label_test_run = _Tkinter.Label(master=self.window, text="Choose test run:")

        self.labelframe_preprocessing = _Tkinter.LabelFrame(master=self.window, text="Preprocessing")
        self.label_preprocessing = _Tkinter.Label(master=self.labelframe_preprocessing,  text="Child widget of the Preprocessing")
        self.label_preprocessing.pack(padx=10, pady=10)
        self.labelframe_preprocessing.pack()

        self.labelframe_processing = _Tkinter.LabelFrame(master=self.window, text="Processing")
        self.label_processing = _Tkinter.Label(master=self.labelframe_processing, text="Child widget of the Processing")
        self.label_processing.pack(padx=10, pady=10)
        self.labelframe_processing.pack(padx=10, pady=200)

        self.labelframe_postprocessing = _Tkinter.LabelFrame(master=self.window, text="Postprocessing")
        self.label_postprocessing = _Tkinter.Label(master=self.labelframe_postprocessing, text="Child widget of the Postprocessing")
        self.label_postprocessing.pack(padx=10, pady=10)
        self.labelframe_postprocessing.pack()


        #self.progress_bar = _Tkinter.ttk.Progressbar(master=self.window, orient=_Tkinter.HORIZONTAL, length=500, maximum=100, mode="determinate", variable=self.var_progress)

    def _place_widgets(self):
        #self.label_vector_image.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.E+_Tkinter.N)
        #self.label_vteststudio_image.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.N)

        #self.label_cb_image.grid(row=3, column=0, columnspan=3, sticky=_Tkinter.E)
        #self.label_project.grid(row=0, column=0, stick=_Tkinter.W)
        #self.option_menu_project.grid(row=4, column=1, columnspan=2, sticky=_Tkinter.W)
        #self.label_tracker.grid(row=1, column=0, stick=_Tkinter.W)
        #self.option_menu_tracker.grid(row=5, column=1, columnspan=2, sticky=_Tkinter.W)
        #self.label_test_run.grid(row=2, column=0, stick=_Tkinter.W)
        #self.progress_bar.grid(row=8, column=1, columnspan=2, sticky=_Tkinter.W, padx=10)
        #self.label_merit.grid(row=9, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.S)
        #self.label_merit_image.grid(row=9, column=0, columnspan=3, sticky=_Tkinter.E+_Tkinter.S)

        #self.labelframe_preprocessing.grid(row=7, column=0, columnspan=3, sticky=_Tkinter.W)
        #self.labelframe_processing.grid(row=8, column=0, columnspan=3, sticky=_Tkinter.W)
        #self.labelframe_postprocessing.grid(row=9, column=0, columnspan=3, sticky=_Tkinter.W)

        #self.label_output.grid(row=10, column=0, columnspan=3)
        None

    def _config_widgets(self):
        None

    def _define_binds(self):
        self.window.bind("<Return>", self.import_test_results)
        self.window.bind("<Control-KeyPress-s>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-S>", self._bind_ctr_s)

    def _bind_ctr_s(self, _event):
        None

    def _import_settings_set_data(self, settings_set):
        None

    def _export_settings_set_data(self):
        None

    def select_result_file_path(self, *_args):
        None

    def import_test_results(self):
        None


# -------------------------------------------------- Project window ------------------------------------------------- #


class ProjectWindow():
    # position and size
    WINDOW_SIZE = {"width": 300, "height": 800, }
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["height"]) // 2,
                                  (GetSystemMetrics(1) - WINDOW_SIZE["width"]) // 2)
    WINDOW_DIMENTIONS = "%dx%d" % (WINDOW_SIZE["width"], WINDOW_SIZE["height"])
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)
    CB_LOGO_SIZE = (50, 50)
    VECTOR_LOGO_SIZE = (80, 30)
    VTESTSTUDIO_LOGO_SIZE = (50, 50)

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.title("Project Window")
        self.window.geometry(self.WINDOW_DIMENTIONS)
        self.window.resizable(width=False, height=True)
        self._define_variables()
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        self._config_widgets()

    def _define_variables(self):
        self.var_project = _Tkinter.StringVar(master=self.window)
        self.var_tracker = _Tkinter.StringVar(master=self.window)
        self.var_test_run = _Tkinter.StringVar(master=self.window)
        self.var_test_results_path = _Tkinter.StringVar(master=self.window)
        self.var_progress = _Tkinter.DoubleVar(master=self.window, value=0.0)
        self.test_runs = {"": ""}

    def _create_widgets(self):
        self.main_menu_bar = _Tkinter.Menu(master=self.window)
        self.menu_file = _Tkinter.Menu(master=self.main_menu_bar, tearoff=0)
        self.menu_file.add_separator()
        self.menu_file.add_cascade(label="Exit", command=self.window.destroy)
        #self.menu_file.add_cascade(label="Exit", command=super(LoggingWindow, self).__del__())  # use parent constructor
        self.main_menu_bar.add_cascade(label="File", menu=self.menu_file)
        self.label_input = _Tkinter.Label(master=self.window, text="INPUT:", font=("Times", 20, "bold"))
        self.label_test_results = _Tkinter.Label(master=self.window, text="vTest Studio test results:")
        self.entry_test_results_path = _Tkinter.Entry(master=self.window, textvariable=self.var_test_results_path, width=65)
        #self.button_select_test_results_file = _Tkinter.Button(master=self.window, text="Select file", command=self.select_result_file_path)
        self.label_output = _Tkinter.Label(master=self.window, text="OUTPUT:", font=("Times", 20, "bold"))
        self.label_project = _Tkinter.Label(master=self.window, text="Choose project:")
        self.label_tracker = _Tkinter.Label(master=self.window, text="Choose tracker:")
        self.label_test_run = _Tkinter.Label(master=self.window, text="Choose test run:")
        self.option_menu_test_run = _Tkinter.OptionMenu(self.window, self.var_test_run, *self.test_runs)
        #self.button_import = _Tkinter.Button(master=self.window, text="Import Test Results", font=("Times", 12, "normal"), command=self.import_test_results)
        self.label_progress = _Tkinter.Label(master=self.window, text="Importing progress:")

    def _place_widgets(self):
        self.window.config(menu=self.main_menu_bar)
        self.label_input.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.N)
        self.label_test_results.grid(row=1, column=0, sticky=_Tkinter.W)
        self.entry_test_results_path.grid(row=1, column=1, sticky=_Tkinter.W + _Tkinter.E, padx=10)
        #self.button_select_test_results_file.grid(row=1, column=2, padx=10)
        self.label_output.grid(row=3, column=0, columnspan=3)
        self.label_project.grid(row=4, column=0, stick=_Tkinter.W)
        self.label_tracker.grid(row=5, column=0, stick=_Tkinter.W)
        self.label_test_run.grid(row=6, column=0, stick=_Tkinter.W)
        self.option_menu_test_run.grid(row=6, column=1, columnspan=2, sticky=_Tkinter.W)
        #self.button_import.grid(row=7, column=0, columnspan=3, pady=10)
        self.label_progress.grid(row=8, column=0, stick=_Tkinter.W)

    def _config_widgets(self):
        None

    def _define_binds(self):
        self.window.bind("<Return>", self.return_button)
        self.window.bind("<Control-KeyPress-s>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-S>", self._bind_ctr_s)

    def _bind_ctr_s(self, _event):
        None

    def return_button(self):
        None


# -------------------------------------------------- Etiquette parse ------------------------------------------------ #


class EtiquetteWindow():
    # position and size
    WINDOW_SIZE = {"width": 500, "height": 500, }
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["height"]) // 2,
                                  (GetSystemMetrics(1) - WINDOW_SIZE["width"]) // 2)
    WINDOW_DIMENTIONS = "%dx%d" % (WINDOW_SIZE["width"], WINDOW_SIZE["height"])
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)
    CB_LOGO_SIZE = (50, 50)
    VECTOR_LOGO_SIZE = (80, 30)
    VTESTSTUDIO_LOGO_SIZE = (50, 50)

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.title("Etiquette Window")
        self.window.geometry(self.WINDOW_DIMENTIONS)
        self.window.resizable(width=False, height=False)
        self._define_variables()
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        self._config_widgets()

    def _define_variables(self):
        None

    def _create_widgets(self):
        self.label_input = _Tkinter.Label(master=self.window, text="label_input", font=("Times", 20, "bold"))
        self.label_output = _Tkinter.Label(master=self.window, text="label_output", font=("Times", 20, "bold"))
        self.label_project = _Tkinter.Label(master=self.window, text="label_project")
        self.label_tracker = _Tkinter.Label(master=self.window, text="label_tracker")
        self.label_test_run = _Tkinter.Label(master=self.window, text="label_test_run")
        self.label_progress = _Tkinter.Label(master=self.window, text="label_progress")

    def _place_widgets(self):
        self.label_input.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.N)
        self.label_output.grid(row=3, column=0, columnspan=3)
        self.label_project.grid(row=4, column=0, stick=_Tkinter.W)
        self.label_tracker.grid(row=5, column=0, stick=_Tkinter.W)
        self.label_test_run.grid(row=6, column=0, stick=_Tkinter.W)
        self.label_progress.grid(row=8, column=0, stick=_Tkinter.W)

    def _config_widgets(self):
        None

    def _define_binds(self):
        self.window.bind("<Return>", self.return_button)
        self.window.bind("<Control-KeyPress-s>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-S>", self._bind_ctr_s)

    def _bind_ctr_s(self, _event):
        None

    def return_button(self):
        None
