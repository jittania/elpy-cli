# **The Elpy Python CLI**

TBD

---

## **Application Features**

TBD

---

## **Local Setup Instructions**

1. `cd` into top level folder of project

2. Create and activate a virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ # --> Virtual environment is active
```

3. Install dependencies:

```bash
(venv) $ pip install -r requirements.txt
```

4. Make sure the Python Interpreter is set up correctly:
   1. from within VS Code
by selecting SHIFT + CMD + P -> 'Python: Select Interpreter' -> Select the interpreter
path that includes ('venv': venv).
    2. CL...?

5. Create a `.env` file in your root directory containing the following, which can be set up and obtained from here (will have to create your own app first): https://developer.spotify.com/dashboard:

```bash
SPOTIPY_CLIENT_ID='your-spotify-client-id'
SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
SPOTIPY_REDIRECT_URI='your-spotify-reditect-uri'
```

6. Run the following command to execute program:

```bash
(venv) $ python -m elpy_cli
```

7. Run all tests:

```bash
(venv) $ pytest
```
