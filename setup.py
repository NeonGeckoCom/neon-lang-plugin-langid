#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon_lang_plugin_langidpy = ' \
                     'neon_lang_plugin_langidpy:LangIdPyDetector'
setup(
    name='neon_lang_plugin_langidpy',
    version='0.0.1',
    description='',
    url='https://github.com/NeonGeckoCom/neon-lang-plugin-langig',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['neon_lang_plugin_langidpy'],
    install_requires=["ovos-plugin-manager>=0.0.1a2",
                      "langid~=1.1.6"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='neon mycroft plugin language detection',
    entry_points={'neon.plugin.lang.detect': PLUGIN_ENTRY_POINT}
)
