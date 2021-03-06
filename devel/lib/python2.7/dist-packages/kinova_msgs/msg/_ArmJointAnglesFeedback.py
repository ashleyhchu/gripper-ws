# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kinova_msgs/ArmJointAnglesFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import kinova_msgs.msg

class ArmJointAnglesFeedback(genpy.Message):
  _md5sum = "cadc8c9df1338a45563e10d707e71551"
  _type = "kinova_msgs/ArmJointAnglesFeedback"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback
JointAngles angles


================================================================================
MSG: kinova_msgs/JointAngles
float32 joint1
float32 joint2
float32 joint3
float32 joint4
float32 joint5
float32 joint6
float32 joint7
"""
  __slots__ = ['angles']
  _slot_types = ['kinova_msgs/JointAngles']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       angles

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArmJointAnglesFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.angles is None:
        self.angles = kinova_msgs.msg.JointAngles()
    else:
      self.angles = kinova_msgs.msg.JointAngles()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.angles.joint1, _x.angles.joint2, _x.angles.joint3, _x.angles.joint4, _x.angles.joint5, _x.angles.joint6, _x.angles.joint7))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.angles is None:
        self.angles = kinova_msgs.msg.JointAngles()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.angles.joint1, _x.angles.joint2, _x.angles.joint3, _x.angles.joint4, _x.angles.joint5, _x.angles.joint6, _x.angles.joint7,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.angles.joint1, _x.angles.joint2, _x.angles.joint3, _x.angles.joint4, _x.angles.joint5, _x.angles.joint6, _x.angles.joint7))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.angles is None:
        self.angles = kinova_msgs.msg.JointAngles()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.angles.joint1, _x.angles.joint2, _x.angles.joint3, _x.angles.joint4, _x.angles.joint5, _x.angles.joint6, _x.angles.joint7,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
