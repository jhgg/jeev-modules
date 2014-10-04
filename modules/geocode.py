from jeev.message import Attachment
from jeev.utils.importing import import_dotted_path
import module

module.opt(
    'using',
    'The geopy geocoder (or similar interface) to use.',
    default='geopy.geocoders.Nominatim')


@module.opt_validator('using')
def validate_is_geocoder(name):
    try:
        module = import_dotted_path(name)
    except ImportError:
        raise module.ConfigError("Could not import module %s" % name)

    if not hasattr(module, 'geocode'):
        raise module.ConfigError("Module %s does not have a method 'geocode'" % name)

    return module


@module.respond('geocode (.*)$')
@module.async()
def geocode(message, location):
    g = module.opts['using'].geocode(location)
    if g:
        a = Attachment(g.address)
        a.field("Latitude", g.latitude, True)
        a.field("Longitude", g.longitude, True)
        message.reply_with_attachment(a)
    else:
        message.reply_to_user("Couldn't geocode that...")