from setuptools import setup, find_packages
import press_links

dependency_links = [
    'git+ssh://git@github.com/mvpoland/django-templatable-view.git@1.2.0#egg=django_templatable_view-1.2.0'
]

setup(
    name="django-press-links",
    version=press_links.__version__,
    url='https://github.com/citylive/django-press-links',
    license='BSD',
    description="Press app",
    long_description=open('README.rst', 'r').read(),
    author='City Live nv',
    packages=find_packages('.'),
    install_requires=['django-tinymce==1.5.3', 'django_templatable_view'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    dependency_links=dependency_links,
)
