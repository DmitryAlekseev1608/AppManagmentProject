## Постановка задачи

Создание полноценного сервиса видеоаналитики back и front. Выполнение различных детекций и сбор статистики: большие сумки, каски, светоотражающие жилеты, транспорт, а также распознавание скелета человека (17 landscapes), распознавание движений по скелету и отдельно детекция упавших людей.

Распознавание движений человека не будет встроено в back и front, а будет выполнена отдельно в качестве научно-исследовательской работы, под нее будет развернут train и infer (ввиду большого объема работ не успеем возможно встроить ее в сервис за такой короткий срок).

## Авторы работы

|       **ФИО**      	| **Моб. телефон** 	|        **Telegram**       	|
|:------------------:	|:----------------:	|:-------------------------:	|
| `Алексеев Дмитрий` 	| +7 965 225 12 24 	| https://t.me/Alex_alex_68 	|
| `Овченков Андрей`  	| +7 915 165 26 08 	| https://t.me/ovctech      	|
| `Тарасов Алексей`  	| +7 916 476 42 07 	| https://t.me/privetleha   	|

## Научный руководитель

Якимов Павел Николаевич (https://t.me/akhtyamovpavel).

## План выполнения ВКР 

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#aaa;border-spacing:0;}
.tg td{background-color:#fff;border-color:#aaa;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-sej6{border-color:inherit;font-family:"Lucida Console", Monaco, monospace !important;text-align:left;vertical-align:top}
.tg .tg-hv44{border-color:inherit;font-family:"Lucida Console", Monaco, monospace !important;text-align:center;vertical-align:top}
.tg .tg-wi6j{border-color:inherit;font-family:"Lucida Console", Monaco, monospace !important;font-weight:bold;text-align:center;
  vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-wi6j">Наименование<br>работ</th>
    <th class="tg-wi6j">Описание<br>результата</th>
    <th class="tg-wi6j">Срок<br>выполнения</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-sej6">Подготовка и обучение нейронных сетей:<br>- сбор датасета, предобработка данных;<br>- обучение нейонных сетей на базе YOLOv8;<br>- обучение нейронной сети на базе PoseC3d с подбором отдельных<br>предобученных детекторов человека под нее и отдельной предобученной<br>модели по распознаванию скелета.<br>Проработка архитектуры будущего сервиса.</td>
    <td class="tg-sej6">Обученные нейронные сети:<br>- большие сумки;<br>- каски;<br>- светоотражающие жилеты;<br>- транспорт;<br>- распознавание скелета человека (17 landscapes);<br>- распознавание движений по скелету;<br>- упавшие люди.<br>Архитектура сервиса.</td>
    <td class="tg-hv44">01.04.2024</td>
  </tr>
  <tr>
    <td class="tg-sej6">Разработка back части на FastApi и OpenCV betta-версия продукта.<br>Проработка front части на Angular или поиск аналогов, если выбранный<br><span style="font-weight:400;font-style:normal">Angular не сможет обеспечить нужный функционал. Улучшение качества</span><br><span style="font-weight:400;font-style:normal">моделей (</span>при необходимости<span style="font-weight:400;font-style:normal">).</span><br><span style="font-weight:400;font-style:normal">Разработка телеграмм-бота.</span><br><span style="font-weight:400;font-style:normal">Разработка БД на СУБД PostgreSQL.</span></td>
    <td class="tg-sej6">Кодовая база betta-версия.<br>Улучшенные модели (при необходимости).</td>
    <td class="tg-hv44">01.05.2024</td>
  </tr>
  <tr>
    <td class="tg-sej6">Встраивание в продукт различных open-source систем и доработка back<br>и front части (при необходимости и если успеем сделать основную часть):<br><span style="font-weight:500;font-style:normal">- Celery;</span><span style="font-weight:400;font-style:normal">- nginx;</span>- Redis;<span style="font-weight:400;font-style:normal">- firewall UFW</span>.<br><br><span style="font-style:italic">Если не успеем, то будем сдавать сервис для изолированных систем, где </span><br><span style="font-style:italic">ничего из этого использовать не получится.</span></td>
    <td class="tg-sej6">Готовый сервис видеоаналитики.</td>
    <td class="tg-hv44">01.06.2024</td>
  </tr>
</tbody>
</table>

|                                                                                                                                                          Наименование работ                                                                                                                                                          	|                                                                                                   Описание результата                                                                                                  	| Срок выполнения 	|
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:---------------:	|
| Подготовка и обучение нейронных сетей: - сбор датасета, предобработка данных; - обучение нейонных сетей на базе YOLOv8; - обучение нейронной сети на базе PoseC3d с подбором отдельных предобученных детекторов человека под нее и отдельной предобученной модели по распознаванию скелета. Проработка архитектуры будущего сервиса. 	| Обученные нейронные сети: - большие сумки; - каски; - светоотражающие жилеты; - транспорт; - распознавание скелета человека (17 landscapes); - распознавание движений по скелету; - упавшие люди. Архитектура сервиса. 	|    01.04.2024   	|
| Разработка back части на FastApi и OpenCV betta-версия продукта. Проработка front части на Angular или поиск аналогов, если выбранный Angular не сможет обеспечить нужный функционал. Улучшение качества моделей (при необходимости). Разработка телеграмм-бота. Разработка БД на СУБД PostgreSQL.                                   	| Кодовая база betta-версия. Улучшенные модели (при необходимости).                                                                                                                                                      	|    01.05.2024   	|
| Встраивание в продукт различных open-source систем и доработка back и front части (при необходимости и если успеем сделать основную часть): - Celery;- nginx;- Redis;- firewall UFW.  Если не успеем, то будем сдавать сервис для изолированных систем, где  ничего из этого использовать не получится.                              	| Готовый сервис видеоаналитики.                                                                                                                                                                                         	|    01.06.2024   	|