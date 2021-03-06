#-----------------------------------------------------------------------------
# Copyright (c) 2013-2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


hiddenimports = ["sip",
                 "PyQt5.QtCore",
                 "PyQt5.QtGui",
                 "PyQt5.QtNetwork"
                 ]
# WebKit definitely does not imply any of the following,
# which needlessly inflate the app.
#"PyQt5.QtQuick",
#"PyQt5.QtQml",
#"PyQt5.QtSql",
#"PyQt5.QtSensors"
