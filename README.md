Программа для парсинга новостных страниц.

Программа использует файл config.ini для данных о кодировке, путях к тексту и заголовкам для разных газет.

Парсинг страницы осуществляется с использованием библиотеки lxml, элементы выделяются с помощью xpath.

Название текстового файла формируется из url.

Метод writeline печатает в текстовый файл согласно требованиям о ширине строки 80 символов и разделении абзацев пустой строкой.
