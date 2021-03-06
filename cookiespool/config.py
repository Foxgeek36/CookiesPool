'''
[配置模块]
'''

# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'foobared'

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类 ->如扩展其他站点,在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类 ->如扩展其他站点,在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000

# 产生器开关,模拟登录添加Cookies
GENERATOR_PROCESS = False
# 验证器开关,循环检测数据库中Cookies是否可用,不可用则删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = True
