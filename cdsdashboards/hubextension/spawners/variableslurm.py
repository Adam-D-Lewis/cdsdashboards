from batchspawner import SlurmSpawner
from .variablemixin import VariableMixin, MetaVariableMixin, Command


class VariableSlurmSpawner(SlurmSpawner, VariableMixin, metaclass=MetaVariableMixin):
    default_presentation_cmd = Command(
        ['jhsingle_native_proxy'],
        allow_none=False,
        help="""
        The command to run presentations through jhsingle_native_proxy, can be a string or list.
        Default is ['jhsingle_native_proxy'].
        """
    ).tag(config=True)

