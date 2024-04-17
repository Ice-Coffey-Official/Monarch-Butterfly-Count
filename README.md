# Monarch Butterfly Count

This program scrapes data from the [Western Monarch Count Website] (https://westernmonarchcount.org/data/) to gather information on monarch butterfly sightings from 1997 to 2024. It then extracts coordinates of where the butterflies were spotted using the [ArcGIS Experience Link] (https://experience.arcgis.com/experience/f9c6ce4664e0470eb681a46a143477ed/).

## How to Use
1. Make sure to have python and edge installed on your machine. If using a different web browser/driver, make sure to modify the code accordingly.

[Python Installation](https://www.python.org/downloads/)

[Edge Installation](https://www.microsoft.com/en-us/edge/download?form=MM1475)

2. cd into the project directory (wherever you saved it on your machine + "cd Monarch-Butterfly-Count")

3. Install the requirements with "pip install -r requirements.txt".

4. Run the program with "python ScrapeMonarchs.py". It takes anywhere from 30 minutes to an hour to complete, because there is backoff built in. Don't worry that it doesn't finish immediately.

5. Use the extracted data for your research, analysis, or any other purposes.


## Disclaimer
Please note that web scraping may be subject to legal restrictions depending on the website's terms of service. It is recommended to review and comply with the website's policies before using this scraper. 

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute this tool according to the terms of the license.

For any questions or feedback, please contact [flatwhitecoffey@gmail.com](mailto:flatwhitecoffey@gmail.com). Thank you for using Monarch Butterfly Count!
