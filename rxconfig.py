import reflex as rx
import os

API_URL = os.getenv("API_URL", "https://your-vercel-domain.vercel.app/api")
config = rx.Config(
    app_name="nova",
    plugins=[rx.plugins.TailwindV3Plugin()],
    REFLEX_api_url=API_URL,
)