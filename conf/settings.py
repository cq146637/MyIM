__author__ = 'Cq'

MYSQL_CONN = {
    'HOST': "192.168.47.135",
    'USERNAME': "admin",
    'PASSWORD': "123456",
    'PORT': "3306",
    'DB': "myim"
}

MASTER_SERVER = {
    'PORT': 10002,
    'ADDRESS': '127.0.0.1'
}

LOGIN_SERVER = {
    'PORT': 9999,
    'ADDRESS': "127.0.0.1"
}

FILE_SERVER = {
    'PORT': 9998,
    'ADDRESS': "127.0.0.1"
}

CHAT_SERVER = {
    'PORT': 9997,
    'ADDRESS': "127.0.0.1"
}

HEARTBEAT_SERVER = {
    'PORT': 9996,
    'ADDRESS': "127.0.0.1"
}

CONN_TYPE = {
    'login': 1,
    'logout': 2,
    'register': 3,
    'unregister': 4,
    'heartbeat': 5,
    'create_personal_room_server': 6,
    'destroy_personal_room_server': 7,
    'create_personal_room_client': 8,
    'destroy_personal_room_client': 9,
    'create_peer_to_peer_chat_server': 10,
    'destroy_peer_to_peer_chat_server': 11,
    'download_file': 12,
    'upload_file': 13,
    'edit_personal_information': 14,
    'save_personal_room_message': 15,
    'save_peer_to_peer_chat_message': 16,
}

REPLY_CODE = {
    'success': 1001,
    'failure': 1002,
    'file_not_found': 1003,
    'unknown': 1004,
}