from p2pool.yrmix import networks

PARENT = networks.nets['yrmix']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '7242ef345e1bed6b'.decode('hex')
PREFIX = '3b3e1286f446b891'.decode('hex')
COINBASEEXT = '0D2F5032506F6F6C2D444153482F'.decode('hex')
P2P_PORT = 8998
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7902
BOOTSTRAP_ADDRS = 'yrmix01.p2poolmining.us p2pool.2sar.ru yrmix02.p2poolmining.us p2pool.yrmix.siampm.com yrmix03.p2poolmining.us crypto.office-on-the.net yrmix04.p2poolmining.us'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-yrmix'
VERSION_CHECK = lambda v: v >= 120100
