import pkg_resources
#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


def includeme(config):
    # Expose capability.
    config.add_api_capability("woleet",
                              version=__version__,
                              description="Handle anchors callback URLs",
                              url="https://github.com/Kinto/kinto-woleet/")

    config.scan('kinto_woleet.views')
