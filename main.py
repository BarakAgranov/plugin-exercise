import logging.config
import pluggy
from dotenv import load_dotenv
from fastapi import Path, Query, Depends
from fastapi.routing import APIRouter

import dependencies
from dependencies import get_third_party_plugin, get_data_collector
from plugin_manager import PluginSpec
from plugins.data_collection_plugins import fetch_data_collection_plugin, stream_data_collection_plugin, DataCollector
from plugins.third_party_plugins import dummyapi_plugin, ThirdPartyPlugin

load_dotenv()  # Load environment variables
logging.config.fileConfig("logging.ini")  # Set up logging configuration


if __name__ == "__main__":
    tpp = dependencies.get_third_party_plugin()
    dcp = dependencies.get_data_collector("fetch")

