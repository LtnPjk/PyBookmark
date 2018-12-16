# PyBookMark
Python terminal application to manipulate bookmarks of PDF files.

## Features
* Generate .txt of existing bookmark heirarchy in pdf
* Add bookmarks to pdf from existing .txt heirarchy
* Auto-add bookmarks to pdf from predefined per-page pattern


## Examples
python3 PyBookMark input.pdf output.pdf 
//Creates a new pdf output.pdf from input.pdf and adds bookmarks from default pattern in config.

python3 PyBookMark input.pdf output.txt -e
//Extracts bookmark heirarchy to output.txt

python3 PyBookMark input.pdf output.pdf instructions.txt
//Creates a new pdf and depending of formatting of instructions.txt, either adds bookmarks from text file or uses text file as pattern to generate bookmarks.

## Author
* **Olle Olofsson** - *Initial work* - [LtnPjk] 

## License
This project is licensed under GNU GPL
