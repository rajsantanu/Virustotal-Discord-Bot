# Discord URL Analyzer Bot 🛡️

**A Discord bot that analyzes every URL sent in chat using VirusTotal and takes appropriate actions.**

## 🚧 Project Status: UNDER CONSTRUCTION 🚧

---

## 📝 Description

This bot helps Discord server moderators by scanning all URLs shared in the server using VirusTotal.  
If malicious content is detected, it can notify the server or respond accordingly.

### 🔍 Current Functionality

- 🖼️ **URL Detection**:  
  - Detects URLs from messages and edited messages using regex.  
- 🔍 **VirusTotal Integration**:  
  - Analyzes each URL with VirusTotal's API to retrieve safety stats.  
- 📨 **User Notifications**:  
  - Sends a message with analysis results for detected URLs.  

---

## ⚙️ Technologies Used

- 🐍 Python 3.12 *(Tested and stable; Python 3.13.1 caused dependency issues)* 
- 🤖 Discord.py  
- 🛠️ VirusTotal API  
- 📡 Requests  

---

## 🚀 Setup Instructions

1. **Clone the repository**:  
    ```bash
    git clone https://github.com/your_username/repo_name.git
    cd repo_name
    ```

2. **Install dependencies**:  
    ```bash
    pip install -r requirements.txt
    ```
3. **Prepare the credentials file**:  
    - Create a `creds.txt` file in the root directory with:  
      ```
      DISCORD_TOKEN
      VIRUSTOTAL_API_KEY
      ```
      *Line 1:* Your Discord bot token  
      *Line 2:* Your VirusTotal API key  

4. **Run the bot**:  
    ```bash
    python virustotal_discord_bot.py
    ```
---

## ⚠️ Security Disclaimer

This bot uses the VirusTotal API to analyze URLs. Ensure you comply with VirusTotal's usage policies and never use this tool maliciously.  

---

## 🛠️ Future Plans

- 🛑 Delete malicious messages automatically.  
- 🚨 Notify moderators/admins about malicious links.  
- 🗂️ Log scanned URLs in a database.  
- 🚷 Optionally ban users for repeated malicious link sharing.  

---
💡 *Contributions are welcome! Feel free to open an issue or pull request if you'd like to help out.*
---

🌐 [GitHub Profile](https://github.com/Yajus114)
