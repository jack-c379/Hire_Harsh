"""
Compatibility patch for Python 3.14 + ChromaDB + Pydantic v1 issue
This must be imported before chromadb is imported

Workaround: Monkeypatch chromadb's Settings class after import
"""
import sys
import os

if sys.version_info >= (3, 14):
    # Set environment variable that chromadb might check
    os.environ.setdefault("CHROMA_SERVER_NOFILE", "65536")
    
    # Patch chromadb config after import
    def patch_chromadb_config():
        try:
            import chromadb.config
            # Add the problematic field with a type annotation
            if hasattr(chromadb.config.Settings, '__annotations__'):
                chromadb.config.Settings.__annotations__['chroma_server_nofile'] = int
        except Exception:
            pass
    
    # We'll call this after chromadb imports, but before it's used
    import atexit
    atexit.register(patch_chromadb_config)

