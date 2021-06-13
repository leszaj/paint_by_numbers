from os import path, getcwd
from copy import deepcopy
import tkinter as _Tkinter
#from ttk import Progressbar, Separator
from PIL import ImageTk, Image
from win32api import GetSystemMetrics

"""
from Functionalities import log_into_cb, export_cb_req_to_vector, import_vt_tc_to_cb, import_vt_results_to_cb, \
    import_diva_tc_to_cb, import_diva_results_to_cb
from CodeBeamer_Handlers import get_test_runs
from Utilities import REPOSITORY_PATH, FILTER_TYPES, REQUIREMENTS_FILTERS_MAPPING, filter_trackers, \
    does_dir_contain_file_with_extension, find_files_with_extension, open_manual_in_browser, \
    set_export_verification_links_flag, get_export_verification_links_flag
from Common_Popups import display_error_functionality_not_available, display_error_type_again, display_error_busy, display_error_incorrect_test_project_path,\
    display_window_save_as, display_window_open_file, display_window_open_directory, display_test_runs_update_error
from GUI_settings import open_settings_file, save_settings_file

"""


# ------------------------------------------------------- PATHS ------------------------------------------------------ #


# folders paths
SETTINGS_PATH = getcwd() + "\\Settings"
IMAGES_PATH = getcwd()[:getcwd().find("01_CommonTools\\CBInterface")] + "01_CommonTools\\CBInterface\\resources\\"
# merit images paths
IMAGE_MERIT_ICO = IMAGES_PATH + "Merit.ico"
IMAGE_MERIT_LOGO = IMAGES_PATH + "Merit_logo.png"
# codeBeamer images paths
IMAGE_CODEBEAMER = IMAGES_PATH + "CodeBeamer.png"
IMAGE_CODEBEAMER_LOGO = IMAGES_PATH + "CodeBeamer_logo.png"
# vector images paths
IMAGE_VECTOR_LOGO = IMAGES_PATH + "Vector_logo.png"
IMAGE_VTESTSTUDIO_LOGO = IMAGES_PATH + "vTestStudio_logo.png"
IMAGE_DIVA_LOGO = IMAGES_PATH + "DiVa_logo.png"



# ---------------------------------------------------- logging obj ---------------------------------------------------- #


