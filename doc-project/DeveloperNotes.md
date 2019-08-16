PythonForMatlabCoders Developer Notes
=====================================

# How it works

This site is designed for use on GitHub Pages. It uses Jekyll to generate the site files from Markdown.

## Building the combined doc

The main document files are the `0*-<chaptername>.md` files. There's a combined
`PythonForMatlabProgrammers.md` file that’s derived from these by concatenating them.
Even though it’s a derived document, it still needs to be checked in to the Git 
repo for our GitHub Pages site to work. So, whenever you change any content in any
of the chapters, rebuild the derived files by doing this:

```
cd docs
make
```

And then check in the modified files to Git.

## Running the site locally

You can use Jekyll to run the site locally so you can preview your changes before pushing them up to GitHub.

To do this, you’ll need Ruby and Bundler. Install Ruby, and then run `gem install bundler`.

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
