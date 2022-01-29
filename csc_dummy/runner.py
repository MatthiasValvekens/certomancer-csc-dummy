from aiohttp import web
from certomancer import registry

from .csc_dummy_server import CSCWithCertomancer, DummyServiceParams


def run_from_file(cfg_path, port, require_hash_pinning=True):
    cfg = registry.CertomancerConfig.from_file(cfg_path)
    csc_app = CSCWithCertomancer(
        cfg, service_params=DummyServiceParams(
            hash_pinning_required=require_hash_pinning
        )
    )
    csc_app.register_routes()
    web.run_app(
        csc_app.app, host='localhost', port=port,
    )
