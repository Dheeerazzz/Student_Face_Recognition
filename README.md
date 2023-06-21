# Student Face Recognition Project

This project is developed for campus security purposes to identify students of the college and detect strangers within the campus.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)
- [Output Image](#output-image)

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/Dheeerazzz/Student_Face_Recognition
   ```

2. Navigate to the project directory:
   ```shell
   cd Student_Face_Recognition

   ```

3. Install the necessary requirements:
   ```shell
   pip install -r requirements.txt
   ```

4. Obtain the required files:
   - Download the `serviceAccountKey.json` file for Firebase authentication.
   - Prepare a folder named `Images` containing student images in the project directory.

5. Configure Firebase:
   - Create a Firebase project and obtain the `databaseURL` and `storageBucket`.
   - Replace the placeholders in the `serviceAccountKey.json` file with your Firebase project credentials.
   - Update the `databaseURL` and `storageBucket` in the `firebase_admin.initialize_app()` function call in the code.

## Usage

1. Run the main Python script:
   ```shell
   python main.py
   ```

2. The script captures video from the default webcam and performs face recognition tasks.

3. To interrupt and quit the script, press the `Esc` key.

## References

- Link to the reference video: [Face Recognition UI Design and Working](https://youtu.be/iBomaK2ARyI)

## Output Image

![Output Image](abc)


