import logging


logger=logging.getLogger('test')
logger.setLevel(logging.INFO)

console_stream=logging.StreamHandler()
format_console=logging.Formatter("%(asctime)s -- %(message)s  -- %(level)s")

console_stream.setFormatter(format_console)

logger.addHandler(console_stream)



logger.info("helo")