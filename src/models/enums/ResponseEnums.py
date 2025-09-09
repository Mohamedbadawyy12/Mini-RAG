from enum import Enum
class ResponseSignal(Enum):



    FILE_VALIDATED_SUCCESS="file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_TYPE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_FAILED= "file _upload_failed"
    FILE_UPLOAD_SUCCESS= "file _upload_success"
