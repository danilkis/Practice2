<!DOCTYPE html>
<html>
<head>
    <title>ГрафМастер</title>
    <link rel="stylesheet" type="text/css" href="/css/home.css">
    <script src="/js/home.js"></script>
</head>
<body>
    <div id="topbar">
        <img src="/image/Logo.png" alt="Logo">
        <a href="/">Главная</a>
        <a href="/about">О нас</a>
    </div>
    <header>
        <h1>Решение графов</h1>
    </header>
    <main>
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
    </main>
</body>
</html>
