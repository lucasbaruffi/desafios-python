def make_readable(seconds):
    return(f"{str(seconds // 3600).zfill(2)}:{str((seconds % 3600) // 60).zfill(2)}:{str(seconds % 60).zfill(2)}")