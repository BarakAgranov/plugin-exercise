import pluggy
from fastapi import FastAPI
import routes, exception_handlers
from plugin_manager import PluginSpec as plugin_spec
from plugins.third_party_plugins import dummyapi_plugin
from plugins.data_collection_plugins import stream_data_collection_plugin, fetch_data_collection_plugin

app = FastAPI()

plugin_manager = pluggy.PluginManager("my_system")
plugin_manager.add_hookspecs(plugin_spec)


plugin_manager.register(dummyapi_plugin)
plugin_manager.register(fetch_data_collection_plugin)
plugin_manager.register(stream_data_collection_plugin)

app.include_router(routes.router)
