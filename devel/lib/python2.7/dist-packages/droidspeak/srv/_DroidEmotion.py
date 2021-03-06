# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from droidspeak/DroidEmotionRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class DroidEmotionRequest(genpy.Message):
  _md5sum = "3121217addb14943825726ec606b461f"
  _type = "droidspeak/DroidEmotionRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 NORMAL=0
uint8 HAPPY=1
uint8 SORRY=2
uint8 ANGRY=3
uint8 JADED=4
uint8 LOOK_LEFT=5
uint8 LOOK_RIGHT=6
uint8 LOOK_UP=7
uint8 LOOK_DOWN=8
uint8 BLINK=9

uint8 emotion
duration duration
"""
  # Pseudo-constants
  NORMAL = 0
  HAPPY = 1
  SORRY = 2
  ANGRY = 3
  JADED = 4
  LOOK_LEFT = 5
  LOOK_RIGHT = 6
  LOOK_UP = 7
  LOOK_DOWN = 8
  BLINK = 9

  __slots__ = ['emotion','duration']
  _slot_types = ['uint8','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       emotion,duration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DroidEmotionRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.emotion is None:
        self.emotion = 0
      if self.duration is None:
        self.duration = genpy.Duration()
    else:
      self.emotion = 0
      self.duration = genpy.Duration()

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
      buff.write(_get_struct_B2i().pack(_x.emotion, _x.duration.secs, _x.duration.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.duration is None:
        self.duration = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.emotion, _x.duration.secs, _x.duration.nsecs,) = _get_struct_B2i().unpack(str[start:end])
      self.duration.canon()
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
      buff.write(_get_struct_B2i().pack(_x.emotion, _x.duration.secs, _x.duration.nsecs))
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
      if self.duration is None:
        self.duration = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.emotion, _x.duration.secs, _x.duration.nsecs,) = _get_struct_B2i().unpack(str[start:end])
      self.duration.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B2i = None
def _get_struct_B2i():
    global _struct_B2i
    if _struct_B2i is None:
        _struct_B2i = struct.Struct("<B2i")
    return _struct_B2i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from droidspeak/DroidEmotionResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class DroidEmotionResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "droidspeak/DroidEmotionResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DroidEmotionResponse, self).__init__(*args, **kwds)

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
      pass
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
      pass
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
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class DroidEmotion(object):
  _type          = 'droidspeak/DroidEmotion'
  _md5sum = '3121217addb14943825726ec606b461f'
  _request_class  = DroidEmotionRequest
  _response_class = DroidEmotionResponse
