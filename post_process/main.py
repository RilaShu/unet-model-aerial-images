from binary import opencv_binary
from smooth import opencv_smooth


if __name__ == "__main__":
    opencv_binary('origin', 'binary')
    opencv_smooth('binary', 'result')