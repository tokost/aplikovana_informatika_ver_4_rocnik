# setup.py

from setuptools import find_packages, setup
setup(
    name='mypythonlib',  # toto je nazov nasej kniznice
    # packages=find_packages(), nahradili sme prikazom ktory
    packages=find_packages(include=['mypythonlib']),  # vlozi do kniznice
    # iba subory z nasho adresara
    version='0.1.0',
    description='Moja prvá knižnica Python',
    author='Tomáš Tokoš',
    license='SŠŠ Trenčín',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
)
