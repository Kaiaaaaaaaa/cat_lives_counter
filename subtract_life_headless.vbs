Option Explicit

Dim wshShell, fso, scriptDir, scriptPath
Set wshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

scriptPath = scriptDir & "\lifeCountModifier.py"

wshShell.Run "pythonw """ & scriptPath & """ dec", 0, True
