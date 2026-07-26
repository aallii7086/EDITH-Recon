import socket

def main():
    print("=" * 50)
    print("      NETWORK RECON TOOLKIT v1.3")
    print("=" * 50)

    target = input("Enter Target: ")
    
    if len(target) == 0:
      print ("[-]Error: Target cannot be empty.")
    else:
       
      print ("[+] Target Accepted:", target)
      
      ip = socket.gethostbyname(target)

      print ("[+] IP Address:", ip)


if __name__ == "__main__":
    main()
