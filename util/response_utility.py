"""
    common json response structure
"""
from config.http_status_code import HttpStatusCodes
from dto import response_dto


def create_response(message: str, status: str, data=None):
    """
    function for mapping the response
    """
    final_response = response_dto.Response()
    final_response.message = message
    final_response.status = status
    if data is not None:
        final_response.data = data
    return final_response


def create_api_response(
    success: bool, result=None, success_message=None, failure_message=None
):
    if success:
        status_code = HttpStatusCodes.StatusCodes.SUCCESS_OK_200
        status_description = (
            success_message
            if success_message
            else HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200
        )
    else:
        status_code = HttpStatusCodes.StatusCodes.NOT_FOUND_404
        status_description = (
            failure_message
            if failure_message
            else HttpStatusCodes.StatusCodesDescription.NOT_FOUND_404
        )

    return create_response(status_description, status_code, result)
