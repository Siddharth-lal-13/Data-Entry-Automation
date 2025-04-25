# Data Entry Automation

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.9+-orange)
![Requests](https://img.shields.io/badge/Requests-2.25+-red)

## Overview

Data Entry Automation is a powerful Python-based solution designed to streamline repetitive data entry tasks. By leveraging web scraping technologies like Selenium WebDriver and BeautifulSoup, this tool extracts data from websites and automatically enters it into online forms, saving countless hours of manual data entry.

In this demonstration, the application scrapes property listings from a Zillow clone website and enters the data into a Google Form, which can then be easily exported to spreadsheet formats for analysis or record keeping.

## Features

- **Automated Web Scraping**: Extract property information including addresses, prices, and links from listing websites
- **Form Automation**: Automatically populate Google Forms with scraped data
- **Flexible Data Export**: Convert form responses to Excel, Google Sheets, or CSV formats
- **Customizable Delay Settings**: Configure wait times to accommodate website loading speeds
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Data-Entry-Automation.git
cd Data-Entry-Automation
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

1. Set up your Google Form with fields matching the data you want to collect (address, price, link)

2. Update the constants in the script with your form URL and target website
```python
GOOGLE_FORM = "your_google_form_url_here"
ZILLOW_URL = "target_website_url_here"
```

3. Run the script
```bash
python main.py
```

4. Access your Google Form responses and export them to your preferred format (Sheets, Excel, CSV)

## How It Works

1. **Data Extraction**: The program uses BeautifulSoup to parse the HTML of the specified website and extract property information.

2. **Browser Automation**: Selenium WebDriver opens a Chrome browser instance and navigates to the Google Form.

3. **Form Population**: The script automatically fills in form fields with the extracted data.

4. **Form Submission**: Once all fields are filled, the form is submitted and the process repeats for all entries.

## Customization

You can easily adapt this tool to work with different websites and forms:
- Modify the HTML element selectors in the BeautifulSoup section to target different data
- Update the XPath expressions to match the structure of your specific Google Form
- Adjust the timing parameters to accommodate different website loading speeds

## Requirements

- Python 3.9+
- Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- Internet connection

## Acknowledgments

- This project was inspired by the need to automate repetitive data entry tasks
- Thanks to the developers of Selenium and BeautifulSoup for their amazing tools

---

## 📄 License

Copyright (c) 2024 Siddharth-lal-13

This project is made available for **educational and non-commercial use only**.

You may:
- View and study this code
- Fork it for personal or academic learning
- Reference it with attribution

You may not:
- Use this project or any portion for commercial purposes
- Modify and redistribute it
- Deploy it publicly without explicit written permission from the author

For commercial licensing or collaboration inquiries, please contact: siddharthlal99@gmail.com

This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
See https://creativecommons.org/licenses/by-nc-nd/4.0/

---

## 👤 Author

**Developed by Siddharth Lal**  
- Email: [siddharthlal99@gmail.com](mailto:siddharthlal99@gmail.com)
- GitHub: [Siddharth-lal-13](https://github.com/Siddharth-lal-13)

Feel free to connect for collaboration or inquiries!

