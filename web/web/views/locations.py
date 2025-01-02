import reflex as rx
from ..backend.locations_state import LocationsState, Location


def _header_cell(text: str, icon: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def _show_item(item: Location, index: int) -> rx.Component:
    bg_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 1),
        rx.color("accent", 2),
    )
    hover_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 3),
        rx.color("accent", 3),
    )
    return rx.table.row(
        rx.table.cell(item.country),
        rx.table.row_header_cell(item.name),
        rx.table.cell(item.id),
        rx.table.cell(item.countryCode),
        style={"_hover": {"bg": hover_color}, "bg": bg_color},
        align="center",
    )


def _pagination_view() -> rx.Component:
    return (
        rx.hstack(
            rx.text(
                "Page ",
                rx.code(LocationsState.page_number),
                f" of {LocationsState.total_pages}",
                justify="end",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=LocationsState.first_page,
                    opacity=rx.cond(LocationsState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(LocationsState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=LocationsState.prev_page,
                    opacity=rx.cond(LocationsState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(LocationsState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=LocationsState.next_page,
                    opacity=rx.cond(
                        LocationsState.page_number == LocationsState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        LocationsState.page_number == LocationsState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=LocationsState.last_page,
                    opacity=rx.cond(
                        LocationsState.page_number == LocationsState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        LocationsState.page_number == LocationsState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                align="center",
                spacing="2",
                justify="end",
            ),
            spacing="5",
            margin_top="1em",
            align="center",
            width="100%",
            justify="end",
        ),
    )


def main_table() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.cond(
                    LocationsState.sort_reverse,
                    rx.icon(
                        "arrow-down-z-a",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=LocationsState.toggle_sort,
                    ),
                    rx.icon(
                        "arrow-down-a-z",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=LocationsState.toggle_sort,
                    ),
                ),
                rx.select(
                    [
                        "name",
                        "id",
                        "countryCode",
                        "country",
                    ],
                    placeholder="Sort By: Name",
                    size="3",
                    on_change=LocationsState.set_sort_value,
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    rx.input.slot(
                        rx.icon("x"),
                        justify="end",
                        cursor="pointer",
                        on_click=LocationsState.setvar("search_value", ""),
                        display=rx.cond(LocationsState.search_value, "flex", "none"),
                    ),
                    value=LocationsState.search_value,
                    placeholder="Search here...",
                    size="3",
                    max_width=["150px", "150px", "200px", "250px"],
                    width="100%",
                    variant="surface",
                    color_scheme="gray",
                    on_change=LocationsState.set_search_value,
                ),
                align="center",
                justify="end",
                spacing="3",
            ),
            rx.button(
                rx.icon("arrow-down-to-line", size=20),
                "Export",
                size="3",
                variant="surface",
                display=["none", "none", "none", "flex"],
                on_click=rx.download(url="/example.json"),
            ),
            spacing="3",
            justify="between",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Country", "earth"),
                    _header_cell("Name", "map-pin"),
                    _header_cell("ID", "barcode"),
                    _header_cell("Country Code", "map"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    LocationsState.get_current_page,
                    lambda item, index: _show_item(item, index),
                )
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        _pagination_view(),
        width="100%",
    )