class LoggingWindow:
    # position and size
    WINDOW_SIZE = {"width": 304, "height": 203}
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["width"]) // 2, (GetSystemMetrics(1) - WINDOW_SIZE["height"]) // 2)
    # images sizes
    CB_IMAGE_SIZE = (300, 80)
    MERIT_LOGO_SIZE = (78, 30)

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("CBInterface 12.0 - log in")
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=False, height=False)
        # execute sub-functions
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        # loop the window to keep it open until close event
        self.window.mainloop()

    def _create_widgets(self):
        """
        Method creates widgets that are used in this window.

        :return: None
        """
        # load images
        #self.img_cb = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_CODEBEAMER).resize(self.CB_IMAGE_SIZE, Image.ANTIALIAS))
        #self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        # define window objects
        self.label_cb_image = _Tkinter.Label(master=self.window, image=self.img_cb)
        self.label_name = _Tkinter.Label(master=self.window, text="Username:")
        self.entry_name = _Tkinter.Entry(master=self.window)
        self.label_password = _Tkinter.Label(master=self.window, text="Password:")
        self.entry_password = _Tkinter.Entry(master=self.window, show="*")
        self.button_log_in = _Tkinter.Button(master=self.window, text="Log me into codeBeamer", command=self.log_in_button_event, font=("Times", 12, "normal"))
        self.label_merit_text = _Tkinter.Label(master=self.window, text="Merit Automotive Electronics", font=("Times", 8, "italic"))
        self.label_merit_image = _Tkinter.Label(master=self.window, image=self.img_merit_logo)

    def _place_widgets(self):
        """
        Method places widgets in the window.

        :return: None
        """
        # place objects in window
        self.label_cb_image.grid(row=0, column=0, columnspan=2)
        self.label_name.grid(row=1, column=0, sticky=_Tkinter.W)
        self.entry_name.grid(row=1, column=1, ipadx=40, padx=10)
        self.label_password.grid(row=2, column=0, sticky=_Tkinter.W)
        self.entry_password.grid(row=2, column=1, ipadx=40, padx=10)
        self.button_log_in.grid(row=3, column=0, columnspan=2, pady=5)
        self.label_merit_text.grid(row=4, column=0, columnspan=2, sticky=_Tkinter.S+_Tkinter.W)
        self.label_merit_image.grid(row=4, column=0, columnspan=2, sticky=_Tkinter.S+_Tkinter.E)

    def _define_binds(self):
        """
        Method links button binds with functions/methods.

        :return: None
        """
        None#self.window.bind("<F1>", bind_open_manual)
        self.window.bind("<Return>", self.log_in_button_event)
        self.window.bind("<Control-KeyPress-a>", self._bind_ctr_a)
        self.window.bind("<Control-KeyPress-A>", self._bind_ctr_a)

    def _bind_ctr_a(self, event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+a bind is pressed.

        :param event:
            Standard parameter passed by bind method.

        :return: None
        """
        if event.widget in (self.entry_name, self.entry_password):
            None#bind_select_all(event)

    def log_in_button_event(self, *_args):
        """
        Function that is executed after pressing 'log in' button.
        It tries to establish connection with codeBeamer server and then try to log in the user.
        It throws different errors when:
        - connection with codeBeamer server could not be established
        - username/password are incorrect

        :return: None
        """
        global Username
        global Password
        global CB_Version
        global Projects
        global Projects_Names

        # update global - username, password
        Username = self.entry_name.get()
        Password = self.entry_password.get()

        self.button_log_in.config(text="Logging into codeBeamer..", font=("Times", 12, "italic"))
        self.button_log_in.update()

        #is_ok, CB_Version, Projects = log_into_cb(user=Username, password=Password, parent_window=self.window)
        Projects.update({"": ["", {"": ["", ""]}]})
        Projects_Names = Projects.keys()
        Projects_Names.sort()

        #if is_ok:
        #    self.window.destroy()
        #    ActionWindow()
        #else:
        #    self.button_log_in.config(text="Log me into codeBeamer", font=("Times", 12, "normal"))
       #     self.button_log_in.update()


# -------------------------------------------------- Choose purpose -------------------------------------------------- #


class ActionWindow:
    # position and size
    WINDOW_SIZE = {"width": 429, "height": 351}
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["width"]) // 2, (GetSystemMetrics(1) - WINDOW_SIZE["height"]) // 2)
    # images sizes
    CB_IMAGE_SIZE = (400, 107)
    MERIT_LOGO_SIZE = (78, 30)
    VECTOR_LOGO_SIZE = (80, 30)
    VTESTSTUDIO_LOGO_SIZE = (70, 70)
    DIVA_LOG_SIZE = (60, 60)

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("CBInterface 12.0 - choose action")
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=False, height=False)
        # execute sub-functions
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        # loop the window to keep it open until close event
        self.window.mainloop()

    def _create_widgets(self):
        """
        Method creates widgets that are used in this window.

        :return: None
        """
        # load images
        self.img_cb = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_CODEBEAMER).resize(self.CB_IMAGE_SIZE, Image.ANTIALIAS))
        self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        self.img_vector_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_VECTOR_LOGO).resize(self.VECTOR_LOGO_SIZE, Image.ANTIALIAS))
        self.img_vteststudio_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_VTESTSTUDIO_LOGO).resize(self.VTESTSTUDIO_LOGO_SIZE, Image.ANTIALIAS))
        self.img_diva_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_DIVA_LOGO).resize(self.DIVA_LOG_SIZE, Image.ANTIALIAS))
        # define window objects
        self.label_cb_image = _Tkinter.Label(master=self.window, image=self.img_cb)
        self.label_vector_logo = _Tkinter.Label(master=self.window, image=self.img_vector_logo)
        self.label_vteststudio_logo = _Tkinter.Label(master=self.window, image=self.img_vteststudio_logo)
        self.label_diva_logo = _Tkinter.Label(master=self.window, image=self.img_diva_logo)
        self.separator_horizontal_1 = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        self.button_cb_req_to_vector = _Tkinter.Button(master=self.window, command=self.open_export_req_to_vector_window, width=45, text="Export codeBeamer requirements to Vector format.")
        self.separator_horizontal_2 = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        self.button_vt_tc_to_cb = _Tkinter.Button(master=self.window, command=self.open_import_vt_tc_window, width=45, text="Import codeBeamer test procedures from vTest Studio.")
        self.button_vt_res_to_cb = _Tkinter.Button(master=self.window, command=self.open_import_vt_res_window, width=45, text="Import codeBeamer test results from vTest Studio.")
        self.separator_horizontal_3 = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        self.button_diva_tc_to_cb = _Tkinter.Button(master=self.window, command=self.open_import_diva_tc_window, width=45, text="Import codeBeamer test cases from CANoe.DiVa.")
        self.button_diva_res_to_cb = _Tkinter.Button(master=self.window, command=self.open_import_diva_res_window, width=45, text="Import codeBeamer test results from CANoe.DiVa.")
        self.separator_horizontal_4 = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        self.label_merit_text = _Tkinter.Label(master=self.window, text="Merit Automotive Electronics", font=("Times", 8, "italic"))
        self.label_merit_logo = _Tkinter.Label(master=self.window, image=self.img_merit_logo)

    def _place_widgets(self):
        """
        Method places widgets in the window.

        :return: None
        """
        # place objects in window
        self.label_cb_image.grid(row=0, column=0, columnspan=2, sticky=_Tkinter.N)
        self.separator_horizontal_1.grid(row=1, column=0, columnspan=2, sticky=_Tkinter.W + _Tkinter.E, pady=2, padx=5)
        self.label_vector_logo.grid(row=2, column=0, padx=5)
        self.button_cb_req_to_vector.grid(row=2, column=1, padx=5, pady=5)
        self.separator_horizontal_2.grid(row=3, column=0, columnspan=2, sticky=_Tkinter.W+_Tkinter.E, pady=2, padx=5)
        self.label_vteststudio_logo.grid(row=4, rowspan=2, column=0, padx=5)
        self.button_vt_tc_to_cb.grid(row=4, column=1, padx=5, pady=5)
        self.button_vt_res_to_cb.grid(row=5, column=1, padx=5, pady=5)
        self.separator_horizontal_3.grid(row=6, column=0, columnspan=2, sticky=_Tkinter.W+_Tkinter.E, pady=2, padx=5)
        self.label_diva_logo.grid(row=7, rowspan=2, column=0, padx=5)
        self.button_diva_tc_to_cb.grid(row=7, column=1, padx=5, pady=5)
        self.button_diva_res_to_cb.grid(row=8, column=1, padx=5, pady=5)
        self.separator_horizontal_4.grid(row=9, column=0, columnspan=2, sticky=_Tkinter.W+_Tkinter.E, pady=2, padx=5)
        self.label_merit_text.grid(row=10, column=0, columnspan=2, sticky=_Tkinter.S+_Tkinter.W)
        self.label_merit_logo.grid(row=10, column=0, columnspan=2, sticky=_Tkinter.S+_Tkinter.E)

    def _define_binds(self):
        """
        Method links button binds with functions/methods.

        :return: None
        """
        #self.window.bind("<F1>", bind_open_manual)
        self.window.bind("1", self.open_export_req_to_vector_window)
        self.window.bind("2", self.open_import_vt_tc_window)
        self.window.bind("3", self.open_import_vt_res_window)
        self.window.bind("4", self.open_import_diva_tc_window)
        self.window.bind("5", self.open_import_diva_res_window)

    @staticmethod
    def open_export_req_to_vector_window(*_args):
        """
        Method opens window for requirement export to vector format.

        :return: None
        """
        VectorRequirementsExportWindow()

    @staticmethod
    def open_import_vt_tc_window(*_args):
        """
        Method opens window for test cases import from vTest Studio.

        :return: None
        """
        VTestStudioTestCasesImportWindow()

    @staticmethod
    def open_import_vt_res_window(*_args):
        """
        Method opens window for test results import from vTest Studio.

        :return: None
        """
        #VTestStudioTestResultsImportWindow()


# --------------------------------------------------- Requirements --------------------------------------------------- #


class VectorRequirementsExportWindow():
    # position and size
    WINDOW_SIZE = {"width": 664, "height": 314}
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["width"]) // 2, (GetSystemMetrics(1) - WINDOW_SIZE["height"]) // 2)
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)
    CB_LOGO_SIZE = (50, 50)
    VECTOR_LOGO_SIZE = (80, 30)
    # settings
    SETTINGS_FILE_PATH = SETTINGS_PATH + "\\VectorRequirementsExport.cbi-set"
    Settings = []
    # other
    DEFAULT_NUMBER_OF_FILTERS = 0
    MAX_NUMBER_OF_FILTERS = 10
    FILTER_TYPES = None#FILTER_TYPES

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("CBInterface 12.0 - export requirements to vector format")
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=False, height=False)
        # use parent constructor
        super(VectorRequirementsExportWindow, self).__init__()
        # import previously saved settings
        #self._import_settings_file()
        # execute sub-functions
        self._define_variables()
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        self._config_widgets()
        # loop the window to keep it open until close event
        self.window.mainloop()

    def _define_variables(self):
        """
        Method define variables that are used in this window.

        :return: None
        """
        self.var_file_path = _Tkinter.StringVar(master=self.window, value="")
        self.var_project = _Tkinter.StringVar(master=self.window)
        self.var_tracker = _Tkinter.StringVar(master=self.window)
        self.var_progress = _Tkinter.DoubleVar(master=self.window, value=0.0)
        self.var_number_of_filters = _Tkinter.IntVar(master=self.window, value=self.DEFAULT_NUMBER_OF_FILTERS)
        # define filters variables in list
        self.var_use_filter_list = []
        self.var_filter_value_list = []
        self.var_filter_type_list = []
        self.var_filter_variable_list = []
        for i in range(self.MAX_NUMBER_OF_FILTERS):
            self.var_use_filter_list.append(_Tkinter.BooleanVar(master=self.window))
            self.var_filter_value_list.append(_Tkinter.StringVar(master=self.window, value=""))
            self.var_filter_type_list.append(_Tkinter.StringVar(master=self.window))
            self.var_filter_variable_list.append(_Tkinter.StringVar(master=self.window))

    def _create_widgets(self):
        """
        Method creates widgets that are used in this window.

        :return: None
        """
        # create menu bar
        self.main_menu_bar = _Tkinter.Menu(master=self.window)
        # add menu - file
        self.menu_file = _Tkinter.Menu(master=self.main_menu_bar, tearoff=0)
        None#self.menu_file.add_cascade(label="Help", command=bind_open_manual)
        self.menu_file.add_separator()
        self.menu_file.add_cascade(label="Exit", command=self.window.destroy)
        self.main_menu_bar.add_cascade(label="File", menu=self.menu_file)
        # add menu - settings
        self._create_settings_menu(main_menu_bar=self.main_menu_bar)
        # load images
        self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        self.img_cb_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_CODEBEAMER_LOGO).resize(self.CB_LOGO_SIZE, Image.ANTIALIAS))
        self.img_vector_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_VECTOR_LOGO).resize(self.VECTOR_LOGO_SIZE, Image.ANTIALIAS))
        # define window objects
        self.label_input = _Tkinter.Label(master=self.window, text="INPUT:", font=("Times", 20, "bold"))
        self.label_cb_image = _Tkinter.Label(master=self.window, image=self.img_cb_logo)
        self.label_project = _Tkinter.Label(master=self.window, text="Choose project:")
        self.option_menu_project = _Tkinter.OptionMenu(self.window, self.var_project, *Projects_Names)
        self.label_tracker = _Tkinter.Label(master=self.window, text="Choose tracker:")
        self.option_menu_tracker = _Tkinter.OptionMenu(self.window, self.var_tracker, *Projects[self.var_project.get()][1].keys())
        self.label_filter_number = _Tkinter.Label(master=self.window, text="Choose filters number:")
        self.option_menu_filters_number = _Tkinter.OptionMenu(self.window, self.var_number_of_filters, *[str(i) for i in range(self.MAX_NUMBER_OF_FILTERS+1)])
        self.frame_filters = _Tkinter.Frame(master=self.window, bd=2, relief=_Tkinter.RIDGE)
        self.separator_horizontal = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        self.label_output = _Tkinter.Label(master=self.window, text="OUTPUT:", font=("Times", 20, "bold"))
        self.label_vector_image = _Tkinter.Label(master=self.window, image=self.img_vector_logo)
        self.label_file_desc = _Tkinter.Label(master=self.window, text="Vector trace items:")
        self.entry_file_path = _Tkinter.Entry(master=self.window, textvariable=self.var_file_path)
        self.button_select_file = _Tkinter.Button(master=self.window, text="Save as", command=self.select_requirements_file_path)
        self.button_export = _Tkinter.Button(master=self.window, text="Export Requirements", command=self.export_requirements, font=("Times", 12, "normal"))
        self.label_progress = _Tkinter.Label(master=self.window, text="Exporting progress:")
        self.progress_bar = _Tkinter.Progressbar(master=self.window, orient=_Tkinter.HORIZONTAL, mode="determinate", maximum=100, variable=self.var_progress)
        self.label_merit = _Tkinter.Label(master=self.window, font=("Times", 8, "italic"), text="Merit Automotive Electronics")
        self.label_merit_image = _Tkinter.Label(master=self.window, image=self.img_merit_logo)
        # define filter objects in list (adjust its number to Number_of_Filters variable)
        self.label_filter_list = []
        self.checkbutton_filter_list = []
        self.entry_filter_value_list = []
        self.option_menu_filter_type_list = []
        self.option_menu_filter_variable_list = []
        for i in range(self.MAX_NUMBER_OF_FILTERS):
            self.label_filter_list.append(_Tkinter.Label(master=self.frame_filters, text="Set filter %d:" % (i+1), width=8))
            self.checkbutton_filter_list.append(_Tkinter.Checkbutton(master=self.frame_filters, variable=self.var_use_filter_list[i]))
            self.entry_filter_value_list.append(_Tkinter.Entry(master=self.frame_filters, textvariable=self.var_filter_value_list[i]))
            None#self.option_menu_filter_type_list.append(_Tkinter.OptionMenu(self.frame_filters, self.var_filter_type_list[i], *FILTER_TYPES))
            None#self.option_menu_filter_variable_list.append(_Tkinter.OptionMenu(self.frame_filters, self.var_filter_variable_list[i], *REQUIREMENTS_FILTERS_MAPPING.keys()))

    def _place_widgets(self):
        """
        Method places widgets in the window.

        :return: None
        """
        self._place_filter_widgets()
        # add menu bar
        self.window.config(menu=self.main_menu_bar)
        # place objects in window
        self.label_input.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.N)
        self.label_cb_image.grid(row=0, column=2, rowspan=2, sticky=_Tkinter.E+_Tkinter.N, padx=5, pady=5)
        self.label_project.grid(row=1, column=0, sticky=_Tkinter.W, padx=5)
        self.option_menu_project.grid(row=1, column=1, sticky=_Tkinter.W)
        self.label_tracker.grid(row=2, column=0, sticky=_Tkinter.W, padx=5)
        self.option_menu_tracker.grid(row=2, column=1,sticky=_Tkinter.W)
        self.label_filter_number.grid(row=3, column=0, sticky=_Tkinter.W, padx=5)
        self.option_menu_filters_number.grid(row=3, column=1, sticky=_Tkinter.W)
        self.frame_filters.grid(row=4, column=0, columnspan=3, padx=15, sticky=_Tkinter.N+_Tkinter.E+_Tkinter.S+_Tkinter.W)
        self.separator_horizontal.grid(row=5, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.E, pady=5, padx=5)
        self.label_output.grid(row=6, column=0, columnspan=3, sticky=_Tkinter.N)
        self.label_vector_image.grid(row=6, column=0, columnspan=3, sticky=_Tkinter.N+_Tkinter.E)
        self.label_file_desc.grid(row=7, column=0, sticky=_Tkinter.W, padx=5)
        self.entry_file_path.grid(row=7, column=1, sticky=_Tkinter.W, padx=10, ipadx=160)
        self.button_select_file.grid(row=7, column=2, sticky=_Tkinter.W)
        self.button_export.grid(row=8, column=0, columnspan=3, pady=10)
        self.label_progress.grid(row=9, column=0, sticky=_Tkinter.W, padx=5)
        self.progress_bar.grid(row=9, column=1, columnspan=2, sticky=_Tkinter.W+_Tkinter.E, padx=10)
        self.label_merit.grid(row=10, column=0, columnspan=3, sticky=_Tkinter.S+_Tkinter.W)
        self.label_merit_image.grid(row=10, column=0, columnspan=3, sticky=_Tkinter.S+_Tkinter.E)

    def _place_filter_widgets(self, *_args):
        """
        Method places widgets related to filters in the frame_filters.

        :return: None
        """
        filters_number = self.var_number_of_filters.get()
        for i in range(filters_number):
            self.label_filter_list[i].grid(row=i, column=0, sticky=_Tkinter.W, padx=2)
            self.checkbutton_filter_list[i].grid(row=i, column=1, sticky=_Tkinter.W)
            self.entry_filter_value_list[i].grid(row=i, column=2, sticky=_Tkinter.W+_Tkinter.E, ipadx=65, padx=2)
            self.option_menu_filter_type_list[i].grid(row=i, column=3, sticky=_Tkinter.E, padx=2)
            self.option_menu_filter_variable_list[i].grid(row=i, column=4, sticky=_Tkinter.E, padx=2)
        for i in range(filters_number, self.MAX_NUMBER_OF_FILTERS):
            self.label_filter_list[i].grid_forget()
            self.checkbutton_filter_list[i].grid_forget()
            self.entry_filter_value_list[i].grid_forget()
            self.option_menu_filter_type_list[i].grid_forget()
            self.option_menu_filter_variable_list[i].grid_forget()
        self.frame_filters.update()
        if filters_number == 0:
            self.frame_filters.grid_forget()
        else:
            self.frame_filters.grid(row=4, column=0, columnspan=5, padx=15, sticky=_Tkinter.N+_Tkinter.E+_Tkinter.S+_Tkinter.W)

    def _config_widgets(self):
        """
        Method configures additional settings for widgets.

        :return: None
        """
        # configure width of option menu widgets
        self.option_menu_project.config(width=60)
        self.option_menu_tracker.config(width=60)
        self.option_menu_filters_number.config(width=5)
        for i in range(self.MAX_NUMBER_OF_FILTERS):
            self.option_menu_filter_type_list[i].config(width=5)
            self.option_menu_filter_variable_list[i].config(width=25)
        # trace values
        self.var_project.trace("w", self._update_trackers)
        self.var_number_of_filters.trace("w", self._place_filter_widgets)

    def _define_binds(self):
        """
        Method links button binds with functions/methods.

        :return: None
        """
        #self.window.bind("<F1>", bind_open_manual)
        self.window.bind("<Return>", self.export_requirements)
        self.window.bind("<Control-KeyPress-a>", self._bind_ctr_a)
        self.window.bind("<Control-KeyPress-A>", self._bind_ctr_a)
        self.window.bind("<Control-KeyPress-s>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-S>", self._bind_ctr_s)

    def _update_trackers(self, *_args):
        """
        Method updates option_menu_tracker with trackers available for this project.

        :return: None
        """
        self.option_menu_tracker["menu"].delete(0, "end")
        trackers = None#[""] + filter_trackers(projects=Projects, project=self.var_project.get(), trackers_type="Requirement")
        trackers.sort()
        for _tracker in trackers:
            self.option_menu_tracker["menu"].add_command(label=_tracker, command=lambda value=_tracker: self.var_tracker.set(value))
        self.var_tracker.set("")
        self.option_menu_tracker.update()

    def _bind_ctr_a(self, event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+a bind is pressed.

        :param event:
            Standard parameter passed by bind method.

        :return: None
        """
        if event.widget in [self.entry_file_path] + self.entry_filter_value_list:
            None#bind_select_all(event)

    def _bind_ctr_s(self, _event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+s bind is pressed.

        :param _event:
            Standard parameter passed by bind method.

        :return: None
        """
        self._save_settings()

    def _import_settings_set_data(self, settings_set):
        """
        Method imports settings set data into window variables.

        :param settings_set: dict
            Dictionary with data to import.

        :return: None
        """
        self.var_project.set(settings_set["self.var_project"])
        self.var_tracker.set(settings_set["self.var_tracker"])
        if settings_set["self.var_file_path"].startswith("\\"):
            None#_var_file_path = REPOSITORY_PATH + settings_set["self.var_file_path"]
        else:
            _var_file_path = settings_set["self.var_file_path"]
        self.var_file_path.set(_var_file_path)
        for var_name, value in settings_set.iteritems():
            if var_name in ("Setting name", "self.var_project", "self.var_tracker", "self.var_file_path"):
                continue
            None#if type(value) in (str, unicode):
            None  #   exec ("%s.set('%s')" % (var_name, value))
            None#else:
            None  #    exec("%s.set(%s)" % (var_name, value))

    def _export_settings_set_data(self):
        """
        Method exports window variables into settings set data.

        :return: dict
            Dictionary with exported data.
        """
        settings_set = {
            "self.var_project": self.var_project.get(),
            "self.var_tracker": self.var_tracker.get(),
            "self.var_number_of_filters": self.var_number_of_filters.get(),
            #"self.var_file_path": self.var_file_path.get().replace(REPOSITORY_PATH, "")
        }
        for i in range(self.MAX_NUMBER_OF_FILTERS):
            settings_set["self.var_use_filter_list[%d]" % i] = self.var_use_filter_list[i].get()
            settings_set["self.var_filter_value_list[%d]" % i] = self.var_filter_value_list[i].get()
            settings_set["self.var_filter_type_list[%d]" % i] = self.var_filter_type_list[i].get()
            settings_set["self.var_filter_variable_list[%d]" % i] = self.var_filter_variable_list[i].get()
        return settings_set

    def _get_filters(self):
        """
        Method extracts filters settings from variables.

        :return: filters #list
            Each list element contains settings of one filter:
            - value (string)
            - filter type (string)
            - variable name (string)
        """
        filters = []
        for i in range(self.var_number_of_filters.get()):
            if self.var_use_filter_list[i].get():
                None  # filters.append([self.var_filter_value_list[i].get(), self.var_filter_type_list[i].get(),
                None  #                 REQUIREMENTS_FILTERS_MAPPING[self.var_filter_variable_list[i].get()]])
        return filters

    def select_requirements_file_path(self, *_args):
        """
        Method helps user to choose path for output file with requirements.

        :return: None
        """
        file_path = None#display_window_save_as(title="Save requirements file as", initial_directory=self.var_file_path.get(),
        None  #                       file_types=(("vTest Studio files", "*.vti-tso"), ("XML files", "*.xml"), ("All files", "*.*")),
        None  #                       default_extension=".vti-tso", parent_window=self.window)
        file_path = None#file_path.replace("/", "\\")
        if file_path:
            self.var_file_path.set(file_path)

    def export_requirements(self, *_args):
        """
        Method starts exporting process of codeBeamer requirements into vector format.

        :return: None
        """
        global Process_Running

        if Process_Running:
            None#display_error_busy(parent_window=self.window)
        else:
            # update status
            Process_Running = True
            self.button_export.config(text="Exporting Requirements..", font=("Times", 12, "italic"))
            self.button_export.update()
            # collect variables
            output_file_path = self.var_file_path.get()
            project_name = self.var_project.get()
            project_uri = Projects[project_name][0]
            tracker_name = self.var_tracker.get()
            tracker_uri = Projects[project_name][1][tracker_name][0]
            pbt = (self.progress_bar, self.var_progress, 0., 100.)
            filters =self._get_filters()
            # execute function
                #export_cb_req_to_vector(user=Username, password=Password, output_file_path=output_file_path, project=(project_name, project_uri), tracker=(tracker_name, tracker_uri),   items_filters=filters, progress_bar_tuple=pbt, parent_window=self.window)
            # update status
            self.button_export.config(text="Export Requirements", font=("Times", 12, "normal"))
            self.button_export.update()
            Process_Running = False


# ------------------------------------------- vTest Studio test procedures ------------------------------------------- #


class VTestStudioTestCasesImportWindow():
    # position and size
    WINDOW_SIZE = {"width": 643, "height": 610}
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["width"]) // 2, (GetSystemMetrics(1) - WINDOW_SIZE["height"]) // 2)
    CANVAS_FILES_SIZE = {"width": 600, "height": 250}
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)
    CB_LOGO_SIZE = (50, 50)
    VECTOR_LOGO_SIZE = (80, 30)
    VTESTSTUDIO_LOGO_SIZE = (50, 50)
    # settings
    SETTINGS_FILE_PATH = SETTINGS_PATH + "\\VTTestProceduresImport.cbi-set"
    Settings = []

    def __init__(self):
        self.window = _Tkinter.Tk()
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("CBInterface 12.0 - import vTest Studio test procedures")
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=False, height=False)
        # use parent constructor
        super(VTestStudioTestCasesImportWindow, self).__init__()
        # import previously saved settings
        self._import_settings_file()
        # execute sub-functions
        self._define_variables()
        self._create_widgets()
        self._place_widgets()
        self._define_binds()
        self._config_widgets()
        # loop the window to keep it open until close event
        self.window.mainloop()

    def _define_variables(self):
        """
        Method define variables that are used in this window.

        :return: None
        """
        self.var_project = _Tkinter.StringVar(master=self.window)
        self.var_tracker = _Tkinter.StringVar(master=self.window)
        self.var_progress = _Tkinter.DoubleVar(master=self.window, value=0.0)
        self.var_test_project_path = _Tkinter.StringVar(master=self.window, value="-")
        self.var_test_project_files = _Tkinter.StringVar(master=self.window, value="-")
        self.project_vtt_files = {}
        self.project_vparam_files = {}

    def _create_widgets(self):
        """
        Method creates widgets that are used in this window.

        :return: None
        """
        # create menu bar
        self.main_menu_bar = _Tkinter.Menu(master=self.window)
        # add menu - file
        self.menu_file = _Tkinter.Menu(master=self.main_menu_bar, tearoff=0)
        self.menu_file.add_cascade(label="Open Project", command=self.open_project)
        self.menu_file.add_separator()
        None#self.menu_file.add_cascade(label="Help", command=bind_open_manual)
        self.menu_file.add_separator()
        self.menu_file.add_cascade(label="Exit", command=self.window.destroy)
        self.main_menu_bar.add_cascade(label="File", menu=self.menu_file)
        # add menu - settings
        self._create_settings_menu(main_menu_bar=self.main_menu_bar, set_verification_links=True)
        # load images
        self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        self.img_cb_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_CODEBEAMER_LOGO).resize(self.CB_LOGO_SIZE, Image.ANTIALIAS))
        self.img_vector_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_VECTOR_LOGO).resize(self.VECTOR_LOGO_SIZE, Image.ANTIALIAS))
        self.img_vteststudio_logo = ImageTk.PhotoImage(master=self.window,image=Image.open(IMAGE_VTESTSTUDIO_LOGO).resize(self.VTESTSTUDIO_LOGO_SIZE, Image.ANTIALIAS))
        # define window objects - input
        self.label_input = _Tkinter.Label(master=self.window, text="INPUT:", font=("Times", 20, "bold"))
        self.label_vector_image = _Tkinter.Label(master=self.window, image=self.img_vector_logo)
        self.label_vteststudio_image = _Tkinter.Label(master=self.window, image=self.img_vteststudio_logo)
        self.frame_files = _Tkinter.Frame(master=self.window, borderwidth=1, relief=_Tkinter.SUNKEN)
        self.button_select_files = _Tkinter.Button(master=self.window, text="Select files", font=("Times", 12, "normal"), command=self.select_files)
        # define window objects - shared
        self.separator_horizontal = _Tkinter.Separator(master=self.window, orient=_Tkinter.HORIZONTAL)
        # define window objects - output
        self.label_output = _Tkinter.Label(master=self.window, text="OUTPUT:", font=("Times", 20, "bold"))
        self.label_cb_image = _Tkinter.Label(master=self.window, image=self.img_cb_logo)
        self.label_project = _Tkinter.Label(master=self.window, text="Choose project:")
        self.option_menu_project = _Tkinter.OptionMenu(self.window, self.var_project, *Projects_Names)
        self.label_tracker = _Tkinter.Label(master=self.window, text="Choose tracker:")
        self.option_menu_tracker = _Tkinter.OptionMenu(self.window, self.var_tracker, *Projects[self.var_project.get()][1].keys())
        self.button_import = _Tkinter.Button(master=self.window, text="Import Test Cases Procedures", font=("Times", 12, "normal"), command=self.import_test_procedures)
        self.label_progress = _Tkinter.Label(master=self.window, text="Importing progress:")
        self.progress_bar = _Tkinter.Progressbar(master=self.window, orient=_Tkinter.HORIZONTAL, length=500, maximum=100, mode="determinate", variable=self.var_progress)
        # define window objects - shared
        self.label_merit = _Tkinter.Label(master=self.window, font=("Times", 8, "italic"), text="Merit Automotive Electronics")
        self.label_merit_image = _Tkinter.Label(master=self.window, image=self.img_merit_logo)
        # define frame widgets
        self._create_frame_files_widgets()

    def _create_frame_files_widgets(self):
        """
        Method creates widgets that are used in this frame.

        :return: None
        """
        self.canvas_files = _Tkinter.Canvas(master=self.frame_files)
        self.frame_files_scrollbar_x = _Tkinter.Scrollbar(master=self.frame_files, orient=_Tkinter.HORIZONTAL, command=self.canvas_files.xview)
        self.frame_files_scrollbar_y = _Tkinter.Scrollbar(master=self.frame_files, orient=_Tkinter.VERTICAL, command=self.canvas_files.yview)
        self.frame_in_canvas_files = _Tkinter.Frame(master=self.canvas_files)
        self.label_project_path_text = _Tkinter.Label(master=self.frame_in_canvas_files, text="Project path:")
        self.label_project_path = _Tkinter.Label(master=self.frame_in_canvas_files, textvariable=self.var_test_project_path)
        self.label_project_files_text = _Tkinter.Label(master=self.frame_in_canvas_files, text="Project files:")
        self.label_project_files = _Tkinter.Label(master=self.frame_in_canvas_files, textvariable=self.var_test_project_files, justify=_Tkinter.LEFT)

    def _place_widgets(self):
        """
        Method places widgets in the window.

        :return: None
        """
        # add menu bar
        self.window.config(menu=self.main_menu_bar)
        # place objects in frame_files
        self._place_frame_files_widgets()
        # place objects in window
        self.label_input.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.N)
        self.label_vector_image.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.E+_Tkinter.N)
        self.label_vteststudio_image.grid(row=0, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.N)
        self.frame_files.grid(row=1, column=0, columnspan=3, stick=_Tkinter.N+_Tkinter.E+_Tkinter.S+_Tkinter.W, padx=10, pady=10)
        self.button_select_files.grid(row=2, column=0, columnspan=3)
        self.separator_horizontal.grid(row=3, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.E, pady=10)
        self.label_output.grid(row=4, column=0, columnspan=3)
        self.label_cb_image.grid(row=4, column=0, columnspan=3, sticky=_Tkinter.E)
        self.label_project.grid(row=5, column=0, stick=_Tkinter.W)
        self.option_menu_project.grid(row=5, column=1, columnspan=2, sticky=_Tkinter.W)
        self.label_tracker.grid(row=6, column=0, stick=_Tkinter.W)
        self.option_menu_tracker.grid(row=6, column=1, columnspan=2, sticky=_Tkinter.W)
        self.button_import.grid(row=7, column=0, columnspan=3, pady=10)
        self.label_progress.grid(row=8, column=0, stick=_Tkinter.W)
        self.progress_bar.grid(row=8, column=1, columnspan=2, sticky=_Tkinter.W, padx=10)
        self.label_merit.grid(row=9, column=0, columnspan=3, sticky=_Tkinter.W+_Tkinter.S)
        self.label_merit_image.grid(row=9, column=0, columnspan=3, sticky=_Tkinter.E+_Tkinter.S)

    def _place_frame_files_widgets(self):
        """
        Method places widgets in the frame_files.

        :return: None
        """
        # place objects in frame_files
        self.canvas_files.grid(row=0, column=0)
        self.frame_files_scrollbar_x.grid(row=1, column=0, sticky=_Tkinter.E + _Tkinter.S + _Tkinter.W)
        self.frame_files_scrollbar_y.grid(row=0, column=1, sticky=_Tkinter.N + _Tkinter.E + _Tkinter.S)
        # place objects in canvas_files
        self.frame_in_canvas_files.pack()
        self.canvas_files.create_window((0, 0), window=self.frame_in_canvas_files, anchor="nw")
        # place objects in frame_in_canvas_files
        self.label_project_path_text.grid(row=0, column=0, sticky=_Tkinter.W)
        self.label_project_path.grid(row=1, column=0, sticky=_Tkinter.W, padx=20)
        self.label_project_files_text.grid(row=2, column=0, sticky=_Tkinter.W)
        self.label_project_files.grid(row=3, column=0, sticky=_Tkinter.W, padx=20)

    def _define_binds(self):
        """
        Method links button binds with functions/methods.

        :return: None
        """
        None#self.window.bind("<F1>", bind_open_manual)
        self.window.bind("<Return>", self.import_test_procedures)
        self.window.bind("<Control-KeyPress-s>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-S>", self._bind_ctr_s)
        self.window.bind("<Control-KeyPress-O>", self._bind_ctr_o)
        self.window.bind("<Control-KeyPress-o>", self._bind_ctr_o)
        self.frame_in_canvas_files.bind("<Configure>", self._config_canvas_files)

    def _config_widgets(self):
        """
        Method configures additional settings for widgets.

        :return: None
        """
        # configure width of option menu widgets
        self.option_menu_project.config(width=60)
        self.option_menu_tracker.config(width=60)
        # configured frame_files widgets
        self.canvas_files.configure(yscrollcommand=self.frame_files_scrollbar_y.set, xscrollcommand=self.frame_files_scrollbar_x.set)
        self._config_canvas_files()
        # trace values
        self.var_project.trace("w", self._update_trackers)

    def _config_canvas_files(self, *_args):
        """
        Method configures canvas files in order to keep its size and possibility of scrolling.

        :return: None
        """
        self.canvas_files.configure(scrollregion=self.canvas_files.bbox("all"), **self.CANVAS_FILES_SIZE)

    def _update_trackers(self, *_args):
        """
        Method updates option_menu_tracker with trackers available for this project.

        :return: None
        """
        self.option_menu_tracker["menu"].delete(0, "end")
        trackers = None#[""] + filter_trackers(projects=Projects, project=self.var_project.get(), trackers_type="Test Case")
        trackers.sort()
        for _tracker in trackers:
            self.option_menu_tracker["menu"].add_command(label=_tracker, command=lambda value=_tracker: self.var_tracker.set(value))
        self.var_tracker.set("")
        self.option_menu_tracker.update()

    def _bind_ctr_s(self, _event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+s bind is pressed.

        :param _event:
            Standard parameter passed by bind method.

        :return: None
        """
        self._save_settings()

    def _bind_ctr_o(self, _event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+o bind is pressed.

        :param _event:
            Standard parameter passed by bind method.

        :return: None
        """
        self.open_project()

    def _import_settings_set_data(self, settings_set):
        """
        Method imports settings set data into window variables.

        :param settings_set: dict
            Dictionary with data to import.

        :return: None
        """
        self.var_project.set(settings_set["self.var_project"])
        self.var_tracker.set(settings_set["self.var_tracker"])
        if settings_set["self.var_test_project_path"].startswith("\\"):
            None  #project_path = REPOSITORY_PATH + settings_set["self.var_test_project_path"]
        else:
            None#project_path = settings_set["self.var_test_project_path"]

        #if does_dir_contain_file_with_extension(dir_path=project_path, extension=".vtsoproj"):
        #   self.var_test_project_path.set(project_path)
        #   self._find_project_files()
            imported_vtt_files = settings_set["self.project_vtt_files"]
            for vtt_file in self.project_vtt_files.iterkeys():
                self.project_vtt_files[vtt_file][0] = imported_vtt_files.get(vtt_file, [False, ])[0]
            imported_vparam_files = settings_set["self.project_vparam_files"]
            for vparam_file in self.project_vparam_files.iterkeys():
                self.project_vparam_files[vparam_file][0] = imported_vparam_files.get(vparam_file, [True, ])[0]
        self._update_files_shown()

    def _export_settings_set_data(self):
        """
        Method exports window variables into settings set data.

        :return: dict
            Dictionary with exported data.
        """
        settings_set = {
            "self.var_project": self.var_project.get(),
            "self.var_tracker": self.var_tracker.get(),
            #"self.var_test_project_path": self.var_test_project_path.get().replace(REPOSITORY_PATH, ""),
            "self.project_vparam_files": self.project_vparam_files,
            "self.project_vtt_files": self.project_vtt_files,
        }
        return settings_set

    def _find_project_files(self):
        """
        Method finds all files with *.vtt and *.vparam extension in test project directory.
        It updates variables that stores names and paths of this files

        :return: None
        """
        self.project_vtt_files.clear()
        self.project_vparam_files.clear()

        """
        for vtt_file_path in find_files_with_extension(dir_path=self.var_test_project_path.get(), extension=".vtt", nested_search=True):
            vtt_file_name = path.basename(vtt_file_path)
            self.project_vtt_files[vtt_file_name] = [True, vtt_file_path]
        for vparam_file_path in find_files_with_extension(dir_path=self.var_test_project_path.get(), extension=".vparam", nested_search=True):
            vparam_file_name = path.basename(vparam_file_path)
            if vparam_file_name.endswith("=PA.vparam"): # skip files created by vTest Studio
                continue
            self.project_vparam_files[vparam_file_name] = [True, vparam_file_path]
        self._update_files_shown()
        """

    def _update_files_shown(self):
        """
        Method updates text that is shown in frame_files widget.

        :return: None
        """
        # update vtt files
        vtt_files_names = self.project_vtt_files.keys()
        vtt_files_names.sort()
        vtt_files_str = ""
        for vtt_file in vtt_files_names:
            if self.project_vtt_files[vtt_file][0]:
                vtt_files_str += "\t- %s\n" % vtt_file
        if vtt_files_str:
            vtt_files_str.rstrip("\n")
        else:
            vtt_files_str = "\tNo files"
        # update vparam files
        vparam_files_names = self.project_vparam_files.keys()
        vparam_files_names.sort()
        vparam_files_str = ""
        for vparam_file in vparam_files_names:
            if self.project_vparam_files[vparam_file][0]:
                vparam_files_str += "\t- %s\n" % vparam_file
        if vparam_files_str:
            vparam_files_str.rstrip("\n")
        else:
            vparam_files_str = "\tNo files"
        self.var_test_project_files.set("Test Tree files with test cases:\n%s\nParameter files:\n%s" % (vtt_files_str, vparam_files_str))

    def _save_files_selection(self, vtt_files_selection, vparam_files_selection):
        """
        Method updates selection of files.

        :param vtt_files_selection: dict
            Dictionary with files selection to set.
            Keys: string
                Names of files.
            Values: bool
                Whether value was selected or not.
        :param vparam_files_selection: dict
            Dictionary with files selection to set.
            Keys: string
                Names of files.
            Values: bool
                Whether value was selected or not.

        :return: None
        """
        for vtt_file, status in vtt_files_selection.iteritems():
            if self.project_vtt_files.has_key(vtt_file):
                self.project_vtt_files[vtt_file][0] = status
        for vparam_file, status in vparam_files_selection.iteritems():
            if self.project_vparam_files.has_key(vparam_file):
                self.project_vparam_files[vparam_file][0] = status
        self._update_files_shown()

    def open_project(self, *_args):
        """
        Method opens dialog window and helps user to find path of vTest Studio project.

        :return: None
        """
        project_path = None#display_window_open_directory(title="Select directory with vTestStudio project:", initial_directory=self.var_test_project_path.get(), parent_window=self.window)
        project_path = project_path.replace("/", "\\")

    def select_files(self, *_args):
        """
        Method opens new top level window in order to help user select files to import.

        :return: None
        """
        main_files = {}
        additional_files = {}
        for vtt_file, (status, file_path) in self.project_vtt_files.iteritems():
            main_files[vtt_file] = status
        for vparam_file, (status, file_path) in self.project_vparam_files.iteritems():
            additional_files[vparam_file] = status
        TopLevelSelectFiles(main_files_name="vTest Studio test tree files:", main_files_dict=main_files,
                            additional_files_name="vTest Studio parameters files:", additional_files_dict=additional_files,
                            func_save=self._save_files_selection, parent_window=self.window)

    def import_test_procedures(self, *_args):
        """
        Method starts importing process of vTest Studio test procedure into codeBeamer.

        :return: None
        """
        global Process_Running

        if Process_Running:
            None #display_error_busy(parent_window=self.window)
        else:
            # update status
            Process_Running = True
            self.button_import.config(text="Importing Test Procedures..", font=("Times", 12, "italic"))
            self.button_import.update()
            # collect variables
            test_tree_files_paths = [vtt_file_path for vtt_file, (selected, vtt_file_path) in self.project_vtt_files.iteritems() if selected ]
            parameters_files_paths = [vparam_file_path for vparam_file, (selected, vparam_file_path) in self.project_vparam_files.iteritems() if selected ]
            project_name = self.var_project.get()
            project_uri = Projects[project_name][0]
            tracker_name = self.var_tracker.get()
            tracker_uri = Projects[project_name][1][tracker_name][0]
            pbt = (self.progress_bar, self.var_progress, 0., 100.)
            # execute function
                #import_vt_tc_to_cb(user=Username, password=Password, test_tree_files_paths=test_tree_files_paths, parameters_files_paths=parameters_files_paths, project=(project_name, project_uri), tracker=(tracker_name, tracker_uri), progress_bar_tuple=pbt, parent_window=self.window)
            # update status
            self.button_import.config(text="Import Test Cases Procedures", font=("Times", 12, "normal"))
            self.button_import.update()
            Process_Running = False





# --------------------------------------------- Top Level - Select Files --------------------------------------------- #


class TopLevelSelectFiles:
    # position and size
    WINDOW_SIZE = {"width": 400, "height": 400}
    CANVAS_FILES_SIZE = {"width": 450, "height": 500}
    # images sizes
    MERIT_LOGO_SIZE = (78, 30)

    def __init__(self, main_files_name, main_files_dict, additional_files_name, additional_files_dict, func_save, parent_window=None):
        # link method
        self._save_settings = func_save
        # create top level window
        self.window = _Tkinter.Toplevel(master=parent_window)
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("Select files")
        # execute sub-functions
        self._define_variables(main_files_dict=main_files_dict, additional_files_dict=additional_files_dict)
        self._create_widgets(main_files_name=main_files_name, additional_files_name=additional_files_name)
        self._place_widgets()
        self._define_binds()
        self._config_widgets()
        self.window.attributes('-topmost', True)

    def _define_variables(self, main_files_dict, additional_files_dict):
        """
        Method define variables that are used in this window.

        :param main_files_dict: dict
            Dictionary with names and initial states of files.
            Keys: string
                Name of file.
            Values: bool
                - True - file shall be selected
                - False - file shall be deselected
        :param additional_files_dict: dict
            Dictionary with names and initial states of files.
            Keys: string
                Name of file.
            Values: bool
                - True - file shall be selected
                - False - file shall be deselected

        :return: None
        """
        self.main_files = main_files_dict.keys()
        self.additional_files = additional_files_dict.keys()
        self.main_files.sort()
        self.additional_files.sort()
        # list variables for many files
        self.var_set_main_files_list = []
        self.var_set_additional_files_list = []
        for main_file in self.main_files:
            self.var_set_main_files_list.append(_Tkinter.BooleanVar(master=self.window, value=main_files_dict.get(main_file, True)))
        for additional_file in self.additional_files:
            self.var_set_additional_files_list.append(_Tkinter.BooleanVar(master=self.window, value=additional_files_dict.get(additional_file, True)))

    def _create_widgets(self, main_files_name, additional_files_name):
        """
        Method creates widgets that are used in this window.

        :param main_files_name: string
            Name of main files group.
        :param additional_files_name: string
            Name of additional files group.

        :return: None
        """
        # create menu bar
        self.main_menu_bar = _Tkinter.Menu(master=self.window)
        # add menu - file
        self.menu_file = _Tkinter.Menu(master=self.main_menu_bar, tearoff=0)
        self.menu_file.add_cascade(label="Select all files", command=self._select_all_files)
        self.menu_file.add_cascade(label="Deselect all files", command=self._deselect_all_files)
        self.menu_file.add_separator()
        #self.menu_file.add_cascade(label="Help", command=bind_open_manual)
        self.menu_file.add_separator()
        self.menu_file.add_cascade(label="Exit", command=self.window.destroy)
        self.main_menu_bar.add_cascade(label="File", menu=self.menu_file)
        # load images
        self.img_merit_logo = ImageTk.PhotoImage(master=self.window, image=Image.open(IMAGE_MERIT_LOGO).resize(self.MERIT_LOGO_SIZE, Image.ANTIALIAS))
        # window objects
        self.frame_files = _Tkinter.Frame(master=self.window)
        self.button_save = _Tkinter.Button(master=self.window, text="Save", font=("Times", 12, "normal"), command=self.save_settings)
        self.label_merit_text = _Tkinter.Label(master=self.window, text="Merit Automotive Electronics", font=("Times", 8, "italic"))
        self.label_merit_image = _Tkinter.Label(master=self.window, image=self.img_merit_logo)
        # create widgets inside fram_files
        self._create_frame_files_widgets(main_files_name=main_files_name, additional_files_name=additional_files_name)

    def _create_frame_files_widgets(self, main_files_name, additional_files_name):
        """
        Method creates widgets that are used in this frame.

        :return: None
        """
        self.canvas_files = _Tkinter.Canvas(master=self.frame_files)
        self.frame_files_scrollbar_x = _Tkinter.Scrollbar(master=self.frame_files, orient=_Tkinter.HORIZONTAL, command=self.canvas_files.xview)
        self.frame_files_scrollbar_y = _Tkinter.Scrollbar(master=self.frame_files, orient=_Tkinter.VERTICAL, command=self.canvas_files.yview)
        self.frame_in_canvas_files = _Tkinter.Frame(master=self.canvas_files)
        self.label_main_files = _Tkinter.Label(master=self.frame_in_canvas_files, text=main_files_name, font=("Times", 12, "normal"))
        self.label_additional_files = _Tkinter.Label(master=self.frame_in_canvas_files, text=additional_files_name, font=("Times", 12, "normal"))
        # list variables for many files
        self.checkbuttons_main_files_list = []
        self.labels_main_files_list = []
        self.checkbuttons_additional_files_list = []
        self.labels_additional_files_list = []
        for i, main_file in enumerate(self.main_files):
            self.checkbuttons_main_files_list.append(_Tkinter.Checkbutton(master=self.frame_in_canvas_files, variable=self.var_set_main_files_list[i]))
            self.labels_main_files_list.append(_Tkinter.Label(master=self.frame_in_canvas_files, text=main_file))
        for i, additional_file in enumerate(self.additional_files):
            self.checkbuttons_additional_files_list.append(_Tkinter.Checkbutton(master=self.frame_in_canvas_files, variable=self.var_set_additional_files_list[i]))
            self.labels_additional_files_list.append(_Tkinter.Label(master=self.frame_in_canvas_files, text=additional_file))

    def _place_widgets(self):
        """
        Method places widgets in the window.

        :return: None
        """
        # menu bar
        self.window.config(menu=self.main_menu_bar)
        # place objects inside frame_files
        self._place_frame_files_widgets()
        # place objects in window
        self.frame_files.grid(row=0, column=0)
        self.button_save.grid(row=1, column=0)
        self.label_merit_text.grid(row=2, column=0, sticky=_Tkinter.W+_Tkinter.S)
        self.label_merit_image.grid(row=2, column=0, sticky=_Tkinter.E+_Tkinter.S)

    def _place_frame_files_widgets(self):
        """
        Method places widgets in the frame_files.

        :return: None
        """
        # place objects in frame_files
        self.canvas_files.grid(row=0, column=0)
        self.frame_files_scrollbar_x.grid(row=1, column=0, sticky=_Tkinter.E+_Tkinter.S+_Tkinter.W)
        self.frame_files_scrollbar_y.grid(row=0, column=1, sticky=_Tkinter.N+_Tkinter.E+_Tkinter.S)
        # place objects in canvas_files
        self.frame_in_canvas_files.pack()
        self.canvas_files.create_window((0, 0), window=self.frame_in_canvas_files, anchor="nw")
        # place objects in frame_in_canvas_files
        self.label_main_files.grid(row=0, column=0, columnspan=2, sticky=_Tkinter.W, padx=5, pady=5)
        c1 = len(self.main_files)
        c2 = len(self.additional_files)
        for i in range(c1):
            self.checkbuttons_main_files_list[i].grid(row=i+1, column=0, sticky=_Tkinter.W, padx=10)
            self.labels_main_files_list[i].grid(row=i+1, column=1, sticky=_Tkinter.W)
        self.label_additional_files.grid(row=c1+1, column=0, columnspan=2, sticky=_Tkinter.W, padx=5, pady=5)
        for i in range(c2):
            self.checkbuttons_additional_files_list[i].grid(row=i+c1+2, column=0, sticky=_Tkinter.W, padx=10)
            self.labels_additional_files_list[i].grid(row=i+c1+2, column=1, sticky=_Tkinter.W)

    def _config_widgets(self):
        """
        Method configures additional settings for widgets.

        :return: None
        """
        self.canvas_files.configure(yscrollcommand=self.frame_files_scrollbar_y.set, xscrollcommand=self.frame_files_scrollbar_x.set)
        self._config_canvas_files()

    def _config_canvas_files(self, *_args):
        """
        Method configures canvas files in order to keep its size and possibility of scrolling.

        :return: None
        """
        self.canvas_files.configure(scrollregion=self.canvas_files.bbox("all"), **self.CANVAS_FILES_SIZE)

    def _define_binds(self):
        """
        Method links button binds with functions/methods.

        :return: None
        """
        None#self.window.bind("<F1>", bind_open_manual)
        self.window.bind("<Control-KeyPress-s>", self.save_settings)
        self.window.bind("<Control-KeyPress-S>", self.save_settings)
        self.frame_in_canvas_files.bind("<Configure>", self._config_canvas_files)

    def _select_all_files(self, *_args):
        """
        Method selects all files on this window.

        :return: None
        """
        for var in self.var_set_main_files_list + self.var_set_additional_files_list:
            var.set(True)

    def _deselect_all_files(self, *_args):
        """
        Method deselects all files on this window.

        :return: None
        """
        for var in self.var_set_main_files_list + self.var_set_additional_files_list:
            var.set(False)

    def save_settings(self, *_args):
        """
        Method saves selection of all files and passes results to master window via _save_settings method.

        :return: None
        """
        main_files_selection = {}
        additional_files_selection = {}
        for i, main_file in enumerate(self.main_files):
            main_files_selection[main_file] = self.var_set_main_files_list[i].get()
        for i, additional_file in enumerate(self.additional_files):
            additional_files_selection[additional_file] = self.var_set_additional_files_list[i].get()
        self._save_settings(main_files_selection, additional_files_selection)
        self.window.destroy()


# --------------------------------------------- Top Level - Save Settings -------------------------------------------- #


class TopLevelSaveSettings:
    # position and size
    WINDOW_SIZE = {"width": 250, "height": 107}
    WINDOW_POSITION = "+%d+%d" % ((GetSystemMetrics(0) - WINDOW_SIZE["width"]) // 2, (GetSystemMetrics(1) - WINDOW_SIZE["height"]) // 2)

    def __init__(self, func_save_set, parent_window=None):
        # link method
        self._save_settings_set = func_save_set
        # create window
        self.window = _Tkinter.Toplevel(master=parent_window)
        self.window.iconbitmap(IMAGE_MERIT_ICO)
        self.window.title("Save settings as")
        self.window.minsize(**self.WINDOW_SIZE)
        self.window.geometry(self.WINDOW_POSITION)
        self.window.resizable(width=True, height=False)
        # define binds
        None#self.window.bind("<F1>", bind_open_manual)
        self.window.bind("<Control-KeyPress-a>", self._bind_ctr_a)
        self.window.bind("<Control-KeyPress-A>", self._bind_ctr_a)
        self.window.bind("<Return>", self._save_set)
        # define widgets
        self.label_setting_set_name = _Tkinter.Label(master=self.window, text="Type name:", font=("Times", 12, "normal"))
        self.entry_settings_set_name = _Tkinter.Entry(master=self.window)
        self.button_save = _Tkinter.Button(master=self.window, text="Save", font=("Times", 12, "normal"), command=self._save_set)
        # place widgets
        self.label_setting_set_name.pack(side=_Tkinter.TOP, anchor=_Tkinter.N + _Tkinter.W, padx=5, pady=5)
        self.entry_settings_set_name.pack(side=_Tkinter.TOP, fill=_Tkinter.X, padx=5, pady=5)
        self.button_save.pack(side=_Tkinter.BOTTOM, padx=5, pady=5)

    def _bind_ctr_a(self, event):
        """
        Method specifies what happens to each widget (and especially which widgets are affected) after ctrl+a bind is pressed.

        :param event:
            Standard parameter passed by bind method.

        :return: None
        """
        if event.widget in (self.entry_settings_set_name, ):
            None#bind_select_all(event)

    def _save_set(self, *_args):
        """
        Method tries to save settings set under name that was typed by used.
        It uses function that was previously given as parameter in constructor.

        :return: None
        """
        if self._save_settings_set(self.entry_settings_set_name.get().strip()):
            self.window.destroy()
        else:
            None#display_error_type_again(value_name="settings set name", parent_window=self.window)


