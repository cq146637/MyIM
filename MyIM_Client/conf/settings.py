__author__ = 'Cq'

LOGIN_SERVER = {
    'PORT': 10002,
    'ADDRESS': "127.0.0.1"
}

PEER_SERVER = {
    'PORT': [10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013],
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

HEARTBEAT_INTERVAL = 3


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