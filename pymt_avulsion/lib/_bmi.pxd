


cdef extern from "bmi.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_avulsion(BMI_Model *model)


