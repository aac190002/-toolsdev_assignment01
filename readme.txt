toolsdev_assignment01
Asmita Chitale
Assignment 01
ATCM 3311.0U1
06/11/2020


=== EXTERNAL MODULES ===

This script requires the following additional Python 3 modules:

1. newspaper3k - Specified in instructions
2. nltk - Specified in instructions
3. progressbar2 - To show progress while downloading news articles


=== FILE DESCRIPTIONS ===
- src - directory for the source code
	- gathernews.py - the main Python 3 script
	- page_template.html - template for the extra feature, an HTML page with clickable links
	- card_template.html - template for the extra feature, HTML cards with clickable links
- .gitignore - list of paths for GitHub to ignore, such as venv and .idea
- github.txt - has a link to the GitHub page for this project
- news_summary.txt - text output as specified in the instructions
- readme.txt - this file
- yournews.html - the extra feature, a generated custom HTML page


=== NOTES FOR INSTRUCTOR ===

1. The extra feature is a custom HTML summary page of the filtered articles. The top_image member of newspaper3k articles is used, and the HTML page is formatted using Bootstrap.
2. The name of the module is 'newspaper3k', but to import it you have to use 'import newspaper'
3. Ars Technica happens to have more articles than the other news sources