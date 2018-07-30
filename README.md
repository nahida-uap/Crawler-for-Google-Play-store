# Crawler-for-Google-Play-store
This is a Python based Google Play Crawler which require:
- Python
- Selenium (Install - pip install selenium)
- beautifulsoup4
- Chromedriver (need to place in the same working directory)

As Input user need to pass single or multi URL: urls = ["https://play.google.com/store/apps/details?id=com.facebook.orca" ] In returns the program will retrun the following fields and will store into seperate CSV files:
- App title
- Review text body
- Creation Date
- Corresponding Rating

To run the code type the following command:
> python google-play-store-review-crawler.py

*Modify the code based on the number of reviews need to extract.
