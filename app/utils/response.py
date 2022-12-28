status_code = {
    "ok": 200,
    "create": 201,
    "Unauthorized": 401,
    "not_found": 404,
    "internal_server_error": 500,
}


def Ok(data):
    return {"STATUS": status_code["ok"], "MESSAGE": "Successfull", "data": data}


def Create(data):
    return {"status": status_code["create"], "message": "Create", "data": data}


def Unauthorized(data):
    return {
        "status": status_code["Unauthorized"],
        "message": "Unauthorized",
        "data": data,
    }


def Not_Found(data):
    return {"status": 404, "message": "Not Found", "error": data}


def Internal_server_error(data):
    print(data)
    return {"status": 500, "message": "Internal Server Error", "data": data}
