

# ------------------------------------------------- Global Variables ------------------------------------------------ #
class GlobalVariables:

    App_version = 1
    Process_Running = False

    Username = "bartosz.leszaj@gmail.com"
    Password = None
    Credentials = [
        "04f197f43889333d60d43a5e2fd41651df9c88e0150c34bd6e13d54b59143591",
        "425c97ee7a4ee1083e2c86abf6af5982de39b81329fb62ccca7709715965f910",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" # empty string - TO BE REMOVED
    ]

    Settings_file = '_settings.xml'
    Hash_list_file = '_hash_sha256'

# ------------------------------------------------- Other Variables ------------------------------------------------- #

"""
PROJECT_PATH = _os.getcwd()[:_os.getcwd().rfind("\\")]
FILES_PATH = PROJECT_PATH + "\\resources"
FILES_NAMES = ["CodeBeamer.png", "CodeBeamer_logo.png", "Merit.ico", "Merit_logo.png", "Vector_logo.png", "DiVa_logo.png", "vTestStudio_logo.png"]

setup(
    name = "CodeBeamerInterface",
    description="Tool for integration codeBeamer with Vector applications (vTest Studio and CANoe.DiVa).",
    version = 0,
    data_files = [FILES_PATH+"\\"+file_name for file_name in FILES_NAMES],
    windows = [{
        "script": "CBInterface_window_version.py",
        "copyright": "Merit Automotive Electronics",
    }],
    options = {
        "py2exe":{
            "includes": [
                "Data_Structures", "Common_Popups", "Common_Messages", "Messages_Logging", "Utilities",
                "CodeBeamer_Primitives", "CodeBeamer_Handlers",
                "VT_Requirements_Parser", "VT_TC_Parser", "VT_Results_Parser", #"Diva_Parser",
                "GUI", "GUI_settings", "Functionalities", "Exported_Data_Validation",
                "os", "copy",
                "xml", "openpyxl", "requests",
                "Tkinter", "ttk", "tkMessageBox", "tkFileDialog", "win32api", "PIL",
            ],
            "dist_dir": PROJECT_PATH+"\\"+"executable_window",
        }
    }
)

"""
