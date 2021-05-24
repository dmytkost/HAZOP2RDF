from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


def get_author():
    author = ["Dmytro Kostiuk",
              "Vincenz Christian Forkel",
              "Artan Kabashi",
              "Marcus Rothhaupt"]

    author_str = ", ".join(author)

    return author_str


def get_author_email():
    author_email = ["dmytro.kostiuk@mailbox.tu-dresden.de",
                    "vincenz_christian.forkel@mailbox.tu-dresden.de",
                    "marcus.rothhaupt@mailbox.tu-dresden.de",
                    "artan.kabashi@mailbox.tu-dresden.de"]

    author_email_str = ", ".join(author_email)

    return author_email_str


setup(name="cli",
      version="0.2.0",
      author=get_author(),
      author_email=get_author_email(),
      description="CAE-PA",
      platforms=["Windows", "macOS"],
      packages=find_packages(),
      include_package_date=True,
      install_requires=read_requirements(),
      entry_points="""
        [console_scripts]
        cli=src.cli:cli
    """)
