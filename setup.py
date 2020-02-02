"""The setup script."""

from setuptools import setup, find_packages


setup_requirements = ['pytest-runner', 'flake8-plugin-utils']


setup(
    author="Ruslan Kirilyuk",
    author_email='godi4e@gmail.com',
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Flake8 plugin to check allure decorators on test classes and methods",
    license="MIT license",
    include_package_data=True,
    keywords=[
        'flake8', 'pytest', 'py.test', 'allure'
    ],
    name='flake8_allure_pytest',
    packages=find_packages(include=['flake8_allure_pytest']),
    setup_requires=setup_requirements,
    version='0.0.1',
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'AL = flake8_allure_pytest.plugin:AllurePytestPlugin',
        ],
    },
)
