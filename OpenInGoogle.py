"""
OpenInGoogle.py

Upload a local Microsoft Office file to Google Drive, convert it to the
matching Google Docs/Sheets/Slides format, and open it in a browser.
"""

from __future__ import annotations

import sys
import webbrowser
from pathlib import Path
from typing import Dict

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SCOPES = ["https://www.googleapis.com/auth/drive.file"]

SCRIPT_DIR = Path(__file__).resolve().parent
CREDENTIALS_FILE = SCRIPT_DIR / "credentials.json"
TOKEN_FILE = SCRIPT_DIR / "token.json"

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


def get_drive_service():
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                raise FileNotFoundError(
                    f"Missing {CREDENTIALS_FILE}. "
                    "Download your Google OAuth Desktop App credential and save it as credentials.json."
                )

            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")

    return build("drive", "v3", credentials=creds)


def upload_convert_and_open(file_path: str) -> None:
    path = Path(file_path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    ext = path.suffix.lower()

    if ext not in GOOGLE_MIME_TYPES:
        supported = ", ".join(sorted(GOOGLE_MIME_TYPES.keys()))
        raise ValueError(f"Unsupported file type: {ext}. Supported types: {supported}")

    service = get_drive_service()

    metadata = {
        "name": path.stem,
        "mimeType": GOOGLE_MIME_TYPES[ext],
    }

    media = MediaFileUpload(str(path), resumable=True)

    created = (
        service.files()
        .create(body=metadata, media_body=media, fields="id,name,webViewLink")
        .execute()
    )

    web_view_link = created.get("webViewLink")

    if not web_view_link:
        raise RuntimeError("Google Drive upload succeeded, but no webViewLink was returned.")

    print(f"Created Google file: {created.get('name', path.stem)}")
    print(f"Opening: {web_view_link}")
    webbrowser.open(web_view_link)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage:")
        print(r'  python OpenInGoogle.py "C:\path\to\file.docx"')
        return 2

    try:
        upload_convert_and_open(sys.argv[1])
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
