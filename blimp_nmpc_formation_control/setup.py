from setuptools import find_packages, setup

package_name = 'blimp_nmpc_formation_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(
        include=["blimp_nmpc_formation_control.config"],
        exclude=["test"]
    ),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mohamed-Taha',
    maintainer_email='mohamed.a.m.i.taha@gmail.com',
    description='Calculate and relay formation parameters to blimps',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'blimp_nmpc_formation_controller = blimp_nmpc_formation_control.blimp_nmpc_formation_controller:main'
        ],
    },
)
