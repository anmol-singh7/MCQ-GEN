from setuptools import find_packages, setup

setup(
    name ='mcqgenerator',
    version='0.0.1',
    author='anmol',
    author_email="singhanmol0984@gmail.com",
    install_requires=["openai","langchain-huggingface","huggingface_hub","transformers","accelerate","langchain","langchain-community","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
