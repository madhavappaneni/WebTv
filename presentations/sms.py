from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_SOCKS5

Connection.set_proxy_info(
    'example.com',
    5000,
    proxy_type=PROXY_TYPE_SOCKS5,
    proxy_user='username',
    proxy_pass='password',
)