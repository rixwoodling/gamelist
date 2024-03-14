# EmulationStation Game List Generator

This Python script automates the creation of a `gamelist.xml` file for each ROM in your collection, making it easier to manage your games in EmulationStation. By reading a CSV file containing details about your games, the script generates an XML file that EmulationStation can use to display game information.

## Features

- Automatically generates a `gamelist.xml` file from a CSV file.
- Supports adding game name, description, path, image, video, genre, release date, developer, publisher, and players count.

## Requirements

- Python 3.x
- A CSV file with the columns: name, desc, file, genre, releasedate, developer, publisher, players. The `file` column should include the ROM filename.

## Setup

1. Ensure Python 3.x is installed on your system.
2. Place the script in a directory of your choice.

## Usage

1. Prepare your CSV file with the required columns (name, desc, file, genre, releasedate, developer, publisher, players).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script by executing:

```
python gamelist_generator.py yourfile.csv
```

Replace `yourfile.csv` with the path to your CSV file.

## CSV File Format

Your CSV file should follow this format:

```
name,desc,file,genre,releasedate,developer,publisher,players
Super Mario Bros.,Classic platformer game.,super_mario_bros.nes,Platform,1985-09-13,Nintendo,Nintendo,2
```

Ensure that your CSV file includes headers and that each game entry is on a new line.

## Output

The script will generate a `gamelist.xml` file in the same directory as your CSV file. This XML file can then be used by EmulationStation to display detailed information about your games.

## Note

- The script assumes that your image and video files are named the same as your ROM files, with the respective `.png` and `.mp4` extensions.
- Make sure the ROM files mentioned in your CSV file exist in the same directory as the CSV file or adjust the `path` in the XML accordingly.

---

I hope this README helps you get started with using the script! If you have any questions or need further assistance, feel free to ask.

