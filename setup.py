import setuptools

setuptools.setup(
    name="change-event-service",
    version="2.0.2",
    author="Ramazan Çetin",
    author_email="lramazancetinl@gmail.com",
    description="Change Event Service",
    url="https://github.com/mantis-software-company/change-event-service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['Flask~=2.0.2', 'flask-smorest~=0.36.0', 'marshmallow~=3.14.1', 'pyctuator~=0.18.1',
                      'SQLAlchemy~=1.4.29', 'SQLAlchemy-Utils~=0.38.2', 'Flask-APScheduler==1.12.3',
                      'pika~=1.2.0', 'python-slugify~=5.0.2', 'requests~=2.27.1'],
    python_requires=">3.8.*, <4",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)
