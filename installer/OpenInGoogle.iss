; Inno Setup script for OpenInGoogle
#define MyAppName "OpenInGoogle"
#define MyAppVersion "1.1.2"
#define MyAppPublisher "David Randall"
#define MyAppExeName "OpenInGoogle.exe"

[Setup]
AppId={{7B5633BC-22F3-4E7D-962B-4B0F63C9B8D1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=..\release
OutputBaseFilename=OpenInGoogleSetup-v{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
UninstallDisplayIcon={app}\{#MyAppExeName}

[Dirs]
Name: "{userappdata}\OpenInGoogle"

[Files]
Source: "..\dist\OpenInGoogle.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\SETUP_FOR_USERS.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\OBTAIN_GOOGLE_CREDENTIALS_BEGINNER_GUIDE.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\SECURITY_AND_PRIVACY.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\TROUBLESHOOTING.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\credentials-folder\SAVE_YOUR_GOOGLE_CREDENTIALS_HERE.txt"; DestDir: "{userappdata}\OpenInGoogle"; Flags: ignoreversion

[Icons]
Name: "{group}\OpenInGoogle"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Setup Google Credentials"; Filename: "{app}\{#MyAppExeName}"; Parameters: "--setup-credentials"
Name: "{group}\Open Credentials Folder"; Filename: "{app}\{#MyAppExeName}"; Parameters: "--open-credentials-folder"

Name: "{group}\Beginner Credential Guide"; Filename: "notepad.exe"; Parameters: """{app}\OBTAIN_GOOGLE_CREDENTIALS_BEGINNER_GUIDE.md"""
Name: "{group}\Setup Instructions"; Filename: "notepad.exe"; Parameters: """{app}\SETUP_FOR_USERS.md"""
Name: "{group}\Security and Privacy"; Filename: "notepad.exe"; Parameters: """{app}\SECURITY_AND_PRIVACY.md"""
Name: "{group}\Troubleshooting"; Filename: "notepad.exe"; Parameters: """{app}\TROUBLESHOOTING.md"""

Name: "{group}\Uninstall OpenInGoogle"; Filename: "{uninstallexe}"

[Registry]
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.docx\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Docs"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.docx\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.doc\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Docs"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.doc\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.rtf\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Docs"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.rtf\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.txt\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Docs"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.txt\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xlsx\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Sheets"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xlsx\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xls\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Sheets"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xls\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xlsm\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Sheets"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.xlsm\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.csv\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Sheets"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.csv\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.pptx\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Slides"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.pptx\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.ppt\shell\OpenInGoogle"; ValueType: string; ValueName: ""; ValueData: "Open in Google Slides"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.ppt\shell\OpenInGoogle\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletekey

[Run]
Filename: "notepad.exe"; Parameters: """{app}\SETUP_FOR_USERS.md"""; Description: "Open setup instructions"; Flags: postinstall skipifsilent
Filename: "{app}\{#MyAppExeName}"; Parameters: "--setup-credentials"; Description: "Start Google credentials setup"; Flags: postinstall skipifsilent
