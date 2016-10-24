"""
Open and close time calculation tester
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""

import arrow
import acp_times as acp

def same(real, expected):
	print(real, expected)
	return real == expected

#200
def test_open_lt_200():
	assert same(acp.open_time(130, 200, '2017-01-01T00:00'), arrow.get('2017-01-01T03:49').isoformat())

def test_close_lt_200():
	assert same(acp.close_time(130, 200, '2017-01-01T00:00'), arrow.get('2017-01-01T08:40').isoformat())

def test_open_long_200():
	print('"should" be {}'.format(arrow.get('2017-01-01T05:53').isoformat()))
	assert same(acp.open_time(210, 200, '2017-01-01T00:00'), arrow.get('2017-01-01T05:53').isoformat())

def test_close_long_200():
	print('"should" be {}'.format(arrow.get('2017-01-01T13:20').isoformat()))
	assert same(acp.close_time(210, 200, '2017-01-01T00:00'), arrow.get('2017-01-01T13:30').isoformat())

#300
def test_open_lt_300():
	assert same(acp.open_time(230, 300, '2017-01-01T00:00'), arrow.get('2017-01-01T06:49').isoformat())

def test_close_lt_300():
	assert same(acp.close_time(230, 300, '2017-01-01T00:00'), arrow.get('2017-01-01T15:20').isoformat())

def test_open_long_300():
	print('"should" be {}'.format(arrow.get('2017-01-01T09:00').isoformat()))
	assert same(acp.open_time(310, 300, '2017-01-01T00:00'), arrow.get('2017-01-01T09:00').isoformat())

def test_close_long_300():
	print('"should" be {}'.format(arrow.get('2017-01-01T13:20').isoformat()))
	assert same(acp.close_time(310, 300, '2017-01-01T00:00'), arrow.get('2017-01-01T20:00').isoformat())

#400
def test_open_lt_400():
	assert same(acp.open_time(330, 400, '2017-01-01T00:00'), arrow.get('2017-01-01T09:57').isoformat())

def test_close_lt_400():
	assert same(acp.close_time(330, 400, '2017-01-01T00:00'), arrow.get('2017-01-01T22:00').isoformat())

def test_open_long_400():
	print('"should" be {}'.format(arrow.get('2017-01-01T12:08').isoformat()))
	assert same(acp.open_time(410, 400, '2017-01-01T00:00'), arrow.get('2017-01-01T12:08').isoformat())

def test_close_long_400():
	print('"should" be {}'.format(arrow.get('2017-01-02T02:40').isoformat()))
	assert same(acp.close_time(410, 400, '2017-01-01T00:00'), arrow.get('2017-01-02T03:00').isoformat())

#600
def test_open_lt_600():
	assert same(acp.open_time(530, 600, '2017-01-01T00:00'), arrow.get('2017-01-01T16:28').isoformat())

def test_close_lt_600():
	assert same(acp.close_time(530, 600, '2017-01-01T00:00'), arrow.get('2017-01-02T11:20').isoformat())

def test_open_long_600():
	print('"should" be {}'.format(arrow.get('2017-01-01T18:48').isoformat()))
	assert same(acp.open_time(610, 600, '2017-01-01T00:00'), arrow.get('2017-01-01T18:48').isoformat())

def test_close_long_600():
	print('"should" be {}'.format(arrow.get('2017-01-01T16:00').isoformat()))
	assert same(acp.close_time(610, 600, '2017-01-01T00:00'), arrow.get('2017-01-02T16:00').isoformat())

#1000
def test_open_lt_1000():
	assert same(acp.open_time(930, 1000, '2017-01-01T00:00'), arrow.get('2017-01-02T06:35').isoformat())

def test_close_lt_1000():
	assert same(acp.close_time(930, 1000, '2017-01-01T00:00'), arrow.get('2017-01-03T20:53').isoformat())

def test_open_long_1000():
	print('"should" be {}'.format(arrow.get('2017-01-02T09:05').isoformat()))
	assert same(acp.open_time(1010, 1000, '2017-01-01T00:00'), arrow.get('2017-01-02T09:05').isoformat())

def test_close_long_1000():
	print('"should" be {}'.format(arrow.get('2017-01-04T03:00').isoformat()))
	assert same(acp.close_time(1010, 1000, '2017-01-01T00:00'), arrow.get('2017-01-04T03:00').isoformat())