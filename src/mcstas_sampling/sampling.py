from juliacall import Main as jl
import pathlib

julia_path = pathlib.Path(__file__).parent
jl.include(str(julia_path / "sampling_toNexus.jl"))

if __name__ == "__main__":
    print("Yay the packaging worked")

