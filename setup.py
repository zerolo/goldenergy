from setuptools import setup, find_namespace_packages

setup(
    name="goldenergy",
    version="0.0.1",
    description="Library to interact with Goldenergy API. Intended to be used for Home Assistant integration",
    python_requires='>=3',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    install_requires=[
        'python-dateutil',
        'aiohttp'
    ]
)
