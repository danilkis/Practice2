<!DOCTYPE html>
<html>
<head>
  <title>Информация</title>
  <link rel="stylesheet" type="text/css" href="/css/info.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <script src="/js/info.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400&display=swap" rel="stylesheet">
</head>
<body>
  <a href="/" class="back-button">
    <img src="/image/btn_back.png" alt="Назад" >
  </a>
  <header>
    <h1>Информация</h1>
  </header>
  <div class="button-row">
      <button onclick="scrollToInfo1()" class="goto_button">Вычисления в графах</button>
      <button onclick="scrollToInfo2()" class="goto_button">Построение по заданным графам</button>
      <button onclick="scrollToInfo3()" class="goto_button">Поиск по заданным графам</button>
  </div>
  <div class="informat">
  <p>
     На сайте решаются некоторые задачи с неориентированными графами.<br> 
     1) Вы можете посчитать:<br> 
     - число ребер в заданных графах;<br> 
     - число изолированных подграфов в первом графе;<br>
     - диаметр второго графа — длину максимальной цепи в графе.<br>
     2) Для заданных графов построится:<br>
     - новый граф — объединение двух графов;<br>
     - подграф — пересечение двух графов;<br>
     - подграф — дополнение первого графа до полного.<br>
     3) Поиск:<br>
     - числа ребер, выходящих из каждой вершины обоих графов (степени
вершин).<br>
     - всех правильных графов из N вершин.<br>
  </p>
  </div>
  <!-- Добавляем якорные ссылки для перемещения -->
  <div id="info1" class="info-section">
    <p>
     1) Подсчет числа ребер в неориентированном графе:<br> 
     В неориентированном графе каждое ребро соединяет две вершины и не имеет направления.<br> 
     Чтобы посчитать число ребер в неориентированном графе, можно использовать формулу:<br> 
     Число ребер = Сумма степеней всех вершин / 2<br> 
     Где степень вершины - это количество ребер, инцидентных данной вершине.<br> 
     Для подсчета числа ребер в графе, необходимо посчитать степень каждой вершины и сложить полученные значения. <br> 
     Затем полученную сумму разделить на 2.<br> 
     <p>
     </p>
     2) Подсчет числа изолированных подграфов в первом графе:<br> 
     Изолированный подграф - это подграф, который состоит только из одной вершины и не имеет ребер,<br> 
     соединяющих эту вершину с другими вершинами в графе.<br> 
     Чтобы посчитать число изолированных подграфов в графе, <br> 
     нужно подсчитать количество вершин, которые не имеют ребер, и которые не связаны с другими вершинами.<br> 
     <p>
     </p>
     3) Подсчет диаметра графа:<br> 
     Диаметр графа определяется как максимальная длина цепи (путь), соединяющей две вершины в графе. <br> 
     Цепь - это последовательность ребер и вершин, такая что каждое ребро соединяет две соседние вершины в цепи.<br> 
     Для поиска диаметра второго графа и нахождения длины максимальной цепи, можно использовать алгоритм обхода графа в глубину (Depth-First Search) или алгоритм Флойда-Уоршелла (Floyd-Warshall). <br> 
     Оба алгоритма позволяют найти все возможные пути между вершинами в графе и определить максимальную длину цепи.<br> 
     Примерный алгоритм для нахождения диаметра графа:<br> 
     Для каждой вершины в графе запустите алгоритм обхода графа в глубину или алгоритм Флойда-Уоршелла, начиная с данной вершины.<br> 
     В каждом запущенном алгоритме, сохраняйте максимальную длину найденной цепи.<br> 
     После выполнения алгоритма для каждой вершины, выберите максимальную длину цепи среди всех запущенных алгоритмов. Это и будет диаметр графа.<br> 

  </p>
  </div>

  <div id="info2" class="info-section">
    <p>
     1) Объединение двух графов:<br> 
     Для объединения двух графов необходимо соединить их вершины и ребра.<br> 
     Если графы представлены списком вершин и списком ребер, можно выполнить следующие шаги для объединения:<br> 
     - Создайте новый пустой граф, который будет представлять объединение двух графов.<br> 
     - Добавьте все вершины из первого графа в новый граф.<br> 
     - Добавьте все вершины из второго графа в новый граф.<br>  
     Обратите внимание, что вершины из второго графа должны быть переименованы, чтобы избежать конфликтов с вершинами из первого графа.<br> 
     - Добавьте все ребра из первого графа в новый граф.<br> 
     - Добавьте все ребра из второго графа в новый граф.<br>  
     - При добавлении ребер из второго графа, учтите изменение их вершин: каждая вершина в ребре из второго графа должна быть переименована в новое имя вершины из второго графа.<br> 
     - Новый граф представляет объединение двух графов.<br> 
     <p>
     </p>
     2) Пересечение двух графов: <br> 
     - Создайте новый пустой граф, который будет представлять пересечение двух графов.<br> 
     - Найдите общие вершины, которые присутствуют и в первом, и во втором графе.<br> 
     - Добавьте общие вершины в новый граф.<br> 
     - Добавьте только те ребра, которые соединяют общие вершины, в новый граф.<br> 
     - Новый граф представляет пересечение двух графов.<br> 
     <p>
     </p>
     3) Дополнение первого графа до полного: <br> 
     - Создайте полный граф, который содержит все вершины из первого графа.  <br> 
     - Это означает, что каждая вершина первого графа будет связана со всеми остальными вершинами в этом полном графе. <br>  
     - Например, если у вас есть граф с вершинами [1, 2, 3], то полный граф будет содержать все возможные ребра между этими вершинами. <br> 
     - Определите ребра, которые отсутствуют в первом графе.  <br> 
     - Для этого пройдитесь по всем возможным парам вершин в полном графе и проверьте, есть ли соответствующее ребро в первом графе.  <br> 
     - Если ребра нет, добавьте его в первый граф. <br> 
     - После добавления всех отсутствующих ребер первый граф станет полным графом, где каждая вершина связана со всеми остальными вершинами (кроме самой себя). <br> 
  </p>
  </div>

  <div id="info3" class="info-section">
    <p>
     1)Расчет степеней вершин:<br> 
       - Проход по каждой вершине графа.<br> 
       - Для каждой вершины, посчитать количество ненулевых элементов в соответствующей строке или столбце матрицы смежности. Это количество и будет степенью вершины.<br> 
       - Записать полученные значения степеней для каждой вершины графа.<br> 
       <p>
     </p>
     2)Поиск всех правильных графов из N вершин:<br> 
       - Задать количество вершин графа N.<br> 
       - Создать пустой граф с N вершинами.<br> 
       - Задать степень вершин графа как равную N-1 (все вершины имеют одинаковую степень).<br> 
       - Создать массив с N элементами, инициализировать его значением N-1 (начальная степень каждой вершины).<br> 
       - Задать переменную total_edges = N * (N-1) / 2 (общее количество ребер в полном графе).<br> 
       - Создать вложенный цикл для перебора возможных ребер:<br> 
       - Внешний цикл по i от 0 до N-1 (индекс вершины, от которой исходит ребро).<br> 
        - Внутренний цикл по j от i+1 до N (индекс вершины, к которой направлено ребро).<br> 
        - Проверить, что массив степеней вершин i и j больше 0:<br> 
       - Если оба элемента массива больше 0, то добавить ребро между вершинами i и j.<br> 
       - Уменьшить значения элементов массива степеней вершин i и j на 1.<br> 
       - Уменьшить total_edges на 1.<br> 
        - Проверить, что total_edges равно 0 (все ребра добавлены) и массив степеней вершин содержит только нули (степени всех вершин равны).<br> 
       - Если условие выполнено, то найден правильный граф. Выполнить отображение графа<br> 
  </p>
  </div>


</body>
</html>