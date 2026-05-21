from __future__ import annotations

import os
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import Dict, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SCOPES = ["https://www.googleapis.com/auth/drive.file"]
APP_NAME = "OpenInGoogle"

APPDATA_DIR = Path(os.environ.get("APPDATA", str(Path.home()))) / APP_NAME
APPDATA_DIR.mkdir(parents=True, exist_ok=True)

CREDENTIALS_FILE = APPDATA_DIR / "credentials.json"
TOKEN_FILE = APPDATA_DIR / "token.json"
HELP_FILE = APPDATA_DIR / "SAVE_YOUR_GOOGLE_CREDENTIALS_HERE.txt"

GOOGLE_CLOUD_CONSOLE_URL = "https://console.cloud.google.com/"
GOOGLE_API_LIBRARY_URL = "https://console.cloud.google.com/apis/library/drive.googleapis.com"
GOOGLE_CREDENTIALS_URL = "https://console.cloud.google.com/apis/credentials"

GOOGLE_MIME_TYPES: Dict[str, str] = {
    ".docx": "application/vnd.google-apps.document",
    ".doc": "application/vnd.google-apps.document",
    ".rtf": "application/vnd.google-apps.document",
    ".txt": "application/vnd.google-apps.document",
    ".xlsx": "application/vnd.google-apps.spreadsheet",
    ".xls": "application/vnd.google-apps.spreadsheet",
    ".xlsm": "application/vnd.google-apps.spreadsheet",
    ".csv": "application/vnd.google-apps.spreadsheet",
    ".pptx": "application/vnd.google-apps.presentation",
    ".ppt": "application/vnd.google-apps.presentation",
}

HELP_TEXT = f"""SAVE YOUR GOOGLE CREDENTIALS HERE

OpenInGoogle needs a Google OAuth Desktop App credential file.

The required final file name is:

    credentials.json

The required final location is:

    {CREDENTIALS_FILE}

BEGINNER SETUP SUMMARY

1. Go to Google Cloud Console:
   {GOOGLE_CLOUD_CONSOLE_URL}

2. Create a project named something like:
   OpenInGoogle Personal

3. Enable the Google Drive API:
   {GOOGLE_API_LIBRARY_URL}

4. Configure the OAuth consent screen:
   - User type: External, unless you are using Google Workspace and know you need Internal
   - App name: OpenInGoogle Personal
   - User support email: your email
   - Developer contact email: your email
   - Add yourself as a test user if Google asks

5. Create OAuth credentials:
   {GOOGLE_CREDENTIALS_URL}

6. Choose:
   Create Credentials > OAuth client ID > Desktop app

7. Download the JSON file.

8. Rename the downloaded file to:
   credentials.json

9. Move credentials.json into this folder:
   {APPDATA_DIR}

10. Try OpenInGoogle again.

IMPORTANT

Do not share:
- credentials.json
- token.json

These files are private to your Google account.
"""


def ensure_help_file() -> None:
    """Create the credentials folder and help file."""
    APPDATA_DIR.mkdir(parents=True, exist_ok=True)
    HELP_FILE.write_text(HELP_TEXT, encoding="utf-8")


def show_box(title: str, message: str, error: bool = False) -> None:
    """Show a simple Windows message box."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()

        if error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)

        root.destroy()
    except Exception:
        print(f"{title}\n{message}")


def ask_yes_no(title: str, message: str) -> bool:
    """Ask a yes/no question with a Windows message box."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        result = messagebox.askyesno(title, message)
        root.destroy()
        return bool(result)
    except Exception:
        print(f"{title}\n{message}")
        return False


def open_credentials_folder() -> None:
    """Open the folder where credentials.json must be saved."""
    ensure_help_file()

    try:
        os.startfile(str(APPDATA_DIR))
    except Exception:
        webbrowser.open(str(APPDATA_DIR))


def open_setup_guide() -> None:
    """
    Open the local credentials setup guide.

    Important:
    Use Notepad explicitly so Windows does not ask the user how to open .txt/.md files.
    """
    ensure_help_file()

    try:
        subprocess.Popen(["notepad.exe", str(HELP_FILE)])
    except Exception:
        try:
            os.startfile(str(HELP_FILE))
        except Exception:
            webbrowser.open(str(HELP_FILE))


