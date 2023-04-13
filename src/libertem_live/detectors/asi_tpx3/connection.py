import os
from typing import Optional
import tempfile

from libertem.common.math import prod

from libertem_live.detectors.base.connection import (
    PendingAcquisition, DetectorConnection,
)

from libertem_asi_tpx3 import ASITpx3Connection


class AsiPendingAcquisition(PendingAcquisition):
    def __init__(self, acquisition_header):
        self._acquisition_header = acquisition_header

    @property
    def header(self):
        return self._acquisition_header

    @property
    def nimages(self) -> int:
        nav_shape = self._acquisition_header.get_nav_shape()
        return prod(nav_shape)

    def __repr__(self):
        return f"<AsiPendingAcquisition header={self._acquisition_header}>"


class AsiDetectorConnection(DetectorConnection):
    def __init__(
        self,
        uri: str,
        num_slots: int,
        bytes_per_chunk: int,
        chunks_per_stack: int = 24,
        huge_pages: bool = False,
    ):
        self._passive_started = False
        self._uri = uri

        self._num_slots = num_slots
        self._bytes_per_chunk = bytes_per_chunk
        self._huge_pages = huge_pages
        self._chunks_per_stack = chunks_per_stack

        self._conn = self._connect()

    def _connect(self):
        handle_path = self._make_handle_path()
        return ASITpx3Connection(
            uri=self._uri,
            chunks_per_stack=self._chunks_per_stack,
            num_slots=self._num_slots,
            bytes_per_chunk=self._bytes_per_chunk,
            huge=self._huge_pages,
            handle_path=handle_path,
        )

    def wait_for_acquisition(
        self, timeout: float,
    ) -> Optional[AsiPendingAcquisition]:
        if not self._passive_started:
            self._conn.start_passive()
            self._passive_started = True
        header = self._conn.wait_for_arm(timeout)
        if header is None:
            return None
        return AsiPendingAcquisition(
            acquisition_header=header,
        )

    def get_conn_impl(self):
        return self._conn

    @classmethod
    def _make_handle_path(cls):
        temp_path = tempfile.mkdtemp()
        return os.path.join(temp_path, 'asi-shm-socket')

    def stop_series(self):
        pass  # TODO: what to do?

    def close(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def reconnect(self):
        if self._conn is not None:
            self.close()
        self._conn = self._connect()

    def log_stats(self):
        self._conn.log_shm_stats()
