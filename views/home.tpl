<!DOCTYPE html>
<html>
<head>
    <title>ГрафМастер</title>
    <link rel="stylesheet" type="text/css" href="/css/home.css">
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Open+Sans:300,400,600,700&amp;lang=en" />
    <script src="/js/home.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400&display=swap" rel="stylesheet">
</head>
<body onload="loadSavedData()">
    <div id="topbar">
        <img src="/image/Logo.png" alt="Logo">
        <a href="/info">Информация</a>
        <a href="/about">О нас</a>
    </div>
    <header>
        <h1>Решение графов</h1>
    </header>
    <main>
            <div class="main_page">
                <div id="headings">
                <h2>Количество вершин</h2>
                <input type="number" id="numFields" min="2" max="10" onchange="updateInputFields()" />
                <h2>Матрица смежности вершин 1</h2>
                <div id="gridContainer1" class="grid-container">
                <!-- Grid 1 will be dynamically generated here -->
                </div>
                <h2>Матрица смежности вершин 2</h2>
                <div id="gridContainer2" class="grid-container">
                <!-- Grid 2 will be dynamically generated here -->
                </div>
                <div class="button-row">
                <button id="count"  class="count-button button-gradient" onclick="countButton()">Вычислениe</button>
                <button id="count1" class="count-button button-gradient1" onclick="countButton1()">Построение</button>
                <button id="count2" class="count-button button-gradient2" onclick="countButton2()">Поиск</button>
                </div>
                <div class="var1">
                  <p> Информация о графах: </p>
                  <h2 id="message">
                      % for msg in message:
                          <p>{{ msg }}</p>
                      % end
                  </h2>
                </div>
            </div>
            <div class="image_grid">
            <h2>Исходные графы</h2>
                <div class="graphs">
                    <img src="/graphs_images/graph_source_1.png" alt="Граф 1">
                </div>
                <div class="graphs">
                    <img src="/graphs_images/graph_source_2.png" alt="Граф 2">
                </div>
            </div>
            <div class="image_grid">
            <h2>Результирующие графы</h2>
                <div class="graphs_result">
                    <img src="/graphs_images/graph_result_1.png" alt="Граф 1">
                </div>
                <div class="graphs_result">
                    <img src="/graphs_images/graph_result_2.png" alt="Граф 2">
                </div>
            </div>
        </div>
    </main>
    <footer>
        <p>ФСПО ГУАП &copy; 2023</p>
    </footer>
</body>
</html>
