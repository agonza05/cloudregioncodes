"""The table page."""

from ..templates import template
from ..backend.table_state import TableState
from ..views.table import main_table

import reflex as rx


@template(route="/cloudProviders", title="Cloud Providers", on_load=TableState.load_entries)
def table() -> rx.Component:
    """The cloud providers page.

    Returns:
        The UI for the cloud providers page.
    """
    return rx.vstack(
        rx.heading("Cloud Providers", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
