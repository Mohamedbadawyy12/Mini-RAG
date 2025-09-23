from enum import Enum
class ResponseSignal(Enum):



    FILE_VALIDATED_SUCCESS="file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_TYPE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_FAILED= "file _upload_failed"
    FILE_UPLOAD_SUCCESS= "file _upload_success"
    PROCESSING_SUCCESS="processing_success"
    PROCESSING_FAILED="processing_failed"
    NO_FILES_ERROR="not_found_files"
    FILE_ID_ERORR="no_file_found_with_whis_id"
    PROJECT_NOT_FOUND_ERROR="project_not_found"
    INSERT_INTO_VECTORDB_ERROR="insert_into_vectordb_erorr"
    INSERT_INTO_VECTORDB_SUCCESS="insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED="vectordb_collection_retieved"
    VECTORDB_SEARCH_ERROR="vectordb_search_erorr"
    VECTORDB_SEARCH_SUCCESS="vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"
    