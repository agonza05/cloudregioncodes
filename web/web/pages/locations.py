"""The table page."""

from ..templates import template
from ..backend.locations_state import LocationsState
from ..views.locations import main_table

import reflex as rx


@template(route="/locations", title="Locations", on_load=LocationsState.load_entries)
def table() -> rx.Component:
    """The locations page.

    Returns:
        The UI for the locations page.
    """
    return rx.vstack(
        rx.heading("Locations", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
