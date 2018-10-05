from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Avulsion

Avulsion = bmi_factory(Avulsion)

del bmi_factory
