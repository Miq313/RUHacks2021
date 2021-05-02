"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections

from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export

from typing import TypeVar

def batch_fft(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchFFT", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_fft_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchFFT", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchFFT = tf_export("raw_ops.BatchFFT")(_ops.to_raw_op(batch_fft))


def batch_fft_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchFFT", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_fft2d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchFFT2D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_fft2d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchFFT2D", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchFFT2D = tf_export("raw_ops.BatchFFT2D")(_ops.to_raw_op(batch_fft2d))


def batch_fft2d_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchFFT2D", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_fft3d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchFFT3D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_fft3d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchFFT3D", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchFFT3D = tf_export("raw_ops.BatchFFT3D")(_ops.to_raw_op(batch_fft3d))


def batch_fft3d_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchFFT3D", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_ifft(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchIFFT", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_ifft_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchIFFT", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchIFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchIFFT = tf_export("raw_ops.BatchIFFT")(_ops.to_raw_op(batch_ifft))


def batch_ifft_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchIFFT", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchIFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_ifft2d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchIFFT2D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_ifft2d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchIFFT2D", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchIFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchIFFT2D = tf_export("raw_ops.BatchIFFT2D")(_ops.to_raw_op(batch_ifft2d))


def batch_ifft2d_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchIFFT2D", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchIFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_ifft3d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "BatchIFFT3D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return batch_ifft3d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchIFFT3D", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchIFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchIFFT3D = tf_export("raw_ops.BatchIFFT3D")(_ops.to_raw_op(batch_ifft3d))


def batch_ifft3d_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"BatchIFFT3D", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchIFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.fft', v1=['signal.fft', 'spectral.fft', 'fft'])
@deprecated_endpoints('spectral.fft', 'fft')
def fft(input, name=None):
  r"""Fast Fourier transform.

  Computes the 1-dimensional discrete Fourier transform over the inner-most
  dimension of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "FFT", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return fft_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            fft, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "FFT", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          fft, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "FFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

FFT = tf_export("raw_ops.FFT")(_ops.to_raw_op(fft))


def fft_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"FFT", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "FFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.fft2d', v1=['signal.fft2d', 'spectral.fft2d', 'fft2d'])
@deprecated_endpoints('spectral.fft2d', 'fft2d')
def fft2d(input, name=None):
  r"""2D fast Fourier transform.

  Computes the 2-dimensional discrete Fourier transform over the inner-most
  2 dimensions of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "FFT2D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return fft2d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            fft2d, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "FFT2D", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          fft2d, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "FFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

FFT2D = tf_export("raw_ops.FFT2D")(_ops.to_raw_op(fft2d))


def fft2d_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"FFT2D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "FFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.fft3d', v1=['signal.fft3d', 'spectral.fft3d', 'fft3d'])
@deprecated_endpoints('spectral.fft3d', 'fft3d')
def fft3d(input, name=None):
  r"""3D fast Fourier transform.

  Computes the 3-dimensional discrete Fourier transform over the inner-most 3
  dimensions of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "FFT3D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return fft3d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            fft3d, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "FFT3D", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          fft3d, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "FFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

FFT3D = tf_export("raw_ops.FFT3D")(_ops.to_raw_op(fft3d))


def fft3d_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"FFT3D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "FFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.ifft', v1=['signal.ifft', 'spectral.ifft', 'ifft'])
@deprecated_endpoints('spectral.ifft', 'ifft')
def ifft(input, name=None):
  r"""Inverse fast Fourier transform.

  Computes the inverse 1-dimensional discrete Fourier transform over the
  inner-most dimension of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IFFT", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return ifft_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            ifft, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IFFT", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          ifft, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IFFT = tf_export("raw_ops.IFFT")(_ops.to_raw_op(ifft))


def ifft_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.ifft2d', v1=['signal.ifft2d', 'spectral.ifft2d', 'ifft2d'])
@deprecated_endpoints('spectral.ifft2d', 'ifft2d')
def ifft2d(input, name=None):
  r"""Inverse 2D fast Fourier transform.

  Computes the inverse 2-dimensional discrete Fourier transform over the
  inner-most 2 dimensions of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IFFT2D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return ifft2d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            ifft2d, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IFFT2D", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          ifft2d, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IFFT2D = tf_export("raw_ops.IFFT2D")(_ops.to_raw_op(ifft2d))


def ifft2d_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IFFT2D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('signal.ifft3d', v1=['signal.ifft3d', 'spectral.ifft3d', 'ifft3d'])
@deprecated_endpoints('spectral.ifft3d', 'ifft3d')
def ifft3d(input, name=None):
  r"""Inverse 3D fast Fourier transform.

  Computes the inverse 3-dimensional discrete Fourier transform over the
  inner-most 3 dimensions of `input`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IFFT3D", name, input)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return ifft3d_eager_fallback(
          input, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      result = _dispatch.dispatch(
            ifft3d, (), dict(input=input, name=name)
          )
      if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return result
      raise
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IFFT3D", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          ifft3d, (), dict(input=input, name=name)
        )
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Tcomplex", _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IFFT3D = tf_export("raw_ops.IFFT3D")(_ops.to_raw_op(ifft3d))


