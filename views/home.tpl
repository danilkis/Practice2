<!DOCTYPE html>
<html>
<head>
    <title>ГрафМастер</title>
    <link rel="stylesheet" type="text/css" href="/css/home.css">
    <script>
       function updateInputFields() {
            var numFields = parseInt(document.getElementById('numFields').value);
            var gridContainer1 = document.getElementById('gridContainer1');
            var gridContainer2 = document.getElementById('gridContainer2');
            gridContainer1.innerHTML = ''; // Clear existing grid 1
            gridContainer2.innerHTML = ''; // Clear existing grid 2

            for (var i = 0; i < numFields; i++) {
                var gridRow1 = document.createElement('div');
                var gridRow2 = document.createElement('div');
                gridRow1.className = 'grid-row';
                gridRow2.className = 'grid-row';

                for (var j = 0; j < numFields; j++) {
                    var gridItem1 = document.createElement('div');
                    var gridItem2 = document.createElement('div');
                    gridItem1.className = 'grid-item';
                    gridItem2.className = 'grid-item';
                    var checkbox1 = document.createElement('input');
                    var checkbox2 = document.createElement('input');
                    checkbox1.type = 'checkbox';
                    checkbox2.type = 'checkbox';

                    // Disable checkboxes where i < j or i = j
                    if (i < j || i === j) {
                        checkbox1.disabled = true;
                        checkbox2.disabled = true;
                    }

                    gridItem1.appendChild(checkbox1);
                    gridRow1.appendChild(gridItem1);
                    gridItem2.appendChild(checkbox2);
                    gridRow2.appendChild(gridItem2);
                }

                gridContainer1.appendChild(gridRow1);
                gridContainer2.appendChild(gridRow2);
            }
        }
    </script>
</head>
<body>
    <div id="topbar">
        <img src="/static/logo.png" alt="Logo">
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
        <button>Рассчитать</button>
    </main>
</body>
</html>
