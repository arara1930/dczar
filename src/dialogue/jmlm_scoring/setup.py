from setuptools import find_packages, setup

setup(
    name="jmlm",
    version="0.1",
    description="Japanese Masked Language Model Scoring",
    packages=find_packages("jmlm"),
    package_dir={"": "jmlm"},
    install_requires=["transformers", "unidic_lite", "fugashi", "ipadic"],
    extras_require={},
    zip_safe=False,
)
