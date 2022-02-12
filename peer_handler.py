from network import *


def main():
    peer_handler = Peer_Handler()
    log.info("Peer_handler start")
    peer_handler.main_loop()


main()
