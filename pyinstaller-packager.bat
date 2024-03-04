cd %~dp0
pyinstaller --noconfirm --log-level=WARN ^
--noconsole --onedir --name="CoPilotAPI" ^
--distpath="C:\Users\earter.freeman\source\dist" ^
--workpath="C:\Users\earter.freeman\source\build" ^
--add-data="C:\Users\earter.freeman\source\nssm-64.exe;." ^
--add-data="C:\Users\earter.freeman\source\nssm-32.exe;." ^
--path="C:\Users\earter.freeman\source\repos\CoPilotAPI" ^
--icon="C:\Users\earter.freeman\source\repos\CoPilotAPI\octopus.ico" ^
CoPilotAPI.py