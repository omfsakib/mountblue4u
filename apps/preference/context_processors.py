from apps.preference.models import PreferenceModel, MenuModel


def get_context(request):
    preference = PreferenceModel.objects.last()
    menus = MenuModel.objects.filter(is_active=True)
    context = {
        'preference': preference,
        'main_menu': menus.filter(type=MenuModel.MenuType.main)
    }

    return context
