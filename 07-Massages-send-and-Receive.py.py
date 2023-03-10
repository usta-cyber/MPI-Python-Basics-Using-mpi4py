from mpi4py import MPI

# Get the rank of the process
rank = MPI.COMM_WORLD.rank

# Send a message to the other process
if rank == 0:
    message = "Hello from process 0"
    MPI.COMM_WORLD.isend(message, dest=1)
elif rank == 1:
    # Receive the message from the other process
    message = MPI.COMM_WORLD.irecv(source=0)
    print(f"Received message: {message}")

    # Send a reply to the other process
    reply = "Hello from process 1"
    MPI.COMM_WORLD.send(reply, dest=0)