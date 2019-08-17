PythonForMatlabProgrammers Developer Notes
==========================================

# How it works

This site is designed for use on GitHub Pages. It uses Jekyll to generate the site files from Markdown.

## Setting up required tools

To use this, you'll need:

* A Unix environment (Mac, Linux, or Linux on Windows)
* Ruby
* Jekyll
* wkhtmltopdf
* Python 3
* pdfkit Python library

To install all this on macOS:

```
brew install ruby python
gem install jekyll bundler
pip install pdfkit
brew cask install wkhtmltopdf
```

## Building the combined docs

The main document files are the `0*-<chaptername>.md` files. There's a combined
`PythonForMatlabProgrammers.md` file that’s derived from these by concatenating them,
and a `PythonForMatlabProgrammers.pdf` that’s derived from the combined `.md` file.
Even though these are derived documents, they still need to be checked in to the Git 
repo for our GitHub Pages site to work. So, whenever you change any content in any
of the chapters, rebuild the derived files by doing this:

```
cd docs
make
```

And then commit the modified files to Git.

NOTE: For now, don’t commit the generated/modified PDF file to Git, because our
PDF generation stuff is producing a lousily-formatted PDF. We’re working on it.

## Running the site locally

You can use Jekyll to run the site locally so you can preview your changes before pushing them up to GitHub.

### One-time setup

To install the stuff you need to run the site, cd into the `docs/` directory and run `bundle install`.

### Running the site

To run the site, cd into the `docs/` directory and run `bundle exec jekyll serve`.

If you‘ve made any changes to the doc, make sure you rebuild the derived files
as described in “Building the combined doc” above.

# Prose style guide

* Oxford commas
* Name stylings:
  * MATLAB, Python
