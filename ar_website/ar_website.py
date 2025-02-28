import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    pass

# Navigation Bar
def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading(
                "🏁 SpeedFreaks",
                size="6",
                color="black",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "1rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "1rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            style={
                "position": "absolute",
                "left": "3%",
                "top": "1.6rem",
                "transform": "translateY(-50%)",
                "@media (max-width: 768px)": {
                    "position": "static",
                    "transform": "none",
                    "text_align": "left",
                    "width": "100%",
                    "margin_top": "1rem",
                },
            },
        ),
        rx.box(
            rx.link(
                "Home",
                href="#",
                color="white",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "0.7rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "0.5rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            rx.link(
                "Instagram",
                href="https://www.instagram.com/speedfreaksxx?igsh=MWtvM2FoZzBycXhuMw%3D%3D&utm_source=qr",
                color="white",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "0.7rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "0.5rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            rx.link(
                "Contact",
                href="https://www.linkedin.com/in/andres-rivas-m200998/",
                color="white",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "0.7rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "0.5rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            style={
                "position": "absolute",
                "right": "5%",
                "top": "40%",
                "transform": "translateY(-50%)",
                "display": "flex",
                "gap": "2rem",
                "@media (max-width: 768px)": {
                    "position": "static",
                    "transform": "none",
                    "flex_direction": "column",  # Stack links vertically
                    "align_items": "center",
                    "gap": "0.3rem",  # Reduce gap between links
                    "margin_top": "1rem",
                },
            }
        ),
        style={
            "background": "rgba(0, 0, 0, 0.2)",
            "position": "sticky",
            "top": "0",
            "width": "100%",
            "height": "4rem",
            "z_index": "10",
            "@media (max-width: 768px)": {
                "height": "auto",
                "padding": "1rem",
            },
        },
    )

# Hero Section - Using absolute positioning
def hero_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "🏁 SpeedFreaks",
                size="9",
                color="black",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "2.5rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "1.5rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            rx.text(
                "Crafted for Enthusiasts, Driven by Speed",
                size="5",
                color="white",
                style={
                    "@media (max-width: 768px)": {
                        "font_size": "1.25rem",  # Smaller font size for mobile
                    },
                    "@media (max-width: 414px)": {
                        "font_size": "1rem",  # Even smaller for iPhone XR
                    },
                },
            ),
            rx.link(
                rx.button("🔥Hot Sales!"),
                href="https://www.facebook.com/profile.php?id=100069765637816/",
                is_external=True,
            ),
            spacing="5",
            align_items="flex-start",  # Default alignment for larger screens
            style={
                "position": "absolute",
                "right": "52%",
                "top": "40%",
                "transform": "translateY(-50%)",
                "background": "rgba(0, 0, 0, 0.1)",
                "padding": "2rem",
                "border_radius": "10px",
                "@media (max-width: 768px)": {
                    "position": "static",
                    "transform": "none",
                    "align_items": "center",  # Center alignment for mobile
                    "text_align": "center",
                    "width": "100%",
                    "padding": "1rem",
                    "margin_top": "2rem",
                },
                "@media (max-width: 414px)": {
                    "padding": "0.5rem",  # Smaller padding for iPhone XR
                },
            }
        ),
        min_height="85vh",
        width="100%",
        position="relative",
    )

# Featured Products Section
def featured_products() -> rx.Component:
    return rx.vstack(
        rx.heading("Limited Edition", size="7", color="white", style={"@media (max-width: 768px)": {"font_size": "2rem"}}),
        rx.flex(
            rx.link(
                rx.box(rx.image(src="/product_1.jpg", width="100%", height="auto", max_width="300px"), padding="5px"),
                href="https://www.ebay.com/itm/387136422467",
                is_external=True,
            ),
            rx.link(
                rx.box(rx.image(src="/product_2.jpg", width="100%", height="auto", max_width="300px"), padding="5px"),
                href="https://www.ebay.com/itm/404633764752",
                is_external=True,
            ),
            rx.link(
                rx.box(rx.image(src="/product_3.jpg", width="100%", height="auto", max_width="260px"), padding="5px"),
                href="https://www.ebay.com/itm/404563623981",
                is_external=True,
            ),
            justify="center",
            align_items="center",
            width="100%",
            flex_wrap="wrap",
            gap="10px",
            style={
                "@media (max-width: 768px)": {
                    "flex_direction": "column",
                    "gap": "2rem",
                },
            },
        ),
        spacing="5",
        padding_y="2rem",
        width="100%",
        align_items="center",
    )

# Footer Section
def footer() -> rx.Component:
    return rx.box(
        rx.text("© 2025 SpeedFreaks. All rights reserved.", color="white"),
        padding="2rem",
        style={
            "background": "rgba(0, 0, 0, 0.6)",
            "text_align": "center",
            "width": "100%",
        },
    )

# Main Page Layout
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            hero_section(),
            featured_products(),
            width="100%",
        ),
        footer(),
        style={
            "width": "100%",
            "min-height": "100vh",
            "margin": "0",
            "padding": "0",
            "background-image": "url('/Ducati_Background.jpg')",
            "background-size": "cover",
            "background-position": "center center",
            "background-repeat": "no-repeat",
            "background-attachment": "fixed",
            "overflow-x": "hidden",
            "@media (max-width: 768px)": {
                "background-size": "cover",
                "background_position": "center center",
            },
        },
    )

# App Initialization
app = rx.App()
app.add_page(index)
