import setuptools

setuptools.setup(
    name="ChangeEventLogService",
    version="1.0.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['marshmallow~=3.14.0', 'Flask~=2.0.2', 'flask-smorest~=0.35.0',
                      'Flask-SQLAlchemy~=2.5.1', 'SQLAlchemy-Utils~=0.37.8', 'pyctuator~=0.16.0', 'requests~=2.26.0',
                      'SQLAlchemy~=1.4.25', 'PyJWT~=2.3.0', 'oauthlib~=3.1.1', 'psycopg2-binary~=2.9.2',
                      'cryptography>=3.3.1', 'apscheduler==3.8.1', 'pika==1.2.0'],
    python_requires=">3.8.*, <4",
    packages=setuptools.find_packages(),
    scripts=['change_event_query/app.py']
)
