from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

'''
获取代理IP，访问接口（http://localhost:5555/random）即可，
'''
def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
