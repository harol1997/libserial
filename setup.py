from setuptools import setup

readme = open("./README.md", "r")

setup(
    name="htlib",
    packages=['htlib'],
    version='0.1',
    description='',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Harol Alvarado',
    author_email='',
    url='https://github.com/harol1997/htlib/archive/refs/heads/main.zip',
    download_url='',
    keywords=['iot', 'pyserial'],
    classifiers=[],
    license='MIT',
    include_package_data=True
)