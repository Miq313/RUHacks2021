# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Built-in optimizer classes.

For more examples see the base class `tf.keras.optimizers.Optimizer`.

"""

from __future__ import print_function as _print_function

import sys as _sys

from . import schedules
from tensorflow.python.keras.optimizer_v2.adadelta import Adadelta
from tensorflow.python.keras.optimizer_v2.adagrad import Adagrad
from tensorflow.python.keras.optimizer_v2.adam import Adam
from tensorflow.python.keras.optimizer_v2.adamax import Adamax
from tensorflow.python.keras.optimizer_v2.ftrl import Ftrl
from tensorflow.python.keras.optimizer_v2.gradient_descent import SGD
from tensorflow.python.keras.optimizer_v2.nadam import Nadam
from tensorflow.python.keras.optimizer_v2.optimizer_v2 import OptimizerV2 as Optimizer
from tensorflow.python.keras.optimizer_v2.rmsprop import RMSprop
from tensorflow.python.keras.optimizers import deserialize
from tensorflow.python.keras.optimizers import get
from tensorflow.python.keras.optimizers import serialize

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.optimizers", public_apis=None, deprecation=True,
      has_lite=False)