def open_google_cloud_pages() -> None:
    """Open the Google Cloud setup pages."""
    webbrowser.open(GOOGLE_CLOUD_CONSOLE_URL)
    webbrowser.open(GOOGLE_API_LIBRARY_URL)
    webbrowser.open(GOOGLE_CREDENTIALS_URL)


def run_credentials_setup_prompt() -> None:
    """
    Beginner-friendly credential setup flow.

    Opens:
    - the local credentials folder
    - the local setup guide in Notepad
    - optionally the Google Cloud setup pages
    """
    ensure_help_file()
    open_credentials_folder()
    open_setup_guide()

    msg = (
        "OpenInGoogle needs a Google OAuth Desktop App credential file.\n\n"
        "I opened the folder where the file must be saved and opened a setup guide.\n\n"
        "Required file name:\n"
        "credentials.json\n\n"
        "Required folder:\n"
        f"{APPDATA_DIR}\n\n"
        "Would you like me to open the Google Cloud setup pages in your browser?"
    )

    if ask_yes_no("OpenInGoogle Setup", msg):
        open_google_cloud_pages()


def choose_file() -> Optional[str]:
    """Open a file picker if the app is launched without a file path."""
    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Choose an Office file to open in Google",
            filetypes=[
                (
                    "Supported Office files",
                    "*.docx *.doc *.rtf *.txt *.xlsx *.xls *.xlsm *.csv *.pptx *.ppt",
                ),
                ("Word files", "*.docx *.doc *.rtf *.txt"),
                ("Excel files", "*.xlsx *.xls *.xlsm *.csv"),
                ("PowerPoint files", "*.pptx *.ppt"),
                ("All files", "*.*"),
            ],
        )

        root.destroy()
        return file_path or None
    except Exception:
        return None


def get_drive_service():
    """Authenticate with Google and return a Drive API service client."""
    ensure_help_file()
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                run_credentials_setup_prompt()

                raise FileNotFoundError(
                    "Google credentials are not set up yet.\n\n"
                    "I opened the folder where credentials.json must be saved.\n\n"
                    "After you create/download your Google OAuth Desktop App credential, rename it to:\n\n"
                    "credentials.json\n\n"
                    "Then save it here:\n\n"
                    f"{CREDENTIALS_FILE}\n\n"
                    "Then try opening the Office file again."
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE),
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")

    return build("drive", "v3", credentials=creds)


def upload_convert_and_open(file_path: str) -> None:
    """Upload the selected file, convert it, and open it in the browser."""
    path = Path(file_path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"File not found:\n{path}")

    ext = path.suffix.lower()

    if ext not in GOOGLE_MIME_TYPES:
        supported = ".docx, .doc, .rtf, .txt, .xlsx, .xls, .xlsm, .csv, .pptx, .ppt"
        raise ValueError(
            f"Unsupported file type: {ext}\n\n"
            f"Supported file types:\n{supported}"
        )

    service = get_drive_service()

    media = MediaFileUpload(str(path), resumable=True)

    metadata = {
        "name": path.stem,
        "mimeType": GOOGLE_MIME_TYPES[ext],
    }

    created = (
        service.files()
        .create(
            body=metadata,
            media_body=media,
            fields="id,name,webViewLink",
        )
        .execute()
    )

    link = created.get("webViewLink")

    if not link:
        raise RuntimeError("Upload succeeded, but Google did not return a web link.")

    webbrowser.open(link)


def main() -> int:
    ensure_help_file()

    if len(sys.argv) >= 2:
        arg = sys.argv[1]

        if arg == "--open-credentials-folder":
            open_credentials_folder()
            return 0

        if arg == "--setup-credentials":
            run_credentials_setup_prompt()
            return 0

        if arg == "--open-google-cloud-setup":
            open_google_cloud_pages()
            return 0

        file_path = arg
    else:
        file_path = choose_file()

    if not file_path:
        return 0

    try:
        upload_convert_and_open(file_path)
        return 0
    except Exception as exc:
        show_box(APP_NAME, str(exc), error=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
