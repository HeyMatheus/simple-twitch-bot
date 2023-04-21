import socket
import time

CHANNEL = "SOME CHANNEL NAME"  # Channel name
NICK = "TheuzinXYZ"  # Twitch User
OAUTH = "*********"  # https://twitchapps.com/tmi

print(f"-> Conectando ao chat da twitch ({CHANNEL}).")
sock = socket.socket()
time.sleep(1)
try:
    print("-> Connected :D")
    sock.connect(("irc.chat.twitch.tv", 6667))
    sock.send(bytes("PASS " + OAUTH + "\r\n", "UTF-8"))
    sock.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
    sock.send(bytes("JOIN #" + CHANNEL + "\r\n", "UTF-8"))
    while True:
        message = sock.recv(2048).decode("UTF-8")
        if "PING :tmi.twitch.tv" in message:
            sock.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
        name = message.split("!", 1)[0][1:]
        message = message.split("PRIVMSG", 1)[-1].split(":", 1)[-1][:-1]
        print(f"{name}: {message}")
except KeyboardInterrupt:
    pass
except:
    print("-> Went Wrong D:")
