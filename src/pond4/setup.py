from setuptools import find_packages, setup

package_name = 'pond4'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igor',
    maintainer_email='igor.garcia@sou.inteli.edu.br',
    description='Pacote para um chatbot com LLM<',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'llama = pond4.llama:main', 
        ],
    },
)
