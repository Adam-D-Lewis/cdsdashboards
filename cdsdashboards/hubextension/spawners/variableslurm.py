from batchspawner import SlurmSpawner
from .variablemixin import VariableMixin, MetaVariableMixin, Command


class VariableSlurmSpawner(SlurmSpawner, VariableMixin, metaclass=MetaVariableMixin):
    default_presentation_cmd = Command(
        ['jhsingle-native-proxy'],
        allow_none=False,
        help="""
        The command to run presentations through jhsingle-native-proxy, can be a string or list.
        Default is ['jhsingle-native-proxy'].
        """
    ).tag(config=True)

