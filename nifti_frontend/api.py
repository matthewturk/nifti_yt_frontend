"""
API for Nifti frontend



"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, yt Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from .data_structures import \
      NiftiGrid, \
      NiftiHierarchy, \
      NiftiDataset

from .fields import \
      NiftiFieldInfo

from .io import \
      NiftiIOHandler
