""" Socket Test: Simple socket connection test tool """

import socket
import sys

def run(connections, target_host, target_port):
	""" Run the test """

	socks = []
	connection_failed = False
	successful_connections = 0
	print 'Socket Test attempting %d connections' % connections

	# Open as many connections as possible up to `connections` sockets
	for i in range(0, connections):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socks.append(sock)
		try:
			sock.connect((target_host, target_port))
			successful_connections += 1
		except Exception as e:
			# Print stats on first failure (so we get estimated results early before the test finishes)
			if not connection_failed:
				print 'First connect failure after %d connections' % (i)
				connection_failed = True

	# Close the sockets
	for sock in socks:
		try:
			sock.close()
		except Exception:
			pass

	# Print summary
	width = len(str(connections))
	failed_connections = connections - successful_connections
	print 'Total successful connections: %s/%d' % (str(successful_connections).rjust(width), connections)
	print 'Total failed connections    : %s/%d' % (str(failed_connections).rjust(width), connections)

def exit_with_usage():
	""" Print usage and exit the program """

	print 'usage: st.py connections_number host:port'
	sys.exit(1)

if __name__ == '__main__':
	try:
		connections = int(sys.argv[1])
		target = sys.argv[2].split(':')

		if len(target) < 2:
			exit_with_usage()

		target_host = target[0]
		target_port = int(target[1])
	except Exception as e:
		print str(e)
		exit_with_usage()

	run(connections, target_host, target_port)
