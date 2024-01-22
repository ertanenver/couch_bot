from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from funcs.get_month import get_month, months

def get_inlane_keyboard(mode):
    if mode == 'main_menu':
        keyb_main_menu = InlineKeyboardBuilder()
        keyb_main_menu.button(text='В основное меню ⤴️', callback_data='button_0')
        return keyb_main_menu.as_markup()

    if mode == 'welcome_msg':
        keyb_welcome_msg = InlineKeyboardBuilder()
        keyb_welcome_msg.button(text='Создание квитанций', callback_data='kvit_mode')
        keyb_welcome_msg.button(text='Работа со сверкой', callback_data='sverka_mode')
        #keyb_welcome_msg.button(text='Соревнования', callback_data='comp_mode')
        keyb_welcome_msg.button(text='Настройки', callback_data='settings')
        keyb_welcome_msg.adjust(2,1)
        return keyb_welcome_msg.as_markup()

    if mode == 'show_password':
        keyb_show_password = InlineKeyboardBuilder()
        keyb_show_password.button(text='Показать пароль', callback_data='show_password')
        keyb_show_password.adjust(1)
        return keyb_show_password.as_markup()
    
    if mode == 'hide_password':
        keyb_hide_password = InlineKeyboardBuilder()
        keyb_hide_password.button(text='Скрыть пароль', callback_data='hide_password')
        keyb_hide_password.adjust(1)
        return keyb_hide_password.as_markup()

#                               Кнопки по квитанциям
    if mode == 'kvit':
        keyb_kvit = InlineKeyboardBuilder()
        keyb_kvit.button(text='Загрузить из файла', callback_data='kvit_file_mode')
        keyb_kvit.button(text='Загрузить из ведомости', callback_data='kvit_vedomost_mode')
        keyb_kvit.button(text='Создать локально', callback_data='kvit_local_mode')
        keyb_kvit.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_kvit.adjust(1)
        return keyb_kvit.as_markup()
    
    if mode == 'kvit_file_mode': # загрузка данных из файла
        keyb_kvit_file_mode = InlineKeyboardBuilder()
        keyb_kvit_file_mode.button(text='Получить файл-шаблон', callback_data='kvit_send_file_example')
        keyb_kvit_file_mode.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_kvit_file_mode.adjust(1)
        return keyb_kvit_file_mode.as_markup()

    if mode == 'kvit_local_mode': # локальный ввод данных
        keyb_kvit_local_mode = InlineKeyboardBuilder()
        keyb_kvit_local_mode.button(text='➕', callback_data='kvit_local_mode_add_person')
        keyb_kvit_local_mode.button(text='✅ Готово', callback_data='kvit_local_mode_done')
        keyb_kvit_local_mode.button(text='❌ Отменить', callback_data='kvit_local_mode_cancel')
        keyb_kvit_local_mode.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_kvit_local_mode.adjust(1,2,1)
        return keyb_kvit_local_mode.as_markup()

    if mode == 'kvit_purpose': # обычное назначение платежа
        dict = get_month()
        keyb_kvit_purpose = InlineKeyboardBuilder()
        keyb_kvit_purpose.button(text=f'{dict["previous_month"].title()}', callback_data=f'kvit_purpose_previous_month')
        keyb_kvit_purpose.button(text=f'{dict["current_month"].title()}', callback_data=f'kvit_purpose_current_month')
        keyb_kvit_purpose.button(text=f'{dict["following_month"].title()}', callback_data=f'kvit_purpose_following_month')
        keyb_kvit_purpose.button(text=f'✏️ Ввести самостоятельно ✏️', callback_data='kvit_input_purpose_mode')
        keyb_kvit_purpose.button(text=f'Ежегодный членский взнос', callback_data='kvit_yearly_fee_mode')
        keyb_kvit_purpose.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_kvit_purpose.adjust(3,1,1,1)
        return keyb_kvit_purpose.as_markup()

    if mode == 'kvit_purpose_input_purpose_mode': 
        keyb_purpose_input_purpose_mode = InlineKeyboardBuilder()
        for month in months:
            keyb_purpose_input_purpose_mode.button(text=f'{months[month]}', callback_data=f'kvit_purpose_{month}')
        keyb_purpose_input_purpose_mode.adjust(3)
        return keyb_purpose_input_purpose_mode.as_markup()




#                               Кнопки по настройкам
    if mode == 'settings': 
        keyb_settings = InlineKeyboardBuilder()
        keyb_settings.button(text='📄 Кол-во квитанций на листе', callback_data='settings_sum_kvit')
        keyb_settings.button(text='⚡️ Фича', callback_data='settings_feature')
        keyb_settings.button(text='🔔 Напоминания', callback_data='settings_notification')
        keyb_settings.button(text='👤 Выйти из аккаунта', callback_data='unlogin')
        keyb_settings.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_settings.adjust(1,1,2,1)
        return keyb_settings.as_markup()

    if mode == 'settings_notification': 
        keyb_settings_notification = InlineKeyboardBuilder()
        keyb_settings_notification.button(text='Напоминать об отправке ведомости', callback_data='settings_notification_vedomost')
        keyb_settings_notification.button(text='Напоминать о генерации квитанций', callback_data='settings_notification_kvit')
        keyb_settings_notification.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_settings_notification.adjust(1)
        return keyb_settings_notification.as_markup()
    
    if mode == 'settings_sum_kvit':
        keyb_settings_sum_kvit = InlineKeyboardBuilder()
        keyb_settings_sum_kvit.button(text='3 квитанции',callback_data="keyb_settings_sum_kvit_3")
        keyb_settings_sum_kvit.button(text='4 квитанции',callback_data="keyb_settings_sum_kvit_4")
        keyb_settings_sum_kvit.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_settings_sum_kvit.adjust(2,1)
        return keyb_settings_sum_kvit.as_markup()



#                               Кнопки по соревнованиям
    if mode == 'comp':
        keyb_comp = InlineKeyboardBuilder()
        keyb_comp.button(text='🔍 Поиск', callback_data='comp_search')
        keyb_comp.button(text='👊 Сила удара / разбивание', callback_data='comp_sila_udara')
        keyb_comp.button(text='👊 Спецтехника', callback_data='comp_sila_udara')
        keyb_comp.button(text='↗️ Загрузить протокол', callback_data='comp_upload_protocol')
        keyb_comp.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_comp.adjust(1,1,1,2)
        return keyb_comp.as_markup()

    if mode == 'comp_search':
        keyb_comp_search = InlineKeyboardBuilder()
        keyb_comp_search.button(text='🔍 Спортсмен ', callback_data='comp_search_sportsman')
        keyb_comp_search.button(text='🔍 Тренер ', callback_data='comp_search_coach')
        keyb_comp_search.button(text='🔍 Клуб ', callback_data='comp_search_club')
        keyb_comp_search.button(text='🔍 Регион ', callback_data='comp_search_region')
        keyb_comp_search.button(text='В основное меню ⤴️', callback_data='button_0')
        keyb_comp_search.adjust(2,2,1)
        return keyb_comp_search.as_markup()
        
        
        