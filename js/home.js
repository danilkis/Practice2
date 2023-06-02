function updateInputFields() {
  var numFieldsInput = document.getElementById('numFields');
  var numFields = parseInt(document.getElementById('numFields').value);

  // Ограничение допустимого значения
  var min = 2;
  var max = 10;
  if (numFields < min) {
    numFields = min;
  } else if (numFields > max) {
    numFields = max;
  }
  numFieldsInput.value = numFields;

  var gridContainer1 = document.getElementById('gridContainer1');
  var gridContainer2 = document.getElementById('gridContainer2');
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var storedCheckboxStates = {}; // Stores the checkbox states from localStorage

  checkboxes.forEach(function (checkbox) {
    var checkboxState = localStorage.getItem(checkbox.id);
    if (checkboxState !== null) {
      storedCheckboxStates[checkbox.id] = checkboxState === 'true';
    }
  });

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

      // Assign checkbox IDs
      checkbox1.id = i + ' ' + j;
      checkbox2.id = i + ' ' + j + ' sec'; // Add "_2" to the ID of checkboxes in the second grid

      gridItem1.appendChild(checkbox1);
      gridRow1.appendChild(gridItem1);
      gridItem2.appendChild(checkbox2);
      gridRow2.appendChild(gridItem2);

      // Set the checked state from stored values
      if (storedCheckboxStates[checkbox1.id] !== undefined) {
        checkbox1.checked = storedCheckboxStates[checkbox1.id];
      }

      // Call checkRelatedCheckboxes if checkbox is checked
      if (checkbox1.checked) {
        checkRelatedCheckboxes(checkbox1);
      }
    }

    gridContainer1.appendChild(gridRow1);
    gridContainer2.appendChild(gridRow2);
  }

  // Add event listeners to checkboxes
  addCheckboxEventListeners();
  localStorage.setItem('numFields', numFields);
}




function addCheckboxEventListeners() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            checkRelatedCheckboxes(checkbox);
            var gridContainerIndex = checkbox.id.endsWith("grid2") ? 'gridContainer2' : 'gridContainer1';
            // Save the checkbox state to localStorage with grid container index and checkbox id as the key
            localStorage.setItem(gridContainerIndex + ':' + checkbox.id, checkbox.checked);
        });
    });
}

function loadSavedData() {
  // Load the previously entered number of fields from localStorage
  var numFields = localStorage.getItem('numFields');
  if (numFields) {
    document.getElementById('numFields').value = numFields;
    updateInputFields();
  }

  // Load the checkbox states from localStorage
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(function(checkbox) {
    // Get the grid container index
    var gridContainerIndex = checkbox.id.endsWith("_2") ? 'gridContainer1' : 'gridContainer2';

    // Get the checkbox state from localStorage using grid container index and checkbox id as the key
    var checkboxState = localStorage.getItem(checkbox.id);
    if (checkboxState) {
      checkbox.checked = checkboxState === 'true';
    }
  });
}

function checkRelatedCheckboxes(checkbox) {
  var checkboxId = checkbox.id.split(" ");
  if (checkboxId[2] != "sec") {
    var isCheckboxInSecondGrid = true;
  } else {
    var isCheckboxInSecondGrid = false;
  }
  var mirroredId = checkboxId[1] + " " + checkboxId[0];
  var mirroredIdSec = checkboxId[1] + " " + checkboxId[0] + " sec";
  var mirroredCheckbox = document.getElementById(mirroredId);
  var mirroredCheckboxSec = document.getElementById(mirroredIdSec);
  if (isCheckboxInSecondGrid) {
    mirroredCheckbox.checked = checkbox.checked;
    // Save checkbox state to localStorage
    localStorage.setItem(checkbox.id, checkbox.checked);
  } else {
    mirroredCheckboxSec.checked = checkbox.checked;
    // Save checkbox state to localStorage
    localStorage.setItem(checkbox.id, checkbox.checked);
  }
}

function saveMatrices(url) {
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
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('Request successful');
            window.location.reload();
        }
    };

    xhr.send(JSON.stringify({ matrix1: jsonMatrix1, matrix2: jsonMatrix2 }));
}



function countButton() {
    saveMatrices('/'); // Call the saveMatrices() function for the first button
    // Additional code for the first button...
}

function countButton1() {
    saveMatrices('/operations'); // Call the saveMatrices() function for the first button
    // Additional code for the first button...
}

function countButton2() {
    saveMatrices('/find'); // Call the saveMatrices() function for the second button
    // Additional code for the second button...
}
