import six
import types
from itertools import islice

from scrapy.utils.misc import walk_modules
from scrapy.utils.spider import iter_spider_classes


def get_spider_class(spider_name, project_settings):
    spider_modules = project_settings.get('SPIDER_MODULES')
    for spider_module in spider_modules:
        modules = walk_modules(spider_module)
        for module in islice(modules, 1, None):
            for spider_class in iter_spider_classes(module):
                if spider_class.name == spider_name:
                    return spider_class
    return None


def python_version():
    return 2 if six.PY2 else 3


def ensure_generator(arg):
	if isinstance(arg, types.GeneratorType):
		return arg
	iterator = iter(arg or ())
	return (x for x in (arg) or ())
	 
	

