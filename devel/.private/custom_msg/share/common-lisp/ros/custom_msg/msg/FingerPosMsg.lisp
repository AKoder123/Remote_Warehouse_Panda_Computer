; Auto-generated. Do not edit!


(cl:in-package custom_msg-msg)


;//! \htmlinclude FingerPosMsg.msg.html

(cl:defclass <FingerPosMsg> (roslisp-msg-protocol:ros-message)
  ((pos_1
    :reader pos_1
    :initarg :pos_1
    :type cl:float
    :initform 0.0)
   (pos_2
    :reader pos_2
    :initarg :pos_2
    :type cl:float
    :initform 0.0))
)

(cl:defclass FingerPosMsg (<FingerPosMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FingerPosMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FingerPosMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg-msg:<FingerPosMsg> is deprecated: use custom_msg-msg:FingerPosMsg instead.")))

(cl:ensure-generic-function 'pos_1-val :lambda-list '(m))
(cl:defmethod pos_1-val ((m <FingerPosMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg-msg:pos_1-val is deprecated.  Use custom_msg-msg:pos_1 instead.")
  (pos_1 m))

(cl:ensure-generic-function 'pos_2-val :lambda-list '(m))
(cl:defmethod pos_2-val ((m <FingerPosMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg-msg:pos_2-val is deprecated.  Use custom_msg-msg:pos_2 instead.")
  (pos_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FingerPosMsg>) ostream)
  "Serializes a message object of type '<FingerPosMsg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos_1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pos_2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FingerPosMsg>) istream)
  "Deserializes a message object of type '<FingerPosMsg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_2) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FingerPosMsg>)))
  "Returns string type for a message object of type '<FingerPosMsg>"
  "custom_msg/FingerPosMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FingerPosMsg)))
  "Returns string type for a message object of type 'FingerPosMsg"
  "custom_msg/FingerPosMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FingerPosMsg>)))
  "Returns md5sum for a message object of type '<FingerPosMsg>"
  "0ebc591d2739c3a5a1e50adfe2a7e48b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FingerPosMsg)))
  "Returns md5sum for a message object of type 'FingerPosMsg"
  "0ebc591d2739c3a5a1e50adfe2a7e48b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FingerPosMsg>)))
  "Returns full string definition for message of type '<FingerPosMsg>"
  (cl:format cl:nil "float32 pos_1~%float32 pos_2~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FingerPosMsg)))
  "Returns full string definition for message of type 'FingerPosMsg"
  (cl:format cl:nil "float32 pos_1~%float32 pos_2~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FingerPosMsg>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FingerPosMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'FingerPosMsg
    (cl:cons ':pos_1 (pos_1 msg))
    (cl:cons ':pos_2 (pos_2 msg))
))
