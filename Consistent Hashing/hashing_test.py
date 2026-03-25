from consistent_hashing import ConsistentHashing
import matplotlib.pyplot as plt

x = ConsistentHashing(['A', 'B', 'C', 'D', 'E', 'F'])

positions = [h / (2**128) for h in x.ring]

plt.scatter(positions, [1]*len(positions))
plt.yticks([])
plt.title("Consistent Hash Ring Distribution")
plt.show()

def ring_segments(ring):
    segments = []
    n = len(ring)

    for i in range(n):
        cur = ring[i]
        nxt = ring[(i+1) % n]

        if nxt < cur:
            nxt += 2**128

        segments.append(nxt - cur)

    return segments

l = ring_segments(x.ring)
print(l)
print(max(l))
print(min(l))
print(sum(l)/len(l))

print(x.ring[:20])
for h in x.ring[:20]:
    print(h, x.hash_to_server[h])

