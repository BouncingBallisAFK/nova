import reflex as rx

config = rx.Config(
    app_name="nova",
    plugins=[rx.plugins.TailwindV3Plugin()],
    api_url="http://nova-lemon-omega.vercel.app:8000",
)