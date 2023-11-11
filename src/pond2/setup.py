import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'pond2'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igor',
    maintainer_email='igor.garcia@sou.inteli.edu.br',
    description='Pacote para mapeamento da área e para o deslocamento do turtlebot.',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tartabot= pond2.tartabot:main',
            'teleop= pond2.teleop:main'
        ],
    },
)