def ifft3d_eager_fallback(input, name, ctx):
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  _inputs_flat = [input]
  _attrs = ("Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IFFT3D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def irfft(input, fft_length, Treal=_dtypes.float32, name=None):
  r"""Inverse real-valued fast Fourier transform.

  Computes the inverse 1-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most dimension of `input`.

  The inner-most dimension of `input` is assumed to be the result of `RFFT`: the
  `fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If
  `fft_length` is not provided, it is computed from the size of the inner-most
  dimension of `input` (`fft_length = 2 * (inner - 1)`). If the FFT length used to
  compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along the axis `IRFFT` is computed on, if `fft_length / 2 + 1` is smaller
  than the corresponding dimension of `input`, the dimension is cropped. If it is
  larger, the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [1]. The FFT length.
    Treal: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Treal`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IRFFT", name, input, fft_length, "Treal", Treal)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return irfft_eager_fallback(
          input, fft_length, Treal=Treal, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IRFFT", input=input, fft_length=fft_length, Treal=Treal, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IRFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IRFFT = tf_export("raw_ops.IRFFT")(_ops.to_raw_op(irfft))


def irfft_eager_fallback(input, fft_length, Treal, name, ctx):
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", Treal, "Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IRFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IRFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def irfft2d(input, fft_length, Treal=_dtypes.float32, name=None):
  r"""Inverse 2D real-valued fast Fourier transform.

  Computes the inverse 2-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most 2 dimensions of `input`.

  The inner-most 2 dimensions of `input` are assumed to be the result of `RFFT2D`:
  The inner-most dimension contains the `fft_length / 2 + 1` unique components of
  the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
  from the size of the inner-most 2 dimensions of `input`. If the FFT length used
  to compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along each axis `IRFFT2D` is computed on, if `fft_length` (or
  `fft_length / 2 + 1` for the inner-most dimension) is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [2]. The FFT length for each dimension.
    Treal: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Treal`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IRFFT2D", name, input, fft_length, "Treal", Treal)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return irfft2d_eager_fallback(
          input, fft_length, Treal=Treal, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IRFFT2D", input=input, fft_length=fft_length, Treal=Treal, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IRFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IRFFT2D = tf_export("raw_ops.IRFFT2D")(_ops.to_raw_op(irfft2d))


def irfft2d_eager_fallback(input, fft_length, Treal, name, ctx):
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", Treal, "Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IRFFT2D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IRFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def irfft3d(input, fft_length, Treal=_dtypes.float32, name=None):
  r"""Inverse 3D real-valued fast Fourier transform.

  Computes the inverse 3-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most 3 dimensions of `input`.

  The inner-most 3 dimensions of `input` are assumed to be the result of `RFFT3D`:
  The inner-most dimension contains the `fft_length / 2 + 1` unique components of
  the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
  from the size of the inner-most 3 dimensions of `input`. If the FFT length used
  to compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along each axis `IRFFT3D` is computed on, if `fft_length` (or
  `fft_length / 2 + 1` for the inner-most dimension) is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      A complex tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [3]. The FFT length for each dimension.
    Treal: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Treal`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "IRFFT3D", name, input, fft_length, "Treal", Treal)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return irfft3d_eager_fallback(
          input, fft_length, Treal=Treal, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "IRFFT3D", input=input, fft_length=fft_length, Treal=Treal, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "IRFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

IRFFT3D = tf_export("raw_ops.IRFFT3D")(_ops.to_raw_op(irfft3d))


def irfft3d_eager_fallback(input, fft_length, Treal, name, ctx):
  if Treal is None:
    Treal = _dtypes.float32
  Treal = _execute.make_type(Treal, "Treal")
  _attr_Tcomplex, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.complex64, _dtypes.complex128, ], _dtypes.complex64)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", Treal, "Tcomplex", _attr_Tcomplex)
  _result = _execute.execute(b"IRFFT3D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "IRFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def rfft(input, fft_length, Tcomplex=_dtypes.complex64, name=None):
  r"""Real-valued fast Fourier transform.

  Computes the 1-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most dimension of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT` only returns the
  `fft_length / 2 + 1` unique components of the FFT: the zero-frequency term,
  followed by the `fft_length / 2` positive-frequency terms.

  Along the axis `RFFT` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [1]. The FFT length.
    Tcomplex: An optional `tf.DType` from: `tf.complex64, tf.complex128`. Defaults to `tf.complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tcomplex`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "RFFT", name, input, fft_length, "Tcomplex", Tcomplex)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return rfft_eager_fallback(
          input, fft_length, Tcomplex=Tcomplex, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RFFT", input=input, fft_length=fft_length, Tcomplex=Tcomplex,
                name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RFFT = tf_export("raw_ops.RFFT")(_ops.to_raw_op(rfft))


def rfft_eager_fallback(input, fft_length, Tcomplex, name, ctx):
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _attr_Treal, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.float32, _dtypes.float64, ], _dtypes.float32)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", _attr_Treal, "Tcomplex", Tcomplex)
  _result = _execute.execute(b"RFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "RFFT", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def rfft2d(input, fft_length, Tcomplex=_dtypes.complex64, name=None):
  r"""2D real-valued fast Fourier transform.

  Computes the 2-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most 2 dimensions of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT2D` only returns the
  `fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
  of `output`: the zero-frequency term, followed by the `fft_length / 2`
  positive-frequency terms.

  Along each axis `RFFT2D` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [2]. The FFT length for each dimension.
    Tcomplex: An optional `tf.DType` from: `tf.complex64, tf.complex128`. Defaults to `tf.complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tcomplex`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "RFFT2D", name, input, fft_length, "Tcomplex", Tcomplex)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return rfft2d_eager_fallback(
          input, fft_length, Tcomplex=Tcomplex, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RFFT2D", input=input, fft_length=fft_length, Tcomplex=Tcomplex,
                  name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RFFT2D = tf_export("raw_ops.RFFT2D")(_ops.to_raw_op(rfft2d))


def rfft2d_eager_fallback(input, fft_length, Tcomplex, name, ctx):
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _attr_Treal, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.float32, _dtypes.float64, ], _dtypes.float32)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", _attr_Treal, "Tcomplex", Tcomplex)
  _result = _execute.execute(b"RFFT2D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "RFFT2D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def rfft3d(input, fft_length, Tcomplex=_dtypes.complex64, name=None):
  r"""3D real-valued fast Fourier transform.

  Computes the 3-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most 3 dimensions of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT3D` only returns the
  `fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
  of `output`: the zero-frequency term, followed by the `fft_length / 2`
  positive-frequency terms.

  Along each axis `RFFT3D` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [3]. The FFT length for each dimension.
    Tcomplex: An optional `tf.DType` from: `tf.complex64, tf.complex128`. Defaults to `tf.complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tcomplex`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "RFFT3D", name, input, fft_length, "Tcomplex", Tcomplex)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      return rfft3d_eager_fallback(
          input, fft_length, Tcomplex=Tcomplex, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
  # Add nodes to the TensorFlow graph.
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RFFT3D", input=input, fft_length=fft_length, Tcomplex=Tcomplex,
                  name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("Treal", _op._get_attr_type("Treal"), "Tcomplex",
              _op._get_attr_type("Tcomplex"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RFFT3D = tf_export("raw_ops.RFFT3D")(_ops.to_raw_op(rfft3d))


def rfft3d_eager_fallback(input, fft_length, Tcomplex, name, ctx):
  if Tcomplex is None:
    Tcomplex = _dtypes.complex64
  Tcomplex = _execute.make_type(Tcomplex, "Tcomplex")
  _attr_Treal, (input,) = _execute.args_to_matching_eager([input], ctx, [_dtypes.float32, _dtypes.float64, ], _dtypes.float32)
  fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
  _inputs_flat = [input, fft_length]
  _attrs = ("Treal", _attr_Treal, "Tcomplex", Tcomplex)
  _result = _execute.execute(b"RFFT3D", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "RFFT3D", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

