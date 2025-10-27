from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("html"))
async def hello(message: Message):
    """Этот обработчик получает сообщения с `/http` командой и выводит HTML"""
    text = """
    <b>Жирный текст</b>
    <i>Курсивный текст</i>
    <u>Подчеркнутый текст</u>
    <s>Зачеркнутый текст</s>

    <b>Жирный <i>жирный курсив</i> внутри</b>
    <u>Подчеркнутый <s>подчеркнутый зачеркнутый</s> внутри</u>

    <a href="https://example.com">Встроенная ссылка</a>
    <code>Моноширинный текст (код)</code>

    <pre><code class="language-python">Блок кода
    с несколькими строками
    </code></pre>

    Не нужно экранировать символы!
    """
    await message.answer(text, parse_mode="HTML") # Изменяем режим на HTML, если по умолчанию используется другой

@router.message(Command("markdown"))
async def hello(message: Message):
    """Этот обработчик получает сообщения с `/markdown` командой и выводит Markdown"""
    text = """
    *Жирный текст*
    _Курсивный текст_
    __Подчеркнутый__
    ~Зачеркнутый текст~

    *Жирный _жирный курсив_ внутри*
    __Подчеркнутый ~подчеркнутый зачеркнутый~ внутри__

    [Встроенная ссылка](https://example.com)
    [Текст кнопки](buttonurl:https://example.com)

    `Моноширинный текст (код)`
    ```python
    Блок кода
    с несколькими строками
    ``` 
    """
    await message.answer(text, parse_mode=ParseMode.MARKDOWN_V2) # Изменяем режим на MARKDOWN_V2, если по умолчанию используется другой