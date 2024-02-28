# arXiv Submission Tips & Tricks
Some typical issues crop up when one uses an `aastex` class file on Overleaf to prepare a paper and then submits it to arXiv.


## Delete Unnecessary Files

The default `aastex` template on Overleaf comes with a few additional `.tex` files that can confuse the arXiv compiler. Delete all unnecessary `.tex` files. Some common ones are:-
* `natnotes.tex`
* `natbib.tex`
* `aassymbols.tex`

## Download the `.bbl` file
The best way to do this is to create a copy of your project on Overleaf; then hit submit. From the resulting search box, select arXiv; and this will generate a zip file with the `.bbl` file included and named exactly how the arXiv system prefers it to be.


## Specific Issues for `minted` Package

arXiv cannot process using the `--shell-escape` option while compiling with LaTeX, as this is disabled in arXiv's system for security reasons. This typically leads to the arXiv system refusing to compile submissions that are using minted. Here are some workarounds:-

* If you are importing `amsmath`, but not using it, comment it out
* Load the `hyperref` package at the end
* Now, on Overleaf, pass the following options to the `minted` package `\usepackage[finalizecache,cachedir=minted-cache]{minted}`
* This will create a folder in the compile directory called `minted-cache` that will contain a few files. 
* Download the `.zip` from Overleaf. Note that Overleaf doesn't include these cache files in this zip. 
* Expand the zip, and create a folder within the main directory called `minted-cache`. Download the contents of the cache by navigating to `Logs & Output Files` --> `Other logs and files`. Put all the downloaded cache files into the `minted-cache` folder
* Now, in the unzipped folder, open `main.tex` and freeze the minted cache by changing the package loading options to `\usepackage[frozencache,cachedir=minted-cache]{minted}`
* Now, rezip this folder and upload to arXiv. 
