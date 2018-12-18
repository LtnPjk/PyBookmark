# PyBookMark
Python terminal application to manipulate bookmarks of PDF files.

## Features
* Generate .txt of existing bookmark heirarchy in pdf
* Add bookmarks to pdf from existing .txt heirarchy
* Auto-add bookmarks to pdf from predefined per-page pattern

## Examples
python3 PyBookMark.py -i "input.pdf" -o "output.txt" -e
//Extracts bookmark heirarchy to output.txt

python3 PyBookMark.py -i "input.pdf" -o "output.pdf" -p "instructions.txt"
//Creates a new pdf and depending of formatting of instructions.txt, either adds bookmarks from text file or uses text file as pattern to generate bookmarks.

python3 PyBookMark.py -b "path to folder" -p "instructions.txt"
//Applies operation to all PDFs in specified folder and puts the new files, with unchanged names, in a new subfolder.

## Author
* **Olle Olofsson** - *Initial work* - [LtnPjk] 

## License
This project is licensed under GNU GPL
