# ISKCON Website - Run Commands

Here are all the commands you need to run and manage the website.

## 1. First Time Setup (New Computer)
If you are running this on a new computer, install the required libraries first:
```cmd
pip install -r requirements.txt
```

## 2. Start the Website (Local)
The easiest way is to double-click **`run_website.bat`**.
Or run this command manually:
```cmd
python backend/app.py
```
*   **Local Link:** `http://localhost:5000`
*   **Admin Dashboard:** `http://localhost:5000/admin.html`

## 3. Share with Friends (Public Link)
To generate a link that works anywhere in the world:
Double-click **`get_public_link.bat`**.
Or run this command manually:
```cmd
ssh -o StrictHostKeyChecking=no -p 443 -R0:localhost:5000 a.pinggy.io
```

## 4. Fix Network Issues (Firewall)
If friends on the same Wi-Fi cannot connect:
Right-click **`fix_firewall.bat`** and "Run as Administrator".
Or run this command in Administrator PowerShell:
```powershell
New-NetFirewallRule -DisplayName 'ISKCON Website' -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow
```

## 5. Database Management
To clear all data (Use with caution!):
**Clear Subscribers:**
```cmd
curl -X DELETE http://localhost:5000/api/subscribers
```
**Clear Donations:**
```cmd
curl -X DELETE http://localhost:5000/api/donations
```
