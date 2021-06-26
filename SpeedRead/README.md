# SpeedRead

This programm help you to read your text faster, by showing just one word at the time.

## Installation

First, you need to have python3 installed on your machine (which is the case for a lot of Linux distributions out of the box).
To verify this, you can run the following command:
```bash
python3 --version
```
If you're given an output, it means that you have python3 installed.

If not, you have to install it:
```bash
sudo apt update
sudo apt install python3
```

Then, you have to download the main.py (you can clone the entire repository by typing the following commands or juste download the file yourself) file and put it in a directory with a file named "text.txt".
```bash
git clone https://github.com/LePtitSuisse/pythonUsefull.git
mkdir SpeedRead
cp /pythonUsefull/SpeedRead/main.py /SpeedRead
cd SpeedRead && touch text.txt
```

## Usage

You just have to paste the text you want to read in the file "text.txt" and then run the "main.py"
```bash
python3 main.py
```
You can then tell which speed you want.
