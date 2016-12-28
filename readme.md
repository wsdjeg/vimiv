![vimiv banner](https://raw.githubusercontent.com/karlch/vimiv/master/icons/vimiv_banner_400.png)

[![License badge](https://img.shields.io/aur/license/vimiv.svg)](https://raw.githubusercontent.com/karlch/vimiv/master/LICENSE)
[![Coverage](https://codecov.io/gh/karlch/vimiv/branch/master/graph/badge.svg)](https://codecov.io/gh/karlch/vimiv)
[![Code Health](https://landscape.io/github/karlch/vimiv/master/landscape.svg?style=flat)](https://landscape.io/github/karlch/vimiv/master)
[![Version badge](https://img.shields.io/aur/version/vimiv.svg)](https://aur.archlinux.org/packages/vimiv/)

#### Version 0.8 (unreleased)

[Releases](https://github.com/karlch/vimiv/releases "releases")
|
[Website](http://karlch.github.io/vimiv/ "website")
|
[Documentation](http://karlch.github.io/vimiv/documentation/ "website")
|
[Changelog](http://karlch.github.io/vimiv/changelog/ "changelog")

Vimiv is an image viewer with vim-like keybindings. It is written in python3
using the Gtk3 toolkit. Some of the features are:
* Thumbnail mode
* Simple library browser
* Basic image editing
* Command line with tab completion

For much more information please check out the
[documentation](http://karlch.github.io/vimiv/documentation/ "documentation").
If you are new to vimiv, this is a good place to
[get started](http://karlch.github.io/vimiv/documentation/usage/ "usage")
.

## Screenshots

#### Open image and library

<img src="http://karlch.github.io/vimiv/images/screenshots/library.png" alt="Library" width="700">

#### Thumbnail mode

<img src="http://karlch.github.io/vimiv/images/screenshots/thumbnail.png" alt="Thumbnail" width="700">

## Installation
Install the dependencies listed below first. To use the
development version clone this repository,
for the latest stable check out the 
<a href="https://github.com/karlch/vimiv/releases">releases</a>
page. To install a simple `# make install` should suffice. To remove vimiv the
standard `# make uninstall` works.  You may need to update your icon cache after
installation.

For Arch Linux users there are two packages in the AUR.
<a href="https://aur.archlinux.org/packages/vimiv/">vimiv</a> for the
stable version and
<a href="https://aur.archlinux.org/packages/vimiv-git/">vimiv-git</a>
for the development branch.

## Dependencies
* python3
* python-gobject
* gtk3
* python-pillow
* python-setuptools (for installation)
* jhead (optional for much better autorotation depending on EXIF data)

## Thanks to
* James Campos, author of [Pim](https://github.com/Narrat/Pim) which was the
  starting point for vimiv
* Bert Muennich, author of [sxiv](https://github.com/muennich/sxiv) which
  inspired many of the features of vimiv.
* Anyone who has contributed or reported bugs
