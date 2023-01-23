from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import src.data.buttons as buttons
import src.data.keyboards as keyboards
from src.data.faculties import BACHELOR_FACULTIES, MASTER_FACULTIES
from src.data.faculty import Faculty
from src.data.speciality import Speciality, SpecialityCallback
from src.functionality.util import handle_button, inline_buttons
from src.routing.back_button import NavigateBackCallback
from src.routing.main_menu import Degree
from src.routing.menu import Menu

router = Router()


async def get_data_from_state(state: FSMContext):
    degree = await state.get_state()
    data = await state.get_data()

    faculty_callback = data.get('faculty')
    speciality_callback = data.get('speciality')

    faculty_list = BACHELOR_FACULTIES if degree is Degree.bachelor else MASTER_FACULTIES

    faculty: Faculty = faculty_list[faculty_callback]

    if speciality_callback is not None:
        speciality: Speciality = faculty.get_speciality(speciality_callback.name)
        return faculty, speciality

    return faculty


@router.callback_query(NavigateBackCallback.filter(F.menu == Menu.DEGREE))
async def back_from_faculties(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(keyboards.DEGREE)


@router.callback_query(Degree.bachelor, handle_button(buttons.FACULTIES))
async def bachelor_faculties(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(keyboards.BACHELOR_FACULTIES)


@router.callback_query(Degree.master, handle_button(buttons.FACULTIES))
async def bachelor_faculties(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(keyboards.MASTER_FACULTIES)


@router.callback_query(NavigateBackCallback.filter(F.menu == Menu.FACULTIES))
async def back_from_specialities(callback_query: CallbackQuery, state: FSMContext):
    degree = await state.get_state()
    await callback_query.message.edit_reply_markup(
        keyboards.BACHELOR_FACULTIES if degree is Degree.bachelor else keyboards.MASTER_FACULTIES
    )


@router.callback_query(Degree.bachelor, handle_button(*inline_buttons(keyboards.BACHELOR_FACULTIES)))
async def choose_bachelor_faculty(callback_query: CallbackQuery, state: FSMContext):
    chosen_faculty = BACHELOR_FACULTIES[callback_query.data]
    await state.update_data(faculty=chosen_faculty.callback_data)
    await callback_query.message.edit_reply_markup(chosen_faculty.specialities_as_markup)


@router.callback_query(Degree.master, handle_button(*inline_buttons(keyboards.MASTER_FACULTIES)))
async def choose_master_faculty(callback_query: CallbackQuery, state: FSMContext):
    chosen_faculty = MASTER_FACULTIES[callback_query.data]
    await state.update_data(faculty=chosen_faculty.callback_data)
    await callback_query.message.edit_reply_markup(chosen_faculty.specialities_as_markup)


@router.callback_query(Degree.bachelor, SpecialityCallback.filter())
async def choose_bachelor_speciality(callback_query: CallbackQuery, callback_data: SpecialityCallback,
                                     state: FSMContext):
    await state.update_data(speciality=callback_data)
    await callback_query.message.edit_reply_markup(keyboards.SPECIALITY)


@router.callback_query(Degree.master, SpecialityCallback.filter())
async def choose_master_speciality(callback_query: CallbackQuery, callback_data: SpecialityCallback, state: FSMContext):
    await state.update_data(speciality=callback_data)
    await callback_query.message.edit_reply_markup(keyboards.SPECIALITY)


@router.callback_query(handle_button(*inline_buttons(keyboards.SPECIALITY)))
async def speciality_info(callback_query: CallbackQuery, state: FSMContext):
    _, speciality = await get_data_from_state(state)
    await callback_query.message.answer(text=getattr(speciality, callback_query.data))
