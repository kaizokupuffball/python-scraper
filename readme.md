# Python Scraper

This is a very simple scraper for directory listed websites.
It is not multithreaded or whatever to do multiple parallell file downloads. It takes one file at a time, but I'm open for pull requests if anyone know's how to do that. :)

When i say directory listed websites i mean theese kind of websites.

![example_website](https://dpsvdv74uwwos.cloudfront.net/statics/img/blogposts/directory_listing_enabled.png)

To run the script make sure to be in the same directory as the script and run: `python scraper.py`

You will need to enter the URL you want to scrape and i directory name you want the scraper to save the files to. The directory will be created inside the script directory.

You will also be asked for what files you want to download. This cannot be empty. 
You can write either `*` wich will download everything or you can write `.jpg, .png, .bmp` (comma separated extensions string).

Last you will be asked if anything should be ignored. And this ignore list is based on the link TEXT, not the HREF or file extension. A good option would be to write `Parent Directory` or any other stuff you want to ignore.
