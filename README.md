# Socket Test

Socket Test is a dead simple socket connection test tool.

## Overview

Its purpose is to test socket connections to a givent host and port.

It was made to help debug kernel limits and sysctl tuning, before running load tests such as wrk, ab, etc.
For example to verify that a target host can accept a certain amount of socket connections.

## Usage

	$ st.py 20000 10.0.1.42:80
	Socket Test attempting 20000 connections
	First connect failure after 16359 connections
	Total successful connections: 16359/20000
	Total failed connections    :  3641/20000

	$ st.py
	usage: st.py connections_number host:port
