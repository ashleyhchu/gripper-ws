// Generated by gencpp from file test_rospy/TransitiveMsg1.msg
// DO NOT EDIT!


#ifndef TEST_ROSPY_MESSAGE_TRANSITIVEMSG1_H
#define TEST_ROSPY_MESSAGE_TRANSITIVEMSG1_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <test_rospy/TransitiveMsg2.h>

namespace test_rospy
{
template <class ContainerAllocator>
struct TransitiveMsg1_
{
  typedef TransitiveMsg1_<ContainerAllocator> Type;

  TransitiveMsg1_()
    : msg2()  {
    }
  TransitiveMsg1_(const ContainerAllocator& _alloc)
    : msg2(_alloc)  {
  (void)_alloc;
    }



   typedef  ::test_rospy::TransitiveMsg2_<ContainerAllocator>  _msg2_type;
  _msg2_type msg2;





  typedef boost::shared_ptr< ::test_rospy::TransitiveMsg1_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_rospy::TransitiveMsg1_<ContainerAllocator> const> ConstPtr;

}; // struct TransitiveMsg1_

typedef ::test_rospy::TransitiveMsg1_<std::allocator<void> > TransitiveMsg1;

typedef boost::shared_ptr< ::test_rospy::TransitiveMsg1 > TransitiveMsg1Ptr;
typedef boost::shared_ptr< ::test_rospy::TransitiveMsg1 const> TransitiveMsg1ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_rospy::TransitiveMsg1_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::test_rospy::TransitiveMsg1_<ContainerAllocator1> & lhs, const ::test_rospy::TransitiveMsg1_<ContainerAllocator2> & rhs)
{
  return lhs.msg2 == rhs.msg2;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::test_rospy::TransitiveMsg1_<ContainerAllocator1> & lhs, const ::test_rospy::TransitiveMsg1_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace test_rospy

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_rospy::TransitiveMsg1_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rospy::TransitiveMsg1_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rospy::TransitiveMsg1_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
{
  static const char* value()
  {
    return "72751523a989ee2c7a44c006464315e9";
  }

  static const char* value(const ::test_rospy::TransitiveMsg1_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x72751523a989ee2cULL;
  static const uint64_t static_value2 = 0x7a44c006464315e9ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_rospy/TransitiveMsg1";
  }

  static const char* value(const ::test_rospy::TransitiveMsg1_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
{
  static const char* value()
  {
    return "TransitiveMsg2 msg2\n"
"\n"
"\n"
"================================================================================\n"
"MSG: test_rospy/TransitiveMsg2\n"
"test_rosmaster/Composite data\n"
"\n"
"================================================================================\n"
"MSG: test_rosmaster/Composite\n"
"# composite message. required for testing import calculation in generators\n"
"CompositeA a\n"
"CompositeB b\n"
"\n"
"================================================================================\n"
"MSG: test_rosmaster/CompositeA\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: test_rosmaster/CompositeB\n"
"# copy of geometry_msgs/Point for testing\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::test_rospy::TransitiveMsg1_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.msg2);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TransitiveMsg1_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_rospy::TransitiveMsg1_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_rospy::TransitiveMsg1_<ContainerAllocator>& v)
  {
    s << indent << "msg2: ";
    s << std::endl;
    Printer< ::test_rospy::TransitiveMsg2_<ContainerAllocator> >::stream(s, indent + "  ", v.msg2);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSPY_MESSAGE_TRANSITIVEMSG1_H