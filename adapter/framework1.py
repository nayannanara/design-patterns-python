from core.router import router1


def post_http():
    http_message = {
        'method': 'post',
        'header': {
            'token': 'Bearer asdasdsadadasda',
            'origin': 'http://example.com'
        },
        'body': {
            'name': 'nay',
            'message': 'hey, nay'
        }
    }

    router1(http_message)