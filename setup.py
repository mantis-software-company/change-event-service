import setuptools

setuptools.setup(
    name="change-event-service",
    version="1.0.0-6",
    author="Ramazan Çetin, Fatih Mehmet ARSLAN",
    author_email="lramazancetinl@gmail.com, contact@fmarslan.com",
    contributors=[
        ['Furkan Kalkan', 'furkankalkan@mantis.com.tr', 'maintainer'],
        ['Derya Pelin Deniz', 'deryapelindenizzz@gmail.com', 'maintainer'],
        ['Fatih Mehmet ARSLAN', 'contact@fmarslan.com', 'maintainer'],
    ],
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
    install_requires=['Flask~=2.0.2', 'flask-smorest~=0.35.0', 'Flask-SQLAlchemy~=2.5.1','SQLAlchemy~=1.4.25', 'apscheduler==3.8.1', 'pika==1.2.0', 'pyctuator~=0.16.0', 'psycopg2-binary~=2.9.2',
                      'marshmallow~=3.14.0', 'SQLAlchemy-Utils~=0.37.8',  'requests~=2.26.0'],
    python_requires=">3.8.*, <4",
    packages=setuptools.find_packages(),
    scripts=['bin/change_event_service']
)
