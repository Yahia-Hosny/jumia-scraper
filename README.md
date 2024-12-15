# jumia-scraper
This project is a web scraper designed to extract product information (names and prices) from the [Jumia Android Phones](https://www.jumia.com.eg/android-phones/) page. The data is saved in a CSV file for further analysis.  **Note:** This project is intended for educational purposes only.
## Features
- Extracts product names and prices.
- Handles pagination to scrape data across multiple pages.
- Automatically dismisses pop-up windows if they appear.

## Technologies Used
- Python
- Selenium for web scraping
- pandas for data processing

## Prerequisites
- Python 3.7 or later installed.
- Google Chrome browser installed.
- ChromeDriver compatible with your browser version.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Yahia-Hosny/jumia-scraper.git
   ```
2. Install the required dependencies:
   ```bash
   pip install selenium pandas
   ```
3. Download and configure ChromeDriver:
   - [Download ChromeDriver](https://chromedriver.chromium.org/downloads).
   - Place the `chromedriver` executable in your PATH or specify its location in the script.

## Usage
1. Run the script:
   ```bash
   python web_scraber.py
   ```
2. The extracted data will be saved in a file named `products.csv`.

## Notes
- Ensure that your Chrome browser version matches the ChromeDriver version.
- If the scraper fails due to website changes, update the XPath/CSS selectors accordingly.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
