##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.ZenUtils.Utils import unused


# Patch last to avoid import recursion problems.
from ZenPacks.zenoss.PythonCollector import patches
unused(patches)
