from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="healthcare-rcm-analytics",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Healthcare Revenue Cycle Analytics Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/healthcare-rcm-analytics",
    packages=find_packages(),
    python_requires=">=3.9",
)
