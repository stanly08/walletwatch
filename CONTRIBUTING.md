# Contributing to walletwatch

Thank you for considering contributing to walletwatch! We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and more.

## Getting Started

1. **Fork the repository**: Click the "Fork" button at the top of this page to create a copy of the repository under your GitHub account.

2. **Clone your fork**:
   ```bash
   git clone https://github.com/stanly08/walletwatch.git

3.Create a new branch for your contribution:
   ```
   git checkout -b feature-or-bugfix-name-or-documentation-improvements
  ```
4.Install the dependencies: Make sure you have the necessary dependencies installed by running:

  ```
  pip install -r requirements.txt
  ```
5. You may also want to create and activate a virtual environment:
  ```
  python3 -m venv myenv
  ```

6. Activate the environment:
   On windows
   ```
   venv\Scripts\activate
   ```
   On mac or Linux
   ```
   source venv/bin/activate
    ```

7. Make your changes: Implement your changes, and don't forget to write tests if applicable.

8. Run the tests: Ensure that your changes do not break any existing functionality by running the tests:
  ```
  pytest
  ```
9. Commit your changes:
  ```
  git commit -m "Description of the change"
  ```
10. Push to your fork:
  ```
  git push origin feature-or-bugfix-name-or-documentation-improvements
  ```
11. Create a Pull Request: Go to the original repository on GitHub and click on "New Pull Request". Provide a clear and descriptive title for your pull request and include a summary of the changes you've made.
