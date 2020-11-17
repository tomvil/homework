import ipaddress

def main():
    #Quit if these are typed
    quit_messages = ['q', 'quit']
    #Read the network variable from command line and verify if it's legit.
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

    #Read the ip variable from command line and verify if it's legit.
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

    #Finally, check if given ip address is in the given network
    if ipaddress.ip_address(ip) in ipaddress.ip_network(network):
        print ("IP Address {} belongs to {} network".format(ip, network))
    else:
        print ("IP Address {} does not belong to {} network".format(ip, network))

if __name__ == '__main__':
    print ("If you want to exit just type 'quit' or 'q' at any time!\n")
    while True:
        main()
