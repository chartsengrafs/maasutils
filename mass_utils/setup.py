from setuptools import setup
setup(name='maas_utils',
version='0.1',
description='Package for EDA, Transform, and modeling in Pandas, Spark, H2O, XGBoost',
author='Erik Case',
author_email='e.case@f5.com',
license='MIT',
packages=['faker', 'pandas', 'pyspark', 'koalas', 'h2o', 'pysparkling'],
zip_safe=False)