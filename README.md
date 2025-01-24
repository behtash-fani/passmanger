# **Password Manager in Python**

A simple and secure password manager built with Python and SQLite. This application allows you to store, retrieve, and manage your passwords for various apps and websites. The project is Dockerized for easy deployment and consistent execution across environments.

---

## **Features**
- **Store Passwords:** Save app names, URLs, usernames, and passwords securely.
- **Retrieve Passwords:** Find passwords by app name or username.
- **Encryption:** Passwords are encrypted before being stored in the database.
- **Docker Support:** Easily run the application in a Docker container.
- **User-Friendly Menu:** Interactive command-line interface for managing passwords.

---

## **Technologies Used**
- **Python:** Core programming language.
- **SQLite:** Lightweight database for storing password information.
- **Cryptography:** Library for encrypting and decrypting sensitive data.
- **Docker:** Containerization for easy deployment.

---

## **Prerequisites**
Before running the project, ensure you have the following installed:
- **Python 3.9 or higher**
- **Docker** (optional, for containerized execution)
- **Git** (for cloning the repository)

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone git@github.com:behtash-fani/passmanger.git
cd passmanger
```

### **2. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
#### **Without Docker**
```bash
python password_manager.py
```

#### **With Docker**
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Run the container:
   ```bash
   docker-compose up
   ```

---

## **Usage**
Once the application is running, you'll see a menu with the following options:
1. **Save Account Information:** Enter app name, URL, username, and password to store your credentials.
2. **Find Accounts by Username:** Retrieve all accounts associated with a specific username.
3. **Find Password by App Name:** Retrieve the password for a specific app or website.
4. **Exit:** Quit the application.

---

## **Project Structure**
```
password_manager/
├── database/               # Database management module
│   ├── __init__.py
│   └── database_manager.py
├── utils/                  # Utility functions (e.g., input validation)
│   ├── __init__.py
│   └── input_validation.py
├── menu.py                 # Menu and user interaction logic
├── password_manager.py     # Main application script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
└── docker-compose.yml      # Docker Compose configuration
```

---

## **Encryption**
Passwords are encrypted using the `cryptography` library before being stored in the database. The encryption key is generated automatically and stored in memory. **For production use, ensure the encryption key is securely managed.**

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- Thanks to the Python community for awesome libraries and tools.
- Inspired by the need for a simple, secure, and open-source password manager.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Behtash Fani**  
- GitHub: [behtash-fani](https://github.com/behtash-fani)  
- Email: [behtash.fani@gmail.com](mailto:behtash.fani@gmail.com)
