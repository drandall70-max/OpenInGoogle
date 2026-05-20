# Adds a right-click context menu item for supported Office file types.
# It does not overwrite your default double-click app.

$ErrorActionPreference = "Stop"

$InstallDir = "C:\OpenInGoogle"
$PythonScript = Join-Path $InstallDir "OpenInGoogle.py"
$PythonExe = (Get-Command python.exe -ErrorAction Stop).Source

if (!(Test-Path $PythonScript)) {
    throw "Cannot find $PythonScript. Make sure OpenInGoogle.py is in C:\OpenInGoogle."
}

$extensions = @(
    ".docx", ".doc", ".rtf", ".txt",
    ".xlsx", ".xls", ".xlsm", ".csv",
    ".pptx", ".ppt"
)

foreach ($ext in $extensions) {
    $baseKey = "HKCU:\Software\Classes\SystemFileAssociations\$ext\shell\OpenInGoogle"
    $commandKey = "$baseKey\command"

    New-Item -Path $baseKey -Force | Out-Null
    New-Item -Path $commandKey -Force | Out-Null

    Set-ItemProperty -Path $baseKey -Name "(default)" -Value "Open in Google Docs"
    Set-ItemProperty -Path $baseKey -Name "Icon" -Value "chrome.exe"

    $command = "`"$PythonExe`" `"$PythonScript`" `"%1`""
    Set-ItemProperty -Path $commandKey -Name "(default)" -Value $command
}

Write-Host "Installed right-click menu: Open in Google Docs"
