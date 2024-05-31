"""
    Entry-point script for the whole program

    To run from command line:

    $ python -m elpy_cli
"""
from elpy_cli import __app_name__, __version__, spotipy_example

def run_cli():
    """
    """
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
    print("============================\n")
    print(f"{__app_name__} v{__version__}")
    print("\n============================\n")
    print("𓆏 ⊹☾⋆⁺₊🎧✩°｡ 𓆏 ⊹☾⋆⁺₊🎧✩°｡ 𓆏\n")

    spotipy_example.spotipy_example_call()

    print("\n============================\n")
    print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")