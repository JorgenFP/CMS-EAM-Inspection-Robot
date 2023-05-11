# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_robot_interfaces:srv/SetLed.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetLed_Request(type):
    """Metaclass of message 'SetLed_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.SetLed_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_led__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_led__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_led__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_led__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_led__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetLed_Request(metaclass=Metaclass_SetLed_Request):
    """Message class 'SetLed_Request'."""

    __slots__ = [
        '_led1_status',
        '_led2_status',
        '_led3_status',
    ]

    _fields_and_field_types = {
        'led1_status': 'boolean',
        'led2_status': 'boolean',
        'led3_status': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.led1_status = kwargs.get('led1_status', bool())
        self.led2_status = kwargs.get('led2_status', bool())
        self.led3_status = kwargs.get('led3_status', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.led1_status != other.led1_status:
            return False
        if self.led2_status != other.led2_status:
            return False
        if self.led3_status != other.led3_status:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def led1_status(self):
        """Message field 'led1_status'."""
        return self._led1_status

    @led1_status.setter
    def led1_status(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led1_status' field must be of type 'bool'"
        self._led1_status = value

    @builtins.property
    def led2_status(self):
        """Message field 'led2_status'."""
        return self._led2_status

    @led2_status.setter
    def led2_status(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led2_status' field must be of type 'bool'"
        self._led2_status = value

    @builtins.property
    def led3_status(self):
        """Message field 'led3_status'."""
        return self._led3_status

    @led3_status.setter
    def led3_status(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led3_status' field must be of type 'bool'"
        self._led3_status = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetLed_Response(type):
    """Metaclass of message 'SetLed_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.SetLed_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_led__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_led__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_led__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_led__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_led__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetLed_Response(metaclass=Metaclass_SetLed_Response):
    """Message class 'SetLed_Response'."""

    __slots__ = [
        '_led1_status_success',
        '_led1_status_message',
        '_led2_status_success',
        '_led2_status_message',
        '_led3_status_success',
        '_led3_status_message',
    ]

    _fields_and_field_types = {
        'led1_status_success': 'boolean',
        'led1_status_message': 'string',
        'led2_status_success': 'boolean',
        'led2_status_message': 'string',
        'led3_status_success': 'boolean',
        'led3_status_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.led1_status_success = kwargs.get('led1_status_success', bool())
        self.led1_status_message = kwargs.get('led1_status_message', str())
        self.led2_status_success = kwargs.get('led2_status_success', bool())
        self.led2_status_message = kwargs.get('led2_status_message', str())
        self.led3_status_success = kwargs.get('led3_status_success', bool())
        self.led3_status_message = kwargs.get('led3_status_message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.led1_status_success != other.led1_status_success:
            return False
        if self.led1_status_message != other.led1_status_message:
            return False
        if self.led2_status_success != other.led2_status_success:
            return False
        if self.led2_status_message != other.led2_status_message:
            return False
        if self.led3_status_success != other.led3_status_success:
            return False
        if self.led3_status_message != other.led3_status_message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def led1_status_success(self):
        """Message field 'led1_status_success'."""
        return self._led1_status_success

    @led1_status_success.setter
    def led1_status_success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led1_status_success' field must be of type 'bool'"
        self._led1_status_success = value

    @builtins.property
    def led1_status_message(self):
        """Message field 'led1_status_message'."""
        return self._led1_status_message

    @led1_status_message.setter
    def led1_status_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'led1_status_message' field must be of type 'str'"
        self._led1_status_message = value

    @builtins.property
    def led2_status_success(self):
        """Message field 'led2_status_success'."""
        return self._led2_status_success

    @led2_status_success.setter
    def led2_status_success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led2_status_success' field must be of type 'bool'"
        self._led2_status_success = value

    @builtins.property
    def led2_status_message(self):
        """Message field 'led2_status_message'."""
        return self._led2_status_message

    @led2_status_message.setter
    def led2_status_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'led2_status_message' field must be of type 'str'"
        self._led2_status_message = value

    @builtins.property
    def led3_status_success(self):
        """Message field 'led3_status_success'."""
        return self._led3_status_success

    @led3_status_success.setter
    def led3_status_success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led3_status_success' field must be of type 'bool'"
        self._led3_status_success = value

    @builtins.property
    def led3_status_message(self):
        """Message field 'led3_status_message'."""
        return self._led3_status_message

    @led3_status_message.setter
    def led3_status_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'led3_status_message' field must be of type 'str'"
        self._led3_status_message = value


class Metaclass_SetLed(type):
    """Metaclass of service 'SetLed'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.srv.SetLed')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_led

            from my_robot_interfaces.srv import _set_led
            if _set_led.Metaclass_SetLed_Request._TYPE_SUPPORT is None:
                _set_led.Metaclass_SetLed_Request.__import_type_support__()
            if _set_led.Metaclass_SetLed_Response._TYPE_SUPPORT is None:
                _set_led.Metaclass_SetLed_Response.__import_type_support__()


class SetLed(metaclass=Metaclass_SetLed):
    from my_robot_interfaces.srv._set_led import SetLed_Request as Request
    from my_robot_interfaces.srv._set_led import SetLed_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
