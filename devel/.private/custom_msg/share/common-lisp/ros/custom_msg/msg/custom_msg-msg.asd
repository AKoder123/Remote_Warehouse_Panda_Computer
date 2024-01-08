
(cl:in-package :asdf)

(defsystem "custom_msg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FingerPosMsg" :depends-on ("_package_FingerPosMsg"))
    (:file "_package_FingerPosMsg" :depends-on ("_package"))
  ))