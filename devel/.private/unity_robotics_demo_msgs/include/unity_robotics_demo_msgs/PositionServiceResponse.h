// Generated by gencpp from file unity_robotics_demo_msgs/PositionServiceResponse.msg
// DO NOT EDIT!


#ifndef UNITY_ROBOTICS_DEMO_MSGS_MESSAGE_POSITIONSERVICERESPONSE_H
#define UNITY_ROBOTICS_DEMO_MSGS_MESSAGE_POSITIONSERVICERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <unity_robotics_demo_msgs/PosRot.h>

namespace unity_robotics_demo_msgs
{
template <class ContainerAllocator>
struct PositionServiceResponse_
{
  typedef PositionServiceResponse_<ContainerAllocator> Type;

  PositionServiceResponse_()
    : output()  {
    }
  PositionServiceResponse_(const ContainerAllocator& _alloc)
    : output(_alloc)  {
  (void)_alloc;
    }



   typedef  ::unity_robotics_demo_msgs::PosRot_<ContainerAllocator>  _output_type;
  _output_type output;





  typedef boost::shared_ptr< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> const> ConstPtr;

}; // struct PositionServiceResponse_

typedef ::unity_robotics_demo_msgs::PositionServiceResponse_<std::allocator<void> > PositionServiceResponse;

typedef boost::shared_ptr< ::unity_robotics_demo_msgs::PositionServiceResponse > PositionServiceResponsePtr;
typedef boost::shared_ptr< ::unity_robotics_demo_msgs::PositionServiceResponse const> PositionServiceResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator1> & lhs, const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator2> & rhs)
{
  return lhs.output == rhs.output;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator1> & lhs, const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace unity_robotics_demo_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f40a8c9d0d5d19208415bd9f23e5aa3f";
  }

  static const char* value(const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf40a8c9d0d5d1920ULL;
  static const uint64_t static_value2 = 0x8415bd9f23e5aa3fULL;
};

template<class ContainerAllocator>
struct DataType< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "unity_robotics_demo_msgs/PositionServiceResponse";
  }

  static const char* value(const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "PosRot output\n"
"\n"
"================================================================================\n"
"MSG: unity_robotics_demo_msgs/PosRot\n"
"float32 pos_x\n"
"float32 pos_y\n"
"float32 pos_z\n"
"float32 rot_x\n"
"float32 rot_y\n"
"float32 rot_z\n"
"float32 rot_w\n"
;
  }

  static const char* value(const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.output);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PositionServiceResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::unity_robotics_demo_msgs::PositionServiceResponse_<ContainerAllocator>& v)
  {
    s << indent << "output: ";
    s << std::endl;
    Printer< ::unity_robotics_demo_msgs::PosRot_<ContainerAllocator> >::stream(s, indent + "  ", v.output);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UNITY_ROBOTICS_DEMO_MSGS_MESSAGE_POSITIONSERVICERESPONSE_H
