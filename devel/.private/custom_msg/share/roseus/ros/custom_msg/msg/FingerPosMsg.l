;; Auto-generated. Do not edit!


(when (boundp 'custom_msg::FingerPosMsg)
  (if (not (find-package "CUSTOM_MSG"))
    (make-package "CUSTOM_MSG"))
  (shadow 'FingerPosMsg (find-package "CUSTOM_MSG")))
(unless (find-package "CUSTOM_MSG::FINGERPOSMSG")
  (make-package "CUSTOM_MSG::FINGERPOSMSG"))

(in-package "ROS")
;;//! \htmlinclude FingerPosMsg.msg.html


(defclass custom_msg::FingerPosMsg
  :super ros::object
  :slots (_pos_1 _pos_2 ))

(defmethod custom_msg::FingerPosMsg
  (:init
   (&key
    ((:pos_1 __pos_1) 0.0)
    ((:pos_2 __pos_2) 0.0)
    )
   (send-super :init)
   (setq _pos_1 (float __pos_1))
   (setq _pos_2 (float __pos_2))
   self)
  (:pos_1
   (&optional __pos_1)
   (if __pos_1 (setq _pos_1 __pos_1)) _pos_1)
  (:pos_2
   (&optional __pos_2)
   (if __pos_2 (setq _pos_2 __pos_2)) _pos_2)
  (:serialization-length
   ()
   (+
    ;; float32 _pos_1
    4
    ;; float32 _pos_2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _pos_1
       (sys::poke _pos_1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pos_2
       (sys::poke _pos_2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _pos_1
     (setq _pos_1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pos_2
     (setq _pos_2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msg::FingerPosMsg :md5sum-) "0ebc591d2739c3a5a1e50adfe2a7e48b")
(setf (get custom_msg::FingerPosMsg :datatype-) "custom_msg/FingerPosMsg")
(setf (get custom_msg::FingerPosMsg :definition-)
      "float32 pos_1
float32 pos_2
")



(provide :custom_msg/FingerPosMsg "0ebc591d2739c3a5a1e50adfe2a7e48b")


