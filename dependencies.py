import plugin_manager


async def get_third_party_plugin(plugin_name: str):
    return plugin_manager.hook.get_third_party_plugin(plugin_name=plugin_name)


async def get_data_collector(collector_type: str):
    return plugin_manager.hook.get_data_collector(collector_type=collector_type)
