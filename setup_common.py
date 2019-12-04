try:
    # Python 2.x
    from configparser import SafeConfigParser
except ImportError:
    # Python 3.x
    from configparser import ConfigParser as SafeConfigParser

def get_metadata_and_options():
    config = SafeConfigParser()
    config.read(['metadata.cfg', 'site.cfg'])

    metadata = dict(config.items('metadata'))
    options = dict(config.items('options'))

    metadata['py_modules'] = list([_f for _f in metadata['py_modules'].split('\n') if _f])
    metadata['classifiers'] = list([_f for _f in metadata['classifiers'].split('\n') if _f])

    return metadata, options

def enabled(options, option):
    value = options[option]
    s = value.lower()
    if s in ('yes','true','1','y'):
        return True
    elif s in ('no', 'false', '0', 'n'):
        return False
    else:
        raise ValueError("Unknown value %s for option %s" % (value, option))

def create_release_file(metadata):
    rel = open("MySQLdb/release.py",'w')
    rel.write("""
__author__ = "%(author)s <%(author_email)s>"
version_info = %(version_info)s
__version__ = "%(version)s"
""" % metadata)
    rel.close()
