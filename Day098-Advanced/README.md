# `Day 98 - Advanced`


## `Objective` : Custom Automation

### Step-by-Step Thought Process
1. Identify the Problem: The primary issue here is that files downloaded from the internet often end up in a single folder without any organization, making it difficult to locate specific types of files quickly. 
2. Choose the Automation Tool: For this task, we'll use Python along with the os module for interacting with the operating system and the shutil module for moving files around. We might also need the fnmatch module for matching filenames against patterns. 
3. Design the Solution:
- Scan the downloads folder for all files.
- Categorize each file based on its extension (file type).
- Move each file to a corresponding subfolder within the downloads folder, creating these subfolders if they don't already exist.
4. Considerations:
- Ensure the script doesn't move files that are currently being used or accessed.
- Handle cases where files might have no extension or multiple extensions.
- Provide an option to exclude certain file types from automatic organization.


```
This script automatically organizes files in the specified downloads folder into subfolders based on their file type.
It uses built-in Python modules (os, shutil, fnmatch) for file manipulation and pattern matching.
Before running the script, ensure you replace '/path/to/your/downloads/folder' with the actual path to your downloads folder.
Consider adding error handling to manage unexpected issues, such as permission errors or disk space issues.
Regularly review and update the list of directories and their associated file extensions to accommodate new file types as needed.
```
