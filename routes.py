from fastapi import APIRouter, Depends, Query, Path
from plugins.third_party_plugins import ThirdPartyPlugin
from plugins.data_collection_plugins import DataCollector
from dependencies import get_third_party_plugin, get_data_collector


router = APIRouter()


@router.get("/{plugin_name}", summary="Get data from the specified plugin", response_description="Data from the specified plugin")
async def get_data(plugin_name: str = Path(..., description="Name of the plugin"),
                   collector_type: str = Query("fetch", description="Type of data collector, either 'fetch' or 'stream'"),
                   third_party_plugin: ThirdPartyPlugin = Depends(get_third_party_plugin),
                   data_collector: DataCollector = Depends(get_data_collector)):
    if not third_party_plugin or not data_collector:
        return {"error": "Invalid plugin or data collector"}

    response = await data_collector.collect_data(third_party_plugin.endpoint, third_party_plugin.headers)
    processed_data = await third_party_plugin.process_response(response)

    return processed_data
git remote set-url origin [https://github.com/BarakAgranov/plugin-exercise.git]
git remote add origin https://github.com/BarakAgranov/plugin-exercise.git
