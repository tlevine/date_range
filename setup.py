from distutils.core import setup

setup(name='date_range',
    maintainer='Thomas Levine',
    maintainer_email='_@thomaslevine.com',
    description='Like the builtin range function, but for datetime.date objects',
    url='https://github.com/tlevine/date_range.git',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    py_modules=['date_range'],
    install_requires = [],
    version='0.0.1',
    license='LGPL'
)
