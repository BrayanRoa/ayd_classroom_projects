status_code = {
    "ok": 200,
    "create": 201,
    "Unauthorized": 401,
    "not_found": 404,
    "internal_server_error": 500,
}


def Ok(data):
    return {"Status": status_code["ok"], "Message": "Successfull", "data": data}


def Create(data):
    return {"Status": status_code["create"], "Message": "Create", "data": data}


def Unauthorized(data):
    return {
        "Status": status_code["Unauthorized"],
        "Message": "Unauthorized",
        "Msg": data,
    }


def Not_Found(data):
    return {"Status": 404, "Message": "Not Found", "Msg": data}


def Internal_server_error(data):
    print(data)
    return {"status": 500, "message": "Internal Server Error", "msg": data}
