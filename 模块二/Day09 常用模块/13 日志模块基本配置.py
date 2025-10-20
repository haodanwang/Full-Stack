import sys

from loguru import logger

logger.configure(
    handlers=[
        # 控制台
        {
            "sink": sys.stderr,
            "format": "<g>{time}</g>|<lvl>{level:10}</lvl>|<c>{module}</c>:{line:4}|<lvl>{message}</lvl>",
            # "colorize": False,
            "level": "INFO",
        },
        # 日志文件
        {"sink": "mylog2.log"},
    ]
)

logger.debug("这是一条测试日志")
logger.info("这是一条正常日志")
logger.success("这是一条成功日志")
logger.warning("这是一条警告日志")
logger.error("这是一条错误日志")
logger.critical("这是一条严重错误日志")
