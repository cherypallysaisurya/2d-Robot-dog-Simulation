from setuptools import setup, find_packages

setup(
    name="robot_behavior",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A 2D robot simulation framework for educational purposes",
    long_description=open("README.md").read() if __name__ == "__main__" else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="robot simulation education programming tkinter",
    project_urls={
        "Source": "https://github.com/your-username/robot-behavior",
        "Documentation": "https://github.com/your-username/robot-behavior/blob/main/README.md",
    },
)
