// Auto-generated. Do not edit!

// (in-package custom_msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class FingerPosMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pos_1 = null;
      this.pos_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('pos_1')) {
        this.pos_1 = initObj.pos_1
      }
      else {
        this.pos_1 = 0.0;
      }
      if (initObj.hasOwnProperty('pos_2')) {
        this.pos_2 = initObj.pos_2
      }
      else {
        this.pos_2 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FingerPosMsg
    // Serialize message field [pos_1]
    bufferOffset = _serializer.float32(obj.pos_1, buffer, bufferOffset);
    // Serialize message field [pos_2]
    bufferOffset = _serializer.float32(obj.pos_2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FingerPosMsg
    let len;
    let data = new FingerPosMsg(null);
    // Deserialize message field [pos_1]
    data.pos_1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pos_2]
    data.pos_2 = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg/FingerPosMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0ebc591d2739c3a5a1e50adfe2a7e48b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 pos_1
    float32 pos_2
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FingerPosMsg(null);
    if (msg.pos_1 !== undefined) {
      resolved.pos_1 = msg.pos_1;
    }
    else {
      resolved.pos_1 = 0.0
    }

    if (msg.pos_2 !== undefined) {
      resolved.pos_2 = msg.pos_2;
    }
    else {
      resolved.pos_2 = 0.0
    }

    return resolved;
    }
};

module.exports = FingerPosMsg;
