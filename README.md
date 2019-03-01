# interlinear-tanakh

As I started my journey of learning Hebrew, I became interested in buying an interlinear Tanakh.  However, the interlinear Tanakhs that I found didn't seem to be the best quality - either the pages had no space for notes, the print required a magnifying glass, or the Hebrew words were not printed clearly and consistently.

So, I decided to write two Python scripts:  

1) A web scraper to scrape data from BibleHub.com and store the data in a SQLite database
2) A script that generates a PDF for each book in the Tanakh based on the data in the SQLite database.

I'm pleased with the first iteration of this idea and thought I'd share it with others, so I've created [this](http://tanakh-jones-chris.s3-website-us-east-1.amazonaws.com/) simple website.

Future enhancements might include customizable spacing and data points (the romanized word, chapter numbers, verse numbers, etc) :).
