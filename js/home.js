function updateInputFields() {
    var numFields = parseInt(document.getElementById('numFields').value);
    var gridContainer1 = document.getElementById('gridContainer1');
    var gridContainer2 = document.getElementById('gridContainer2');
    gridContainer1.innerHTML = ''; // Clear existing grid 1
    gridContainer2.innerHTML = ''; // Clear existing grid 2

    for (var i = 0; i < numFields; i++) {
        var gridRow1 = document.createElement('div');
        var gridRow2 = document.createElement('div');
        gridRow1.className = 'grid-row'; //TODO: Симетричные включения
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

function saveMatrices() {
    var gridContainer1 = document.getElementById('gridContainer1');
    var gridContainer2 = document.getElementById('gridContainer2');
    var numFields = parseInt(document.getElementById('numFields').value);
    var matrix1 = [];
    var matrix2 = [];

    // Retrieve values from gridContainer1
    for (var j = 0; j < numFields; j++) {
        var row = [];
        for (var i = 0; i < numFields; i++) {
            var gridRow = gridContainer1.getElementsByClassName('grid-row')[i];
            var checkboxes = gridRow.getElementsByTagName('input');
            row.push(checkboxes[j].checked ? 1 : 0);
        }
        matrix1.push(row);
    }

    // Retrieve values from gridContainer2
    for (var j = 0; j < numFields; j++) {
        var row = [];
        for (var i = 0; i < numFields; i++) {
            var gridRow = gridContainer2.getElementsByClassName('grid-row')[i];
            var checkboxes = gridRow.getElementsByTagName('input');
            row.push(checkboxes[j].checked ? 1 : 0);
        }
        matrix2.push(row);
    }

    // Create JSON objects
    var jsonMatrix1 = JSON.stringify(matrix1);
    var jsonMatrix2 = JSON.stringify(matrix2);

    // Make the POST request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('Request successful');
            // Handle the response if needed
        }
    };

    xhr.send(JSON.stringify({ matrix1: jsonMatrix1, matrix2: jsonMatrix2 }));
}

function countButton1() {
    saveMatrices(); // Call the saveMatrices() function for the first button
    // Additional code for the first button...
}

function countButton2() {
    saveMatrices(); // Call the saveMatrices() function for the second button
    // Additional code for the second button...
}
