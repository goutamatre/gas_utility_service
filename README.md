# gas_utility_service


# Gas Utility Service

## Overview
This project, **Gas Utility Service**, is designed to manage and optimize gas utilities efficiently. It includes features for tracking gas usage, monitoring supply, and generating reports.

## Features
- Gas usage tracking
- Supply monitoring
- Report generation
- User authentication

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- Git
- Virtual Environment (venv)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/goutamatre/gas_utility_service.git
   ```
2. Navigate to the project directory:
   ```bash
   cd gas_utility_service
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Git Setup & Troubleshooting
If you encounter authentication issues while pushing to GitHub, follow these steps:

### Set Up Git Identity
```bash
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

### Switch to Main Branch
```bash
git checkout -b main  # Create and switch to the main branch
git branch -M main    # Rename branch to main
```

### Fix Authentication Issues
Since GitHub removed password authentication, you must use a **Personal Access Token (PAT)**:
1. Go to [GitHub Token Settings](https://github.com/settings/tokens)
2. Generate a token with `repo` and `workflow` scopes
3. Use the token instead of your password when pushing:
   ```bash
   git remote set-url origin https://<USERNAME>:<PERSONAL_ACCESS_TOKEN>@github.com/goutamatre/gas_utility_service.git
   ```
4. Push the changes:
   ```bash
   git push -u origin main
   ```

Alternatively, you can set up **SSH authentication**:
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
cat ~/.ssh/id_rsa.pub  # Copy and add this key to GitHub SSH settings
```
Then, update the remote URL:
```bash
git remote set-url origin git@github.com:goutamatre/gas_utility_service.git
git push -u origin main
```

## Usage
Run the project using:
```bash
python main.py
```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

