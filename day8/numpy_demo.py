import numpy as np

list_a = [10, 20, 30]
list_b = [1, 2, 3]

print("list addition:", list_a + list_b)

arr_a = np.array(list_a)
arr_b = np.array(list_b)

print("array addition:", arr_a + arr_b)

tickets = np.array(
    [
        [120, 1, 30],
        [80, 0, 180],
        [250, 3, 1440],
        [60, 0, 10],
    ],
    dtype=float,
)

print("\nTicket info:")
print(tickets)

print("Shape:", tickets.shape)
print("im:", tickets.ndim)
print("type:", tickets.dtype)

print("\n First ticket info:", tickets[0])
print("fist time ", tickets[0][2])

waiting_times = tickets[:, 2]
print("Waiting times:", waiting_times)

waiting_hours = waiting_times / 60
print("Waiting hours:", waiting_hours)

print("\n Ticket C:", tickets[2])

print("description words", tickets[:, 0])

description_words = tickets[:, 0]
ave_words = np.mean(description_words)
print("Average words:", ave_words)

file_attachments = tickets[:, 1]
mask = file_attachments > 0
at_least_one_attachment = tickets[mask]
print("Tickets with at least one attachment:", at_least_one_attachment)
print("shape", at_least_one_attachment.shape)