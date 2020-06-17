import setuptools

setuptools.setup(
    name='EZlogR',
    version='0.8dev',
    author='Jeremy Gillespie',
    author_email='jeremy@kodeslingr.com',
    description='This is a simple logging tool to help devs focus on writing code instead of writing logs.',
    url='http://www.ezlogr.com',
    packages=setuptools.find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    python_requires='>=3.6'
)