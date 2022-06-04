// Generated by gencpp from file test_roslib_comm/SameSubMsg3.msg
// DO NOT EDIT!


#ifndef TEST_ROSLIB_COMM_MESSAGE_SAMESUBMSG3_H
#define TEST_ROSLIB_COMM_MESSAGE_SAMESUBMSG3_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test_roslib_comm
{
template <class ContainerAllocator>
struct SameSubMsg3_
{
  typedef SameSubMsg3_<ContainerAllocator> Type;

  SameSubMsg3_()
    : a(0)
    , b(0.0)
    , c()
    , d()
    , e()  {
      d.assign(0);
  }
  SameSubMsg3_(const ContainerAllocator& _alloc)
    : a(0)
    , b(0.0)
    , c(_alloc)
    , d()
    , e(_alloc)  {
  (void)_alloc;
      d.assign(0);
  }



   typedef int32_t _a_type;
  _a_type a;

   typedef float _b_type;
  _b_type b;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _c_type;
  _c_type c;

   typedef boost::array<uint64_t, 10>  _d_type;
  _d_type d;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _e_type;
  _e_type e;





  typedef boost::shared_ptr< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> const> ConstPtr;

}; // struct SameSubMsg3_

typedef ::test_roslib_comm::SameSubMsg3_<std::allocator<void> > SameSubMsg3;

typedef boost::shared_ptr< ::test_roslib_comm::SameSubMsg3 > SameSubMsg3Ptr;
typedef boost::shared_ptr< ::test_roslib_comm::SameSubMsg3 const> SameSubMsg3ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator1> & lhs, const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator2> & rhs)
{
  return lhs.a == rhs.a &&
    lhs.b == rhs.b &&
    lhs.c == rhs.c &&
    lhs.d == rhs.d &&
    lhs.e == rhs.e;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator1> & lhs, const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace test_roslib_comm

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "49145a54e4be1a218629e518575a0bf3";
  }

  static const char* value(const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x49145a54e4be1a21ULL;
  static const uint64_t static_value2 = 0x8629e518575a0bf3ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_roslib_comm/SameSubMsg3";
  }

  static const char* value(const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"# Lots of comments\n"
"int32 a  #And more comments\n"
"float32 b\n"
"string c\n"
"# And also some white space\n"
"\n"
"\n"
"uint64[10] d\n"
" float64[] e\n"
"\n"
;
  }

  static const char* value(const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
      stream.next(m.c);
      stream.next(m.d);
      stream.next(m.e);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SameSubMsg3_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_roslib_comm::SameSubMsg3_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_roslib_comm::SameSubMsg3_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<int32_t>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<float>::stream(s, indent + "  ", v.b);
    s << indent << "c: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.c);
    s << indent << "d[]" << std::endl;
    for (size_t i = 0; i < v.d.size(); ++i)
    {
      s << indent << "  d[" << i << "]: ";
      Printer<uint64_t>::stream(s, indent + "  ", v.d[i]);
    }
    s << indent << "e[]" << std::endl;
    for (size_t i = 0; i < v.e.size(); ++i)
    {
      s << indent << "  e[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.e[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSLIB_COMM_MESSAGE_SAMESUBMSG3_H