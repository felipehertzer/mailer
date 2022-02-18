from setuptools import setup

setup(
    name='mailer',
    version="0.8.1",
    description="A module to send email simply in Python",
    author="Felipe Hertzer and Ryan Ginstrom",
    author_email='felipe@hertzer.net',
    url="https://github.com/felipehertzer/mailer",
    py_modules=["mailer"],
    keywords=["email", "smtp"],
    license="MIT License",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
