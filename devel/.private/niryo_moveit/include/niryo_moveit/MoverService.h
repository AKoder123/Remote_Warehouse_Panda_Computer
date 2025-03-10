// Generated by gencpp from file niryo_moveit/MoverService.msg
// DO NOT EDIT!


#ifndef NIRYO_MOVEIT_MESSAGE_MOVERSERVICE_H
#define NIRYO_MOVEIT_MESSAGE_MOVERSERVICE_H

#include <ros/service_traits.h>


#include <niryo_moveit/MoverServiceRequest.h>
#include <niryo_moveit/MoverServiceResponse.h>


namespace niryo_moveit
{

struct MoverService
{

typedef MoverServiceRequest Request;
typedef MoverServiceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoverService
} // namespace niryo_moveit


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::niryo_moveit::MoverService > {
  static const char* value()
  {
    return "bd9b8037f9cd4f90705bed544fc4c913";
  }

  static const char* value(const ::niryo_moveit::MoverService&) { return value(); }
};

template<>
struct DataType< ::niryo_moveit::MoverService > {
  static const char* value()
  {
    return "niryo_moveit/MoverService";
  }

  static const char* value(const ::niryo_moveit::MoverService&) { return value(); }
};


// service_traits::MD5Sum< ::niryo_moveit::MoverServiceRequest> should match
// service_traits::MD5Sum< ::niryo_moveit::MoverService >
template<>
struct MD5Sum< ::niryo_moveit::MoverServiceRequest>
{
  static const char* value()
  {
    return MD5Sum< ::niryo_moveit::MoverService >::value();
  }
  static const char* value(const ::niryo_moveit::MoverServiceRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::niryo_moveit::MoverServiceRequest> should match
// service_traits::DataType< ::niryo_moveit::MoverService >
template<>
struct DataType< ::niryo_moveit::MoverServiceRequest>
{
  static const char* value()
  {
    return DataType< ::niryo_moveit::MoverService >::value();
  }
  static const char* value(const ::niryo_moveit::MoverServiceRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::niryo_moveit::MoverServiceResponse> should match
// service_traits::MD5Sum< ::niryo_moveit::MoverService >
template<>
struct MD5Sum< ::niryo_moveit::MoverServiceResponse>
{
  static const char* value()
  {
    return MD5Sum< ::niryo_moveit::MoverService >::value();
  }
  static const char* value(const ::niryo_moveit::MoverServiceResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::niryo_moveit::MoverServiceResponse> should match
// service_traits::DataType< ::niryo_moveit::MoverService >
template<>
struct DataType< ::niryo_moveit::MoverServiceResponse>
{
  static const char* value()
  {
    return DataType< ::niryo_moveit::MoverService >::value();
  }
  static const char* value(const ::niryo_moveit::MoverServiceResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // NIRYO_MOVEIT_MESSAGE_MOVERSERVICE_H
