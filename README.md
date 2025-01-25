# Web2PDF CLI Tool

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/web2pdf)](https://pypi.org/project/web2pdf/)
[![Build Status](https://github.com/devbernie/web2pdf/actions/workflows/build.yml/badge.svg)](https://github.com/devbernie/web2pdf/actions)

**Web2PDF** is a powerful command-line tool for converting websites to PDF files with advanced customization options. Built with Python and Playwright, it supports modern web technologies, including JavaScript-heavy websites.

---

## Features

- 🚀 Convert any website to PDF with a single command
- 🎨 Customize PDF layout (page size, orientation, margins)
- 🔒 Handle authentication (basic auth, cookies)
- ⏱️ Delay rendering to wait for dynamic content
- 📄 Add custom headers and footers
- 🌐 Proxy support for restricted networks
- 🛠️ Batch processing for multiple URLs

---

## Installation

### From PyPI (Recommended)
```bash
pip install web2pdf

### From Source

1.  Clone the repository:

    ```bash
    git clone https://github.com/devbernie/web2pdf.git
    cd web2pdf

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt

3.  Install Playwright browsers:

    ```bash
    playwright install chromium

* * * * *

Usage
-----

### Basic Conversion

```bash
web2pdf https://example.com output.pdf

### Advanced Options

```bash
web2pdf https://example.com report.pdf\
  --page-size A4\
  --orientation landscape\
  --margin 1 1 1 1\
  --header "My Custom Header"\
  --footer "Page {page} of {total}"\
  --delay 5000\
  --auth-user myuser\
  --auth-pass mypass

### Help Command

```bash
web2pdf --help

* * * * *

Configuration
-------------

### Environment Variables

-   `WEB2PDF_PROXY`: Set default proxy server

-   `WEB2PDF_TIMEOUT`: Set default timeout (in milliseconds)

* * * * *

Contributing
------------

We welcome contributions! Please follow these steps:

1.  Fork the repository

2.  Create a new branch (`git checkout -b feature/YourFeature`)

3.  Commit your changes (`git commit -m 'Add some feature'`)

4.  Push to the branch (`git push origin feature/YourFeature`)

5.  Open a Pull Request

* * * * *

License
-------

This project is licensed under the MIT License. See the [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE) file for details.

* * * * *

Support
-------

If you encounter any issues or have questions, please [open an issue](https://github.com/devbernie/web2pdf/issues).

* * * * *

Made with ❤️ by [devbernie](https://github.com/devbernie)