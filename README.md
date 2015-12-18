# Latin Teachers, The Paideia Institute

The Paideia Institute currently has a data set that contains records of Latin and Classics teachers in American High Schools, which was collected manually a couple of years ago. This data set has not been maintained. In this project, the Institute is looking to verify, expand and generally improve these data records.

The Institute has written a two basic web crawlers to assist in improving this data. The first, all_schools, combs [www.privateschoolreview.com/](http://www.privateschoolreview.com/) and yields the websites that are listed for every listed school. The second, schoolsites, crawls this list of sites and searches for instances of phrases like 'Latin', 'Classics', and 'Classical Studies', yielding the URLs on which these phrases are found.

# Technology

These crawlers are written in Python, using a framework called [Scrapy](http://scrapy.org/). A crawler can visit URLs, and search through the information on those sites, yielding URLs that match search terms. In order to run this crawler, open up [Terminal](http://www.macworld.co.uk/feature/mac-software/get-more-out-of-os-x-terminal-3608274/) on Mac, or [Command Prompt](http://winaero.com/blog/how-to-open-elevated-command-prompt-in-windows-10/) on Windows.

If you don't already use Git, [here are instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install it. Once you have Git installed on your computer, navigate to an empty directory in Terminal, and run the following commands.

```
git init
git remote add origin https://github.com/breezycool/latin-teachers
git pull origin master
```

That directory should now have three folders in it, the same as the ones listed at the top of this page. If you're tech savvy, you should now read the [Scrapy docs](http://doc.scrapy.org/en/latest/intro/tutorial.html), or watch one of the [tutorials](https://www.youtube.com/watch?v=758KrjCgkN8) online in order to get the hang of the framework.

If you're not tech savvy, you can still further the project. Open up the file named `Latin.py`, which is inside a directory called `spiders`, inside the `schoolsites` directory. The second line in this file is all that you need to change in order to get different results. This line of code is setting the [Regular Expression](http://www.regular-expressions.info/tutorial.html) that the crawler is looking for on each school's site. If you can [learn what a regular expression is](http://lmgtfy.com/?q=regular+expression+tutorial), then you can just change this one line of code, and re-run the crawler to help out (see below for instructions on how to run the crawler).

# Running the Crawler
Make sure you have downloaded the files in this repository (read the rest of this document if you don't know what this means). Install Scrapy [here](http://doc.scrapy.org/en/latest/intro/install.html), and open up Terminal or Command Prompt and navigate to the *schoolsites* directory. Run the following command, and let the code do it's magic!

`scrapy crawl Latin -a filename=some_urls.txt -o RESULTS.txt`

When the program is finished (it will probably take about twenty minutes), the URLs that your program yielded will be in a file called `RESULTS.txt`.

# Problems
Send an email to kermode@paideia-institute.org, and I'll get back to you as quickly as I can. 




