#!/user/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
import py2exe
import sys

sys.argv.append('py2exe')
includes = ["encodings","encodings.*","sip"]
data_files = [("imgs",glob.glob("Pregnent\\imgs\\*.png")),
              ("sound",glob.glob("Pregnent\\sound\\*.wav")),
              'Pregnent\\conf.ini',
              'Pregnent\\crc.dll'
             ]
options = {"py2exe":
            { "compressed":1,
                "optimize":2,
                "bundle_files":1,
                "includes": includes
                }
            }
        
setup(
        version = "1.0",
        description = "Holter",
        name = "Holter",
        options = options,
        zipfile = None,
        data_files = data_files,
        windows = ['Pregnent/Holter.py']
     )
