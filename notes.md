# Classical Teacher Scraping

- [Base URLS](/Users/lachlankermode/code/paideia/latin-teachers/scrapy/schoolsites/start_urls.txt)
- [First Scrape](/Users/lachlankermode/code/paideia/latin-teachers/scrapy/schoolsites/output.json)
- [Second Scrape (adjusted for `teachers`)](/Users/lachlankermode/code/paideia/latin-teachers/scrapy/schoolsites/dmoz.json)

## Misidentifying Problems
- `Latino` organizations
- `Greek life`, `Greek letters` `Greek organizations` - perhaps just eliminate `Greek` from the search entirely, as it's unlikely high schools will offer it.
- Words like `simulating`, `calculating`, etc, that encapsulate phrases I'm searching for (should put spaces around word in regexp).
- Google Translate injections, where Latin and Greek are options.

## Scraper Issues
- The scraper is looking through all the HTML, not just visible text.
- The scraper is stopping two pages deep, which brute force search takes time and is not yielding relevant pages.
- Too many pages with the same base URL are populating the results (this may be fixed by only searching visible text, as I imagine this happens when one of the topnav links includes a relevant term). 

## Ideas
- Follow *promising* links, rather than performing a brute force search two pages deep.
 - Teacher directories
 - Any link with `Latin` or `Classics` should be marked *v promising*
- Only mine text that is visible on page (no metadata or link url). Links with should not be counted within page text, but should instead be followed if they seem *promising*.
- `Teacher` search isn't necessarily the greatest. I think it will be more productive to make a scraper that identifies school sites that have legitimate classical *activity*, and then human search from those URLs.
- Section of pre-existing latin teachers, and try to write a program that produces the same results
- More general comparisons against pre-existing data, cross-referenced against the data that the script is pulling.

## Actually Useful Links I Happened Across During Sampling
- [http://www.archbishopryan.com//apps/staff/](http://www.archbishopryan.com//apps/staff/)
- [http://www.archbishopryan.com//apps/pages/index.jsp?uREC_ID=285479&type=d&pREC_ID=652845](http://www.archbishopryan.com//apps/pages/index.jsp?uREC_ID=285479&type=d&pREC_ID=652845)
- [http://www.sms.edu/our-programs/travel/index.aspx](http://www.sms.edu/our-programs/travel/index.aspx)
- [http://www.mcgill-toolen.org/apps/departments/clubs.jsp](http://www.mcgill-toolen.org/apps/departments/clubs.jsp)

