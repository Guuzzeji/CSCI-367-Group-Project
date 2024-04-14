# 404
def not_found(e):
      return {
            "status": 404,
            "error": "page does not exist"
      }

# 503
def server_error(e):
      return {
            "status": 503,
            "error": "server issues :("
      }