
# import chromelogger
# import logging
# import re

# _sql_fields_re = re.compile(r'SELECT .*? FROM')

# def truncate_sql(sql):
#     return _sql_fields_re.sub('SELECT ... FROM', sql)

# class ChromeLoggerLogHandler(logging.Handler):
#     """Blah
#     """

#     def __init__(self, include_html=False):
#         logging.Handler.__init__(self)
#         self.createLock()
#         # anything else?

#     def emit(self, record):
#         try:
#             self.acquire()
#             self.format(record)
#             try:
#                 fn = getattr(chromelogger, record.levelname.lower())
#             except:
#                 fn = chromelogger.info
#             msg = "%s: %s" % (record.name, truncate_sql(record.message))
#             fn(msg)
#         finally:
#             self.release()
