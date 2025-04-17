# CLI Task Tracker

CLI Task Tracker is a simple yet powerful command-line application designed to help you manage your tasks directly from your terminal. Built entirely in Python, the project uses only built-in modules (`json`, `sys`, and `datetime`), ensuring a lightweight solution with no external dependencies.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Task Data Structure](#task-data-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
Inspired by the [roadmap.sh Task Tracker](https://roadmap.sh/projects/task-tracker), this project provides 
a hands-on experience for learning CLI application development. The tool is perfect for beginners looking to solidify
their Python skills or advanced users who want a quick and efficient task management solution. 
Importantly, it relies solely on Python’s built-in modules—`json`, `sys`, and `datetime`—
which means you won't need to set up any additional dependencies to run it.

## Features
- **Task Management:** Easily add, update, and delete tasks.
- **Status Tracking:** Mark tasks with statuses such as `todo`, `in-progress`, or `done` to reflect progress.
- **Filtering Options:** List all tasks or filter them by their current status.
- **Lightweight Persistence:** All tasks are stored in a local JSON file, preserving your data between sessions.
- **Zero Dependencies:** Built purely with Python’s standard libraries (`json`, `sys`, and `datetime`), 
resulting in a fast and easy-to-install tool.

## Installation

### Prerequisites
- **Python Environment:** Ensure you have Python 3 installed on your system.
No additional packages are required since only built-in modules are used.

### Steps to Install
1. **Clone the Repository:**
   ``` bash
   git clone https://github.com/yourusername/cli-task-tracker.git
   cd cli-task-tracker
   ```
## Usage
none

## Task Data Structure
Each task is stored in a JSON file with the following properties:
- id: A unique identifier.
- description: A brief description of the task that is manually typed by the user.
- status: The current status (todo, in-progress, or done).
- createdAt: Timestamp when the task was created.
- updatedAt: Timestamp when the task was last updated or got a description.

Example task record:
``` json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "07-04-2025 15:19:48"",
  "updatedAt": "07-04-2025 15:19:48"
}
```

## Contributing
Thank you for considering contributing to **CLI Task Tracker**! Your contributions help improve and expand the project, making it more useful for everyone.

### How to Contribute

1. **Fork the Repository:**  
   Click the **Fork** button at the top right of the repository page to create your own copy.

2. **Clone Your Fork:**  
   ``` bash
   git clone https://github.com/yourusername/cli-task-tracker.git
   cd cli-task-tracker
   ```

3. **Create a New Branch:**
   ``` bash
   git checkout -b feature/your-feature-name
   ```

   When making your changes:
   - Ensure your code follows the project’s style.
   - Write clear, concise commit messages.
   - Update documentation **if** needed.

4. **Commit Your Changes**:

``` bash
git commit -am "Add [feature/bug fix]: Brief description of changes"
``` 
Push Your Branch:

bash
git push origin feature/your-feature-name
Open a Pull Request (PR):

Navigate to the original repository on GitHub.

Open a new PR and describe your changes in detail.

Link to any related issues and explain why your contribution is valuable.

Code Style and Standards


## License
This project is licensed under the **MIT License** – a permissive open-source license that allows users to freely use,
modify, and distribute the software with minimal restrictions.

### Key Terms:
- You can use, modify, and distribute this software for **any** purpose.
- Attribution is **required** – you must include the original copyright notice.
- The software is provided **as-is**, without warranty of any kind.

For the full license text, see the [LICENSE](LICENSE) file in this repository.

## Contact
For any questions, issues, or feedback, don't hesitate to open an issue on GitHub or email me at hmdoonwork71@gmail.com.