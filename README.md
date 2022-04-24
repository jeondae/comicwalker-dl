# comicwalker-dl

A python tool to download free manga/comic from [ComicWalker](https://comic-walker.com/ "ComicWalker official website").

The downloaded images are untouched and original from source, they are not modified in any way. flow:

> image source (.webp) -> download process by python script -> output (.webp)

## Requirements
- python version 3
- essential modules on `requirements.txt`, do `pip install -r requirements.txt`
    - for all modules see inside the code

## Usage
this tool is a standalone python script, you can download the files as a zip/git clone, or just download `walker.py` and the requirements is enough.

0. prep the requirements beforehand
1. put `walker.py` in a folder of your choice
2. open a terminal (.i.e CMD) in that folder
3. see below for detailed usage

all downloaded chapters are saved to `downloaded_chapters\{title}\{chapter}`

---
```
usage: walker.py [-h] [-cid CID] [-nolog]

optional arguments:
  -h, --help  show this help message and exit
  -cid CID    content id, &cid={...}. see url when reading a chapter
  -nolog      no progressive download logs on terminal
```
---

to download a chapter, simply run the .py script by:

```> python walker.py -cid [CID]```

---

example:

```> python walker.py -cid KDCW_CW01000002010001_68```

---

add `-nolog` argument if you want clean terminal output during the progress.

```> python walker.py -cid KDCW_CW01000002010001_68 -nolog```

---

feel free to modify the code as you wish.
