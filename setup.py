import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'vision_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*.py'))),
        (os.path.join('share', package_name, 'config'),
         glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='suke',
    maintainer_email='keisuke.yoshida622@mail.kyutech.jp',
    description='vision node for tomato robots',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_publisher = vision_package.image_publisher:main',
            'yolov5_ros2 = vision_package.yolov5_ros2:main',
            'seg_ros2 = vision_package.seg_ros2:main',
            'harvest_order = vision_package.harvest_order:main',
            'vision_service = vision_package.vision_service:main',
        ],
    },
)
