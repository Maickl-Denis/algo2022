from collections import deque, namedtuple


def net_packets():
    size, n = (int(_) for _ in input().split())
    if n == 0:
        return
    Packet = namedtuple('Packet', ['arrival', 'duration'])
    packets = []
    for i in range(n):
        packets.append(Packet(*(int(_) for _ in input().split())))
    inf = 10 ** 7
    current_processing_ending = inf
    queue = deque()
    for packet in packets:
        while packet.arrival >= current_processing_ending:
            queue.popleft()
            if queue:
                current_processing_ending += queue[0].duration
            else:
                current_processing_ending = inf
        if len(queue) < size:
            if queue:
                print(packet_processing_start)
                packet_processing_start += packet.duration
            else:
                current_processing_ending = packet.arrival + packet.duration
                packet_processing_start = current_processing_ending
                print(packet.arrival)
            queue.append(packet)
        else:
            print(-1)
