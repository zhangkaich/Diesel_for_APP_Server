# coding: utf8

import json
import diesel
import struct
import time
from diesel.protocols.redis import RedisClient
from diesel import fork, quickstop, quickstart, sleep
from config import Configuration
import commands.data_table as data_table


config=Configuration()
server_config = config.get_configuration()
print config.get_configuration()

def change_reconsider_to_meeting(client, reconsider, id, current):
    client.select(data_table.MEETING_TABLE)
    #add meeting to MEETING_TABLE
    key = "meeting" + str(id)
    client.hset(key, 'title', reconsider['title'])
    client.hset(key, 'state', reconsider['state'])
    client.hset(key, 'content', reconsider['content'])
    client.hset(key, 'type', 1)
    client.hset(key, 'time',current)
    client.lpush("list", id)

    #remove reconsider
    client.select(data_table.RECONSIDER_TABLE)
    proposal_key = "reconsider" + str(id)
    client.delete(proposal_key)
    client.lrem("list", id, 1)


def check_reconsider_to_meeting():
    client = RedisClient(host=server_config['redis']['host'], port=server_config['redis']['port'])
    client.select(data_table.RECONSIDER_TABLE)
    while True:
        result = client.sort(key="list", pattern="reconsider*->time",
                            get=None, order='ASC', alpha=False, store=None)
        current = time.time()
        for i in result:
            key = "reconsider" + i
            value = client.hgetall(key)
            print "reconsider start time : %r" % value['time']
            print "reconsider end time : %r" % (float(value['time']) + server_config['check_server']['reconsider_to_meeting']*3600)
            print "current %r" % current
            if (float(value['time']) + 
                server_config['check_server']['reconsider_to_meeting']*3600 <= current):
                #TODO maybe need to check agree count
                print "reconsider_to_meeting %r" % i 
                change_reconsider_to_meeting(client, value, i, current)
        
        sleep(server_config['check_server']['sleep_time'])
        #sleep(60)

def main():
    fork(check_reconsider_to_meeting)

quickstart(main)
