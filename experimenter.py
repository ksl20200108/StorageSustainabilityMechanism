from network import *


def main():
    experimenter = Experimenter()
    log.info("Experimenter start")
    t = threading.Thread(target=experimenter.start_service, args=())
    t.start()
    t.join()


main()
