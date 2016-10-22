"""
Open and close time calculation tester
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""

import arrow
import acp_times as acp

def test_open_lt_200():
	assert acp.open_time(130, 200, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T03:49').isoFormat()

def test_close_lt_200():
	assert acp.close_time(130, 200, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T08:40').isoFormat()

def test_open_long_200():
	assert acp.open_time(210, 200, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T05:53').isoFormat()

def test_close_long_200():
	assert acp.close_time(210, 200, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T13:30').isoFormat()



def test_open_lt_400():
	assert acp.open_time(330, 400, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T09:57').isoFormat()

def test_close_lt_400():
	assert acp.close_time(330, 400, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T22:00').isoFormat()


def test_open_lt_600():
	assert acp.open_time(530, 600, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-01T16:28').isoFormat()

def test_close_lt_600():
	assert acp.close_time(530, 600, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-02T11:20').isoFormat()



def test_open_lt_1000():
	assert acp.open_time(930, 1000, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-02T06:35').isoFormat()

def test_close_lt_1000():
	assert acp.close_time(930, 100, arrow.get('2016-01-01T00:00')) == arrow.get('2016-01-03T20:53').isoFormat()
