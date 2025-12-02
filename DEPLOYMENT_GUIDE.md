# How to Deploy Your Website to the Internet (Render.com)

Since I am an AI, I cannot create an account for you. But I have prepared your files so you can do it easily in 5 minutes.

**IMPORTANT NOTE:**
On the free version of Render, your **Database (SQLite)** will be reset every time the server restarts (about once a day). For a permanent website, you would need a real database like PostgreSQL, but for showing your friend, this is perfect.

### Step 1: Upload to GitHub
1.  Create a new repository on [GitHub.com](https://github.com).
2.  Upload all the files in this folder to that repository.
    -   Make sure `requirements.txt` and `backend/` are in the root.

### Step 2: Deploy on Render
1.  Go to [Render.com](https://render.com) and sign up (it's free).
2.  Click **"New +"** -> **"Web Service"**.
3.  Connect your GitHub account and select your repository.
4.  **Settings:**
    -   **Name**: `iskcon-ahillyanagar` (or anything you like)
    -   **Runtime**: `Python 3`
    -   **Build Command**: `pip install -r requirements.txt`
    -   **Start Command**: `gunicorn backend.app:app`
5.  Click **"Create Web Service"**.

### Step 3: Done!
Render will give you a link like `https://iskcon-ahillyanagar.onrender.com`.
Share this link with your friend!
