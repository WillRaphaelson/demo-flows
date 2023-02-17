from prefect import flow
import os

@flow()
def oh_snap():
    os.unlink()