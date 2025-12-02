# How to Access Your Database (SQLite)

The website is already using **SQLite**. The data is stored in a file named `iskcon.db` inside the `backend` folder.

You can access this data in 3 ways:

## 1. Web Dashboard (Easiest)
- Go to [http://localhost:5000/admin.html](http://localhost:5000/admin.html)
- Login with `admin123`.
- **New Feature**: I have added an "Export to CSV" button so you can open the data in **Excel**.

## 2. Direct File Access (For IT Team)
You can open the database file directly using free software.
1.  Download **[DB Browser for SQLite](https://sqlitebrowser.org/)**.
2.  Open the program.
3.  Click "Open Database" and select `backend/iskcon.db`.
4.  Go to the "Browse Data" tab.
5.  You will see all raw tables: `donations`, `contacts`, `subscribers`.

## 3. Programmatic Access (For Developers)
Developers can connect to the database using Python, Node.js, or any language that supports SQLite.
- **Connection String**: `sqlite:///backend/iskcon.db`
