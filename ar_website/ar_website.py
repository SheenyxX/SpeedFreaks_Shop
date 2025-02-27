import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    pass

# Navigation Bar
def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("🏁 SpeedFreaks", size="6", color="black"),
            style={
                "position": "absolute",
                "left": "3%",  # Move the title to the left
                "top": "50%",
                "transform": "translateY(-50%)",  # Vertical centering trick
            },
        ),
        rx.box(
            rx.link("Home", href="#", color="white"),
            rx.link("Products", href="#", color="white"),
            rx.link("Contact", href="#", color="white"),
            style={
                "position": "absolute",
                "right": "5%",  # Move links to the right
                "top": "50%",
                "transform": "translateY(-50%)",
                "display": "flex",
                "gap": "2rem",  # Space between links
            }
        ),
        style={
            "background": "rgba(0, 0, 0, 0.2)",
            "position": "sticky",
            "top": "0",
            "width": "100%",
            "height": "4rem",  # Fixed navbar height
            "z_index": "10",
        },
    )


# Hero Section - Using absolute positioning
def hero_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("🏁 SpeedFreaks", size="9", color="black"),
            rx.text("Crafted for Enthusiasts, Driven by Speed", size="5", color="wihte"),
            rx.link(
                rx.button("🔥Hot Sales!"),
                href="https://www.facebook.com/profile.php?id=100069765637816/",
                is_external=True,
            ),
            spacing="5",
            align_items="flex-start",  # Align items to the left within this container
            style={
                "position": "absolute",
                "right": "52%",  # Position 20% from the right edge
                "top": "40%",    # Position in the middle vertically
                "transform": "translateY(-50%)",  # Center vertically
                "background": "rgba(0, 0, 0, 0.1)",  # Semi-transparent background
                "padding": "2rem",
                "border_radius": "10px",
            }
        ),
        min_height="85vh",
        width="100%",
        position="relative",  # Required for absolute positioning of children
    )

# Featured Products Section
# Featured Products Section
def featured_products() -> rx.Component:
    return rx.vstack(
        rx.heading("Limited Edition", size="7", color="white"),
        rx.flex(
            rx.link(
                rx.box(rx.image(src="/product_1.jpg", width="300px", height="200px"), padding="5px"),
                href="https://www.ebay.com/itm/387136422467?_trkparms=amclksrc%3DITM%26aid%3D1110018%26algo%3DHOMESPLICE.COMPLISTINGS%26ao%3D1%26asc%3D20220808120223%26meid%3Dab8e4cfa9bbd40d286677ac165cbbdaf%26pid%3D101546%26rk%3D15%26rkt%3D25%26sd%3D387136512271%26itm%3D387136422467%26pmt%3D1%26noa%3D0%26pg%3D3959035%26algv%3DPromotedCompV5WithHighAdFeeWithKnnRecallV1PostRankerMode1WithMyFG%26brand%3DMaisto&_trksid=p3959035.c101546.m1851&itmprp=cksum%3A387136422467ab8e4cfa9bbd40d286677ac165cbbdaf%7Cenc%3AAQAKAAABMHLP2FxpoV60wo2FCLo6WhwQgcx8Hy69mmKyqhd4ZFkoMvAyDIDbFBW64IYHO1rB%252FTm%252BcHC7Yz8svLFZRRyjiUc%252FYijA%252FNKFbGt87quOqeVBvRPLLDQQ7eFrRQ0eiqp1txrKlNNJlNLehw1Uzqu%252FdsP74ocFd12Z5koISdG0wYNN0EcjFudvPbfZrj247DVcpBi3sti4SlKRjuBlJEG62dZgxECUW%252FD2kRL2Z5IKY2y0ml5viy%252FCqpYjBB4A13Jv%252FIxRskXY%252BY%252B0JVYrgekh43KunhS77CNKYwhjMyfuzbIMm8gDQwr8xs0YnsFdK6EfeNT97y%252BNO9LMU%252BXxDuMbk3if4cyUKnQFKALFSK%252BSO4ILljX9Ha2uAPbNEKhW52bbMQRf7xFsatSA%252BphBRflGjJk%253D%7Campid%3APL_CLK%7Cclp%3A3959035&itmmeta=01JN42ATFDK2D49DD7BFVVJ98W",
                is_external=True,
            ),
            rx.link(
                rx.box(rx.image(src="/product_2.jpg", width="300px", height="200px"), padding="5px"),
                href="https://www.ebay.com/itm/404633764752?_skw=superbike+toy&itmmeta=01JN2SW5VCWWQJN3Z4RNTV94ZR&hash=item5e360d4390:g:3esAAOSwI4pf~8un&itmprp=enc%3AAQAKAAAA8FkggFvd1GGDu0w3yXCmi1e53F%2FAfl2VeE3nJgRaQG9v1ZxbrP81nJUJoqIypjXOdntiF%2B5dFpkLQppBN%2FkQQljIZJt%2FCdQ3%2FS7QWnt5NQ91uCG2MhCYIRoiXQxZzIzeXL%2FroZhOExdVYfdgzkbB1OuvTjZov9eLZxqoREGRC5QNBAA2DKH93u922wouFcLCTKzZ46SSFj4BYO0Yp%2B5zJVRLJdw1tOKsUhlNBJ2yJIlV3F4qfHvcV%2B2u0mUmtNxAYAC0VG6TjevgJkaRDpV3hpqbUjOPn7r71AsnLTuVXiEwEkawHgXHXvtMyolepINFhA%3D%3D%7Ctkp%3ABk9SR-7d8NmoZQ",
                is_external=True,
            ),
            rx.link(
                rx.box(rx.image(src="/product_3.jpg", width="260px", height="200px"), padding="5px"),
                href="https://www.ebay.com/itm/404563623981?_skw=superbike+toy&itmmeta=01JN2SW5VC5BRWH6APSS0P1EFP&hash=item5e31df002d:g:oosAAOSwDixjmvPs&itmprp=enc%3AAQAKAAAA8FkggFvd1GGDu0w3yXCmi1e8YgF%2BZOnjRi0Hp3I3xjXtpJ92Rc0RUyr0ZYOLYhEFsktt%2FfYnAt%2Bhs3Dl%2F0VJswZPTjGewVGBVveuiIGxI53zdUR%2BEsQOpgZznU2HpFe1ikH6CGTiFes%2BcfKQuAuRXBGOzrMFr80SFDG6buB1FLX3Scvc%2FAiWUToqhW6H5yDElGU7o5lkqqtIEUTYr3ZJQHSkpjMT7ETpUbJ3g0D2KVx8ZoF7chAYG1GW816POuip5SHAHW22AThM3X%2B1CqfctscT5RYiEdr6djKGjlCNlgUDJX9xWC5yclcycPDjaQ4bfQ%3D%3D%7Ctkp%3ABk9SR-7d8NmoZQ",
                is_external=True,
            ),
            justify="center",
            align_items="center",
            width="100%",
            flex_wrap="wrap",
            gap="10px",
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
        },
    )

# App Initialization
app = rx.App()
app.add_page(index)