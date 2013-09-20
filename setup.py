from setuptools import setup, find_packages

setup(
    name="parent",
    version="0.1",
    install_requires=["requests==1.0.0", "child", ],
    dependency_links=[r'git+ssh://git@github.com/bhodorog/child_prj.git#egg=child-prj-0.1', ],
    packages=find_packages(),
)

