from setuptools import setup, find_packages

setup(
    name="web2pdf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.8",
        "playwright>=1.49.1",
        "python-dotenv>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "web2pdf=web2pdf.cli:main",
        ],
    },
    python_requires=">=3.10",
)