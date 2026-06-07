from setuptools import find_packages, setup


setup(
    name="zenkb",
    version="0.1.0",
    description="Canonical KB pipeline for ZenStatement raw knowledge documents",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[],
    extras_require={"adk": ["google-adk"]},
    python_requires=">=3.9",
    entry_points={"console_scripts": ["zenkb=zenkb.cli:main"]},
)
