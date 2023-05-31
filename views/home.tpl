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
<body>
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
                <input type="number" id="numFields" onchange="updateInputFields()" />
                <h2>Матрица смежности вершин 1</h2>
                <div id="gridContainer1" class="grid-container">
                <!-- Grid 1 will be dynamically generated here -->
                </div>
                <h2>Матрица смежности вершин 2</h2>
                <div id="gridContainer2" class="grid-container">
                <!-- Grid 2 will be dynamically generated here -->
                </div>
                <div class="button-row">
                <button id="count"  class="count-button button-gradient" onclick="saveMatrices()">Рассчитать</button>
                <button id="count1" class="count-button button-gradient1" onclick="countButton1()">Рассчитать 1</button>
                <button id="count2" class="count-button button-gradient2" onclick="countButton2()">Рассчитать 2</button>
                </div>
            </div>
            <div class="image_grid">
            <h2>Построенные графы</h2>
                <div class="creator">
                    <img src="/graphs_images/graph.png" alt="Граф 1">
                </div>
                <div class="creator">
                    <img src="/graphs_images/graph.png" alt="Граф 2">
                </div>
            </div>
            <div class="image_grid">
            <h2>Результирующие графы</h2>
                <div class="creator">
                    <img src="/graphs_images/graph.png" alt="Граф 1">
                </div>
                <div class="creator">
                    <img src="/graphs_images/graph.png" alt="Граф 2">
                </div>
            </div>

        </div>
    </main>
</body>
</html>
