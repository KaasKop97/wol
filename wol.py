import socket
import struct


class Wol:
    BROADCAST_IP = "255.255.255.255"
    DEFAULT_PORT = 9

    def create_magic_packet(self, macaddress):
        """
        :param macaddress: string
        :return: macaddress

        A 'magic packet' starts with 6 bytes of 255 (FF FF FF FF FF FF) and
        then the mac address 16 times.
        Magic packet is magical, since it can wake up computers on the network!
        Only used by the 'Wake On Lan(WOL)' protocol.
        """

        if len(macaddress) is 17:
            macaddress = macaddress.replace(":", "")
        else:
            raise ValueError("Not a valid mac address!")

        data = b'FFFFFFFFFFFF' + (macaddress * 16).encode()
        send_data = b''

        for i in range(0, len(data), 2):
            send_data += struct.pack(b'B', int(data[i: i + 2], 16))
        return send_data

    def send_magic_packet(self, macaddress):
        """
        :param macaddress:
        :return: None

        Sends the magic packet to the PC with the association MAC address
        """

        packet = ""

        try:
            packet = self.create_magic_packet(macaddress)
        except ValueError:
            return False

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.connect((self.BROADCAST_IP, self.DEFAULT_PORT))
        try:
            sock.send(packet)
            return True
        except:
            print("Error")
        sock.close()
