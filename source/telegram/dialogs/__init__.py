from aiogram import Router
from aiogram_dialog import Dialog

from .dialog import dialog


def setup_dialog_routers() -> Router:
    """Setup and return dialog router."""
    router = Router()
    router.include_routers(dialog)
    return router
