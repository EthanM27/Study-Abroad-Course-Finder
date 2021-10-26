


function postData(input) {
    ;
}

function getData() {
    $.ajax({
        type: "GET",
        url: "../course_finder.py",
        data: {},
        success: renderTable
    });
}

function renderTable(response) {
    console.log(response);
    return null;
}

function updateTable() {
    ;
}

getData()