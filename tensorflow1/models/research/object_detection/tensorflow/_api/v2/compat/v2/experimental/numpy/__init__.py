# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""# tf.experimental.numpy: NumPy API on TensorFlow.

This module provides a subset of NumPy API, built on top of TensorFlow
operations. APIs are based on and have been tested with NumPy 1.16 version.

The set of supported APIs may be expanded over time. Also future releases may
change the baseline version of NumPy API being supported. A list of some
systematic differences with NumPy are listed later in the "Differences with
NumPy" section.

## Getting Started

Please also see [TensorFlow NumPy Guide](
https://www.tensorflow.org/guide/tf_numpy).

In the code snippets below, we will assume that `tf.experimental.numpy` is
imported as `tnp` and NumPy is imported as `np`

```python
print(tnp.ones([2,1]) + tnp.ones([1, 2]))
```

## Types

The module provides an `ndarray` class which wraps an immutable `tf.Tensor`.
Additional functions are provided which accept array-like objects. Here
array-like objects includes `ndarrays` as defined by this module, as well as
`tf.Tensor`, in addition to types accepted by NumPy.

A subset of NumPy dtypes are supported. Type promotion follows NumPy
semantics.

```python
print(tnp.ones([1, 2], dtype=tnp.int16) + tnp.ones([2, 1], dtype=tnp.uint8))
```

## Array Interface

The `ndarray` class implements the `__array__` interface. This should allow
these objects to be passed into contexts that expect a NumPy or array-like
object (e.g. matplotlib).

```python
np.sum(tnp.ones([1, 2]) + np.ones([2, 1]))
```


## TF Interoperability

The TF-NumPy API calls can be interleaved with TensorFlow calls
without incurring Tensor data copies. This is true even if the `ndarray` or
`tf.Tensor` is placed on a non-CPU device.

In general, the expected behavior should be on par with that of code involving
`tf.Tensor` and running stateless TensorFlow functions on them.

```python
tnp.sum(tnp.ones([1, 2]) + tf.ones([2, 1]))
```

Note that the `__array_priority__` is currently chosen to be lower than
`tf.Tensor`. Hence the `+` operator above returns a `tf.Tensor`.

Additional examples of interopability include:

*  using `with tf.GradientTape()` scope to compute gradients through the
  TF-NumPy API calls.
*  using `tf.distribution.Strategy` scope for distributed execution
*  using `tf.vectorized_map()` for speeding up code using auto-vectorization



## Device Support

Given that `ndarray` and functions wrap TensorFlow constructs, the code will
have GPU and TPU support on par with TensorFlow. Device placement can be
controlled by using `with tf.device` scopes. Note that these devices could
be local or remote.

```python
with tf.device("GPU:0"):
  x = tnp.ones([1, 2])
print(tf.convert_to_tensor(x).device)
```

## Graph and Eager Modes

Eager mode execution should typically match NumPy semantics of executing
op-by-op. However the same code can be executed in graph mode, by putting it
inside a `tf.function`. The function body can contain NumPy code, and the inputs
can be `ndarray` as well.

```python
@tf.function
def f(x, y):
  return tnp.sum(x + y)

f(tnp.ones([1, 2]), tf.ones([2, 1]))
```
Python control flow based on `ndarray` values will be translated by
[autograph](https://www.tensorflow.org/code/tensorflow/python/autograph/g3doc/reference/index.md)
into `tf.cond` and `tf.while_loop` constructs. The code can be XLA compiled
for further optimizations.

However, note that graph mode execution can change behavior of certain
operations since symbolic execution may not have information that is computed
during runtime. Some differences are:

*   Shapes can be incomplete or unknown in graph mode. This means that
    `ndarray.shape`, `ndarray.size` and `ndarray.ndim` can return `ndarray`
    objects instead of returning integer (or tuple of integer) values.
*   `__len__`, `__iter__` and `__index__` properties of `ndarray`
    may similarly not be supported in graph mode. Code using these
    may need to change to explicit shape operations or control flow
    constructs.
*   Also note the [autograph limitations](
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/limitations.md).


## Mutation and Variables

`ndarrays` currently wrap immutable `tf.Tensor`. Hence mutation
operations like slice assigns are not supported. This may change in the future.
Note however that one can directly construct a `tf.Variable` and use that with
the TF-NumPy APIs.

```python
tf_var = tf.Variable(2.0)
tf_var.assign_add(tnp.square(tf_var))
```

## Differences with NumPy

Here is a non-exhaustive list of differences:

*   Not all dtypes are currently supported. e.g. `np.float96`, `np.float128`.
    `np.object`, `np.str`, `np.recarray` types are not supported.
*   `ndarray` storage is in C order only. Fortran order, views, `stride_tricks`
    are not supported.
*   Only a subset of functions and modules are supported. This set will be
    expanded over time. For supported functions, some arguments or argument
    values may not be supported. This differences are generally provide in the
    function comments. Full `ufunc` support is also not provided.
*   Buffer mutation is currently not supported. `ndarrays` wrap immutable
    tensors. This means that output buffer arguments (e..g `out` in ufuncs) are
    not supported
*   NumPy C API is not supported. NumPy's Cython and Swig integration are not
    supported.

"""

from __future__ import print_function as _print_function

import sys as _sys

from . import random
from tensorflow.python.ops.numpy_ops import issubdtype
from tensorflow.python.ops.numpy_ops import max
from tensorflow.python.ops.numpy_ops import min
from tensorflow.python.ops.numpy_ops import round
from tensorflow.python.ops.numpy_ops.np_array_ops import all
from tensorflow.python.ops.numpy_ops.np_array_ops import amax
from tensorflow.python.ops.numpy_ops.np_array_ops import amin
from tensorflow.python.ops.numpy_ops.np_array_ops import any
from tensorflow.python.ops.numpy_ops.np_array_ops import arange
from tensorflow.python.ops.numpy_ops.np_array_ops import around
from tensorflow.python.ops.numpy_ops.np_array_ops import array
from tensorflow.python.ops.numpy_ops.np_array_ops import asanyarray
from tensorflow.python.ops.numpy_ops.np_array_ops import asarray
from tensorflow.python.ops.numpy_ops.np_array_ops import ascontiguousarray
from tensorflow.python.ops.numpy_ops.np_array_ops import atleast_1d
from tensorflow.python.ops.numpy_ops.np_array_ops import atleast_2d
from tensorflow.python.ops.numpy_ops.np_array_ops import atleast_3d
from tensorflow.python.ops.numpy_ops.np_array_ops import broadcast_arrays
from tensorflow.python.ops.numpy_ops.np_array_ops import broadcast_to
from tensorflow.python.ops.numpy_ops.np_array_ops import compress
from tensorflow.python.ops.numpy_ops.np_array_ops import copy
from tensorflow.python.ops.numpy_ops.np_array_ops import cumprod
from tensorflow.python.ops.numpy_ops.np_array_ops import cumsum
from tensorflow.python.ops.numpy_ops.np_array_ops import diag
from tensorflow.python.ops.numpy_ops.np_array_ops import diag_indices
from tensorflow.python.ops.numpy_ops.np_array_ops import diagflat
from tensorflow.python.ops.numpy_ops.np_array_ops import diagonal
from tensorflow.python.ops.numpy_ops.np_array_ops import dsplit
from tensorflow.python.ops.numpy_ops.np_array_ops import dstack
from tensorflow.python.ops.numpy_ops.np_array_ops import empty
from tensorflow.python.ops.numpy_ops.np_array_ops import empty_like
from tensorflow.python.ops.numpy_ops.np_array_ops import expand_dims
from tensorflow.python.ops.numpy_ops.np_array_ops import eye
from tensorflow.python.ops.numpy_ops.np_array_ops import flip
from tensorflow.python.ops.numpy_ops.np_array_ops import fliplr
from tensorflow.python.ops.numpy_ops.np_array_ops import flipud
from tensorflow.python.ops.numpy_ops.np_array_ops import full
from tensorflow.python.ops.numpy_ops.np_array_ops import full_like
from tensorflow.python.ops.numpy_ops.np_array_ops import hsplit
from tensorflow.python.ops.numpy_ops.np_array_ops import hstack
from tensorflow.python.ops.numpy_ops.np_array_ops import identity
from tensorflow.python.ops.numpy_ops.np_array_ops import imag
from tensorflow.python.ops.numpy_ops.np_array_ops import isscalar
from tensorflow.python.ops.numpy_ops.np_array_ops import ix_
from tensorflow.python.ops.numpy_ops.np_array_ops import mean
from tensorflow.python.ops.numpy_ops.np_array_ops import moveaxis
from tensorflow.python.ops.numpy_ops.np_array_ops import ndim
from tensorflow.python.ops.numpy_ops.np_array_ops import newaxis
from tensorflow.python.ops.numpy_ops.np_array_ops import nonzero
from tensorflow.python.ops.numpy_ops.np_array_ops import ones
from tensorflow.python.ops.numpy_ops.np_array_ops import ones_like
from tensorflow.python.ops.numpy_ops.np_array_ops import pad
from tensorflow.python.ops.numpy_ops.np_array_ops import prod
from tensorflow.python.ops.numpy_ops.np_array_ops import ravel
from tensorflow.python.ops.numpy_ops.np_array_ops import real
from tensorflow.python.ops.numpy_ops.np_array_ops import repeat
from tensorflow.python.ops.numpy_ops.np_array_ops import reshape
from tensorflow.python.ops.numpy_ops.np_array_ops import roll
from tensorflow.python.ops.numpy_ops.np_array_ops import rot90
from tensorflow.python.ops.numpy_ops.np_array_ops import select
from tensorflow.python.ops.numpy_ops.np_array_ops import shape
from tensorflow.python.ops.numpy_ops.np_array_ops import sign
from tensorflow.python.ops.numpy_ops.np_array_ops import size
from tensorflow.python.ops.numpy_ops.np_array_ops import split
from tensorflow.python.ops.numpy_ops.np_array_ops import squeeze
from tensorflow.python.ops.numpy_ops.np_array_ops import stack
from tensorflow.python.ops.numpy_ops.np_array_ops import std
from tensorflow.python.ops.numpy_ops.np_array_ops import sum
from tensorflow.python.ops.numpy_ops.np_array_ops import swapaxes
from tensorflow.python.ops.numpy_ops.np_array_ops import take
from tensorflow.python.ops.numpy_ops.np_array_ops import take_along_axis
from tensorflow.python.ops.numpy_ops.np_array_ops import transpose
from tensorflow.python.ops.numpy_ops.np_array_ops import tri
from tensorflow.python.ops.numpy_ops.np_array_ops import tril
from tensorflow.python.ops.numpy_ops.np_array_ops import triu
from tensorflow.python.ops.numpy_ops.np_array_ops import vander
from tensorflow.python.ops.numpy_ops.np_array_ops import var
from tensorflow.python.ops.numpy_ops.np_array_ops import vsplit
from tensorflow.python.ops.numpy_ops.np_array_ops import vstack
from tensorflow.python.ops.numpy_ops.np_array_ops import where
from tensorflow.python.ops.numpy_ops.np_array_ops import zeros
from tensorflow.python.ops.numpy_ops.np_array_ops import zeros_like
from tensorflow.python.ops.numpy_ops.np_arrays import ndarray
from tensorflow.python.ops.numpy_ops.np_dtypes import bool_
from tensorflow.python.ops.numpy_ops.np_dtypes import complex128
from tensorflow.python.ops.numpy_ops.np_dtypes import complex64
from tensorflow.python.ops.numpy_ops.np_dtypes import complex_
from tensorflow.python.ops.numpy_ops.np_dtypes import float16
from tensorflow.python.ops.numpy_ops.np_dtypes import float32
from tensorflow.python.ops.numpy_ops.np_dtypes import float64
from tensorflow.python.ops.numpy_ops.np_dtypes import float_
from tensorflow.python.ops.numpy_ops.np_dtypes import iinfo
from tensorflow.python.ops.numpy_ops.np_dtypes import inexact
from tensorflow.python.ops.numpy_ops.np_dtypes import int16
from tensorflow.python.ops.numpy_ops.np_dtypes import int32
from tensorflow.python.ops.numpy_ops.np_dtypes import int64
from tensorflow.python.ops.numpy_ops.np_dtypes import int8
from tensorflow.python.ops.numpy_ops.np_dtypes import int_
from tensorflow.python.ops.numpy_ops.np_dtypes import object_
from tensorflow.python.ops.numpy_ops.np_dtypes import string_
from tensorflow.python.ops.numpy_ops.np_dtypes import uint16
from tensorflow.python.ops.numpy_ops.np_dtypes import uint32
from tensorflow.python.ops.numpy_ops.np_dtypes import uint64
from tensorflow.python.ops.numpy_ops.np_dtypes import uint8
from tensorflow.python.ops.numpy_ops.np_dtypes import unicode_
from tensorflow.python.ops.numpy_ops.np_math_ops import abs
from tensorflow.python.ops.numpy_ops.np_math_ops import absolute
from tensorflow.python.ops.numpy_ops.np_math_ops import add
from tensorflow.python.ops.numpy_ops.np_math_ops import allclose
from tensorflow.python.ops.numpy_ops.np_math_ops import angle
from tensorflow.python.ops.numpy_ops.np_math_ops import append
from tensorflow.python.ops.numpy_ops.np_math_ops import arccos
from tensorflow.python.ops.numpy_ops.np_math_ops import arccosh
from tensorflow.python.ops.numpy_ops.np_math_ops import arcsin
from tensorflow.python.ops.numpy_ops.np_math_ops import arcsinh
from tensorflow.python.ops.numpy_ops.np_math_ops import arctan
from tensorflow.python.ops.numpy_ops.np_math_ops import arctan2
from tensorflow.python.ops.numpy_ops.np_math_ops import arctanh
from tensorflow.python.ops.numpy_ops.np_math_ops import argmax
from tensorflow.python.ops.numpy_ops.np_math_ops import argmin
from tensorflow.python.ops.numpy_ops.np_math_ops import argsort
from tensorflow.python.ops.numpy_ops.np_math_ops import array_equal
from tensorflow.python.ops.numpy_ops.np_math_ops import average
from tensorflow.python.ops.numpy_ops.np_math_ops import bitwise_and
from tensorflow.python.ops.numpy_ops.np_math_ops import bitwise_not
from tensorflow.python.ops.numpy_ops.np_math_ops import bitwise_or
from tensorflow.python.ops.numpy_ops.np_math_ops import bitwise_xor
from tensorflow.python.ops.numpy_ops.np_math_ops import cbrt
from tensorflow.python.ops.numpy_ops.np_math_ops import ceil
from tensorflow.python.ops.numpy_ops.np_math_ops import clip
from tensorflow.python.ops.numpy_ops.np_math_ops import concatenate
from tensorflow.python.ops.numpy_ops.np_math_ops import conj
from tensorflow.python.ops.numpy_ops.np_math_ops import conjugate
from tensorflow.python.ops.numpy_ops.np_math_ops import cos
from tensorflow.python.ops.numpy_ops.np_math_ops import cosh
from tensorflow.python.ops.numpy_ops.np_math_ops import count_nonzero
from tensorflow.python.ops.numpy_ops.np_math_ops import cross
from tensorflow.python.ops.numpy_ops.np_math_ops import deg2rad
from tensorflow.python.ops.numpy_ops.np_math_ops import diff
from tensorflow.python.ops.numpy_ops.np_math_ops import divide
from tensorflow.python.ops.numpy_ops.np_math_ops import divmod
from tensorflow.python.ops.numpy_ops.np_math_ops import dot
from tensorflow.python.ops.numpy_ops.np_math_ops import e
from tensorflow.python.ops.numpy_ops.np_math_ops import einsum
from tensorflow.python.ops.numpy_ops.np_math_ops import equal
from tensorflow.python.ops.numpy_ops.np_math_ops import exp
from tensorflow.python.ops.numpy_ops.np_math_ops import exp2
from tensorflow.python.ops.numpy_ops.np_math_ops import expm1
from tensorflow.python.ops.numpy_ops.np_math_ops import fabs
from tensorflow.python.ops.numpy_ops.np_math_ops import fix
from tensorflow.python.ops.numpy_ops.np_math_ops import float_power
from tensorflow.python.ops.numpy_ops.np_math_ops import floor
from tensorflow.python.ops.numpy_ops.np_math_ops import floor_divide
from tensorflow.python.ops.numpy_ops.np_math_ops import gcd
from tensorflow.python.ops.numpy_ops.np_math_ops import geomspace
from tensorflow.python.ops.numpy_ops.np_math_ops import greater
from tensorflow.python.ops.numpy_ops.np_math_ops import greater_equal
from tensorflow.python.ops.numpy_ops.np_math_ops import heaviside
from tensorflow.python.ops.numpy_ops.np_math_ops import hypot
from tensorflow.python.ops.numpy_ops.np_math_ops import inf
from tensorflow.python.ops.numpy_ops.np_math_ops import inner
from tensorflow.python.ops.numpy_ops.np_math_ops import isclose
from tensorflow.python.ops.numpy_ops.np_math_ops import iscomplex
from tensorflow.python.ops.numpy_ops.np_math_ops import iscomplexobj
from tensorflow.python.ops.numpy_ops.np_math_ops import isfinite
from tensorflow.python.ops.numpy_ops.np_math_ops import isinf
from tensorflow.python.ops.numpy_ops.np_math_ops import isnan
from tensorflow.python.ops.numpy_ops.np_math_ops import isneginf
from tensorflow.python.ops.numpy_ops.np_math_ops import isposinf
from tensorflow.python.ops.numpy_ops.np_math_ops import isreal
from tensorflow.python.ops.numpy_ops.np_math_ops import isrealobj
from tensorflow.python.ops.numpy_ops.np_math_ops import kron
from tensorflow.python.ops.numpy_ops.np_math_ops import lcm
from tensorflow.python.ops.numpy_ops.np_math_ops import less
from tensorflow.python.ops.numpy_ops.np_math_ops import less_equal
from tensorflow.python.ops.numpy_ops.np_math_ops import linspace
from tensorflow.python.ops.numpy_ops.np_math_ops import log
from tensorflow.python.ops.numpy_ops.np_math_ops import log10
from tensorflow.python.ops.numpy_ops.np_math_ops import log1p
from tensorflow.python.ops.numpy_ops.np_math_ops import log2
from tensorflow.python.ops.numpy_ops.np_math_ops import logaddexp
from tensorflow.python.ops.numpy_ops.np_math_ops import logaddexp2
from tensorflow.python.ops.numpy_ops.np_math_ops import logical_and
from tensorflow.python.ops.numpy_ops.np_math_ops import logical_not
from tensorflow.python.ops.numpy_ops.np_math_ops import logical_or
from tensorflow.python.ops.numpy_ops.np_math_ops import logical_xor
from tensorflow.python.ops.numpy_ops.np_math_ops import logspace
from tensorflow.python.ops.numpy_ops.np_math_ops import matmul
from tensorflow.python.ops.numpy_ops.np_math_ops import maximum
from tensorflow.python.ops.numpy_ops.np_math_ops import meshgrid
from tensorflow.python.ops.numpy_ops.np_math_ops import minimum
from tensorflow.python.ops.numpy_ops.np_math_ops import mod
from tensorflow.python.ops.numpy_ops.np_math_ops import multiply
from tensorflow.python.ops.numpy_ops.np_math_ops import nanmean
from tensorflow.python.ops.numpy_ops.np_math_ops import nanprod
from tensorflow.python.ops.numpy_ops.np_math_ops import nansum
from tensorflow.python.ops.numpy_ops.np_math_ops import negative
from tensorflow.python.ops.numpy_ops.np_math_ops import nextafter
from tensorflow.python.ops.numpy_ops.np_math_ops import not_equal
from tensorflow.python.ops.numpy_ops.np_math_ops import outer
from tensorflow.python.ops.numpy_ops.np_math_ops import pi
from tensorflow.python.ops.numpy_ops.np_math_ops import polyval
from tensorflow.python.ops.numpy_ops.np_math_ops import positive
from tensorflow.python.ops.numpy_ops.np_math_ops import power
from tensorflow.python.ops.numpy_ops.np_math_ops import ptp
from tensorflow.python.ops.numpy_ops.np_math_ops import rad2deg
from tensorflow.python.ops.numpy_ops.np_math_ops import reciprocal
from tensorflow.python.ops.numpy_ops.np_math_ops import remainder
from tensorflow.python.ops.numpy_ops.np_math_ops import signbit
from tensorflow.python.ops.numpy_ops.np_math_ops import sin
from tensorflow.python.ops.numpy_ops.np_math_ops import sinc
from tensorflow.python.ops.numpy_ops.np_math_ops import sinh
from tensorflow.python.ops.numpy_ops.np_math_ops import sort
from tensorflow.python.ops.numpy_ops.np_math_ops import sqrt
from tensorflow.python.ops.numpy_ops.np_math_ops import square
from tensorflow.python.ops.numpy_ops.np_math_ops import subtract
from tensorflow.python.ops.numpy_ops.np_math_ops import tan
from tensorflow.python.ops.numpy_ops.np_math_ops import tanh
from tensorflow.python.ops.numpy_ops.np_math_ops import tensordot
from tensorflow.python.ops.numpy_ops.np_math_ops import tile
from tensorflow.python.ops.numpy_ops.np_math_ops import trace
from tensorflow.python.ops.numpy_ops.np_math_ops import true_divide
from tensorflow.python.ops.numpy_ops.np_math_ops import vdot
from tensorflow.python.ops.numpy_ops.np_utils import finfo
from tensorflow.python.ops.numpy_ops.np_utils import promote_types
from tensorflow.python.ops.numpy_ops.np_utils import result_type

del _print_function
