# Beginner Guide: Create Your Google Credentials File

OpenInGoogle needs a private Google credential file so it can upload and convert files into **your own Google Drive**.

The file must be named:

```text
credentials.json
```

It must be saved here:

```text
%APPDATA%\OpenInGoogle\credentials.json
```

## Step 1: Open Google Cloud Console

Go to:

```text
https://console.cloud.google.com/
```

Sign in with the Google account you want to use.

## Step 2: Create a project

1. Click the project selector near the top.
2. Click **New Project**.
3. Name it:

```text
OpenInGoogle Personal
```

4. Click **Create**.

## Step 3: Enable the Google Drive API

Open:

```text
https://console.cloud.google.com/apis/library/drive.googleapis.com
```

Make sure your new project is selected.

Click **Enable**.

## Step 4: Configure the OAuth consent screen

1. Go to **APIs & Services > OAuth consent screen**.
2. Choose **External** unless you are using a managed Google Workspace account and know you need **Internal**.
3. Fill in:
   - App name: `OpenInGoogle Personal`
   - User support email: your email
   - Developer contact email: your email
4. Save/continue through the setup.
5. If Google asks for test users, add your own Google email address.

## Step 5: Create the OAuth client

1. Go to:

```text
https://console.cloud.google.com/apis/credentials
```

2. Click **Create Credentials**.
3. Choose **OAuth client ID**.
4. Application type: **Desktop app**.
5. Name:

```text
OpenInGoogle Desktop
```

6. Click **Create**.
7. Click **Download JSON**.

## Step 6: Rename the downloaded file

The file will probably have a long name like:

```text
client_secret_1234567890-abcdef.apps.googleusercontent.com.json
```

Rename it exactly to:

```text
credentials.json
```

## Step 7: Move it to the OpenInGoogle folder

Move `credentials.json` to:

```text
%APPDATA%\OpenInGoogle
```

The final path must be:

```text
%APPDATA%\OpenInGoogle\credentials.json
```

## Step 8: Try the app again

Right-click a Word, Excel, or PowerPoint file and choose:

```text
Open in Google Docs
```

On first use, Google will ask you to approve access.

## Important privacy note

Do not share:

```text
credentials.json
token.json
```

Those files are private to your Google account.
