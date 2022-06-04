# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from test_roslib_comm/SameSubMsg3.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SameSubMsg3(genpy.Message):
  _md5sum = "49145a54e4be1a218629e518575a0bf3"
  _type = "test_roslib_comm/SameSubMsg3"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
# Lots of comments
int32 a  #And more comments
float32 b
string c
# And also some white space


uint64[10] d
 float64[] e

"""
  __slots__ = ['a','b','c','d','e']
  _slot_types = ['int32','float32','string','uint64[10]','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       a,b,c,d,e

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SameSubMsg3, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.a is None:
        self.a = 0
      if self.b is None:
        self.b = 0.
      if self.c is None:
        self.c = ''
      if self.d is None:
        self.d = [0] * 10
      if self.e is None:
        self.e = []
    else:
      self.a = 0
      self.b = 0.
      self.c = ''
      self.d = [0] * 10
      self.e = []

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
      buff.write(_get_struct_if().pack(_x.a, _x.b))
      _x = self.c
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(_get_struct_10Q().pack(*self.d))
      length = len(self.e)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.e))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.a, _x.b,) = _get_struct_if().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.c = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.c = str[start:end]
      start = end
      end += 80
      self.d = _get_struct_10Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.e = s.unpack(str[start:end])
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
      buff.write(_get_struct_if().pack(_x.a, _x.b))
      _x = self.c
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      buff.write(self.d.tostring())
      length = len(self.e)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.e.tostring())
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
      end = 0
      _x = self
      start = end
      end += 8
      (_x.a, _x.b,) = _get_struct_if().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.c = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.c = str[start:end]
      start = end
      end += 80
      self.d = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=10)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.e = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10Q = None
def _get_struct_10Q():
    global _struct_10Q
    if _struct_10Q is None:
        _struct_10Q = struct.Struct("<10Q")
    return _struct_10Q
_struct_if = None
def _get_struct_if():
    global _struct_if
    if _struct_if is None:
        _struct_if = struct.Struct("<if")
    return _struct_if
