# Removes the right-click context menu item created by INSTALL_CONTEXT_MENU.ps1.

$ErrorActionPreference = "Stop"

$extensions = @(
    ".docx", ".doc", ".rtf", ".txt",
    ".xlsx", ".xls", ".xlsm", ".csv",
    ".pptx", ".ppt"
)

foreach ($ext in $extensions) {
    $baseKey = "HKCU:\Software\Classes\SystemFileAssociations\$ext\shell\OpenInGoogle"

    if (Test-Path $baseKey) {
        Remove-Item -Path $baseKey -Recurse -Force
    }
}

Write-Host "Removed right-click menu: Open in Google Docs"
