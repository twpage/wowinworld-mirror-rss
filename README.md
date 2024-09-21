# wowinworld-mirror-rss
 Filters a given RSS feed (In the default case, Wow In the World Podcast) and generates a new RSS feed based off given filter criteria. This is a pretty niche case.

# run
 Execute the python script `wowinworld-mirror-rss.py` 
 If you prefer a Notebook version, use `wowinworld-mirror-rss-v2.ipynb`

# modify
 The filtering is done in the `check_filter` function.
 It is passed in the RSS Entry as an [ElemenTree Element](https://docs.python.org/3/library/xml.etree.elementtree.html)
