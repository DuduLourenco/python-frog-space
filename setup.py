import cx_Freeze

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('main.py', base = "Win32GUI")]

cx_Freeze.setup(
    name = "A Forca - SaPuc",
    options = {"build_exe" : 
        {"packages" : ["pygame"], "include_files" : ['components/', 'assets/']}},
    executables = executables
)