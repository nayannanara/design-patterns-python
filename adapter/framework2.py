from core.router import router1


def post_http():
    http_message = {
        'HTTP_method': 'post',
        'HTTP_header': {
            'token': 'Bearer asdasdsadadasda',
            'origin': 'http://example.com'
        },
        'HTTP_body': {
            'name': 'nay',
            'message': 'hey, nay'
        }
    }

    router1(http_message)