from onnx_tf.handlers.frontend_handler import FrontendHandler
from onnx_tf.handlers.handler import onnx_op
from onnx_tf.handlers.handler import tf_op
from .math_mixin import ReductionMixin


@onnx_op("ReduceMean")
@tf_op("Mean")
class ReduceMean(ReductionMixin, FrontendHandler):

  @classmethod
  def version_1(cls, node, **kwargs):
    return cls.reduction_op(node, **kwargs)
