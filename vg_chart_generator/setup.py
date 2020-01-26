try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Video Game Chart Generator',
    'author': 'Anthony LaRocca',
    'url': 'https://github.com/Stakes84/vg-charts',
    'author_email': 'zensky@gmail.com',
    'version': '1.0.0',
    'install_requires': ['argparse',
                         'matplotlib',
                         'pandas'],
    'packages': ['vg_chart_generator'],
    'package_data':{ 'vg_chart_generator': ['*.csv']},
    'include_package_data': True,
    'name': 'vg_chart_generator',
    'entry_points': {'console_scripts': ['vg-chart-generator=vg_chart_generator:main']}
}

setup(**config)