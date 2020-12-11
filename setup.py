import re
from setuptools import find_namespace_packages
from setuptools import setup


def find_version(path):
  with open(path, 'r', encoding='utf-8') as stream:
    return re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        stream.read(),
        re.M,
    ).group(1)


def read_long_description(path):
  with open(path, 'r', encoding='utf-8') as stream:
    return stream.read()


# @see https://python-packaging.readthedocs.io/en/latest/index.html  # noqa
# @see https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords  # noqa
# @see https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages  # noqa
setup(
    name='python-package-template',
    version=find_version('ilguyi/project/__init__.py'),
    author='Il Gu Yi',
    author_email='ilgu.yi.219@gmail.com',
    url='https://github.com/ilguyi/my-python-package-template',
    license='MIT',
    description='Il Gu Yi\'s python package template',
    long_description=read_long_description('README.md'),
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(include=['ilguyi.*']),
    classifiers=[
      'Environment :: GPU :: NVIDIA CUDA :: 11.0',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=[''],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
      # LIST THE DEPENDENCIES OF YOUR PACKAGE
      # FOR INSTANCE,
      # 'numpy>=1.19.2,
      'pre-commit',
      'nose',
    ],
    entry_points={
      'console_scripts': [
        'project-main = ilguyi.project.main:main',
      ]
    },
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)
