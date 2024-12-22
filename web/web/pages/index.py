"""The overview page of the app."""

from ..config import settings
import reflex as rx
from .. import styles
from ..templates import template
from ..views.charts import (
    StatsState,
)
from ..components.card import card


@template(route="/", title="Overview", on_load=StatsState.randomize_data)
def index() -> rx.Component:
    """The overview page.

    Returns:
        The UI for the overview page.
    """
    return rx.vstack(
        rx.heading(f"Welcome to {settings.app_name}!", size="5"),
        rx.flex(
            rx.input(
                rx.input.slot(rx.icon("search"), padding_left="0"),
                placeholder="Search here...",
                size="3",
                width="100%",
                max_width="450px",
                radius="large",
                style=styles.ghost_input_style,
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        spacing="8",
        width="100%",
    )
