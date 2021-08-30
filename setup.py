import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='timer',
    version='1.0.0',
    author='Janik Fechtelpeter',
    author_email='janik.fechtelpeter@zi-mannheim.de',
    description='Conveniently time python commands',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/jmfechtelpeter/timer',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license='MIT',
    packages=['timer'],
    install_requires=['numpy', 'time'],
)