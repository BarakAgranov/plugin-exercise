import pluggy

hookspec = pluggy.HookspecMarker("plgn4l")
hookimpl = pluggy.HookimplMarker("plgn4l")


class PluginSpec:
    @hookspec
    def get_third_party_plugin(self, plugin_name: str) -> object:
        pass

    @hookspec
    def get_data_collector(self, collector_type: str) -> object:
        pass
