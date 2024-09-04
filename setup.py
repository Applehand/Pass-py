import setuptools

setuptools.setup(
    entry_points={
        'console_scripts': [
            'passpy=passpy.cli:main',
        ]
    }
)