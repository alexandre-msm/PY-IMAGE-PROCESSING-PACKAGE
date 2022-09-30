from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="py_image_processing",
    version="0.0.1",
    author="Alexandre Miranda",
    author_email="alexandre.msm88@gmail.com",
    description="The package 'py_image_processing' combine the colors of the img 2 in the img 1, basically.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
