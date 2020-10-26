# Сервис для удалённого рендеринга сцен Blender (тестовое задание для Luxoft)

## 1
**Задание**
```
Реализация скриптов для запуска приложения, настройки сцен и рендеринга. Ознакомление с 3D приложением и RadeonProRender плагином. 
Желательно использовать python 3.5. 
Приложение можно взять maya или blender (или можете предложить другое, если есть желание). 
Операционная система для maya - win10 или macOS, для blender - win10, ubuntu18, macOS. 
Плагин для рендеринга берем RadeonProRender c официального сайта AMD.
Вам необходимо скачать приложение, установить плагин, поразбираться немного как что работает. Создать простую сцену с шаром и каким-то материалом сверху, освещение по желанию, текстуры тоже. 
На вход скрипту даем архив со сценой и текстурами, либо просто сцену, а также некоторые набор параметров, которые вы придумывайте сами.
На выходе получаем картинку и лог файл приложения. 
Код выкладываем на github. 

Блендер и плагин RadeonProRender являются open source, поэтому в случае проблем можно посмотреть исходный код. 
```

**Ссылки:**
1. https://docs.blender.org/api/current/info_quickstart
2. https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
3. https://blender.stackexchange.com/questions/6817/how-to-pass-command-line-arguments-to-a-blender-python-script
4. https://stackoverflow.com/questions/14982836/rendering-and-saving-images-through-blender-python
5. https://stackoverflow.com/questions/48482513/render-blender-outside-of-blender-gui-with-python
6. https://stackoverflow.com/questions/21406887/subprocess-changing-directory/21406995
7. https://blender.stackexchange.com/questions/80/can-cycles-renders-be-done-from-the-command-line
8. https://stackoverflow.com/questions/15535240/how-to-write-to-stdout-and-to-log-file-simultaneously-with-popen
9. https://pythonz.net/references/named/file.close/
10. https://blender.stackexchange.com/questions/48584/how-to-add-a-texture-to-a-material-using-python

## 2
**Задание**
```
Развертывание Jenkins, создание Pipeline Job, написание своего параметризированного пайплайна. 
Развернуть Jenkins можно локально, но будет отлично, если вы сделаете это в облаке. 
В качестве ноды для рендера вы используете свой ноутбук или ПК. Мы не будем делать какие-то сложные сцены, поэтому слабая производительность не будет проблемой. 
В Jenkins создаем Pipeline Job, добавляем необходимые нам параметры, пишем пайплайн. 
Пайплайн должен исходя из заданых параметров (ссылка на сцену, параметры рендера, название машины или ее лейблы) выбрать исполнителя (ноду) и запустить на ней рендер, забрать результаты и прикрепить к запуску.
```

**Ссылки:**
1. https://www.jenkins.io/doc/book/pipeline/syntax/
2. https://stackoverflow.com/questions/43003510/can-jenkins-job-execute-shell-or-windows-command-conditionally-based-on-agent-os
3. https://stackoverflow.com/questions/43587964/jenkins-pipeline-if-else-not-working
4. https://stackoverflow.com/questions/43587964/jenkins-pipeline-if-else-not-working
5. https://stackoverflow.com/questions/51480440/file-parameter-in-declarative-pipeline
6. https://stackoverflow.com/questions/61057780/unable-to-stash-file-in-jenkins-pipeline
7. https://stackoverflow.com/questions/46448976/jenkins-declarative-pipeline-post-action-success-before-always
8. http://vgaidarji.me/blog/2018/07/30/working-with-jenkinsfile-in-intellij-idea/
9. https://ealebed.github.io/posts/2018/jenkins-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-shared-libraries/
10. https://stackoverflow.com/questions/21045061/git-clone-from-another-directory/21045596
11. https://issues.jenkins-ci.org/browse/JENKINS-62961

***Заметки:***
1. file в замыкании parameters хранить относительный от workspace-а путь к файлу, поэтому приходится использовать 
    строковый путь к нему и java-ские библиотеки, это же сломало render.py, так-как движок блендера понимает только абсолютные пути.
2. Странная логика stash (сначала dir, потом включить файла, просто путь нельзя указать).
3. Декларативный if-else через when сложен (даже в декларативных функциональных языках есть if-else).
4. Проблемы интерфейса: не красивый, не удобный, плагин не установился сразу (кнопки пропали), параметры пайплайна 
    обновляются только после перезапуска, некорректные описания ошибок (Library expected to contain at least one 
    of src or vars directories).
5. Выкачивает весь репозиторий если надо получить jenkinsfile из scm.
6. Задал пути для Gradle и Maven.

## 3
**Задание**
```
Создание Web Service или Teams/Telegram бота. 
Технологии: желательно python 3.5, flask/django на backend, фронт на ваше усмотрение. 
Если не хотите писать веб сервис, то можете взять бота, желательно попробовать teams, если у вас получится с ним работать (я не уверен, что он бесплатно доступен).
Цель: с помощью UI или сообщения боту отправить сцену для рендера, получить изображение в ответ.
```

**Ссылки:**
1. https://stackoverflow.com/questions/8231058/file-type-validation-with-javascript
2. https://stackoverflow.com/questions/857618/javascript-how-to-extract-filename-from-a-file-input-control
3. https://stackoverflow.com/questions/44044373/how-to-properly-throw-an-error-in-vue-js
4. https://developer.mozilla.org/ru/docs/Web/API/FormData/append
5. https://www.tutorialspoint.com/downloading-files-from-web-using-python
6. https://jenkinsapi.readthedocs.io/en/latest/index.html
7. https://github.com/pycontribs/jenkinsapi/issues/428
8. https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#id6
9. https://github.com/pycontribs/jenkinsapi/blob/master/jenkinsapi_tests/systests/test_jenkins_artifacts.py
10. https://stackoverflow.com/questions/57346338/how-to-return-image-stream-and-text-as-json-response-from-python-flask-api
11. https://ru.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html
12. https://www.geeksforgeeks.org/resize-image-proportionally-with-css/
13. https://onlinejpgtools.com/convert-base64-to-jpg