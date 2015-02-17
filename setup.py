from setuptools import setup

setup(
    name='mrs_plugins',
    version='0.1',
    packages=['flow'],
    url='',
    license='',
    author='ben',
    author_email='browland@partners.org',
    description='',
    entry_points={
        "mrs.flow.step": [
            "twix_loader = flow.load:twix_load_step",
            "rda_loader = flow.load:rda_load_step",
            "twix_svs = flow.twix:twix_svs_step",
            "lcmodel = flow.process:lcmodel_process_step",
            "ps2pdf = flow.utility:ps2pdf_step",
            "mail = flow.utility:mail_step",
            "wref = flow.utility:wref_step",
        ],
        "mrs.flow.dict": [
            "twix_loader = flow.load:twix_load_dict",
            "rda_loader = flow.load:rda_load_dict",
            "twix_svs = flow.twix:twix_svs_dict",
            "lcmodel = flow.process:lcmodel_process_dict",
            "ps2pdf = flow.utility:ps2pdf_dict",
            "mail = flow.utility:mail_dict",
            "wref = flow.utility:wref_dict",
        ],
    },
    requires=['pyflow', 'PySide'],
)
