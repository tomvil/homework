import ipaddress

def main():
    quit_messages = ['q', 'quit']
    while True:
        network = str(input("Enter Network: "))
        if not network.lower() in quit_messages:
            try:
                ipaddress.ip_network(network)
            except Exception as error:
                print ("Ooops, Something went wrong: {}".format(error))
                continue
            else:
                break
        else:
            print ("Stopping...")
            quit()

    while True:
        ip = str(input("Enter IP address: "))
        if not ip.lower() in quit_messages:
            try:
                ipaddress.ip_address(ip)
            except Exception as error:
                print ("Ooops, Something went wrong: {}".format(error))
                continue
            else:
                break
        else:
            print ("Stopping...")
            quit()

    if ipaddress.ip_address(ip) in ipaddress.ip_network(network):
        print ("IP Address {} belongs to {} network".format(ip, network))
    else:
        print ("IP Address {} does not belong to {} network".format(ip, network))

if __name__ == '__main__':
    print ("If you want to exit just type 'quit' or 'q' at any time!")
    while True:
        main()
