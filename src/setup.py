from setuptools import find_packages, setup

package_name = "smarturtle_recognise_people"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="temesi",
    maintainer_email="temesi@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "smarturtle_people_CV = smarturtle_recognise_people.smarturtle_people_CV:main"
        ],
    },
)
